tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['task']}")

def mark_done():
    view_tasks()
    try:
        n = int(input("Enter task number to mark done: "))
        tasks[n-1]["done"] = True
        print("Marked as done!")
    except (ValueError, IndexError):
        print("Invalid number.")

def update_task():
    view_tasks()
    try:
        n = int(input("Enter task number to update: "))
        new_task = input(f"Enter new task (current: {tasks[n-1]['task']}): ")
        tasks[n-1]["task"] = new_task
        print("Task updated!")
    except (ValueError, IndexError):
        print("Invalid number.")

def delete_task():
    view_tasks()
    try:
        n = int(input("Enter task number to delete: "))
        removed = tasks.pop(n-1)
        print(f"Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid number.")

while True:
    show_menu()
    choice = input("Choose option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        update_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")