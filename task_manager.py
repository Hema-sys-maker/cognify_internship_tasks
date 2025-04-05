tasks = []

def create_task():
    task = input("Enter task: ")
    tasks.append(task)

def read_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def update_task():
    read_tasks()
    idx = int(input("Enter task number to update: ")) - 1
    tasks[idx] = input("Enter new task: ")

def delete_task():
    read_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    tasks.pop(idx)

def menu():
    while True:
        print("\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break

menu()