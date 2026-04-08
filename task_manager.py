import json
import os
from datetime import datetime
from task import Task

class TaskManager:
    """Клас для управління списком об'єктів Task."""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self._load_tasks()

    def _load_tasks(self):
        """Завантажує завдання з файлу і перетворює їх в об'єкти Task."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # Використовуємо метод класу Task для створення об'єктів
                    self.tasks = [Task.from_dict(t) for t in data]
                    if self.tasks:
                        self.next_id = max(t.task_id for t in self.tasks) + 1
                except json.JSONDecodeError:
                    self.tasks = []
    
    def _save_tasks(self):
        """Зберігає об'єкти Task у текстовий файл."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            # Перетворюємо об'єкти назад у словники для JSON
            json.dump([t.to_dict() for t in self.tasks], f, indent=4, ensure_ascii=False)

    def add_task(self, description: str, priority: int) -> int:
        if not (1 <= priority <= 5):
            raise ValueError("Пріоритет має бути від 1 до 5")
        
        # Створюємо екземпляр класу Task
        new_task = Task(self.next_id, description, priority)
        self.tasks.append(new_task)
        self.next_id += 1
        self._save_tasks()
        return new_task.task_id
    
    def delete_task(self, task_id: int) -> bool:
        initial_len = len(self.tasks)
        # Звертаємося до атрибута об'єкта (t.task_id), а не ключа словника
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < initial_len:
            self._save_tasks()
            return True
        return False
    
    def list_tasks(self, sort_by: str = "priority") -> list:
        if sort_by == "priority":
            return sorted(self.tasks, key=lambda x: x.priority)
        elif sort_by == "date":
            return sorted(self.tasks, key=lambda x: x.creation_date)
        return self.tasks
    
    def mark_done(self, task_id: int) -> bool:
        return self.delete_task(task_id)