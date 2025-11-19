"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Write a Python script to simulate a car loan calculator for Jaguar Land Rover models, considering the promo and price list information from the Jaguar Land Rover Jakarta website.
Generated: DETERMINISTIC_a1e28260de29edbd
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_loan_calculator.py

class Car:
    def __init__(self, model, price):
        """
        Initialize a Car object.

        Args:
            model (str): The car model.
            price (float): The car price.
        """
        self.model = model
        self.price = price

class CarLoanCalculator:
    def __init__(self):
        """
        Initialize a CarLoanCalculator object.
        """
        self.cars = []
        self.promo = {}

    def add_car(self, car):
        """
        Add a car to the calculator.

        Args:
            car (Car): The car to add.
        """
        self.cars.append(car)

    def add_promo(self, model, discount):
        """
        Add a promo for a car model.

        Args:
            model (str): The car model.
            discount (float): The discount percentage.
        """
        self.promo[model] = discount

    def calculate_loan(self, model, down_payment, loan_term, interest_rate):
        """
        Calculate the car loan.

        Args:
            model (str): The car model.
            down_payment (float): The down payment.
            loan_term (int): The loan term in years.
            interest_rate (float): The interest rate.

        Returns:
            dict: The loan details.

        Raises:
            ValueError: If the car model is not found.
        """
        car = next((c for c in self.cars if c.model == model), None)
        if car is None:
            raise ValueError("Car model not found")

        price = car.price
        if model in self.promo:
            price *= (1 - self.promo[model] / 100)

        loan_amount = price - down_payment
        monthly_interest_rate = (interest_rate / 100) / 12
        months = loan_term * 12
        monthly_payment = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

        return {
            "model": model,
            "price": price,
            "down_payment": down_payment,
            "loan_amount": loan_amount,
            "monthly_payment": monthly_payment,
            "loan_term": loan_term,
            "interest_rate": interest_rate,
        }

def main():
    calculator = CarLoanCalculator()

    # Add cars
    calculator.add_car(Car("Jaguar F-PACE", 8000000))
    calculator.add_car(Car("Jaguar XE", 6000000))
    calculator.add_car(Car("Land Rover Discovery", 9000000))

    # Add promos
    calculator.add_promo("Jaguar F-PACE", 5)
    calculator.add_promo("Land Rover Discovery", 3)

    # Calculate loan
    try:
        loan_details = calculator.calculate_loan("Jaguar F-PACE", 2000000, 5, 6)
        print("Loan Details:")
        for key, value in loan_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
