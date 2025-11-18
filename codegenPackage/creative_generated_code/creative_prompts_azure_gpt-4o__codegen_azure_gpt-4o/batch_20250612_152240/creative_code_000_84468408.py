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
from tkinter import Tk, Label, Button, Listbox, filedialog, messagebox

# Constants for the Visual Novel Launcher
SUPPORTED_TITLES = [
    "红发小女孩_5分钟的邂逅",
    "巧克力与香子兰 4"
]
KRKR_EXECUTABLE = "krkr.exe"  # Adjust this to the correct executable file for KRKR

class VisualNovelLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("KRKR Visual Novel Launcher")
        self.root.geometry("400x300")
        
        # UI Elements
        self.label = Label(root, text="Select a Visual Novel:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.listbox = Listbox(root, font=("Arial", 12), height=len(SUPPORTED_TITLES))
        for title in SUPPORTED_TITLES:
            self.listbox.insert("end", title)
        self.listbox.pack(padx=10, pady=10, fill="x")
        
        self.launch_button = Button(root, text="Launch Selected", command=self.launch_title)
        self.launch_button.pack(pady=5)
        
        self.add_button = Button(root, text="Add Game Folder", command=self.add_game_folder)
        self.add_button.pack(pady=5)

    def launch_title(self):
        # Get selected title and verify
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a title to launch!")
            return
        
        selected_title = self.listbox.get(selected_index)
        game_folder = os.path.join(os.getcwd(), selected_title)
        
        if not os.path.exists(game_folder):
            messagebox.showerror("Error", f"Game folder for '{selected_title}' not found!")
            return
        
        # Launch KRKR executable
        executable_path = os.path.join(game_folder, KRKR_EXECUTABLE)
        if not os.path.exists(executable_path):
            messagebox.showerror("Error", f"KRKR executable not found in '{game_folder}'!")
            return
        
        try:
            subprocess.Popen([executable_path], cwd=game_folder)
            messagebox.showinfo("Success", f"{selected_title} launched successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch {selected_title}: {str(e)}")

    def add_game_folder(self):
        # Allow the user to add a custom game folder
        folder_path = filedialog.askdirectory(title="Select Game Folder")
        if not folder_path:
            return
        
        game_title = os.path.basename(folder_path)
        if game_title in SUPPORTED_TITLES:
            messagebox.showwarning("Warning", f"'{game_title}' is already in the list!")
            return
        
        # Add folder to the list
        SUPPORTED_TITLES.append(game_title)
        self.listbox.insert("end", game_title)
        messagebox.showinfo("Success", f"'{game_title}' added successfully!")

# Entry point of the application
if __name__ == "__main__":
    # Create main application window
    root = Tk()
    app = VisualNovelLauncher(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
```
