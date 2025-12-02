import os

FILE_NAME = "tasks.txt"
Tasks = []


# -------------------------------
# Load tasks from file at startup
# -------------------------------
def load_tasks():
    global Tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            Tasks = [line.strip() for line in file.readlines()]
    else:
        Tasks = []


# -------------------------------
# Save tasks to file
# -------------------------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in Tasks:
            file.write(task + "\n")


def show_menu():
    print("""
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
""")


def add_task():
    task_description = input("Enter task description: ")
    Tasks.append(task_description)
    save_tasks()
    print("Task added & saved.")


def view_tasks():
    if not Tasks:
        print("No tasks available.")
        return
    
    for index, item in enumerate(Tasks, start=1):
        print(f"{index}. {item}")


def delete_task():
    if not Tasks:
        print("No tasks to delete.")
        return

    print("You can delete by task number OR task name.")
    choice = input("Enter task number or exact task name: ")
    
    # Delete by number
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(Tasks):
            removed = Tasks.pop(index)
            save_tasks()
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    
    # Delete by task name
    else:
        if choice in Tasks:
            Tasks.remove(choice)
            save_tasks()
            print(f"Deleted task: {choice}")
        else:
            print("Task not found.")


# Load existing tasks when program starts
load_tasks()


# Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye! Tasks saved.")
        break
    else:
        print("Invalid choice, please try again.")
