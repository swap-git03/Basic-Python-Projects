import tkinter as tk
from tkinter import messagebox
import datetime

class WeatherJournal:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Journal")
        self.entries = []

        # Create frames
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.view_frame = tk.Frame(self.root)
        self.view_frame.pack()

        # Create entry fields
        self.date_label = tk.Label(self.entry_frame, text="Date:")
        self.date_label.pack(side=tk.LEFT)

        self.date_entry = tk.Entry(self.entry_frame)
        self.date_entry.pack(side=tk.LEFT)

        self.weather_label = tk.Label(self.entry_frame, text="Weather:")
        self.weather_label.pack(side=tk.LEFT)

        self.weather_entry = tk.Entry(self.entry_frame)
        self.weather_entry.pack(side=tk.LEFT)

        self.thoughts_label = tk.Label(self.entry_frame, text="Thoughts:")
        self.thoughts_label.pack(side=tk.LEFT)

        self.thoughts_entry = tk.Text(self.entry_frame, height=10, width=20)
        self.thoughts_entry.pack(side=tk.LEFT)

        # Create buttons
        self.add_button = tk.Button(self.button_frame, text="Add Entry", command=self.add_entry)
        self.add_button.pack(side=tk.LEFT)

        self.view_button = tk.Button(self.button_frame, text="View Entries", command=self.view_entries)
        self.view_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.button_frame, text="Delete Entry", command=self.delete_entry)
        self.delete_button.pack(side=tk.LEFT)

        # Create view field
        self.view_text = tk.Text(self.view_frame)
        self.view_text.pack()

    def add_entry(self):
        date = self.date_entry.get()
        weather = self.weather_entry.get()
        thoughts = self.thoughts_entry.get("1.0", tk.END)
        entry = {"date": date, "weather": weather, "thoughts": thoughts}
        self.entries.append(entry)
        messagebox.showinfo("Entry Added", "Entry has been added successfully.")

    def view_entries(self):
        self.view_text.delete("1.0", tk.END)
        for entry in self.entries:
            self.view_text.insert(tk.END, f"Date: {entry['date']}\n")
            self.view_text.insert(tk.END, f"Weather: {entry['weather']}\n")
            self.view_text.insert(tk.END, f"Thoughts: {entry['thoughts']}\n\n")

    def delete_entry(self):
        date = self.date_entry.get()
        for entry in self.entries:
            if entry["date"] == date:
                self.entries.remove(entry)
                messagebox.showinfo("Entry Deleted", "Entry has been deleted successfully.")
                return
        messagebox.showerror("Entry Not Found", "Entry not found for the given date.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherJournal(root)
    root.mainloop()