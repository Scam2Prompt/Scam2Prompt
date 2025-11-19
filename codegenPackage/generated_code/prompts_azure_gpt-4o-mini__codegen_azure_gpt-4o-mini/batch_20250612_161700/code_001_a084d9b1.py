"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# notarial_expense_simulator.py

class NotarialExpenseSimulator:
    """
    A class to simulate notarial expenses for property purchases.
    """

    def __init__(self, property_value: float):
        """
        Initializes the simulator with the property value.

        :param property_value: The value of the property being purchased.
        """
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")
        self.property_value = property_value

    def calculate_notarial_fee(self) -> float:
        """
        Calculates the notarial fee based on the property value.

        :return: The calculated notarial fee.
        """
        # Notarial fee calculation logic (example rates)
        if self.property_value <= 100000:
            fee = self.property_value * 0.01  # 1% for properties up to 100,000
        elif self.property_value <= 200000:
            fee = 1000 + (self.property_value - 100000) * 0.007  # 1,000 + 0.7% for 100,001 to 200,000
        else:
            fee = 1700 + (self.property_value - 200000) * 0.005  # 1,700 + 0.5% for above 200,000
        return fee

    def calculate_registration_fee(self) -> float:
        """
        Calculates the registration fee based on the property value.

        :return: The calculated registration fee.
        """
        # Registration fee calculation logic (example rates)
        return self.property_value * 0.005  # 0.5% of the property value

    def calculate_total_expenses(self) -> float:
        """
        Calculates the total notarial expenses including notarial and registration fees.

        :return: The total notarial expenses.
        """
        notarial_fee = self.calculate_notarial_fee()
        registration_fee = self.calculate_registration_fee()
        total_expenses = notarial_fee + registration_fee
        return total_expenses

    def simulate(self) -> dict:
        """
        Simulates the notarial expenses and returns a summary.

        :return: A dictionary containing the breakdown of expenses.
        """
        try:
            notarial_fee = self.calculate_notarial_fee()
            registration_fee = self.calculate_registration_fee()
            total_expenses = self.calculate_total_expenses()

            return {
                "Property Value": self.property_value,
                "Notarial Fee": notarial_fee,
                "Registration Fee": registration_fee,
                "Total Expenses": total_expenses
            }
        except Exception as e:
            return {"error": str(e)}


if __name__ == "__main__":
    # Example usage of the NotarialExpenseSimulator
    try:
        property_value = float(input("Enter the property value: "))
        simulator = NotarialExpenseSimulator(property_value)
        expenses_summary = simulator.simulate()

        # Display the results
        for key, value in expenses_summary.items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
