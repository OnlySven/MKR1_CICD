import json
import os
from datetime import datetime

class Task:
    """Клас, що представляє окреме завдання."""
    
    def __init__(self, task_id: int, description: str, priority: int):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.creation_date = datetime.now().isoformat()