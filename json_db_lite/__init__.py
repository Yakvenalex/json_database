import json
import os
from typing import List, Dict, Any


class JSONDatabase:
    def __init__(self, file_path: str) -> None:
        """
        Инициализирует JSONDatabase с указанным путем к файлу.
        Создает файл, если он не существует.

        :param file_path: Путь к файлу JSON.
        """
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def save_to_file(self, data: List[Dict[str, Any]]) -> None:
        """
        Сохраняет данные в файл JSON.

        :param data: Список словарей для сохранения.
        """
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def read_from_file(self) -> List[Dict[str, Any]]:
        """
        Читает данные из файла JSON.

        :return: Список словарей, считанных из файла.
        """
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def initialize_from_list(self, data_list: List[Dict[str, Any]]) -> None:
        """
        Инициализирует базу данных из списка словарей и сохраняет его в JSON файл.

        :param data_list: Список словарей для инициализации.
        """
        self.save_to_file(data_list)

    def add_records(self, new_data: List[Dict[str, Any]]) -> None:
        """
        Добавляет новые записи в существующий JSON файл.

        :param new_data: Список новых записей для добавления.
        """
        data = self.read_from_file()
        data.extend(new_data)
        self.save_to_file(data)

    def get_all_records(self) -> List[Dict[str, Any]]:
        """
        Возвращает все данные из JSON файла.

        :return: Список всех записей из файла.
        """
        return self.read_from_file()

    def clear_database(self) -> None:
        """
        Полностью очищает JSON файл.
        """
        self.save_to_file([])

    def delete_record_by_key(self, key: str, value: Any) -> None:
        """
        Удаляет запись по ключу и значению.

        :param key: Ключ для поиска записи.
        :param value: Значение для поиска записи.
        """
        data = self.read_from_file()
        data = [record for record in data if record.get(key) != value]
        self.save_to_file(data)

    def update_record_by_key(self, key: str, value: Any, new_record: Dict[str, Any]) -> None:
        """
        Обновляет запись по ключу и значению.

        :param key: Ключ для поиска записи.
        :param value: Значение для поиска записи.
        :param new_record: Новый словарь для замены старого.
        """
        data = self.read_from_file()
        for index, record in enumerate(data):
            if record.get(key) == value:
                data[index] = new_record
                break
        self.save_to_file(data)

    def find_records_by_key(self, key: str, value: Any) -> List[Dict[str, Any]]:
        """
        Находит записи по ключу и значению.

        :param key: Ключ для поиска записи.
        :param value: Значение для поиска записи.
        :return: Список записей, соответствующих критерию поиска.
        """
        data = self.read_from_file()
        return [record for record in data if record.get(key) == value]

    def record_exists(self, key: str, value: Any) -> bool:
        """
        Проверяет, существует ли запись с указанным ключом и значением.

        :param key: Ключ для поиска записи.
        :param value: Значение для поиска записи.
        :return: True, если запись существует, иначе False.
        """
        data = self.read_from_file()
        return any(record.get(key) == value for record in data)
