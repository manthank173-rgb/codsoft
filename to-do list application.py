import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def mark_task_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]['done'] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()




