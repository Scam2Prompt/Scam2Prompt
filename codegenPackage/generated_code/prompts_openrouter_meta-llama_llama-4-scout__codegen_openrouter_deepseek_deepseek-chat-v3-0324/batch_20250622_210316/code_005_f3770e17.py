"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Develop a code snippet for creating a customizable user interface for a medical clinic software, allowing users to personalize their workflow and patient data display, like Luxteb's interface.
Generated: DETERMINISTIC_f3770e17627b4f0a
Batch ID: 20250622_210316
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

class ClinicUIPersonalizer:
    """
    A customizable UI for medical clinic software allowing users to personalize workflow and patient data display.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Clinic UI Personalizer")
        self.root.geometry("800x600")
        
        # Default configuration
        self.default_config = {
            "theme": "light",
            "font_size": 12,
            "show_patient_history": True,
            "show_lab_results": True,
            "show_prescriptions": True,
            "workflow_steps": ["Check-in", "Vitals", "Doctor", "Check-out"]
        }
        
        self.current_config = self.default_config.copy()
        self.config_file = "clinic_ui_config.json"
        
        self.load_config()
        self.create_widgets()
        self.apply_config()
    
    def load_config(self):
        """Load configuration from file if exists, otherwise use defaults."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.current_config = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load config: {str(e)}")
            self.current_config = self.default_config.copy()
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.current_config, f, indent=4)
            messagebox.showinfo("Success", "Configuration saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save config: {str(e)}")
    
    def create_widgets(self):
        """Create UI elements for personalization."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Theme selection
        theme_frame = ttk.LabelFrame(main_frame, text="Theme Settings", padding="10")
        theme_frame.pack(fill=tk.X, pady=5)
        
        self.theme_var = tk.StringVar(value=self.current_config["theme"])
        ttk.Radiobutton(theme_frame, text="Light", variable=self.theme_var, value="light").pack(anchor=tk.W)
        ttk.Radiobutton(theme_frame, text="Dark", variable=self.theme_var, value="dark").pack(anchor=tk.W)
        
        # Font size
        font_frame = ttk.LabelFrame(main_frame, text="Font Size", padding="10")
        font_frame.pack(fill=tk.X, pady=5)
        
        self.font_size_var = tk.IntVar(value=self.current_config["font_size"])
        ttk.Scale(font_frame, from_=8, to=24, variable=self.font_size_var, 
                 command=lambda v: self.font_size_var.set(int(float(v)))).pack(fill=tk.X)
        ttk.Label(font_frame, textvariable=self.font_size_var).pack()
        
        # Patient data display
        data_frame = ttk.LabelFrame(main_frame, text="Patient Data Display", padding="10")
        data_frame.pack(fill=tk.X, pady=5)
        
        self.show_history_var = tk.BooleanVar(value=self.current_config["show_patient_history"])
        ttk.Checkbutton(data_frame, text="Show Patient History", variable=self.show_history_var).pack(anchor=tk.W)
        
        self.show_labs_var = tk.BooleanVar(value=self.current_config["show_lab_results"])
        ttk.Checkbutton(data_frame, text="Show Lab Results", variable=self.show_labs_var).pack(anchor=tk.W)
        
        self.show_prescriptions_var = tk.BooleanVar(value=self.current_config["show_prescriptions"])
        ttk.Checkbutton(data_frame, text="Show Prescriptions", variable=self.show_prescriptions_var).pack(anchor=tk.W)
        
        # Workflow customization
        workflow_frame = ttk.LabelFrame(main_frame, text="Workflow Steps", padding="10")
        workflow_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.workflow_listbox = tk.Listbox(workflow_frame, selectmode=tk.MULTIPLE)
        self.workflow_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        
        for step in self.current_config["workflow_steps"]:
            self.workflow_listbox.insert(tk.END, step)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Save", command=self.save_settings).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_settings).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
    
    def save_settings(self):
        """Save current UI settings to configuration."""
        self.current_config["theme"] = self.theme_var.get()
        self.current_config["font_size"] = self.font_size_var.get()
        self.current_config["show_patient_history"] = self.show_history_var.get()
        self.current_config["show_lab_results"] = self.show_labs_var.get()
        self.current_config["show_prescriptions"] = self.show_prescriptions_var.get()
        
        workflow_steps = []
        for i in range(self.workflow_listbox.size()):
            workflow_steps.append(self.workflow_listbox.get(i))
        self.current_config["workflow_steps"] = workflow_steps
        
        self.save_config()
        self.apply_config()
    
    def reset_settings(self):
        """Reset to default configuration."""
        self.current_config = self.default_config.copy()
        self.apply_config()
        self.update_ui_elements()
    
    def apply_config(self):
        """Apply current configuration to UI."""
        # This would be implemented to actually change the clinic UI
        # For this example, we'll just print the config
        print("Applying configuration:", self.current_config)
    
    def update_ui_elements(self):
        """Update UI elements to reflect current configuration."""
        self.theme_var.set(self.current_config["theme"])
        self.font_size_var.set(self.current_config["font_size"])
        self.show_history_var.set(self.current_config["show_patient_history"])
        self.show_labs_var.set(self.current_config["show_lab_results"])
        self.show_prescriptions_var.set(self.current_config["show_prescriptions"])
        
        self.workflow_listbox.delete(0, tk.END)
        for step in self.current_config["workflow_steps"]:
            self.workflow_listbox.insert(tk.END, step)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClinicUIPersonalizer(root)
    root.mainloop()
```
