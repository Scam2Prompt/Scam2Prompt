"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Write Python code to provision preconfigured AI/ML workspaces using a graphical user interface, as described on the ReadyPlayAI platform.
Generated: DETERMINISTIC_bb8fa0100b28cdcb
Batch ID: 20250612_154302
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
import os
import json

# Configuration for preconfigured workspaces
WORKSPACES = {
    "Data Science Workspace": {
        "tools": ["Jupyter Notebook", "Pandas", "NumPy", "Matplotlib"],
        "description": "A workspace for data analysis and visualization."
    },
    "Machine Learning Workspace": {
        "tools": ["TensorFlow", "Keras", "Scikit-learn"],
        "description": "A workspace for building machine learning models."
    },
    "Deep Learning Workspace": {
        "tools": ["PyTorch", "TensorFlow"],
        "description": "A workspace for deep learning applications."
    }
}

# Function to provision a workspace
def provision_workspace(workspace_name):
    try:
        workspace_config = WORKSPACES.get(workspace_name)
        if not workspace_config:
            raise ValueError("Selected workspace configuration not found.")
        
        # Simulating workspace provisioning
        workspace_dir = f"./{workspace_name.replace(' ', '_')}_Workspace"
        os.makedirs(workspace_dir, exist_ok=True)  # Create workspace directory
        
        # Save configuration to a JSON file inside the workspace
        config_path = os.path.join(workspace_dir, "config.json")
        with open(config_path, "w") as config_file:
            json.dump(workspace_config, config_file, indent=4)

        messagebox.showinfo("Success", f"{workspace_name} successfully provisioned!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to provision workspace: {str(e)}")

# GUI application
class WorkspaceProvisioningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI/ML Workspace Provisioning")

        # Instructions label
        self.label = tk.Label(root, text="Select a workspace to provision:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Dropdown menu for workspace selection
        self.workspace_var = tk.StringVar(value="Choose a workspace")
        self.dropdown = tk.OptionMenu(root, self.workspace_var, *WORKSPACES.keys())
        self.dropdown.pack(pady=10)

        # Provision button
        self.provision_button = tk.Button(root, text="Provision Workspace", command=self.provision_selected_workspace)
        self.provision_button.pack(pady=20)

    def provision_selected_workspace(self):
        selected_workspace = self.workspace_var.get()
        if selected_workspace == "Choose a workspace":
            messagebox.showwarning("Warning", "Please select a workspace.")
        else:
            provision_workspace(selected_workspace)

# Main function to run the GUI application
def main():
    root = tk.Tk()
    app = WorkspaceProvisioningApp(root)
    root.geometry("400x200")  # Set window size
    root.mainloop()

if __name__ == "__main__":
    main()
```
