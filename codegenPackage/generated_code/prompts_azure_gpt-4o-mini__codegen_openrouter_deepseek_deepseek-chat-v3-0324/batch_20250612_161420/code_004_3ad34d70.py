"""
Generated Code Metadata:
========================
Original URL: https://marqador.com
Prompt: Design a user interface component that allows users to select stamp types and add QR codes for contact information, based on the marQadoR product features.
Generated: DETERMINISTIC_3ad34d7072846b7d
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import qrcode
import os

class StampDesignerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("marQadoR Stamp Designer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize variables
        self.stamp_types = ["Round", "Square", "Rectangle", "Custom"]
        self.selected_stamp = tk.StringVar(value=self.stamp_types[0])
        self.contact_info = tk.StringVar()
        self.qr_code_image = None
        self.stamp_preview = None
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Stamp selection frame
        selection_frame = ttk.LabelFrame(main_frame, text="Stamp Configuration", padding="10")
        selection_frame.pack(fill=tk.X, pady=5)
        
        # Stamp type selection
        ttk.Label(selection_frame, text="Stamp Type:").grid(row=0, column=0, sticky=tk.W)
        stamp_dropdown = ttk.Combobox(
            selection_frame, 
            textvariable=self.selected_stamp, 
            values=self.stamp_types,
            state="readonly"
        )
        stamp_dropdown.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        stamp_dropdown.bind("<<ComboboxSelected>>", self.update_preview)
        
        # Contact information input
        ttk.Label(selection_frame, text="Contact Info (for QR Code):").grid(row=1, column=0, sticky=tk.W)
        contact_entry = ttk.Entry(selection_frame, textvariable=self.contact_info, width=40)
        contact_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Generate QR button
        qr_button = ttk.Button(
            selection_frame, 
            text="Generate QR Code", 
            command=self.generate_qr_code
        )
        qr_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Preview frame
        preview_frame = ttk.LabelFrame(main_frame, text="Stamp Preview", padding="10")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_canvas = tk.Canvas(preview_frame, bg="white", width=400, height=300)
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Action buttons frame
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=5)
        
        # Save button
        save_button = ttk.Button(
            action_frame, 
            text="Save Stamp Design", 
            command=self.save_design
        )
        save_button.pack(side=tk.RIGHT, padx=5)
        
        # Reset button
        reset_button = ttk.Button(
            action_frame, 
            text="Reset", 
            command=self.reset_design
        )
        reset_button.pack(side=tk.RIGHT, padx=5)
        
        # Initial preview update
        self.update_preview()
    
    def generate_qr_code(self):
        contact_text = self.contact_info.get().strip()
        if not contact_text:
            messagebox.showwarning("Input Error", "Please enter contact information for the QR code.")
            return
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(contact_text)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            self.qr_code_image = img
            self.update_preview()
            
        except Exception as e:
            messagebox.showerror("QR Generation Error", f"Failed to generate QR code: {str(e)}")
    
    def update_preview(self, event=None):
        self.preview_canvas.delete("all")
        canvas_width = self.preview_canvas.winfo_width()
        canvas_height = self.preview_canvas.winfo_height()
        
        # Draw stamp shape based on selection
        stamp_type = self.selected_stamp.get()
        outline_color = "blue"
        
        if stamp_type == "Round":
            diameter = min(canvas_width, canvas_height) * 0.8
            x1 = (canvas_width - diameter) / 2
            y1 = (canvas_height - diameter) / 2
            x2 = x1 + diameter
            y2 = y1 + diameter
            self.preview_canvas.create_oval(x1, y1, x2, y2, outline=outline_color, width=3)
            
        elif stamp_type == "Square":
            side = min(canvas_width, canvas_height) * 0.8
            x1 = (canvas_width - side) / 2
            y1 = (canvas_height - side) / 2
            x2 = x1 + side
            y2 = y1 + side
            self.preview_canvas.create_rectangle(x1, y1, x2, y2, outline=outline_color, width=3)
            
        elif stamp_type == "Rectangle":
            width = canvas_width * 0.8
            height = canvas_height * 0.6
            x1 = (canvas_width - width) / 2
            y1 = (canvas_height - height) / 2
            x2 = x1 + width
            y2 = y1 + height
            self.preview_canvas.create_rectangle(x1, y1, x2, y2, outline=outline_color, width=3)
            
        elif stamp_type == "Custom":
            # Custom shape would be more complex - placeholder for now
            points = [
                canvas_width * 0.3, canvas_height * 0.2,
                canvas_width * 0.7, canvas_height * 0.2,
                canvas_width * 0.8, canvas_height * 0.5,
                canvas_width * 0.7, canvas_height * 0.8,
                canvas_width * 0.3, canvas_height * 0.8,
                canvas_width * 0.2, canvas_height * 0.5
            ]
            self.preview_canvas.create_polygon(points, outline=outline_color, width=3, fill="")
        
        # Add QR code if generated
        if self.qr_code_image:
            try:
                # Convert PIL image to PhotoImage
                qr_img = ImageTk.PhotoImage(self.qr_code_image)
                
                # Keep reference to prevent garbage collection
                self.stamp_preview = qr_img
                
                # Calculate position (center of stamp)
                qr_size = min(canvas_width, canvas_height) * 0.3
                x = canvas_width / 2 - qr_size / 2
                y = canvas_height / 2 - qr_size / 2
                
                # Place QR code on canvas
                self.preview_canvas.create_image(x, y, image=qr_img, anchor=tk.NW)
                
            except Exception as e:
                messagebox.showerror("Preview Error", f"Failed to update preview: {str(e)}")
    
    def save_design(self):
        if not self.qr_code_image:
            messagebox.showwarning("Save Error", "Please generate a QR code first.")
            return
        
        try:
            # Ask for save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Save Stamp Design"
            )
            
            if not file_path:
                return  # User cancelled
            
            # Create a new image with stamp shape and QR code
            stamp_type = self.selected_stamp.get()
            base_img = Image.new("RGB", (800, 600), "white")
            
            # For simplicity, we'll just save the QR code
            # In a real app, you would composite the stamp shape and QR code
            self.qr_code_image.save(file_path)
            
            messagebox.showinfo("Success", f"Stamp design saved successfully at:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save design: {str(e)}")
    
    def reset_design(self):
        self.selected_stamp.set(self.stamp_types[0])
        self.contact_info.set("")
        self.qr_code_image = None
        self.stamp_preview = None
