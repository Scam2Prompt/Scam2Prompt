"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuki.top
Prompt: Write code to create a KRKR-based visual novel launcher that supports titles like "红发小女孩_5分钟的邂逅" and "巧克力与香子兰 4" as listed on the 朗月天明 website.
Generated: DETERMINISTIC_8446840898a9850b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys
from tkinter import Tk, Label, Button, Listbox, Scrollbar, END, messagebox

class VNLauncher:
    """
    A simple Visual Novel launcher for KRKR-based titles.
    """

    def __init__(self, master):
        self.master = master
        self.master.title("Visual Novel Launcher")
        self.master.geometry("400x300")

        # Titles list
        self.titles = [
            "红发小女孩_5分钟的邂逅",
            "巧克力与香子兰 4"
        ]

        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create and place UI elements for the launcher."""
        self.label = Label(self.master, text="Select a Visual Novel to Launch")
        self.label.pack(pady=10)

        self.listbox = Listbox(self.master)
        self.listbox.pack(fill='both', expand=True, padx=10)

        # Add titles to the listbox
        for title in self.titles:
            self.listbox.insert(END, title)

        # Scrollbar for listbox
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.pack(side='right', fill='y')
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Launch button
        self.launch_button = Button(self.master, text="Launch", command=self.launch_vn)
        self.launch_button.pack(pady=10)

    def launch_vn(self):
        """Launch the selected Visual Novel."""
        selected_title = self.listbox.get(self.listbox.curselection())

        # Define path to the Visual Novel executable
        vn_path = self.get_vn_path(selected_title)
        
        if vn_path:
            try:
                # Attempt to launch the executable
                subprocess.run([vn_path], check=True)
            except subprocess.CalledProcessError as e:
                self.show_error(f"Failed to launch {selected_title}.\nError: {e}")
            except FileNotFoundError:
                self.show_error(f"{selected_title} executable not found.")
        else:
            self.show_error("Selected title path is invalid.")

    def get_vn_path(self, title):
        """Return the file path of the selected Visual Novel."""
        # Assuming all executables are located in a specific directory
        vn_directory = "path/to/visual_novels"  # Change this to the actual path
        vn_file_name = title.replace(" ", "_") + ".exe"  # Assuming .exe extension
        vn_full_path = os.path.join(vn_directory, vn_file_name)

        return vn_full_path if os.path.isfile(vn_full_path) else None

    def show_error(self, message):
        """Display an error message in a message box."""
        messagebox.showerror("Error", message)


if __name__ == "__main__":
    try:
        root = Tk()
        app = VNLauncher(root)
        root.mainloop()
    except Exception as e:
        # Handle any unexpected errors that may occur during startup
        sys.exit(f"An error occurred: {e}")
```
