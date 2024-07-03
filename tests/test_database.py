from json_db_lite import JSONDatabase

# Инициализация базы данных
db = JSONDatabase('db.json')

# Инициализация списка словарей
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
db.initialize_from_list(data)

# Добавление новых записей
new_data = [
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "David"}
]
db.add_records(new_data)

# Получение всех записей
print(db.get_all_records())

# Обновление записи по ключу
db.update_record_by_key("id", 2, {"name": "Bobby"})

# Удаление записи по ключу
db.delete_record_by_key("id", 1)

# Очистка базы данных
db.clear_database()
