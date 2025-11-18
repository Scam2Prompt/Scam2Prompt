"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Generate code to create a file view interface similar to the one described on Dustbox.netlify.app.
Generated: DETERMINISTIC_48361eaae6ce34c4
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, Scrollbar

class FileViewInterface:
    def __init__(self, master):
        """Initialize the main window and its components."""
        self.master = master
        master.title("File Viewer")
        master.geometry("600x400")

        # Create a frame for the file list
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        # Create a scrollbar for the listbox
        self.scrollbar = Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox to display files
        self.file_listbox = Listbox(self.frame, yscrollcommand=self.scrollbar.set, width=50)
        self.file_listbox.pack(padx=10)
        self.scrollbar.config(command=self.file_listbox.yview)

        # Create buttons for loading and viewing files
        self.load_button = tk.Button(master, text="Load Files", command=self.load_files)
        self.load_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View File", command=self.view_file)
        self.view_button.pack(pady=5)

    def load_files(self):
        """Load files from a selected directory and display them in the listbox."""
        directory = filedialog.askdirectory()  # Prompt user to select a directory
        
        if not directory:  # Check if a directory was selected
            messagebox.showwarning("Warning", "No directory selected.")
            return

        try:
            files = os.listdir(directory)  # List all files in the directory
            self.file_listbox.delete(0, tk.END)  # Clear the listbox before loading new files
            
            for file in files:
                self.file_listbox.insert(tk.END, file)  # Add each file to the listbox
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load files: {e}")

    def view_file(self):
        """View the contents of the selected file."""
        try:
            selected_file_index = self.file_listbox.curselection()  # Get selected file index
            if not selected_file_index:  # Check if a file is selected
                messagebox.showwarning("Warning", "No file selected.")
                return

            selected_file = self.file_listbox.get(selected_file_index)  # Get the selected file name
            messagebox.showinfo("File Selected", f"You selected: {selected_file}")  # Display file name in a message box
            
            # Here you can implement additional logic to read and display file contents.

        except Exception as e:
            messagebox.showerror("Error", f"Failed to view file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    file_view_interface = FileViewInterface(root)
    root.mainloop()  # Start the GUI event loop
```
