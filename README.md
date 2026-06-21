# codsoft-todo-list
To-Do List Application (Python)

Overview

This is a simple command-line To-Do List application developed in Python. It allows users to manage their daily tasks efficiently by adding, viewing, updating, marking tasks as completed, and deleting tasks.

Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Update existing tasks
- Delete tasks
- User-friendly menu-driven interface

Requirements

- Python 3.x

How to Run

1. Save the code in a file named "todo.py".
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the program using:

python todo.py

Menu Options

1. Add Task

Allows the user to add a new task to the list.

2. View Tasks

Displays all tasks along with their completion status:

- ✔ = Completed
- ✘ = Not Completed

3. Mark Task Done

Marks a selected task as completed.

4. Update Task

Modifies the description of an existing task.

5. Delete Task

Removes a selected task from the list.

6. Exit

Closes the application.

Data Structure Used

The application stores tasks in a list of dictionaries.

Example:

tasks = [
    {"task": "Complete Assignment", "done": False},
    {"task": "Buy Groceries", "done": True}
]

Exception Handling

The program handles:

- Invalid menu choices
- Non-numeric input
- Invalid task numbers

Sample Output

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Mark Task Done
4. Update Task
5. Delete Task
6. Exit

Choose option: 1
Enter task: Complete Python Project
Task added!

Future Improvements

- Save tasks to a file
- Load tasks automatically on startup
- Add task priorities
- Add due dates
- GUI version using Tkinter

Author

Jashanpreet Singh
