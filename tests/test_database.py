from json_db_lite import JSONDatabase

# Инициализация базы данных
db = JSONDatabase('db.json')


# Добавление новых записей
new_data = [{"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "David"}
]
db.add_records(new_data)

# Получение всех записей
print(db.get_all_records())

# Обновление записи по ключу
db.update_record_by_key(upd_filter={'name': 'David'},
                        new_data=[{"age": 23}, {'job': 'progger'}]
                        )

# Удаление записи по ключу
db.delete_record_by_key("id", 1)

# Очистка базы данных
db.clear_database()