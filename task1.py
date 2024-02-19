class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            print(f"{index}. {task.description} - Priority: {task.priority} - Status: {status}")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            task = Task(description, priority)
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            print("\n===== Your Tasks =====")
            todo_list.display_tasks()
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
