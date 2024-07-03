# JsonDbLite

```markdown
`json-db-lite` - это простой Python класс для управления JSON файлом в качестве базы данных. Он позволяет инициализировать, читать, добавлять, обновлять и удалять записи в JSON файле.


```

## Возможности

- **Создание пустого JSON файла при инициализации объекта**
- **Добавление новых записей**
- **Получение всех записей**
- **Очистка базы данных**
- **Удаление записи по ключу**
- **Обновление записи по ключу**

## Installation

Вы можете установить пакет через pip:

```bash
pip install --upgrade json_db_lite
```

## Использование


Пример простого использования класса JSONDatabase:

```python
from json_db_lite import JSONDatabase

db_client = JSONDatabase('small_db.json')


def add_data_to_db():
    # массовое добавление
    db_client.add_records([{"id": 1, "name": "Sara"},
                           {"id": 2, "name": "Mark"},
                           {"id": 3, "name": "Charlie"},
                           {"id": 4, "name": "David"}
                           ])
    # добавление одной записи
    db_client.add_records({"id": 5, "name": "Alex"})


def get_all_data():
    # возвращаем все данные
    return db_client.get_all_records()


def get_data(key='id', value=4):
    # возвращаем данные по ключу
    return db_client.find_records_by_key(key, value)


def update_data():
    # обновляем данные по ключу у одного словаря
    db_client.update_record_by_key(upd_filter={"id": 4}, new_data=[{"name": "Alex"}, {"age": 31}])

    # обновляем данные по ключу у одного словаря
    db_client.update_record_by_key(upd_filter={"name": "Alex"},
                                   new_data=[{"age": 40}, {"job": "python developer"}])


def dell_data():
    # удаляем данные по ключу
    db_client.delete_record_by_key(key="name", value="Alex")


def dell_all_data():
    db_client.clear_database()
```

## License

Этот проект лицензируется по лицензии [MIT](https://choosealicense.com/licenses/mit/).
