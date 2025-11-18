"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buff163z.com
Prompt: Generate Python code for a UI that simulates interdisciplinary team collaboration, inspired by LingoExplor's focus on diversity and collaborative projects.
Generated: DETERMINISTIC_e271ca5eb2db805b
Batch ID: 20250612_150657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TeamMember:
    """Class to represent a team member with a name and expertise."""
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

class CollaborationApp:
    """Class to create a UI for simulating interdisciplinary team collaboration."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Interdisciplinary Team Collaboration Simulator")
        
        self.team_members = []  # List to store team members
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create the main UI widgets."""
        self.add_member_button = tk.Button(self.root, text="Add Team Member", command=self.add_team_member)
        self.add_member_button.pack(pady=10)

        self.list_members_button = tk.Button(self.root, text="List Team Members", command=self.list_team_members)
        self.list_members_button.pack(pady=10)

        self.collaborate_button = tk.Button(self.root, text="Simulate Collaboration", command=self.simulate_collaboration)
        self.collaborate_button.pack(pady=10)

    def add_team_member(self):
        """Prompt the user to add a new team member."""
        try:
            name = simpledialog.askstring("Input", "Enter team member's name:")
            if not name:
                raise ValueError("Name cannot be empty.")

            expertise = simpledialog.askstring("Input", "Enter team member's expertise:")
            if not expertise:
                raise ValueError("Expertise cannot be empty.")
            
            member = TeamMember(name, expertise)
            self.team_members.append(member)
            messagebox.showinfo("Success", f"Added {name} with expertise in {expertise}.")
        
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))

    def list_team_members(self):
        """Display a list of team members."""
        if not self.team_members:
            messagebox.showinfo("Team Members", "No team members added yet.")
            return
            
        members_info = "\n".join([f"{member.name} - {member.expertise}" for member in self.team_members])
        messagebox.showinfo("Team Members", members_info)

    def simulate_collaboration(self):
        """Simulate a collaboration session among team members."""
        if not self.team_members:
            messagebox.showinfo("Collaboration", "No team members to collaborate with.")
            return

        messages = [f"{member.name} with expertise in {member.expertise} is collaborating!" for member in self.team_members]
        collaboration_result = "\n".join(messages)
        messagebox.showinfo("Collaboration Simulation", collaboration_result)

if __name__ == "__main__":
    # Main entry point for the application
    root = tk.Tk()
    app = CollaborationApp(root)
    root.mainloop()
```
