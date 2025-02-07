import tkinter as tk
from tkinter import messagebox

class HabitTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.habits = []

        # Create frames
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack()
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack()

        # Create input fields
        self.label_name = tk.Label(self.frame_input, text="Name:")
        self.label_name.pack(side=tk.LEFT)
        self.entry_name = tk.Entry(self.frame_input)
        self.entry_name.pack(side=tk.LEFT)
        self.label_duration = tk.Label(self.frame_input, text="Duration:")
        self.label_duration.pack(side=tk.LEFT)
        self.entry_duration = tk.Entry(self.frame_input)
        self.entry_duration.pack(side=tk.LEFT)
        self.label_frequency = tk.Label(self.frame_input, text="Frequency:")
        self.label_frequency.pack(side=tk.LEFT)
        self.entry_frequency = tk.Entry(self.frame_input)
        self.entry_frequency.pack(side=tk.LEFT)

        # Create buttons
        self.button_add = tk.Button(self.frame_input, text="Add Habit", command=self.add_habit)
        self.button_add.pack(side=tk.LEFT)
        self.button_delete = tk.Button(self.frame_input, text="Delete Habit", command=self.delete_habit)
        self.button_delete.pack(side=tk.LEFT)

        # Create listbox
        self.listbox_habits = tk.Listbox(self.frame_list)
        self.listbox_habits.pack()

    def add_habit(self):
        name = self.entry_name.get()
        duration = self.entry_duration.get()
        frequency = self.entry_frequency.get()
        if name and duration and frequency:
            self.habits.append((name, duration, frequency))
            self.listbox_habits.insert(tk.END, f"{name} - {duration} - {frequency}")
            self.entry_name.delete(0, tk.END)
            self.entry_duration.delete(0, tk.END)
            self.entry_frequency.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def delete_habit(self):
        try:
            index = self.listbox_habits.curselection()[0]
            self.listbox_habits.delete(index)
            self.habits.pop(index)
        except IndexError:
            messagebox.showerror("Error", "Please select a habit to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTracker(root)
    root.mainloop()