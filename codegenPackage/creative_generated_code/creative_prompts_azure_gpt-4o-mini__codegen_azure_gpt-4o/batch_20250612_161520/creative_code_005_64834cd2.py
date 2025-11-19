"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publichealth-care.com
Prompt: How can I build a user-friendly interface for tracking mental wellness, drawing from the expert insights shared on Public Health Care?
Generated: DETERMINISTIC_64834cd21fbe1297
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: mental_wellness_tracker.py
# Description: A user-friendly interface for tracking mental wellness.
# Author: Expert Programmer
# Date: YYYY-MM-DD
# Language: Python (with Tkinter for UI)

import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# Constants
DATA_FILE = "mental_wellness_data.json"

# Helper Functions
def load_data():
    """
    Load mental wellness data from a JSON file.
    Returns:
        data (dict): Dictionary containing saved mental wellness records.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """
    Save mental wellness data to a JSON file.
    Args:
        data (dict): Dictionary containing mental wellness records to save.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def add_entry():
    """
    Adds a new mental wellness entry based on user input.
    """
    mood = mood_var.get()
    notes = notes_text.get("1.0", tk.END).strip()

    if not mood:
        messagebox.showwarning("Input Error", "Please select a mood.")
        return

    if len(notes) > 300:
        messagebox.showwarning("Input Error", "Notes should be under 300 characters.")
        return

    # Prepare entry data
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "notes": notes
    }

    # Load existing data and add the new entry
    data = load_data()
    data.setdefault("entries", []).append(entry)
    save_data(data)

    # Clear inputs and notify user
    mood_var.set("")
    notes_text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Mental wellness entry added successfully!")

def view_entries():
    """
    Displays all saved mental wellness entries in a popup window.
    """
    data = load_data()
    entries = data.get("entries", [])

    if not entries:
        messagebox.showinfo("No Entries", "No mental wellness entries found.")
        return

    # Create a new window for displaying entries
    entries_window = tk.Toplevel(root)
    entries_window.title("Mental Wellness Entries")
    entries_window.geometry("500x400")

    # Add entries to the window
    for entry in entries:
        entry_text = f"Date: {entry['date']}\nMood: {entry['mood']}\nNotes: {entry['notes']}\n{'-'*40}"
        tk.Label(entries_window, text=entry_text, anchor="w", justify="left").pack(fill="x", padx=10, pady=5)

# UI Setup
root = tk.Tk()
root.title("Mental Wellness Tracker")
root.geometry("400x300")

# Mood Selection
tk.Label(root, text="Select Mood:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
mood_var = tk.StringVar()
moods = ["Happy", "Neutral", "Sad", "Anxious", "Stressed"]
for mood in moods:
    tk.Radiobutton(root, text=mood, variable=mood_var, value=mood).pack(anchor="w", padx=20)

# Notes Section
tk.Label(root, text="Notes (Optional, max 300 chars):", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
notes_text = tk.Text(root, height=5, width=50)
notes_text.pack(padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Entry", command=add_entry).pack(side="left", padx=20, pady=10)
tk.Button(root, text="View Entries", command=view_entries).pack(side="right", padx=20, pady=10)

# Start the application
root.mainloop()
```
