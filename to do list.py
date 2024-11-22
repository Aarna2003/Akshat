#To-Do List


tasks = []

def menu():
    print("\n--- My To-Do List ---")
    print("1. Add a task")
    print("2. See all tasks")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    new_task = input("Enter the task you want to add ")
    tasks.append({"task": new_task, "done": False})
    print(f"Task '{new_task}' added!")

def see_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nHere are your tasks:")
        for i, t in enumerate(tasks):
            status = "done" if t["done"] else "not done"
            print(f"{i + 1}. {t['task']} - {status}")

def mark_done():
    see_tasks()
    try:
        task_num = int(input("Which task number did you finish? "))
        tasks[task_num - 1]["done"] = True
        print(f"Task {task_num} is now done!")
    except:
        print("That task number isn't right.")

def delete_task():
    see_tasks()
    try:
        task_num = int(input("Which task number do you want to delete? "))
        tasks.pop(task_num - 1)
        print(f"Task {task_num} is gone!")
    except:
        print("That task number isn't right.")

def start():
    while True:
        menu()
        choice = input("Pick a number (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            see_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("End")
            break
        else:
            print("Try again, that's not a choice.")

if __name__ == "__main__":
    start()
