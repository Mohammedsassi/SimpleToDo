todo_list = []

def show_menu():
    print("\nSimple To-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Added task: {task}")

    elif choice == '3':
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(todo_list):
                removed = todo_list.pop(index)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
