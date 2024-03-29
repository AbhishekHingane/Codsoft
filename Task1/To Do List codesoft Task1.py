Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ToDoList:
...     def __init__(self):
...         self.tasks = []
... 
...     def add_task(self, task):
...         self.tasks.append({"task": task, "completed": False})
... 
...     def view_tasks(self):
...         if not self.tasks:
...             print("No tasks in the to-do list.")
...         else:
...             for idx, task in enumerate(self.tasks):
...                 status = "Completed" if task["completed"] else "Incomplete"
...                 print(f"{idx + 1}. [{status}] {task['task']}")
... 
...     def mark_completed(self, task_number):
...         if 1 <= task_number <= len(self.tasks):
...             self.tasks[task_number - 1]["completed"] = True
...             print("Task marked as completed.")
...         else:
...             print("Invalid task number.")
... 
...     def remove_task(self, task_number):
...         if 1 <= task_number <= len(self.tasks):
...             del self.tasks[task_number - 1]
...             print("Task removed.")
...         else:
...             print("Invalid task number.")
... 
... def main():
...     todo_list = ToDoList()
... 
...     while True:
...         print("\n===== TO-DO LIST =====")
...         print("1. Add Task")
...         print("2. View Tasks")
...         print("3. Mark Task as Completed")
...         print("4. Remove Task")
...         print("5. Exit")
... 
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
