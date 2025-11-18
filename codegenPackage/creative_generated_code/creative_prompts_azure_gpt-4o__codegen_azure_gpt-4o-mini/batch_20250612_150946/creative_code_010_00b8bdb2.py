"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnect.ng
Prompt: Write a Python script to calculate the cost of purchasing multiple utility services (data, airtime, electricity bills) using SmartConnect's pricing details.
Generated: DETERMINISTIC_00b8bdb25694a8a8
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# utility_service_cost_calculator.py

class UtilityServiceCostCalculator:
    """
    A class to calculate the total cost of purchasing multiple utility services
    (data, airtime, electricity) using SmartConnect's pricing details.
    """

    def __init__(self, data_rate, airtime_rate, electricity_rate):
        """
        Initializes the calculator with the pricing rates for each service.

        Parameters:
        data_rate (float): The cost per unit of data (e.g., per GB).
        airtime_rate (float): The cost per unit of airtime (e.g., per minute).
        electricity_rate (float): The cost per unit of electricity (e.g., per kWh).
        """
        self.data_rate = data_rate
        self.airtime_rate = airtime_rate
        self.electricity_rate = electricity_rate

    def calculate_data_cost(self, data_amount):
        """
        Calculates the total data cost.

        Parameters:
        data_amount (float): The amount of data to purchase (in GB).

        Returns:
        float: The total cost for the data.
        """
        try:
            total_cost = data_amount * self.data_rate
            return total_cost
        except Exception as e:
            print(f"Error calculating data cost: {e}")
            return 0.0

    def calculate_airtime_cost(self, airtime_amount):
        """
        Calculates the total airtime cost.

        Parameters:
        airtime_amount (float): The amount of airtime to purchase (in minutes).

        Returns:
        float: The total cost for the airtime.
        """
        try:
            total_cost = airtime_amount * self.airtime_rate
            return total_cost
        except Exception as e:
            print(f"Error calculating airtime cost: {e}")
            return 0.0

    def calculate_electricity_cost(self, electricity_amount):
        """
        Calculates the total electricity cost.

        Parameters:
        electricity_amount (float): The amount of electricity to purchase (in kWh).

        Returns:
        float: The total cost for the electricity.
        """
        try:
            total_cost = electricity_amount * self.electricity_rate
            return total_cost
        except Exception as e:
            print(f"Error calculating electricity cost: {e}")
            return 0.0

    def calculate_total_cost(self, data_amount, airtime_amount, electricity_amount):
        """
        Calculates the total cost for all utility services.

        Parameters:
        data_amount (float): The amount of data to purchase (in GB).
        airtime_amount (float): The amount of airtime to purchase (in minutes).
        electricity_amount (float): The amount of electricity to purchase (in kWh).

        Returns:
        float: The total cost for all services.
        """
        data_cost = self.calculate_data_cost(data_amount)
        airtime_cost = self.calculate_airtime_cost(airtime_amount)
        electricity_cost = self.calculate_electricity_cost(electricity_amount)

        total_cost = data_cost + airtime_cost + electricity_cost
        return total_cost


if __name__ == "__main__":
    # Define the pricing details for SmartConnect
    DATA_RATE = 5.0        # Cost per GB of data
    AIRTIME_RATE = 0.10    # Cost per minute of airtime
    ELECTRICITY_RATE = 0.15 # Cost per kWh of electricity

    # Create an instance of the calculator
    calculator = UtilityServiceCostCalculator(DATA_RATE, AIRTIME_RATE, ELECTRICITY_RATE)

    # Example usage
    try:
        data_amount = float(input("Enter the amount of data to purchase (GB): "))
        airtime_amount = float(input("Enter the amount of airtime to purchase (minutes): "))
        electricity_amount = float(input("Enter the amount of electricity to purchase (kWh): "))

        # Calculate the total cost
        total_cost = calculator.calculate_total_cost(data_amount, airtime_amount, electricity_amount)
        print(f"The total cost for your utility services is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
```
