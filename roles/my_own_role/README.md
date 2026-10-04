# my_own_role

Роль для создания текстового файла через кастомный модуль `my_own_module`.

## Переменные

| Переменная | По умолчанию | Описание |
|---|---|---|
| `my_file_path` | `/tmp/default_file.txt` | Путь к создаваемому файлу |
| `my_file_content` | `Default content from role` | Содержимое файла |

## Пример использования

```yaml
- hosts: localhost
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role
