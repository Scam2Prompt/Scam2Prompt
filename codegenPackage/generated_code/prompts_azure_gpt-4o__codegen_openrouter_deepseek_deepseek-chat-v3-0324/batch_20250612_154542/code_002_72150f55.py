"""
Generated Code Metadata:
========================
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a project management dashboard that allows users to oversee project progress, assign priorities (low, medium, high), and manage tasks using the workflow stages (To do, In progress, Done, Backlog) mentioned on the Zapper webpage.
Generated: DETERMINISTIC_72150f557b108309
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class ProjectManagementDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Management Dashboard")
        self.root.geometry("1000x700")
        
        # Data storage
        self.projects = []
        self.current_project = None
        self.data_file = "projects_data.json"
        
        # Load existing data
        self.load_data()
        
        # UI Setup
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Project selection
        self.project_frame = ttk.LabelFrame(self.main_frame, text="Projects", padding="10")
        self.project_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.project_combobox = ttk.Combobox(self.project_frame, state="readonly")
        self.project_combobox.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.project_combobox.bind("<<ComboboxSelected>>", self.load_project)
        
        self.add_project_btn = ttk.Button(self.project_frame, text="Add Project", command=self.add_project)
        self.add_project_btn.pack(side=tk.LEFT)
        
        # Task management
        self.task_management_frame = ttk.LabelFrame(self.main_frame, text="Task Management", padding="10")
        self.task_management_frame.pack(fill=tk.BOTH, expand=True)
        
        # Task input fields
        self.task_input_frame = ttk.Frame(self.task_management_frame)
        self.task_input_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(self.task_input_frame, text="Task:").pack(side=tk.LEFT)
        self.task_entry = ttk.Entry(self.task_input_frame)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        ttk.Label(self.task_input_frame, text="Priority:").pack(side=tk.LEFT, padx=(10, 0))
        self.priority_combobox = ttk.Combobox(self.task_input_frame, values=["Low", "Medium", "High"], state="readonly")
        self.priority_combobox.pack(side=tk.LEFT)
        self.priority_combobox.current(1)
        
        self.add_task_btn = ttk.Button(self.task_input_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Task boards
        self.task_boards_frame = ttk.Frame(self.task_management_frame)
        self.task_boards_frame.pack(fill=tk.BOTH, expand=True)
        
        self.workflow_stages = ["Backlog", "To Do", "In Progress", "Done"]
        self.task_boards = {}
        
        for stage in self.workflow_stages:
            board_frame = ttk.LabelFrame(self.task_boards_frame, text=stage)
            board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            
            tree = ttk.Treeview(board_frame, columns=("priority", "date"), show="headings")
            tree.heading("#0", text="Task")
            tree.heading("priority", text="Priority")
            tree.heading("date", text="Date Added")
            
            tree.column("#0", width=200)
            tree.column("priority", width=80)
            tree.column("date", width=100)
            
            tree.pack(fill=tk.BOTH, expand=True)
            
            # Context menu for task actions
            tree.bind("<Button-3>", self.show_task_context_menu)
            
            # Drag and drop functionality
            tree.bind("<ButtonPress-1>", self.on_drag_start)
            tree.bind("<B1-Motion>", self.on_drag_motion)
            tree.bind("<ButtonRelease-1>", self.on_drop)
            
            self.task_boards[stage] = tree
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X)
        
        # Update UI
        self.update_project_list()
        self.update_status("Ready")
    
    def update_status(self, message):
        self.status_var.set(message)
    
    def update_project_list(self):
        project_names = [project["name"] for project in self.projects]
        self.project_combobox["values"] = project_names
        if project_names:
            self.project_combobox.current(0)
            self.load_project()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    self.projects = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {str(e)}")
                self.projects = []
    
    def save_data(self):
        try:
            with open(self.data_file, "w") as f:
                json.dump(self.projects, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    
    def add_project(self):
        project_name = simpledialog.askstring("Add Project", "Enter project name:")
        if project_name:
            new_project = {
                "name": project_name,
                "tasks": {
                    "Backlog": [],
                    "To Do": [],
                    "In Progress": [],
                    "Done": []
                }
            }
            self.projects.append(new_project)
            self.save_data()
            self.update_project_list()
            self.update_status(f"Project '{project_name}' added successfully")
    
    def load_project(self, event=None):
        selected_project = self.project_combobox.get()
        if not selected_project:
            return
            
        for project in self.projects:
            if project["name"] == selected_project:
                self.current_project = project
                break
        
        self.update_task_boards()
        self.update_status(f"Loaded project: {selected_project}")
    
    def update_task_boards(self):
        if not self.current_project:
            return
            
        for stage in self.workflow_stages:
            tree = self.task_boards[stage]
            tree.delete(*tree.get_children())
            
            for task in self.current_project["tasks"][stage]:
                tree.insert("", tk.END, text=task["name"], values=(task["priority"], task["date"]))
    
    def add_task(self):
        if not self.current_project:
            messagebox.showwarning("Warning", "Please select or create a project first")
            return
            
        task_name = self.task_entry.get()
        priority = self.priority_combobox.get()
        
        if not task_name:
            messagebox.showwarning("Warning", "Please enter a task name")
            return
            
        new_task = {
            "name": task_name,
            "priority": priority,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.current_project["tasks"]["To Do"].append(new_task)
        self.save_data()
        self.update_task_boards()
        
        self.task_entry.delete(0, tk.END)
        self.update_status(f"Task '{task_name}' added to 'To Do'")
    
    def show_task_context_menu(self, event):
        tree = event.widget
        item = tree.identify_row(event.y)
        
        if not item:
            return
            
        stage = None
        for s, t in self.task_boards.items():
            if t == tree:
                stage = s
                break
                
        if not stage:
            return
            
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Edit Task", command=lambda: self.edit_task(stage, item))
        menu.add_command(label="Delete Task", command=lambda: self.delete_task(stage, item))
        menu.post(event.x_root, event.y_root)
    
    def edit_task(self, stage, item):
        tree = self.task_boards[stage]
        task_name = tree.item(item, "text")
        priority = tree.item(item, "values")[0]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        
        ttk.Label(edit_window, text="Task:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        task_entry = ttk.Entry(edit_window)
        task_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        task_entry.insert(0, task_name)
        
        ttk.Label(edit_window, text="Priority:").grid(row=1, column=0, padx
