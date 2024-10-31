todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def view_tasks():
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

def delete_task(index):
    if 0 < index <= len(todo_list):
        todo_list.pop(index - 1)
        print("Task deleted.")
    else:
        print("Invalid index.")

while True:
    command = input("Choose an option (add/view/delete/exit): ").strip().lower()
    if command == 'add':
        task = input("Enter a task: ")
        add_task(task)
    elif command == 'view':
        view_tasks()
    elif command == 'delete':
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif command == 'exit':
        break
    else:
        print("Invalid command")
