Tasks = []
def show_menu():
    print("""
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
""")
    
def add_task():
    task_description = input("Enter task Description: ")
    Tasks.append(task_description)

def view_tasks():
    for index, item in enumerate(Tasks):
        print(f"{index} -> {item}")


def delete_task():
    choice = int(input("Which Tasks Do you want to delete?: "))
    index = choice -1
    if index >= 0 and index < len(Tasks):
            Tasks.pop(index) 
            print("Task deleted successfully.")
    else:
            print("Invalid task number.")
    

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
          print("Good bye")
          break
     else:
          print("Invalid choice, Please try again")