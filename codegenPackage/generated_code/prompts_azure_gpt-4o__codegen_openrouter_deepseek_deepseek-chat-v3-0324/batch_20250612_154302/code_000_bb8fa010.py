"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: Write Python code to provision preconfigured AI/ML workspaces using a graphical user interface, as described on the ReadyPlayAI platform.
Generated: DETERMINISTIC_bb8fa0100b28cdcb
Batch ID: 20250612_154302
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
import subprocess
import sys
from typing import Dict, Optional, List

class AIWorkspaceProvisioner:
    """GUI application for provisioning preconfigured AI/ML workspaces."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the application with main window."""
        self.root = root
        self.root.title("ReadyPlayAI Workspace Provisioner")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load configuration
        self.config = self._load_config()
        if not self.config:
            messagebox.showerror("Error", "Failed to load configuration. Exiting.")
            sys.exit(1)
            
        self._setup_ui()
        
    def _load_config(self) -> Optional[Dict]:
        """Load workspace configurations from file."""
        config_path = os.path.join(os.path.dirname(__file__), "workspace_configs.json")
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            messagebox.showerror("Config Error", f"Failed to load config: {str(e)}")
            return None
    
    def _setup_ui(self):
        """Set up the main UI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Workspace selection
        ttk.Label(main_frame, text="Select Workspace Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.workspace_var = tk.StringVar()
        self.workspace_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.workspace_var,
            values=list(self.config["workspace_types"].keys()),
            state="readonly"
        )
        self.workspace_dropdown.grid(row=0, column=1, sticky=tk.EW, pady=5)
        self.workspace_dropdown.bind("<<ComboboxSelected>>", self._on_workspace_select)
        
        # Configuration options frame
        self.config_frame = ttk.LabelFrame(main_frame, text="Workspace Configuration", padding="10")
        self.config_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=10)
        self.config_frame.columnconfigure(1, weight=1)
        
        # Resource allocation
        ttk.Label(self.config_frame, text="CPU Cores:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.cpu_var = tk.StringVar(value="4")
        ttk.Entry(self.config_frame, textvariable=self.cpu_var).grid(row=0, column=1, sticky=tk.EW, pady=2)
        
        ttk.Label(self.config_frame, text="Memory (GB):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.mem_var = tk.StringVar(value="16")
        ttk.Entry(self.config_frame, textvariable=self.mem_var).grid(row=1, column=1, sticky=tk.EW, pady=2)
        
        ttk.Label(self.config_frame, text="GPU Enabled:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.gpu_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.config_frame, variable=self.gpu_var).grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Workspace name
        ttk.Label(self.config_frame, text="Workspace Name:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.name_var = tk.StringVar()
        ttk.Entry(self.config_frame, textvariable=self.name_var).grid(row=3, column=1, sticky=tk.EW, pady=2)
        
        # Description
        ttk.Label(self.config_frame, text="Description:").grid(row=4, column=0, sticky=tk.NW, pady=2)
        self.desc_var = tk.StringVar()
        self.desc_text = tk.Text(self.config_frame, height=4, width=40)
        self.desc_text.grid(row=4, column=1, sticky=tk.EW, pady=2)
        
        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, sticky=tk.E, pady=10)
        
        ttk.Button(button_frame, text="Provision", command=self._provision_workspace).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.root.quit).pack(side=tk.RIGHT)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN).grid(
            row=3, column=0, columnspan=2, sticky=tk.EW, pady=5
        )
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
    def _on_workspace_select(self, event):
        """Handle workspace type selection."""
        selected = self.workspace_var.get()
        if selected in self.config["workspace_types"]:
            ws_config = self.config["workspace_types"][selected]
            self.cpu_var.set(str(ws_config.get("default_cpu", "4")))
            self.mem_var.set(str(ws_config.get("default_mem", "16")))
            self.gpu_var.set(ws_config.get("gpu_support", False))
            
    def _validate_inputs(self) -> bool:
        """Validate user inputs before provisioning."""
        if not self.workspace_var.get():
            messagebox.showerror("Error", "Please select a workspace type")
            return False
            
        if not self.name_var.get().strip():
            messagebox.showerror("Error", "Workspace name cannot be empty")
            return False
            
        try:
            cpu = int(self.cpu_var.get())
            mem = int(self.mem_var.get())
            if cpu <= 0 or mem <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "CPU and Memory must be positive integers")
            return False
            
        return True
    
    def _provision_workspace(self):
        """Provision the selected workspace with given configuration."""
        if not self._validate_inputs():
            return
            
        workspace_type = self.workspace_var.get()
        workspace_name = self.name_var.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        
        config = {
            "type": workspace_type,
            "name": workspace_name,
            "description": description,
            "cpu": int(self.cpu_var.get()),
            "memory": int(self.mem_var.get()),
            "gpu": self.gpu_var.get()
        }
        
        self.status_var.set("Provisioning...")
        self.root.update()
        
        try:
            # Simulate provisioning process
            result = self._execute_provisioning(config)
            if result:
                messagebox.showinfo("Success", f"Workspace '{workspace_name}' provisioned successfully!")
                self.status_var.set("Ready")
            else:
                messagebox.showerror("Error", "Failed to provision workspace")
                self.status_var.set("Provisioning failed")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error during provisioning")
            
    def _execute_provisioning(self, config: Dict) -> bool:
        """
        Execute the actual provisioning process.
        In a real implementation, this would interface with cloud APIs or infrastructure tools.
        """
        # This is a mock implementation - replace with actual provisioning logic
        print(f"Provisioning workspace with config: {config}")
        
        # Simulate a delay for the provisioning process
        import time
        time.sleep(2)
        
        # Simulate random success/failure
        import random
        return random.random() > 0.2  # 80% success rate for demo purposes

def main():
    """Entry point for the application."""
    root = tk.Tk()
    app = AIWorkspaceProvisioner(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```
