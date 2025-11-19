"""
Generated Code Metadata:
========================
Original URL: https://www.facecar.mx
Prompt: "Develop a simple calculator in Python that determines the total cost of owning a vehicle, including financing costs, similar to Facecar's financing options."
Generated: DETERMINISTIC_a0d02498907875ba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VehicleCostCalculator:
    """
    A simple calculator to determine the total cost of owning a vehicle,
    including financing costs.
    """

    def __init__(self, purchase_price, down_payment, interest_rate, loan_term_years, annual_insurance, annual_maintenance):
        """
        Initializes the VehicleCostCalculator with the necessary parameters.

        :param purchase_price: Total price of the vehicle
        :param down_payment: Initial down payment made
        :param interest_rate: Annual interest rate (as a percentage)
        :param loan_term_years: Duration of the loan in years
        :param annual_insurance: Annual insurance cost
        :param annual_maintenance: Annual maintenance cost
        """
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years
        self.annual_insurance = annual_insurance
        self.annual_maintenance = annual_maintenance

    def calculate_financing_cost(self):
        """
        Calculates the total financing cost of the vehicle.

        :return: Total financing cost
        """
        loan_amount = self.purchase_price - self.down_payment
        monthly_interest_rate = self.interest_rate / 12
        number_of_payments = self.loan_term_years * 12

        # Calculate monthly payment using the formula for an amortizing loan
        if monthly_interest_rate > 0:
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        else:
            monthly_payment = loan_amount / number_of_payments

        total_payment = monthly_payment * number_of_payments
        total_interest = total_payment - loan_amount

        return total_payment, total_interest

    def calculate_total_cost(self):
        """
        Calculates the total cost of owning the vehicle including financing, insurance, and maintenance.

        :return: Total cost of ownership
        """
        total_financing, total_interest = self.calculate_financing_cost()
        total_insurance = self.annual_insurance * self.loan_term_years
        total_maintenance = self.annual_maintenance * self.loan_term_years

        total_cost = total_financing + total_insurance + total_maintenance
        return total_cost, total_interest, total_insurance, total_maintenance

def main():
    """
    Main function to execute the vehicle cost calculator.
    """
    try:
        # Example parameters for the vehicle cost calculation
        purchase_price = 30000  # Vehicle price
        down_payment = 5000      # Down payment
        interest_rate = 5        # Annual interest rate in percentage
        loan_term_years = 5      # Loan term in years
        annual_insurance = 1200   # Annual insurance cost
        annual_maintenance = 800   # Annual maintenance cost

        # Create an instance of the VehicleCostCalculator
        calculator = VehicleCostCalculator(purchase_price, down_payment, interest_rate, loan_term_years, annual_insurance, annual_maintenance)

        # Calculate total cost
        total_cost, total_interest, total_insurance, total_maintenance = calculator.calculate_total_cost()

        # Display results
        print(f"Total Cost of Ownership: ${total_cost:,.2f}")
        print(f"Total Interest Paid: ${total_interest:,.2f}")
        print(f"Total Insurance Cost: ${total_insurance:,.2f}")
        print(f"Total Maintenance Cost: ${total_maintenance:,.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
