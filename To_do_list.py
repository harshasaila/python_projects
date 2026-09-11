import json

def load_tasks():
    try:
        with open("json file for todolist.json",'r') as file:
            return json.load(file)
    except:
        return {"tasks" : []}

def save_tasks(tasks):
    try:
        with open("json file for todolist.json",'w') as file:
            json.dump(tasks,file)

    except:
        print("Failed to Save..")


def create_tasks(tasks):
    description = input("Please enter your description : ")
    if description:
        tasks["tasks"].append({"description" : description, "Completed" : False})
        save_tasks(tasks)
        print("task added..")
    else:
        print("Description shouldn't be empty! Check once...")

def view_tasks(tasks):
    print()
    task_lists = tasks["tasks"]
    if len(task_lists) == 0:
        print("No tasks to show!")
    else:
        print("Your To_do_list is : ")
        for idx,task in enumerate(task_lists):
            status = "[Completed]" if task['Completed'] else "[Pending]"
            print(f"{idx + 1} . {task['description']} | {status}")

def mark_tasks_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the number to mark as Completed : ").strip())
    if 1<=task_number<=(len(tasks["tasks"])):
        tasks["tasks"][task_number - 1]["Completed"]=True
        print("Task updated to completed")
    else:
        print("Enter a valid number....")

def main():
    tasks = load_tasks()

    while True:
        print("\n Welcome to your TO DO LIST")
        print("1.view task")
        print("2.Add task")
        print("3.Complete task")
        print("4.load tasks")
        print("5.Exit")

        asking = input().strip()

        if asking == '1':
            view_tasks(tasks)
        elif asking == '2':
            create_tasks(tasks)
        elif asking == '3':
            mark_tasks_completed(tasks)
        elif asking == '4':
            load_tasks()
        elif asking == '5':
            print("Thank you! Have a nice day :) ")
            break
        else:
            print("You have entered a invalid input! Check once..")

main()