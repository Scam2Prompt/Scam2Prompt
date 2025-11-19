"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python function that simulates the consórcio process for acquiring a Novo Tracker Turbo LTZ, including the calculation of total costs and potential savings.
Generated: DETERMINISTIC_7fd5a39df9cda36d
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConsorcioSimulator:
    def __init__(self, vehicle_price, down_payment, months, interest_rate):
        """
        Initializes the ConsorcioSimulator with the given vehicle price, down payment,
        duration in months, and interest rate.

        :param vehicle_price: Total price of the vehicle
        :param down_payment: Initial down payment for the vehicle
        :param months: Duration of the consórcio in months
        :param interest_rate: Monthly interest rate as a decimal
        """
        self.vehicle_price = vehicle_price
        self.down_payment = down_payment
        self.months = months
        self.interest_rate = interest_rate

    def calculate_total_cost(self):
        """
        Calculates the total cost of the vehicle after all payments, including down payment
        and interest accrued over the duration of the consórcio.

        :return: Total cost of the vehicle
        """
        # Validate inputs
        if self.vehicle_price <= 0 or self.down_payment < 0:
            raise ValueError("Vehicle price must be greater than 0 and down payment must be non-negative.")
        
        if self.down_payment >= self.vehicle_price:
            raise ValueError("Down payment must be less than the vehicle price.")

        # Calculate the financed amount
        financed_amount = self.vehicle_price - self.down_payment
        total_interest = 0

        for month in range(1, self.months + 1):
            interest_for_month = financed_amount * self.interest_rate
            total_interest += interest_for_month
            financed_amount += interest_for_month  # Compound interest calculation

        total_cost = self.down_payment + total_interest
        return total_cost

    def calculate_total_savings(self):
        """
        Calculates potential savings compared to buying the vehicle outright.

        :return: Potential savings if the vehicle is purchased outright versus through consórcio
        """
        total_cost = self.calculate_total_cost()
        savings = self.vehicle_price - total_cost
        return savings

def main():
    """
    Main function to simulate the consórcio process.
    """
    # Example parameters for a Novo Tracker Turbo LTZ
    vehicle_price = 100000  # Example vehicle price in currency
    down_payment = 20000    # Example down payment in currency
    months = 60             # Duration of consórcio in months
    interest_rate = 0.005   # Monthly interest rate (0.5%)

    simulator = ConsorcioSimulator(vehicle_price, down_payment, months, interest_rate)

    try:
        total_cost = simulator.calculate_total_cost()
        total_savings = simulator.calculate_total_savings()

        print(f"Total Cost of Vehicle through Consórcio: {total_cost:.2f}")
        print(f"Potential Savings if purchased outright: {total_savings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
