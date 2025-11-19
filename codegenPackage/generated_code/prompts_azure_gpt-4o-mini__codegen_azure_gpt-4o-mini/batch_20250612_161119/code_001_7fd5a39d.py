"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python function that simulates the consórcio process for acquiring a Novo Tracker Turbo LTZ, including the calculation of total costs and potential savings.
Generated: DETERMINISTIC_7fd5a39df9cda36d
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConsorcioSimulator:
    """
    A class to simulate the consórcio process for acquiring a Novo Tracker Turbo LTZ.
    """

    def __init__(self, vehicle_price, installment_count, interest_rate=0.0):
        """
        Initializes the simulator with the vehicle price, number of installments, and optional interest rate.

        :param vehicle_price: The total price of the vehicle.
        :param installment_count: The number of installments to pay.
        :param interest_rate: The annual interest rate (default is 0.0 for no interest).
        """
        if vehicle_price <= 0:
            raise ValueError("Vehicle price must be greater than zero.")
        if installment_count <= 0:
            raise ValueError("Installment count must be greater than zero.")
        
        self.vehicle_price = vehicle_price
        self.installment_count = installment_count
        self.interest_rate = interest_rate

    def calculate_installment(self):
        """
        Calculates the monthly installment amount.

        :return: The monthly installment amount.
        """
        monthly_interest_rate = self.interest_rate / 12 / 100
        if self.interest_rate > 0:
            # Calculate using the formula for an annuity
            installment = (self.vehicle_price * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -self.installment_count)
        else:
            # Simple division if no interest
            installment = self.vehicle_price / self.installment_count
        
        return installment

    def total_cost(self):
        """
        Calculates the total cost of the vehicle including interest.

        :return: The total cost of the vehicle.
        """
        total_installment = self.calculate_installment() * self.installment_count
        return total_installment

    def potential_savings(self, alternative_price):
        """
        Calculates potential savings if an alternative vehicle price is provided.

        :param alternative_price: The price of the alternative vehicle.
        :return: The potential savings.
        """
        if alternative_price <= 0:
            raise ValueError("Alternative vehicle price must be greater than zero.")
        
        total_cost = self.total_cost()
        savings = total_cost - alternative_price
        return savings if savings > 0 else 0

    def simulate(self):
        """
        Runs the simulation and returns a summary of the results.

        :return: A dictionary containing the installment amount, total cost, and potential savings.
        """
        try:
            installment = self.calculate_installment()
            total_cost = self.total_cost()
            return {
                "monthly_installment": round(installment, 2),
                "total_cost": round(total_cost, 2)
            }
        except Exception as e:
            return {"error": str(e)}


# Example usage:
if __name__ == "__main__":
    try:
        vehicle_price = 100000  # Example vehicle price
        installment_count = 60   # Example number of installments
        interest_rate = 5.0      # Example interest rate

        simulator = ConsorcioSimulator(vehicle_price, installment_count, interest_rate)
        result = simulator.simulate()
        print("Simulation Result:", result)

        # Example of potential savings calculation
        alternative_price = 95000  # Example alternative vehicle price
        savings = simulator.potential_savings(alternative_price)
        print("Potential Savings:", round(savings, 2))
        
    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
