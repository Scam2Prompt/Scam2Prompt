"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: How can I create a user interface for a Tymebank loan application that captures necessary details like income and loan amount?
Generated: DETERMINISTIC_a038a9d29441e7f9
Batch ID: 20250612_162538
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

class LoanApplicationApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("Tymebank Loan Application")

        # Create and place labels and entry fields for user inputs
        self.create_widgets()

    def create_widgets(self):
        """Create the input fields and submit button for the loan application."""
        # Income input
        self.income_label = tk.Label(self.master, text="Monthly Income:")
        self.income_label.grid(row=0, column=0, padx=10, pady=10)
        self.income_entry = tk.Entry(self.master)
        self.income_entry.grid(row=0, column=1, padx=10, pady=10)

        # Loan amount input
        self.loan_label = tk.Label(self.master, text="Loan Amount Requested:")
        self.loan_label.grid(row=1, column=0, padx=10, pady=10)
        self.loan_entry = tk.Entry(self.master)
        self.loan_entry.grid(row=1, column=1, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_application)
        self.submit_button.grid(row=2, columnspan=2, pady=20)

    def submit_application(self):
        """Handle the submission of loan application."""
        try:
            income = float(self.income_entry.get())
            loan_amount = float(self.loan_entry.get())

            if income <= 0 or loan_amount <= 0:
                raise ValueError("Income and Loan Amount must be positive numbers.")

            # In a real application, you'd process the loan application here
            messagebox.showinfo("Success", f"Loan Application Submitted:\nIncome: {income}\nLoan Amount: {loan_amount}")

            # Clear fields after submission
            self.clear_fields()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

    def clear_fields(self):
        """Clear the input fields after submission."""
        self.income_entry.delete(0, tk.END)
        self.loan_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanApplicationApp(root)
    root.mainloop()
```
