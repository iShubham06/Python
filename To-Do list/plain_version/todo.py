def add_task(task_list, task_name):
    task_list.append({"task": task_name, "done": False})



def show_tasks(task_list):
    if not task_list:
        print("No tasks yet.")
    for i, task in enumerate(task_list):
        status = "✔️" if task["done"] else "❌"
        print(f"{i + 1}. {task['task']} [{status}]")

task_list = []


def mark_task_done(task_list, task_number):
    if 0 < task_number <= len(task_list):
        task_list[task_number - 1 ]["done"] = True
        print(f"Task {task_number} marked as done!")
    else:
        print("Invalid task number!")
        
        
def delete_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        removed = task_list.pop(task_number - 1)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number!")
        


while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Quit")
    choice = input(int("Enter your choice: "))

    if choice == 1:
        task_name = input("Enter task: ")
        add_task(task_list, task_name)

    elif choice == 2:
        show_tasks(task_list)
        
    elif choice == 3:
        show_tasks(task_list)
        try:
            task_num = int(input("Enter task number to mark as done: "))
            mark_task_done(task_list, task_num)
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == 4:
        show_tasks(task_list)
        try:
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_list, task_num)
        except ValueError:
            print("Please enter a valid number.")


    elif choice == 5:
        break

    else:
        print("Invalid choice!")