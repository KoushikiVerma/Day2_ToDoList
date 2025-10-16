#Day2 
#CLI To do list app

Task_File = "tasks.txt"

def load_tasks():
    try:
        with open(Task_File,"r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

#to save tasks to file
def save_tasks(tasks):
    with open(Task_File, "w") as file:
        for task in tasks:
            file.write(task + "\n")

#to display all the tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found\n")
    else:
        print("\n Your To-Do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")
        print()

#add a new task
def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append(task)
    save_tasks(tasks)
    print("Task Added Successfully!\n")

#to remove a task from to-do list
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to remove:"))
        if 1<=task_num<=len(tasks):
            removed = tasks.pop(task_num-1)
            save_tasks(tasks)
            print(f"Task'{removed}' removed.\n")
        else:
            print("Invalid task Number\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("------To-Do List App-----")
        print("1.View Tasks")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Exit")
        choice = input("Enter your choice (1-4):")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting.....\n Your tasks are saved")

if __name__ == "__main__":
    main()