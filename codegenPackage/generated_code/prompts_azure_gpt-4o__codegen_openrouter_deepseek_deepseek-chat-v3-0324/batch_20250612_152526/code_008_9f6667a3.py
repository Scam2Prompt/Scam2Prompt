"""
Generated Code Metadata:
========================
Original URL: https://digisou-ltd.com
Prompt: Write code for a UI/UX design prototype that matches the process outlined in DigiSou's software development workflow.
Generated: DETERMINISTIC_9f6667a334285d06
Batch ID: 20250612_152526
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
import json
import os

class DigiSouPrototype:
    def __init__(self, root):
        self.root = root
        self.root.title("DigiSou UI/UX Design Prototype")
        self.root.geometry("900x600")
        self.current_step = 0
        self.project_data = {
            "project_name": "",
            "requirements": [],
            "wireframes": [],
            "mockups": [],
            "feedback": [],
            "final_design": ""
        }
        
        self.setup_ui()
        self.load_data()
    
    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header = ttk.Label(
            self.main_frame, 
            text="DigiSou Design Workflow", 
            font=('Helvetica', 16, 'bold')
        )
        self.header.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.main_frame, 
            orient=tk.HORIZONTAL, 
            length=800, 
            mode='determinate'
        )
        self.progress.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Steps frame
        self.steps_frame = ttk.Frame(self.main_frame)
        self.steps_frame.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        # Content frame
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Navigation buttons
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.prev_btn = ttk.Button(
            self.nav_frame, 
            text="Previous", 
            command=self.prev_step,
            state=tk.DISABLED
        )
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(
            self.nav_frame, 
            text="Next", 
            command=self.next_step
        )
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        self.save_btn = ttk.Button(
            self.nav_frame, 
            text="Save", 
            command=self.save_data
        )
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=3)
        self.main_frame.rowconfigure(2, weight=1)
        
        # Initialize steps
        self.steps = [
            self.create_step_project_info,
            self.create_step_requirements,
            self.create_step_wireframes,
            self.create_step_mockups,
            self.create_step_feedback,
            self.create_step_final_design
        ]
        
        self.update_ui()
    
    def create_step_project_info(self):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Project info form
        ttk.Label(self.content_frame, text="Project Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.project_name_entry = ttk.Entry(self.content_frame, width=40)
        self.project_name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.project_name_entry.insert(0, self.project_data["project_name"])
        
        ttk.Label(self.content_frame, text="Project Description:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.project_desc_text = tk.Text(self.content_frame, width=50, height=10)
        self.project_desc_text.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Add step description
        ttk.Label(
            self.steps_frame, 
            text="1. Project Information\n\nEnter basic project details to get started.",
            justify=tk.LEFT
        ).pack(anchor=tk.W)
    
    def create_step_requirements(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Requirements list
        ttk.Label(self.content_frame, text="Requirements:").grid(row=0, column=0, sticky=tk.W)
        
        self.requirements_list = tk.Listbox(
            self.content_frame, 
            width=50, 
            height=10,
            selectmode=tk.SINGLE
        )
        self.requirements_list.grid(row=1, column=0, sticky=tk.W)
        
        for req in self.project_data["requirements"]:
            self.requirements_list.insert(tk.END, req)
        
        # Requirement controls
        control_frame = ttk.Frame(self.content_frame)
        control_frame.grid(row=1, column=1, sticky=tk.NW, padx=10)
        
        self.req_entry = ttk.Entry(control_frame, width=30)
        self.req_entry.pack(pady=5)
        
        ttk.Button(
            control_frame, 
            text="Add", 
            command=self.add_requirement
        ).pack(pady=2)
        
        ttk.Button(
            control_frame, 
            text="Remove", 
            command=self.remove_requirement
        ).pack(pady=2)
        
        # Step description
        ttk.Label(
            self.steps_frame, 
            text="2. Requirements Gathering\n\nList all functional and non-functional requirements.",
            justify=tk.LEFT
        ).pack(anchor=tk.W)
    
    def create_step_wireframes(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Wireframes list
        ttk.Label(self.content_frame, text="Wireframes:").grid(row=0, column=0, sticky=tk.W)
        
        self.wireframes_list = tk.Listbox(
            self.content_frame, 
            width=50, 
            height=10,
            selectmode=tk.SINGLE
        )
        self.wireframes_list.grid(row=1, column=0, sticky=tk.W)
        
        for wireframe in self.project_data["wireframes"]:
            self.wireframes_list.insert(tk.END, wireframe)
        
        # Wireframe controls
        control_frame = ttk.Frame(self.content_frame)
        control_frame.grid(row=1, column=1, sticky=tk.NW, padx=10)
        
        self.wireframe_entry = ttk.Entry(control_frame, width=30)
        self.wireframe_entry.pack(pady=5)
        
        ttk.Button(
            control_frame, 
            text="Add", 
            command=self.add_wireframe
        ).pack(pady=2)
        
        ttk.Button(
            control_frame, 
            text="Remove", 
            command=self.remove_wireframe
        ).pack(pady=2)
        
        # Step description
        ttk.Label(
            self.steps_frame, 
            text="3. Wireframing\n\nCreate low-fidelity wireframes for key screens.",
            justify=tk.LEFT
        ).pack(anchor=tk.W)
    
    def create_step_mockups(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Mockups list
        ttk.Label(self.content_frame, text="Mockups:").grid(row=0, column=0, sticky=tk.W)
        
        self.mockups_list = tk.Listbox(
            self.content_frame, 
            width=50, 
            height=10,
            selectmode=tk.SINGLE
        )
        self.mockups_list.grid(row=1, column=0, sticky=tk.W)
        
        for mockup in self.project_data["mockups"]:
            self.mockups_list.insert(tk.END, mockup)
        
        # Mockup controls
        control_frame = ttk.Frame(self.content_frame)
        control_frame.grid(row=1, column=1, sticky=tk.NW, padx=10)
        
        self.mockup_entry = ttk.Entry(control_frame, width=30)
        self.mockup_entry.pack(pady=5)
        
        ttk.Button(
            control_frame, 
            text="Add", 
            command=self.add_mockup
        ).pack(pady=2)
        
        ttk.Button(
            control_frame, 
            text="Remove", 
            command=self.remove_mockup
        ).pack(pady=2)
        
        # Step description
        ttk.Label(
            self.steps_frame, 
            text="4. High-Fidelity Mockups\n\nCreate polished visual designs with colors,
