import pytest
from task import Task

@pytest.fixture
def sample_task_data():
    """Фікстура, що повертає словник з даними для створення завдання."""
    return {
        'id': 101,
        'description': "Тестове завдання для перевірки",
        'priority': 2,
        'creation_date': "2026-04-08T15:00:00"
    }

@pytest.fixture
def sample_task():
    """Фікстура, що повертає готовий об'єкт класу Task."""
    return Task(
        task_id=42, 
        description="Написати юніт-тести", 
        priority=1, 
        creation_date="2026-04-08T12:30:00"
    )

def test_task_initialization(sample_task_data):
    """Тест перевіряє правильність ініціалізації об'єкта Task."""
    task = Task.from_dict(sample_task_data)

    assert task.task_id == sample_task_data['id']
    assert task.description == sample_task_data['description']
    assert task.priority == sample_task_data['priority']
    assert task.creation_date == sample_task_data['creation_date']

def test_task_to_dict(sample_task):
    """Тестуємо метод серіалізації об'єкта у словник (для JSON)."""
    task_dict = sample_task.to_dict()
    
    assert isinstance(task_dict, dict)
    assert task_dict['id'] == 42
    assert task_dict['description'] == "Написати юніт-тести"
    assert task_dict['priority'] == 1
    assert task_dict['creation_date'] == "2026-04-08T12:30:00"

def test_task_from_dict(sample_task_data):
    """Тестуємо метод класу (classmethod) десеріалізації зі словника в об'єкт."""
    task = Task.from_dict(sample_task_data)
    
    assert isinstance(task, Task)
    assert task.task_id == 101
    assert task.description == "Тестове завдання для перевірки"
    assert task.priority == 2
    assert task.creation_date == "2026-04-08T15:00:00"