import json
import os
from datetime import datetime

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