"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-zeta.vercel.app
Prompt: How can I create a user interface for reporting transaction delays, similar to the one provided by EVM Zeta?
Generated: DETERMINISTIC_62859f29000c450d
Batch ID: 20250612_161356
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
from datetime import datetime

class TransactionDelayReportApp:
    def __init__(self, root):
        """
        Initializes the main window and its components.
        """
        self.root = root
        self.root.title("Transaction Delay Reporting")
        self.root.geometry("400x300")

        # Labels and Inputs
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the necessary widgets for the application.
        """
        tk.Label(self.root, text="Transaction ID:").pack(pady=5)
        self.transaction_id_entry = tk.Entry(self.root, width=30)
        self.transaction_id_entry.pack(pady=5)

        tk.Label(self.root, text="Report Delay (in hours):").pack(pady=5)
        self.delay_hours_entry = tk.Entry(self.root, width=30)
        self.delay_hours_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit Report", command=self.submit_report)
        self.submit_button.pack(pady=20)

    def submit_report(self):
        """
        Validates input and submits the report.
        """
        transaction_id = self.transaction_id_entry.get()
        delay_hours = self.delay_hours_entry.get()

        # Input validation
        if not transaction_id:
            messagebox.showerror("Input Error", "Transaction ID cannot be empty.")
            return
        if not delay_hours.isdigit():
            messagebox.showerror("Input Error", "Delay must be a valid number.")
            return

        # Prepare the report
        delay_hours = int(delay_hours)
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Dummy submit function (To be replaced with actual backend integration)
        self.save_report(transaction_id, delay_hours, report_time)

    def save_report(self, transaction_id, delay_hours, report_time):
        """
        Simulates saving the report data to a database or an API.
        In production, this function should connect to a database or API.
        """
        try:
            # Simulate a successful report save operation
            print(f"Report Saved: Transaction ID: {transaction_id}, Delay: {delay_hours} hours, Reported at: {report_time}")
            messagebox.showinfo("Success", "Your report has been submitted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the report: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransactionDelayReportApp(root)
    root.mainloop()
```
