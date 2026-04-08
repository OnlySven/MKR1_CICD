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