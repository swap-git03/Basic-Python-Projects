import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame)
        self.task_list.pack(fill="both", expand=True)

        # Create task entry frame
        self.task_entry_frame = tk.Frame(self.root)
        self.task_entry_frame.pack(fill="x")

        # Create task entry
        self.task_entry = tk.Entry(self.task_entry_frame)
        self.task_entry.pack(fill="x", side="left", expand=True)

        # Create add task button
        self.add_task_button = tk.Button(self.task_entry_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(fill="x", side="left")

        # Create delete task button
        self.delete_task_button = tk.Button(self.task_entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(fill="x", side="left")

        # Create update task button
        self.update_task_button = tk.Button(self.task_entry_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(fill="x", side="left")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[task_index] = new_task
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, new_task)
                self.task_entry.delete(0, "end")
            else:
                messagebox.showwarning("Warning", "New task cannot be empty")
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()