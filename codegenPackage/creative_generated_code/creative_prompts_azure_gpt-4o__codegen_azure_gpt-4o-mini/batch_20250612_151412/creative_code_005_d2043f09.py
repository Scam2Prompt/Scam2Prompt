"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write a Python script to simulate Klar's "Meses Sin Intereses" feature for credit card purchases, including monthly payment breakdowns.
Generated: DETERMINISTIC_d2043f098f2b3d2c
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KlarMesesSinIntereses:
    """
    A class to simulate Klar's "Meses Sin Intereses" feature for credit card purchases.
    This feature allows consumers to pay for their purchases in installments without any interest.
    """

    def __init__(self, total_amount, months):
        """
        Initializes the KlarMesesSinIntereses instance.
        
        Parameters:
            total_amount (float): The total amount of the purchase.
            months (int): The number of months for the payment plan.
        
        Raises:
            ValueError: If total_amount is not positive or months is not a positive integer.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be a positive number.")
        if months <= 0:
            raise ValueError("Number of months must be a positive integer.")
        
        self.total_amount = total_amount
        self.months = months

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment amount.
        
        Returns:
            float: The monthly payment amount.
        """
        return self.total_amount / self.months

    def generate_payment_schedule(self):
        """
        Generates a payment schedule for the given months.
        
        Returns:
            list: A list of tuples containing (month, payment_amount).
        """
        monthly_payment = self.calculate_monthly_payment()
        payment_schedule = [(month, monthly_payment) for month in range(1, self.months + 1)]
        return payment_schedule

    def display_payment_schedule(self):
        """
        Displays the payment schedule in a user-friendly format.
        """
        payment_schedule = self.generate_payment_schedule()
        print(f"Payment Schedule for a Total Amount of ${self.total_amount:.2f} over {self.months} months:")
        print("Month\tPayment Amount")
        for month, payment in payment_schedule:
            print(f"{month}\t${payment:.2f}")

def main():
    """
    Main function to run the KlarMesesSinIntereses simulation.
    It prompts the user for input and displays the payment schedule.
    """
    try:
        total_amount = float(input("Enter the total amount of the purchase: "))
        months = int(input("Enter the number of months for the payment plan: "))
        
        klar_simulator = KlarMesesSinIntereses(total_amount, months)
        klar_simulator.display_payment_schedule()
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
