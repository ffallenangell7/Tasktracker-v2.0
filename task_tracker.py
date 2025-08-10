import json
from colorama import Fore, Style, init
import pyfiglet
from datetime import datetime

init(autoreset=True)  # Reset colors after each print

# ----- TITLE -----
def show_title():
    ascii_banner = pyfiglet.figlet_format("Daily Task Tracker", font="slant")
    print(Fore.BLUE + Style.BRIGHT + ascii_banner)
    print(Fore.MAGENTA + "Version 1.0 | Stay organized, stay winning!\n")

# ----- MENU -----
def show_menu():
    print(Fore.YELLOW + "1️⃣  Add Task")
    print(Fore.YELLOW + "2️⃣  View Tasks")
    print(Fore.YELLOW + "3️⃣  Mark Task as Done")
    print(Fore.YELLOW + "4️⃣  Search Tasks")
    print(Fore.YELLOW + "5️⃣  Save Tasks")
    print(Fore.YELLOW + "6️⃣  Load Tasks")
    print(Fore.RED + "0️⃣  Exit\n")

# ----- TASK FUNCTIONS -----
def add_task(tasks):
    text = input(Fore.CYAN + "Task: ")
    due = input(Fore.CYAN + "Due date (YYYY-MM-DD, blank for none): ")
    priority = input(Fore.CYAN + "Priority (High/Medium/Low): ").capitalize()

    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    tasks.append({
        "text": text,
        "due": due if due else None,
        "priority": priority,
        "done": False
    })
    print(Fore.GREEN + "✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print(Fore.RED + "No tasks yet.")
        return
    print(Fore.MAGENTA + "\n--- Task List ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        due = task["due"] if task["due"] else "No due date"
        print(f"{i}. {task['text']} - {status} - Due: {due} - Priority: {task['priority']}")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input(Fore.CYAN + "Enter task number to mark done: "))
        tasks[num-1]["done"] = True
        print(Fore.GREEN + "✅ Task marked as done!")
    except:
        print(Fore.RED + "Invalid choice.")

def search_tasks(tasks):
    term = input(Fore.CYAN + "Search: ").lower()
    results = [t for t in tasks if term in t["text"].lower()]
    if results:
        print(Fore.MAGENTA + "\n--- Search Results ---")
        for i, task in enumerate(results, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['text']} - {status}")
    else:
        print(Fore.RED + "No matches found.")

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
    print(Fore.GREEN + "💾 Tasks saved.")

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.RED + "No saved file found.")
        return []

# ----- MAIN LOOP -----
def main():
    tasks = []
    show_title()

    while True:
        show_menu()
        choice = input(Fore.CYAN + "Select an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            search_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            tasks = load_tasks()
        elif choice == "0":
            print(Fore.YELLOW + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option.")

if __name__ == "__main__":
    main()

