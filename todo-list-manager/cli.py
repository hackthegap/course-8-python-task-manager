from todo_manager.todo import ToDoList

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            try:
                task_index = int(input("Enter the task number to complete: "))
                todo_list.complete_task(task_index)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif choice == "3":
            tasks = todo_list.list_tasks()
            if tasks:
                print("\nTasks:")
                print("\n".join(tasks))
            else:
                print("No tasks found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()