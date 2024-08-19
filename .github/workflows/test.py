class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

def menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    todo_list = ToDoList()

    while True:
        menu()
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == 2:
            title = input("Enter task title to remove: ")
            if todo_list.remove_task(title):
                print("Task removed successfully.")
            else:
                print("Task not found.")
        elif choice == 3:
            todo_list.view_tasks()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4. ")

if __name__ == "__main__":
    main()
