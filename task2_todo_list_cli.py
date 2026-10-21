"""
Task 2: To-Do List CLI App
Users can add, view, remove, and optionally save tasks to a text file.
"""

TASKS_FILE = "tasks.txt"


def show_tasks(tasks):
    """Display tasks with numbers."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\n=== Your Tasks ===")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def save_tasks(tasks):
    """Save all tasks to a text file."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"Tasks saved to {TASKS_FILE}.")
    except OSError as error:
        print(f"Could not save tasks: {error}")


def load_tasks():
    """Load previously saved tasks, if the file exists."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Save tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            save_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
