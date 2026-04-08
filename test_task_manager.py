import pytest
from task_manager import TaskManager

@pytest.fixture
def temp_manager(tmp_path):
    """
    Фікстура створює порожній TaskManager із тимчасовим файлом.
    tmp_path - це вбудована фікстура pytest, яка створює унікальну тимчасову 
    папку для кожного тесту і автоматично видаляє її після завершення.
    Це гарантує, що тести не зіпсують ваш основний файл tasks.json.
    """
    test_file = tmp_path / "test_tasks.json"
    manager = TaskManager(filename=str(test_file))
    return manager

@pytest.fixture
def populated_manager(temp_manager):
    """
    Фікстура, яка використовує іншу фікстуру (temp_manager) 
    і наповнює її тестовими даними.
    """
    temp_manager.add_task("Вивчити Python", priority=3)
    temp_manager.add_task("Написати тести", priority=1)
    temp_manager.add_task("Почитати книгу", priority=5)
    return temp_manager

# Параметризуємо тест для перевірки всіх валідних значень пріоритету (від 1 до 5)
@pytest.mark.parametrize("priority", [1, 2, 3, 4, 5])
def test_add_task_valid_priority(temp_manager, priority):
    """Тест додавання завдання з коректними пріоритетами."""
    task_id = temp_manager.add_task("Тестове завдання", priority)
    
    assert task_id == 1  # Оскільки це перше завдання, ID має бути 1
    assert len(temp_manager.tasks) == 1
    assert temp_manager.tasks[0].priority == priority
    assert temp_manager.tasks[0].description == "Тестове завдання"

# Параметризуємо тест для перевірки НЕвалідних значень (менше 1 і більше 5)
@pytest.mark.parametrize("invalid_priority", [0, 6, -1, 100])
def test_add_task_invalid_priority(temp_manager, invalid_priority):
    """Тест перевіряє, чи викидається помилка ValueError при неправильному пріоритеті."""
    with pytest.raises(ValueError, match="Пріоритет має бути від 1 до 5"):
        temp_manager.add_task("Неправильне завдання", invalid_priority)

def test_delete_task(populated_manager):
    """Тест видалення завдання за ідентифікатором."""
    assert len(populated_manager.tasks) == 3
    
    # Видаляємо завдання з ID 2 ("Написати тести")
    result = populated_manager.delete_task(2)
    
    assert result is True
    assert len(populated_manager.tasks) == 2
    # Перевіряємо, що завдання з ID 2 дійсно зникло
    assert not any(t.task_id == 2 for t in populated_manager.tasks)

def test_delete_nonexistent_task(populated_manager):
    """Тест спроби видалити завдання, якого не існує."""
    result = populated_manager.delete_task(999)
    assert result is False
    assert len(populated_manager.tasks) == 3

# Параметризуємо перевірку сортування
@pytest.mark.parametrize("sort_method, expected_first_task_desc", [
    ("priority", "Написати тести"),  # Найвищий пріоритет (1)
    ("date", "Вивчити Python")       # Додано найпершим
])
def test_list_tasks_sorting(populated_manager, sort_method, expected_first_task_desc):
    """Тест перевіряє правильність сортування списку завдань."""
    sorted_tasks = populated_manager.list_tasks(sort_by=sort_method)
    
    assert len(sorted_tasks) == 3
    assert sorted_tasks[0].description == expected_first_task_desc

def test_mark_done(populated_manager):
    """Тест позначення завдання як виконаного (за умовою - видалення)."""
    result = populated_manager.mark_done(1) # Позначаємо перше виконаним
    
    assert result is True
    assert len(populated_manager.tasks) == 2