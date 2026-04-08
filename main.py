from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Система управління завданнями ===")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Показати список завдань")
        print("4. Позначити як виконане")
        print("0. Вийти")
        
        choice = input("\nОберіть дію (0-4): ")
        
        if choice == '1':
            desc = input("Опис завдання: ")
            try:
                prio = int(input("Пріоритет (1-5, де 1 - найвищий): "))
                t_id = manager.add_task(desc, prio)
                print(f"✅ Завдання успішно додано! ID: {t_id}")
            except ValueError as e:
                print(f"❌ Помилка: {e}. Переконайтесь, що ввели число від 1 до 5.")
                
        elif choice == '2':
            try:
                t_id = int(input("Введіть ID завдання для видалення: "))
                if manager.delete_task(t_id):
                    print("✅ Завдання видалено.")
                else:
                    print("❌ Завдання з таким ID не знайдено.")
            except ValueError:
                print("❌ ID має бути числом.")
                
        elif choice == '3':
            sort_choice = input("Сортувати за (1 - пріоритетом, 2 - датою): ")
            sort_by = "date" if sort_choice == '2' else "priority"
            tasks = manager.list_tasks(sort_by)
            
            if not tasks:
                print("📭 Список завдань порожній.")
            else:
                print("\n--- Список завдань ---")
                for t in tasks:
                    # Виводимо дату лише до секунд або обрізаємо для краси
                    date_short = t.creation_date[:10] 
                    print(f"ID: {t.task_id} | Пріоритет: {t.priority} | Опис: {t.description} | Дата: {date_short}")
                    
        elif choice == '4':
            try:
                t_id = int(input("Введіть ID виконаного завдання: "))
                if manager.mark_done(t_id):
                    print("✅ Завдання позначено як виконане (і видалено).")
                else:
                    print("❌ Завдання з таким ID не знайдено.")
            except ValueError:
                print("❌ ID має бути числом.")
                
        elif choice == '0':
            print("👋 Вихід з програми. До побачення!")
            break
            
        else:
            print("❌ Невідома команда. Оберіть число від 0 до 4.")

if __name__ == "__main__":
    main()