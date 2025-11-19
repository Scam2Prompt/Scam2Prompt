"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write code to create a user-friendly interface for selecting label types (e.g., clothing labels, pencil labels) and uploading designs, based on the product categories on Labelmystuff.com.
Generated: DETERMINISTIC_0a5ea91131cae396
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class LabelDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LabelMyStuff - Design Uploader")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TCombobox', font=('Arial', 10))
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.header = ttk.Label(
            self.main_frame, 
            text="Create Custom Labels", 
            style='Header.TLabel'
        )
        self.header.pack(pady=(0, 20))
        
        # Label type selection
        self.label_type_frame = ttk.Frame(self.main_frame)
        self.label_type_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(
            self.label_type_frame, 
            text="Select Label Type:"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.label_types = [
            "Clothing Labels",
            "Pencil Labels",
            "Book Labels",
            "Jar Labels",
            "Luggage Tags",
            "Bottle Labels",
            "Gift Tags"
        ]
        
        self.label_type_var = tk.StringVar()
        self.label_type_dropdown = ttk.Combobox(
            self.label_type_frame,
            textvariable=self.label_type_var,
            values=self.label_types,
            state="readonly"
        )
        self.label_type_dropdown.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.label_type_dropdown.current(0)
        
        # Design upload section
        self.upload_frame = ttk.Frame(self.main_frame)
        self.upload_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - upload controls
        self.controls_frame = ttk.Frame(self.upload_frame)
        self.controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        
        ttk.Label(
            self.controls_frame,
            text="Upload Your Design:"
        ).pack(pady=(0, 10))
        
        self.upload_btn = ttk.Button(
            self.controls_frame,
            text="Browse Files",
            command=self.browse_files
        )
        self.upload_btn.pack(fill=tk.X, pady=(0, 20))
        
        self.design_name_var = tk.StringVar()
        ttk.Label(
            self.controls_frame,
            text="Design Name:"
        ).pack()
        
        self.design_name_entry = ttk.Entry(
            self.controls_frame,
            textvariable=self.design_name_var
        )
        self.design_name_entry.pack(fill=tk.X, pady=(0, 20))
        
        self.submit_btn = ttk.Button(
            self.controls_frame,
            text="Submit Design",
            command=self.submit_design,
            state=tk.DISABLED
        )
        self.submit_btn.pack(fill=tk.X)
        
        # Right panel - preview
        self.preview_frame = ttk.Frame(self.upload_frame)
        self.preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        ttk.Label(
            self.preview_frame,
            text="Design Preview:"
        ).pack()
        
        self.preview_canvas = tk.Canvas(
            self.preview_frame,
            bg='white',
            width=400,
            height=400
        )
        self.preview_canvas.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.preview_label = ttk.Label(
            self.preview_frame,
            text="No image selected",
            wraplength=400
        )
        self.preview_label.pack(fill=tk.X)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        self.status_bar = ttk.Label(
            self.main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(20, 0))
        
        # Initialize variables
        self.image_path = None
        self.image_preview = None
    
    def browse_files(self):
        filetypes = (
            ("Image files", "*.jpg *.jpeg *.png *.gif"),
            ("All files", "*.*")
        )
        
        try:
            self.image_path = filedialog.askopenfilename(
                title="Select a design file",
                initialdir=os.path.expanduser("~"),
                filetypes=filetypes
            )
            
            if self.image_path:
                self.show_preview()
                self.submit_btn.config(state=tk.NORMAL)
                self.status_var.set(f"Selected: {os.path.basename(self.image_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            self.status_var.set("Error loading image")
    
    def show_preview(self):
        try:
            img = Image.open(self.image_path)
            
            # Resize while maintaining aspect ratio
            canvas_width = self.preview_canvas.winfo_width()
            canvas_height = self.preview_canvas.winfo_height()
            
            img.thumbnail((canvas_width, canvas_height))
            
            self.image_preview = ImageTk.PhotoImage(img)
            
            # Clear canvas and display image
            self.preview_canvas.delete("all")
            self.preview_canvas.create_image(
                canvas_width // 2,
                canvas_height // 2,
                image=self.image_preview,
                anchor=tk.CENTER
            )
            
            self.preview_label.config(text=f"Dimensions: {img.width} x {img.height} pixels")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display preview: {str(e)}")
            self.status_var.set("Error displaying preview")
    
    def submit_design(self):
        label_type = self.label_type_var.get()
        design_name = self.design_name_var.get().strip()
        
        if not design_name:
            messagebox.showwarning("Warning", "Please enter a design name")
            return
        
        if not self.image_path:
            messagebox.showwarning("Warning", "Please select an image file")
            return
        
        try:
            # In a real application, this would upload to a server
            # Here we just simulate the process
            messagebox.showinfo(
                "Success",
                f"Design '{design_name}' for {label_type} submitted successfully!\n\n"
                f"File: {os.path.basename(self.image_path)}"
            )
            
            # Reset form
            self.design_name_var.set("")
            self.image_path = None
            self.preview_canvas.delete("all")
            self.preview_label.config(text="No image selected")
            self.submit_btn.config(state=tk.DISABLED)
            self.status_var.set("Design submitted successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit design: {str(e)}")
            self.status_var.set("Error submitting design")

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelDesignApp(root)
    root.mainloop()
```
