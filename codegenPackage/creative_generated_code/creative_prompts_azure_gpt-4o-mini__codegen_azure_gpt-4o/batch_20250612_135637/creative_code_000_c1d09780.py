"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-voyage.nfts2.me
Prompt: Generate code to create a user interface for reporting NFT scams or intellectual property rights infringements.
Generated: DETERMINISTIC_c1d097809643e686
Batch ID: 20250612_135637
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


class NFTReportApp:
    """
    A GUI application for reporting NFT scams or intellectual property rights infringements.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Report NFT Scam")

        # Window Size Configuration
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Header Label
        self.header_label = tk.Label(
            self.root, text="Report NFT Scam or IP Infringement",
            font=("Arial", 14), pady=10
        )
        self.header_label.pack()

        # Name Field
        self.name_label = tk.Label(self.root, text="Your Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=50)
        self.name_entry.pack(pady=5)

        # Email Field
        self.email_label = tk.Label(self.root, text="Your Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root, width=50)
        self.email_entry.pack(pady=5)

        # Scam Details Field
        self.details_label = tk.Label(self.root, text="Details of the Scam/IP Infringement:")
        self.details_label.pack(pady=5)
        self.details_text = tk.Text(self.root, width=50, height=10)
        self.details_text.pack(pady=5)

        # Proof Upload Field (Mocked as a file path)
        self.proof_label = tk.Label(self.root, text="Proof File Path:")
        self.proof_label.pack(pady=5)
        self.proof_entry = tk.Entry(self.root, width=50)
        self.proof_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.submit_report
        )
        self.submit_button.pack(pady=10)

    def submit_report(self):
        """
        Handles the submission of a report.
        Validates input and displays a confirmation message.
        """
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        details = self.details_text.get("1.0", tk.END).strip()
        proof_path = self.proof_entry.get().strip()

        # Basic validation
        if not name or not email or not details:
            messagebox.showerror("Error", "All fields except 'Proof File Path' are required.")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address.")
            return

        # Confirmation dialog
        confirmation_message = (
            f"Report Submitted by {name}\n\n"
            f"Email: {email}\n"
            f"Details: {details[:100]}...\n"
            f"Proof Path: {proof_path if proof_path else 'None'}"
        )
        messagebox.showinfo("Success", f"Thank you for your report!\n\n{confirmation_message}")

        # Clear fields after submission
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.details_text.delete("1.0", tk.END)
        self.proof_entry.delete(0, tk.END)


if __name__ == "__main__":
    # Initialize Tkinter root and app instance
    root = tk.Tk()
    app = NFTReportApp(root)

    # Run the application
    root.mainloop()
```
