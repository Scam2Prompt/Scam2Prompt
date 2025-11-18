"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Write a Python script to calculate the cost of exchanging an old Suzuki car for a new one, incorporating features from Suzuki Capital Motors' Certified Used Car Program, such as free evaluation and up to one-year warranty.
Generated: DETERMINISTIC_c55ba55f4a4638c5
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarExchangeCalculator:
    """
    A class to calculate the cost of exchanging an old Suzuki car for a new one.
    Incorporates features from Suzuki Capital Motors' Certified Used Car Program.
    """

    def __init__(self, old_car_value: float, new_car_price: float, warranty_cost: float = 0.0):
        """
        Initializes the CarExchangeCalculator with the values of the old car, new car price, and optional warranty cost.

        :param old_car_value: The estimated value of the old Suzuki car.
        :param new_car_price: The price of the new Suzuki car.
        :param warranty_cost: Optional cost of the extended warranty for the new car.
        """
        self.old_car_value = old_car_value
        self.new_car_price = new_car_price
        self.warranty_cost = warranty_cost

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of exchanging the old car for a new one.

        :return: The total cost after accounting for the trade-in value of the old car and any warranty costs.
        """
        try:
            # Calculate total cost considering trade-in value and warranty cost
            total_cost = self.new_car_price - self.old_car_value + self.warranty_cost
            if total_cost < 0:
                total_cost = 0.0  # Ensure total cost is not negative
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return -1  # Indicates an error in calculation

    def display_exchange_details(self):
        """
        Displays the details of the car exchange transaction.
        """
        total_cost = self.calculate_total_cost()
        if total_cost == -1:
            print("Failed to calculate total cost due to an error.")
            return

        print(f"Old Car Value: ${self.old_car_value:.2f}")
        print(f"New Car Price: ${self.new_car_price:.2f}")
        print(f"Warranty Cost: ${self.warranty_cost:.2f}")
        print(f"Total Cost After Exchange: ${total_cost:.2f}")


def main():
    """
    Main function to execute the car exchange calculator.
    """
    try:
        # Example values for the old car, new car price, and warranty cost
        old_car_value = float(input("Enter the value of your old Suzuki car: $"))
        new_car_price = float(input("Enter the price of the new Suzuki car: $"))
        warranty_cost = float(input("Enter the warranty cost (if any, else enter 0): $"))

        # Create an instance of CarExchangeCalculator
        calculator = CarExchangeCalculator(old_car_value, new_car_price, warranty_cost)

        # Display the exchange details
        calculator.display_exchange_details()

    except ValueError:
        print("Invalid input! Please enter numerical values for car prices and warranty costs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
