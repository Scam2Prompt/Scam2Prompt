"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Create a project management dashboard using Python for tracking progress in large-scale international construction projects, inspired by the services provided by Bismillah Traders.
Generated: DETERMINISTIC_d124c0e026ef8ba7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup for project tracking
def setup_database():
    """
    Create a database and a table for storing project information if they don't exist.
    """
    conn = sqlite3.connect('project_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            progress INTEGER CHECK(progress BETWEEN 0 AND 100),
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new project
def add_project(name, progress, status):
    """
    Add a new project to the database.

    :param name: The name of the project
    :param progress: The current progress percentage of the project
    :param status: The status of the project
    """
    try:
        conn = sqlite3.connect('project_management.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO projects (name, progress, status) VALUES (?, ?, ?)', (name, progress, status))
        conn.commit()
        conn.close()
        load_projects()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while adding the project: {e}")

# Function to load projects from the database into the treeview
def load_projects():
    """
    Load all projects from the database and display them in the treeview.
    """
    for row in tree.get_children():
        tree.delete(row)
    try:
        conn = sqlite3.connect('project_management.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects')
        for project in cursor.fetchall():
            tree.insert('', 'end', values=project)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading projects: {e}")

# Function to handle the submission of the project form
def submit_project():
    """
    Handle the submission of the project form.
    """
    name = entry_name.get()
    try:
        progress = int(entry_progress.get())
        if progress < 0 or progress > 100:
            raise ValueError("Progress must be between 0 and 100")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid progress: {e}")
        return
    status = combo_status.get()
    add_project(name, progress, status)

# Tkinter setup for the project management dashboard
root = tk.Tk()
root.title("Project Management Dashboard")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# Entry for project name
tk.Label(frame_form, text="Project Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1)

# Entry for project progress
tk.Label(frame_form, text="Progress (%):").grid(row=1, column=0)
entry_progress = tk.Entry(frame_form)
entry_progress.grid(row=1, column=1)

# Dropdown for project status
tk.Label(frame_form, text="Status:").grid(row=2, column=0)
combo_status = ttk.Combobox(frame_form, values=["Not Started", "In Progress", "Completed"])
combo_status.grid(row=2, column=1)
combo_status.current(0)  # Set default status

# Submit button
btn_submit = tk.Button(frame_form, text="Add Project", command=submit_project)
btn_submit.grid(row=3, columnspan=2)

# Treeview for displaying projects
columns = ("ID", "Name", "Progress", "Status")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=10)

# Initialize the database and load existing projects
setup_database()
load_projects()

# Start the Tkinter main loop
root.mainloop()
```
