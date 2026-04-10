# To-Do List Manager

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if num >= 1 and num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid number!")
    except:
        print("Please enter a valid number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")