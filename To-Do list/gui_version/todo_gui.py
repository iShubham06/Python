import tkinter as tk
from tkinter import messagebox

# --- Reuse your logic ---
task_list = []

def add_task(task_name):
    task_list.append({"task": task_name, "done": False})
    update_listbox()

def show_tasks():
    listbox.delete(0, tk.END)
    for i, task in enumerate(task_list):
        status = "✔️" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i + 1}. {task['task']} [{status}]")

def mark_task_done(task_number):
    if 0 <= task_number < len(task_list):
        task_list[task_number]["done"] = True
        update_listbox()
    else:
        messagebox.showerror("Error", "Invalid task number!")

def delete_task(task_number):
    if 0 <= task_number < len(task_list):
        removed = task_list.pop(task_number)
        update_listbox()
    else:
        messagebox.showerror("Error", "Invalid task number!")

def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(task_list):
        status = "✔️" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i + 1}. {task['task']} [{status}]")


# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List GUI")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

def gui_add_task():
    task = entry.get()
    if task.strip():
        add_task(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

add_btn = tk.Button(root, text="Add Task", command=gui_add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

def gui_mark_done():
    try:
        selected = listbox.curselection()[0]
        mark_task_done(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def gui_delete_task():
    try:
        selected = listbox.curselection()[0]
        delete_task(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

done_btn = tk.Button(root, text="Mark as Done", command=gui_mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=gui_delete_task)
delete_btn.pack(pady=5)

# Start the GUI
root.mainloop()
