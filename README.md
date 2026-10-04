# my_own_namespace.yandex_cloud_elk

Ansible-коллекция с собственным модулем и ролью для домашнего задания Netology.

## Содержимое

- **Модуль** `my_own_module` — создаёт текстовый файл по указанному пути с указанным содержимым.
- **Роль** `my_own_role` — обёртка над модулем, создаёт файл через переменные `my_file_path` и `my_file_content`.

## Установка

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
Использование модуля
yaml
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello!"
Использование роли
yaml
- hosts: localhost
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role
Лицензия
MIT
