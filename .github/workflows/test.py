class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task removed: {task}")
        else:
            print("Task not found!")
    
    def show_tasks(self):
        if len(self.tasks) > 0:
            print("Tasks List:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("No tasks to show.")

    def mark_task_completed(self, task):
        task_index = self.tasks.index(task)
        self.tasks[task_index] = f"{task} (completed)"
        print(f"Task marked as completed: {task}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task}\n")
        print(f"Tasks saved to {filename}")

def main():
    manager = TaskManager()
    
    manager.add_task("Finish homework")
    manager.add_task("Read a book")
    manager.add_task("Buy groceries")
    
    manager.show_tasks()
    
    manager.mark_task_completed("Finish homework")
    
    manager.show_tasks()
    
    manager.remove_task("Buy groceries")
    
    manager.show_tasks()
    
    manager.save_to_file("tasks.txt")
    

if __name__ == "__main__":
    main()
