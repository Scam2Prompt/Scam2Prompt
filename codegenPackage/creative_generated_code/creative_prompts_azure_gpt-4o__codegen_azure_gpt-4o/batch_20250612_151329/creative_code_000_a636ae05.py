"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.insectshieldzoro.com
Prompt: Write Python code to design a user interface for selecting and installing a pleated mosquito net system for UPVC windows, referencing the features described on the Insect Shield ZORO website.
Generated: DETERMINISTIC_a636ae05917f2378
Batch ID: 20250612_151329
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

class MosquitoNetUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mosquito Net Selector")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Title label
        title_label = tk.Label(root, text="Select & Install Mosquito Net System", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        # Frame for input fields
        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill="x")

        # Window dimensions
        tk.Label(input_frame, text="Window Width (in cm):", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.width_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.width_entry.grid(row=0, column=1, padx=10)

        tk.Label(input_frame, text="Window Height (in cm):", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.height_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
        self.height_entry.grid(row=1, column=1, padx=10)

        # Pleated mosquito net system options
        tk.Label(input_frame, text="Select Pleated Mosquito Net Type:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.net_type_var = tk.StringVar(value="Standard")
        net_types = ["Standard", "Deluxe", "Extra Durable"]
        self.net_type_menu = tk.OptionMenu(input_frame, self.net_type_var, *net_types)
        self.net_type_menu.config(font=("Arial", 12))
        self.net_type_menu.grid(row=2, column=1, padx=10)

        # Installation option
        tk.Label(input_frame, text="Installation Type:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
        self.installation_var = tk.StringVar(value="DIY")
        installation_types = ["DIY", "Professional"]
        self.installation_menu = tk.OptionMenu(input_frame, self.installation_var, *installation_types)
        self.installation_menu.config(font=("Arial", 12))
        self.installation_menu.grid(row=3, column=1, padx=10)

        # Submit button
        submit_button = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                  command=self.submit_details)
        submit_button.pack(pady=20)

        # Footer label
        footer_label = tk.Label(root, text="Insect Shield ZORO - Mosquito Net Systems for UPVC Windows",
                                font=("Arial", 10), fg="gray")
        footer_label.pack(pady=10)

    def validate_input(self):
        """Validate user inputs for width and height."""
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            if width <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive integers.")
            return width, height
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}")
            return None, None

    def submit_details(self):
        """Handle the submit button click event."""
        width, height = self.validate_input()
        if width and height:
            net_type = self.net_type_var.get()
            installation_type = self.installation_var.get()

            # Display confirmation of the user's choices
            details = (
                f"Window Dimensions: {width} cm x {height} cm\n"
                f"Pleated Mosquito Net Type: {net_type}\n"
                f"Installation Type: {installation_type}"
            )
            messagebox.showinfo("Selection Confirmed", details)

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = MosquitoNetUI(root)
    root.mainloop()
```
