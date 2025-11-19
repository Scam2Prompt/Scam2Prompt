"""
Generated Code Metadata:
========================
Original URL: https://autoswiftly.com
Prompt: How can I implement a user-friendly interface for a car selection tool based on AutoSwiftly's five-step process?
Generated: DETERMINISTIC_58b74ebaeedc5daa
Batch ID: 20250612_162051
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

class CarSelectionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoSwiftly Car Selection Tool")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Initialize steps
        self.current_step = 0
        self.steps = [
            "Select Vehicle Type",
            "Choose Budget Range",
            "Select Fuel Type",
            "Choose Transmission",
            "Select Additional Features"
        ]
        
        # User selections storage
        self.selections = {
            "vehicle_type": None,
            "budget_range": None,
            "fuel_type": None,
            "transmission": None,
            "features": []
        }
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Progress bar
        self.progress_label = ttk.Label(
            self.main_frame, 
            text=f"Step {self.current_step + 1} of {len(self.steps)}: {self.steps[self.current_step]}"
        )
        self.progress_label.pack(pady=10)
        
        self.progress_bar = ttk.Progressbar(
            self.main_frame, 
            orient=tk.HORIZONTAL, 
            length=600, 
            mode='determinate',
            maximum=len(self.steps)
        )
        self.progress_bar.pack(pady=5)
        self.progress_bar['value'] = self.current_step + 1
        
        # Content frame (changes based on step)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Navigation buttons
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(fill=tk.X, pady=10)
        
        self.back_btn = ttk.Button(
            self.nav_frame, 
            text="Back", 
            command=self.previous_step,
            state=tk.DISABLED
        )
        self.back_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(
            self.nav_frame, 
            text="Next", 
            command=self.next_step
        )
        self.next_btn.pack(side=tk.RIGHT, padx=5)
        
        # Load current step content
        self.load_step_content()
    
    def load_step_content(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Update progress
        self.progress_label.config(
            text=f"Step {self.current_step + 1} of {len(self.steps)}: {self.steps[self.current_step]}"
        )
        self.progress_bar['value'] = self.current_step + 1
        
        # Load appropriate content based on current step
        if self.current_step == 0:  # Vehicle Type
            self.load_vehicle_type_step()
        elif self.current_step == 1:  # Budget Range
            self.load_budget_step()
        elif self.current_step == 2:  # Fuel Type
            self.load_fuel_type_step()
        elif self.current_step == 3:  # Transmission
            self.load_transmission_step()
        elif self.current_step == 4:  # Features
            self.load_features_step()
    
    def load_vehicle_type_step(self):
        label = ttk.Label(
            self.content_frame, 
            text="Select your preferred vehicle type:",
            font=('Arial', 12)
        )
        label.pack(pady=10)
        
        options = ["Sedan", "SUV", "Truck", "Hatchback", "Coupe", "Convertible"]
        self.vehicle_type_var = tk.StringVar()
        
        for option in options:
            rb = ttk.Radiobutton(
                self.content_frame,
                text=option,
                variable=self.vehicle_type_var,
                value=option
            )
            rb.pack(anchor=tk.W, padx=20, pady=5)
    
    def load_budget_step(self):
        label = ttk.Label(
            self.content_frame, 
            text="Select your budget range:",
            font=('Arial', 12)
        )
        label.pack(pady=10)
        
        options = [
            "Under $20,000",
            "$20,000 - $30,000",
            "$30,000 - $40,000",
            "$40,000 - $50,000",
            "Over $50,000"
        ]
        self.budget_var = tk.StringVar()
        
        for option in options:
            rb = ttk.Radiobutton(
                self.content_frame,
                text=option,
                variable=self.budget_var,
                value=option
            )
            rb.pack(anchor=tk.W, padx=20, pady=5)
    
    def load_fuel_type_step(self):
        label = ttk.Label(
            self.content_frame, 
            text="Select your preferred fuel type:",
            font=('Arial', 12)
        )
        label.pack(pady=10)
        
        options = ["Gasoline", "Diesel", "Hybrid", "Electric", "Flex-Fuel"]
        self.fuel_type_var = tk.StringVar()
        
        for option in options:
            rb = ttk.Radiobutton(
                self.content_frame,
                text=option,
                variable=self.fuel_type_var,
                value=option
            )
            rb.pack(anchor=tk.W, padx=20, pady=5)
    
    def load_transmission_step(self):
        label = ttk.Label(
            self.content_frame, 
            text="Select your preferred transmission type:",
            font=('Arial', 12)
        )
        label.pack(pady=10)
        
        options = ["Automatic", "Manual", "Semi-Automatic", "CVT"]
        self.transmission_var = tk.StringVar()
        
        for option in options:
            rb = ttk.Radiobutton(
                self.content_frame,
                text=option,
                variable=self.transmission_var,
                value=option
            )
            rb.pack(anchor=tk.W, padx=20, pady=5)
    
    def load_features_step(self):
        label = ttk.Label(
            self.content_frame, 
            text="Select additional features (multiple selections allowed):",
            font=('Arial', 12)
        )
        label.pack(pady=10)
        
        options = [
            "Sunroof", "Leather Seats", "Navigation System", 
            "Bluetooth", "Backup Camera", "Heated Seats",
            "Apple CarPlay/Android Auto", "Premium Sound System"
        ]
        self.feature_vars = []
        
        for option in options:
            var = tk.IntVar()
            cb = ttk.Checkbutton(
                self.content_frame,
                text=option,
                variable=var
            )
            cb.pack(anchor=tk.W, padx=20, pady=5)
            self.feature_vars.append((option, var))
    
    def validate_current_step(self):
        if self.current_step == 0 and not self.vehicle_type_var.get():
            messagebox.showwarning("Selection Required", "Please select a vehicle type.")
            return False
        elif self.current_step == 1 and not self.budget_var.get():
            messagebox.showwarning("Selection Required", "Please select a budget range.")
            return False
        elif self.current_step == 2 and not self.fuel_type_var.get():
            messagebox.showwarning("Selection Required", "Please select a fuel type.")
            return False
        elif self.current_step == 3 and not self.transmission_var.get():
            messagebox.showwarning("Selection Required", "Please select a transmission type.")
            return False
        return True
    
    def save_current_selection(self):
        if self.current_step == 0:
            self.selections["vehicle_type"] = self.vehicle_type_var.get()
        elif self.current_step == 1:
            self.selections["budget_range"] = self.budget_var.get()
        elif self.current_step == 2:
            self.selections["fuel_type"] = self.fuel_type_var.get()
        elif self.current_step == 3:
            self.selections["transmission"] = self.transmission_var.get()
        elif self.current_step == 4:
            selected_features = [option for option, var in self.feature_vars if var.get()]
            self.selections["features"] = selected_features
    
    def next_step(self):
        if not self.validate_current_step():
            return
        
        self.save_current_selection()
        
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.load_step_content()
            
            # Update button states
            self.back_btn.config(state=tk.NORMAL)
            if self.current_step == len(self.steps) - 1:
