"""
Generated Code Metadata:
========================
Original URL: https://buff163z.com
Prompt: Generate Python code for a UI that simulates interdisciplinary team collaboration, inspired by LingoExplor's focus on diversity and collaborative projects.
Generated: DETERMINISTIC_e271ca5eb2db805b
Batch ID: 20250612_150657
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
from random import choice

class TeamCollaborationUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interdisciplinary Team Collaboration Simulator")
        self.root.geometry("800x600")

        # Create main notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create frames for each tab
        self.project_frame = tk.Frame(self.notebook)
        self.team_frame = tk.Frame(self.notebook)
        self.collaboration_frame = tk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.project_frame, text="Project")
        self.notebook.add(self.team_frame, text="Team")
        self.notebook.add(self.collaboration_frame, text="Collaboration")

        # Project tab
        self.project_label = tk.Label(self.project_frame, text="Project Name:")
        self.project_label.pack()
        self.project_entry = tk.Entry(self.project_frame)
        self.project_entry.pack()
        self.project_description_label = tk.Label(self.project_frame, text="Project Description:")
        self.project_description_label.pack()
        self.project_description_text = tk.Text(self.project_frame, height=10, width=50)
        self.project_description_text.pack()
        self.project_create_button = tk.Button(self.project_frame, text="Create Project", command=self.create_project)
        self.project_create_button.pack()

        # Team tab
        self.team_label = tk.Label(self.team_frame, text="Team Members:")
        self.team_label.pack()
        self.team_listbox = tk.Listbox(self.team_frame)
        self.team_listbox.pack()
        self.team_add_label = tk.Label(self.team_frame, text="Add Team Member:")
        self.team_add_label.pack()
        self.team_add_entry = tk.Entry(self.team_frame)
        self.team_add_entry.pack()
        self.team_add_button = tk.Button(self.team_frame, text="Add to Team", command=self.add_team_member)
        self.team_add_button.pack()

        # Collaboration tab
        self.collaboration_label = tk.Label(self.collaboration_frame, text="Collaboration Ideas:")
        self.collaboration_label.pack()
        self.collaboration_listbox = tk.Listbox(self.collaboration_frame)
        self.collaboration_listbox.pack()
        self.collaboration_add_label = tk.Label(self.collaboration_frame, text="Add Collaboration Idea:")
        self.collaboration_add_label.pack()
        self.collaboration_add_entry = tk.Entry(self.collaboration_frame)
        self.collaboration_add_entry.pack()
        self.collaboration_add_button = tk.Button(self.collaboration_frame, text="Add Collaboration Idea", command=self.add_collaboration_idea)
        self.collaboration_add_button.pack()

        # Initialize project, team, and collaboration data
        self.project_data = {}
        self.team_members = []
        self.collaboration_ideas = []

    def create_project(self):
        project_name = self.project_entry.get()
        project_description = self.project_description_text.get("1.0", tk.END)
        if project_name and project_description:
            self.project_data["name"] = project_name
            self.project_data["description"] = project_description
            messagebox.showinfo("Project Created", f"Project '{project_name}' created successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_team_member(self):
        team_member = self.team_add_entry.get()
        if team_member:
            self.team_members.append(team_member)
            self.team_listbox.insert(tk.END, team_member)
            self.team_add_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a team member's name.")

    def add_collaboration_idea(self):
        collaboration_idea = self.collaboration_add_entry.get()
        if collaboration_idea:
            self.collaboration_ideas.append(collaboration_idea)
            self.collaboration_listbox.insert(tk.END, collaboration_idea)
            self.collaboration_add_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a collaboration idea.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamCollaborationUI(root)
    app.run()
```
