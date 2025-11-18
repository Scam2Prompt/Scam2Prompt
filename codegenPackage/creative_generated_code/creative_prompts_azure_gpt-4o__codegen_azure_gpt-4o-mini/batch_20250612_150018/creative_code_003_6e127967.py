"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write code to automate the generation of contact forms for a packaging manufacturer, including fields for product inquiries about ABS Atlas trays and bakery trays, as described on Isoplas Corporation's website.
Generated: DETERMINISTIC_6e127967ec31037f
Batch ID: 20250612_150018
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

class ContactForm:
    def __init__(self, master):
        """Initialize the contact form GUI."""
        self.master = master
        master.title("Contact Form - Isoplas Corporation")

        # Create and place labels and entry fields
        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=1, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        self.label_product = tk.Label(master, text="Product Inquiry:")
        self.label_product.grid(row=2, column=0, padx=10, pady=5)
        
        self.product_var = tk.StringVar(value="ABS Atlas Trays")
        self.option_menu_product = tk.OptionMenu(master, self.product_var, "ABS Atlas Trays", "Bakery Trays")
        self.option_menu_product.grid(row=2, column=1, padx=10, pady=5)

        self.label_message = tk.Label(master, text="Message:")
        self.label_message.grid(row=3, column=0, padx=10, pady=5)
        self.text_message = tk.Text(master, height=5, width=30)
        self.text_message.grid(row=3, column=1, padx=10, pady=5)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def submit_form(self):
        """Handle form submission and validation."""
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        product = self.product_var.get()
        message = self.text_message.get("1.0", tk.END).strip()

        # Validate input fields
        if not name or not email or not message:
            messagebox.showerror("Input Error", "All fields are required.")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Input Error", "Please enter a valid email address.")
            return

        # Process the form submission
        self.process_submission(name, email, product, message)
        messagebox.showinfo("Success", "Your inquiry has been submitted successfully!")

        # Clear the form after submission
        self.clear_form()

    @staticmethod
    def validate_email(email):
        """Validate the email format using a simple regex."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email)

    def process_submission(self, name, email, product, message):
        """Simulate processing the form submission (e.g., save to a database or send an email)."""
        # Here you can implement your actual submission logic (like sending to an API or saving to a file)
        pass  # Replace with actual processing logic

    def clear_form(self):
        """Clear all fields in the contact form."""
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.product_var.set("ABS Atlas Trays")
        self.text_message.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    contact_form = ContactForm(root)
    root.mainloop()
```
