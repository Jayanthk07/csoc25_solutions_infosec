import json
import os

FILE_NAME = "todo.json"

#we can load data from json to code or save it from code to json by these 2 functions
#i am handling special cases like missing files ,tasks and invalid choices
#i am taking the data from the file and editing and finally updating those changes to the json file

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_user(data):
    user = input("Enter new user: ")
    if user in data:
        print("User already exists!!!")
    else:
        data[user] = []
        print(f"User '{user}' added")

def add_task(data):
    user = input("Enter user: ")
    if user not in data:
        print("User not found")
        return
    task = input("Enter task: ")
    data[user].append({"task": task, "done": False})
    print("Task added")

def view_tasks(data):
    user = input("Enter user: ")
    if user not in data:
        print("User not found")
        return
    if not data[user]:
        print("No tasks found")
        return
    print(f"\nTasks for {user}:")
    for i, t in enumerate(data[user], 1):
        print(f"{i}. {t['task']}  [Done: {t['done']}]")

def mark_task_done(data):
    user = input("Enter user: ")
    if user not in data:
        print("User not found.")
        return
    if not data[user]:
        print("No tasks to mark")
        return
    print("\nTasks:")
    for i, t in enumerate(data[user], 1):
        print(f"{i}. {t['task']} [Done: {t['done']}] ")
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(data[user]):
            data[user][choice - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input")

#here starts my main part of using the functions
data = load_data()

while True:
    print("\n..... To-Do List Menu .....")
    print("1.Add User")
    print("2.Add Task")
    print("3.View Tasks")
    print("4.Mark Task as Done")
    print("5.Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_user(data)
    elif choice == "2":
        add_task(data)
    elif choice == "3":
        view_tasks(data)
    elif choice == "4":
        mark_task_done(data)
    elif choice == "5":
        save_data(data)
        print("Goodbye!!!")
        break
    else:
        print("Invalid choice.")
