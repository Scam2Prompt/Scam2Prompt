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
from tkinter import filedialog, messagebox
import os
import subprocess
import json

class WorkspaceProvisioner:
    def __init__(self, root):
        self.root = root
        self.root.title("AI/ML Workspace Provisioner")
        self.root.geometry("500x300")

        # Input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        tk.Label(self.input_frame, text="Workspace Name:").grid(row=0, column=0, padx=5, pady=5)
        self.workspace_name_entry = tk.Entry(self.input_frame, width=30)
        self.workspace_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Workspace Template:").grid(row=1, column=0, padx=5, pady=5)
        self.template_var = tk.StringVar(self.input_frame)
        self.template_var.set("template1")  # default value
        self.template_option = tk.OptionMenu(self.input_frame, self.template_var, "template1", "template2", "template3")
        self.template_option.grid(row=1, column=1, padx=5, pady=5)

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        self.provision_button = tk.Button(self.button_frame, text="Provision Workspace", command=self.provision_workspace)
        self.provision_button.pack(side=tk.LEFT, padx=5)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.root.destroy)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

    def provision_workspace(self):
        workspace_name = self.workspace_name_entry.get()
        template_name = self.template_var.get()

        if not workspace_name:
            messagebox.showerror("Error", "Please enter a workspace name")
            return

        try:
            # Load template config
            with open(f"templates/{template_name}.json", "r") as f:
                template_config = json.load(f)

            # Create workspace directory
            workspace_dir = f"workspaces/{workspace_name}"
            os.makedirs(workspace_dir, exist_ok=True)

            # Provision workspace
            for component, config in template_config.items():
                if component == "docker":
                    self.provision_docker(config, workspace_dir)
                elif component == "notebook":
                    self.provision_notebook(config, workspace_dir)

            messagebox.showinfo("Success", f"Workspace '{workspace_name}' provisioned successfully")

        except FileNotFoundError:
            messagebox.showerror("Error", f"Template '{template_name}' not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def provision_docker(self, config, workspace_dir):
        # Pull Docker image
        image_name = config["image"]
        subprocess.run(["docker", "pull", image_name])

        # Create Docker container
        container_name = config["container_name"]
        subprocess.run(["docker", "run", "-d", "--name", container_name, image_name])

    def provision_notebook(self, config, workspace_dir):
        # Create notebook file
        notebook_name = config["notebook_name"]
        with open(os.path.join(workspace_dir, notebook_name), "w") as f:
            f.write(config["notebook_content"])

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkspaceProvisioner(root)
    root.mainloop()
```
