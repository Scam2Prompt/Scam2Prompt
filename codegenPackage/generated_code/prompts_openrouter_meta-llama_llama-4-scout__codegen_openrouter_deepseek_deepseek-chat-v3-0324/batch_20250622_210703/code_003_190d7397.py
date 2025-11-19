"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: "Generate a Python code snippet to create a simple calculator for financing options on vehicles like the Kia Sorento at Cid Autos."
Generated: DETERMINISTIC_190d73976e75ff8a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

class VehicleFinanceCalculator:
    """
    A simple GUI calculator for vehicle financing options.
    Calculates monthly payments based on vehicle price, down payment, interest rate, and loan term.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("CID Autos - Vehicle Finance Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Default values
        self.default_vehicle = "Kia Sorento"
        self.default_price = 30000.00
        self.default_down_payment = 5000.00
        self.default_interest_rate = 5.0
        self.default_loan_term = 60  # months
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Vehicle Selection
        tk.Label(self.root, text="Vehicle Model:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.vehicle_entry = tk.Entry(self.root)
        self.vehicle_entry.insert(0, self.default_vehicle)
        self.vehicle_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Vehicle Price
        tk.Label(self.root, text="Vehicle Price ($):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(self.root)
        self.price_entry.insert(0, str(self.default_price))
        self.price_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Down Payment
        tk.Label(self.root, text="Down Payment ($):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.down_payment_entry = tk.Entry(self.root)
        self.down_payment_entry.insert(0, str(self.default_down_payment))
        self.down_payment_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Interest Rate
        tk.Label(self.root, text="Interest Rate (%):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.interest_rate_entry = tk.Entry(self.root)
        self.interest_rate_entry.insert(0, str(self.default_interest_rate))
        self.interest_rate_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Loan Term
        tk.Label(self.root, text="Loan Term (months):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.loan_term_entry = tk.Entry(self.root)
        self.loan_term_entry.insert(0, str(self.default_loan_term))
        self.loan_term_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Calculate Button
        self.calculate_button = tk.Button(
            self.root, 
            text="Calculate Monthly Payment", 
            command=self.calculate_payment
        )
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Result Display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Configure grid weights
        self.root.columnconfigure(1, weight=1)
        
    def calculate_payment(self):
        """Calculate the monthly payment based on user inputs."""
        try:
            # Get values from entries
            price = float(self.price_entry.get())
            down_payment = float(self.down_payment_entry.get())
            interest_rate = float(self.interest_rate_entry.get())
            loan_term = int(self.loan_term_entry.get())
            
            # Validate inputs
            if down_payment >= price:
                raise ValueError("Down payment must be less than vehicle price")
            if loan_term <= 0:
                raise ValueError("Loan term must be greater than 0")
            if interest_rate < 0:
                raise ValueError("Interest rate cannot be negative")
            
            # Calculate loan amount
            loan_amount = price - down_payment
            
            # Monthly interest rate
            monthly_rate = (interest_rate / 100) / 12
            
            # Calculate monthly payment
            if monthly_rate == 0:  # Handle 0% interest case
                monthly_payment = loan_amount / loan_term
            else:
                monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate)**loan_term) / ((1 + monthly_rate)**loan_term - 1)
            
            # Display result
            result_text = f"Monthly Payment: ${monthly_payment:.2f}"
            self.result_label.config(text=result_text)
            
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleFinanceCalculator(root)
    root.mainloop()
```
