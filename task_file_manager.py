filename = "tasks.txt"

def load_tasks():
    try:
        with open(filename, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(filename, "w") as f:
        f.write("\n".join(tasks))

def menu():
    tasks = load_tasks()
    while True:
        print("\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("New task: ")
            tasks.append(task)
        elif choice == "2":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            idx = int(input("Which task to update? ")) - 1
            tasks[idx] = input("New task: ")
        elif choice == "4":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            idx = int(input("Which task to delete? ")) - 1
            tasks.pop(idx)
        elif choice == "5":
            save_tasks(tasks)
            break

menu()