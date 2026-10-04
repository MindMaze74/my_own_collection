#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Your Name
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Creates a text file on a remote host
description:
    - This module creates a text file with specified content on a remote host.
    - It is idempotent: if the file already exists with the same content, no changes are made.
version_added: "1.0.0"
options:
    path:
        description:
            - Path to the file to be created.
        required: true
        type: str
    content:
        description:
            - Content to write to the file.
        required: true
        type: str
author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/example.txt
    content: "Hello, world!"
'''

RETURN = r'''
path:
    description: Path to the created file
    type: str
    returned: always
    sample: '/tmp/example.txt'
content:
    description: Content written to the file
    type: str
    returned: always
    sample: 'Hello, world!'
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    # Check mode — не изменяем систему
    if module.check_mode:
        module.exit_json(**result)

    # Идемпотентность: файл существует и содержимое совпадает?
    file_exists = os.path.exists(path)
    content_matches = False

    if file_exists:
        try:
            with open(path, 'r') as f:
                existing_content = f.read()
            if existing_content == content:
                content_matches = True
        except Exception:
            pass

    if file_exists and content_matches:
        result['changed'] = False
        module.exit_json(**result)

    # Создаём/перезаписываем файл
    try:
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(path, 'w') as f:
            f.write(content)

        result['changed'] = True
    except Exception as e:
        module.fail_json(msg=f"Failed to create file: {str(e)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
