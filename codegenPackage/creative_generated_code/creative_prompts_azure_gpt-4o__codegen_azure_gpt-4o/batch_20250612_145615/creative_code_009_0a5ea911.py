"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Write code to create a user-friendly interface for selecting label types (e.g., clothing labels, pencil labels) and uploading designs, based on the product categories on Labelmystuff.com.
Generated: DETERMINISTIC_0a5ea91131cae396
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import filedialog, messagebox


class LabelSelectorApp:
    def __init__(self, root):
        """
        Initialize the Label Selector Application.
        """
        self.root = root
        self.root.title("Label Type Selector and Design Uploader")
        self.root.geometry("400x300")  # Set default window size

        # Available label types
        self.label_types = ["Clothing Labels", "Pencil Labels", "Bag Labels", "Bottle Labels"]

        # Selected label type variable
        self.selected_label_type = tk.StringVar(value=self.label_types[0])

        # Create the interface
        self.create_widgets()

    def create_widgets(self):
        """
        Create all the widgets for the application.
        """
        # Label for label type selection
        tk.Label(self.root, text="Select Label Type:", font=("Arial", 12)).pack(pady=10)

        # Dropdown menu for label type selection
        label_menu = tk.OptionMenu(self.root, self.selected_label_type, *self.label_types)
        label_menu.config(width=20)
        label_menu.pack(pady=5)

        # Button for uploading design file
        upload_button = tk.Button(self.root, text="Upload Design", command=self.upload_design, font=("Arial", 12))
        upload_button.pack(pady=20)

        # Exit button
        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12))
        exit_button.pack(pady=5)

    def upload_design(self):
        """
        Handle file upload and display selected file.
        """
        try:
            # Open file dialog for selecting design file
            file_path = filedialog.askopenfilename(
                title="Select Design File",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
            )

            if file_path:
                # Display success message with the selected label type and file
                selected_label = self.selected_label_type.get()
                messagebox.showinfo(
                    "File Uploaded",
                    f"Design for '{selected_label}' uploaded successfully!\nFile: {file_path}"
                )
            else:
                # Handle case where no file was selected
                messagebox.showwarning("No File Selected", "Please select a file to upload.")
        except Exception as e:
            # Handle unexpected errors
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Create and run the Label Selector application
    app = LabelSelectorApp(root)

    # Start the Tkinter event loop
    root.mainloop()
```
