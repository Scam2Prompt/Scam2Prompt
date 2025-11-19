"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Construct a user interface component that displays the available leather cases for Emanuelson Reels, ensuring it includes options for customization as mentioned on the website.
Generated: DETERMINISTIC_38bab8a97c09d963
Batch ID: 20250612_162051
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

class LeatherCaseUI:
    def __init__(self, root):
        """
        Initialize the Leather Case UI component.
        
        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Emanuelson Reels - Leather Cases")
        
        # Available leather case options
        self.case_types = ["Classic", "Deluxe", "Vintage"]
        self.colors = ["Black", "Brown", "Tan", "Burgundy"]
        self.engraving_options = ["None", "Initials", "Full Name", "Custom Text"]
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main UI components."""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Case Type Selection
        ttk.Label(self.main_frame, text="Case Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.case_type_var = tk.StringVar()
        self.case_type_dropdown = ttk.Combobox(
            self.main_frame, 
            textvariable=self.case_type_var,
            values=self.case_types,
            state="readonly"
        )
        self.case_type_dropdown.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.case_type_dropdown.current(0)
        
        # Color Selection
        ttk.Label(self.main_frame, text="Color:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.color_var = tk.StringVar()
        self.color_dropdown = ttk.Combobox(
            self.main_frame, 
            textvariable=self.color_var,
            values=self.colors,
            state="readonly"
        )
        self.color_dropdown.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.color_dropdown.current(0)
        
        # Engraving Options
        ttk.Label(self.main_frame, text="Engraving:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.engraving_var = tk.StringVar()
        self.engraving_dropdown = ttk.Combobox(
            self.main_frame, 
            textvariable=self.engraving_var,
            values=self.engraving_options,
            state="readonly"
        )
        self.engraving_dropdown.grid(row=2, column=1, sticky=tk.W, pady=5)
        self.engraving_dropdown.current(0)
        
        # Custom Engraving Text (only visible if engraving is selected)
        self.custom_text_label = ttk.Label(self.main_frame, text="Custom Text:")
        self.custom_text_entry = ttk.Entry(self.main_frame)
        self.engraving_var.trace_add("write", self.toggle_custom_text)
        
        # Preview Button
        self.preview_btn = ttk.Button(
            self.main_frame,
            text="Preview Selection",
            command=self.preview_selection
        )
        self.preview_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Order Button
        self.order_btn = ttk.Button(
            self.main_frame,
            text="Place Order",
            command=self.place_order
        )
        self.order_btn.grid(row=5, column=0, columnspan=2, pady=5)
    
    def toggle_custom_text(self, *args):
        """Show/hide custom text field based on engraving selection."""
        if self.engraving_var.get() in ["Initials", "Full Name", "Custom Text"]:
            self.custom_text_label.grid(row=3, column=0, sticky=tk.W, pady=5)
            self.custom_text_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
        else:
            self.custom_text_label.grid_remove()
            self.custom_text_entry.grid_remove()
    
    def preview_selection(self):
        """Show a preview of the selected options."""
        case_type = self.case_type_var.get()
        color = self.color_var.get()
        engraving = self.engraving_var.get()
        custom_text = self.custom_text_entry.get() if engraving in ["Initials", "Full Name", "Custom Text"] else ""
        
        preview_text = f"Case Type: {case_type}\nColor: {color}\nEngraving: {engraving}"
        if custom_text:
            preview_text += f"\nCustom Text: {custom_text}"
        
        messagebox.showinfo("Selection Preview", preview_text)
    
    def place_order(self):
        """Place the order with selected options."""
        try:
            case_type = self.case_type_var.get()
            color = self.color_var.get()
            engraving = self.engraving_var.get()
            custom_text = self.custom_text_entry.get() if engraving in ["Initials", "Full Name", "Custom Text"] else ""
            
            # Validate inputs
            if not case_type or not color or not engraving:
                raise ValueError("Please select all required options.")
            
            if engraving in ["Initials", "Full Name", "Custom Text"] and not custom_text:
                raise ValueError("Please enter custom text for engraving.")
            
            # Here you would typically send the order to a backend service
            # For demo, we'll just show a success message
            order_summary = (
                f"Order Placed Successfully!\n\n"
                f"Case Type: {case_type}\n"
                f"Color: {color}\n"
                f"Engraving: {engraving}\n"
            )
            if custom_text:
                order_summary += f"Custom Text: {custom_text}\n"
            
            messagebox.showinfo("Order Confirmation", order_summary)
        
        except Exception as e:
            messagebox.showerror("Order Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LeatherCaseUI(root)
    root.mainloop()
```
