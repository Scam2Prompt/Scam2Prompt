"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a script to calculate the total cost of temporary registration for multiple individuals in Adygea, including adjustments for minors and duration of registration, as specified on the website.
Generated: DETERMINISTIC_4fc91acc974b986a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# registration_cost_calculator.py

class RegistrationCostCalculator:
    def __init__(self):
        # Base cost for temporary registration
        self.base_cost = 1000  # in local currency
        # Discount for minors
        self.minor_discount = 0.5  # 50% discount for minors
        # Cost adjustment based on duration of registration (in days)
        self.duration_fee = {
            'up_to_30_days': 0,
            '31_to_90_days': 200,
            'more_than_90_days': 500
        }

    def calculate_cost(self, age, duration):
        """
        Calculate the total cost of registration.

        Parameters:
        age (int): Age of the individual
        duration (int): Duration of registration in days

        Returns:
        float: Total cost of registration
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        cost = self.base_cost

        # Adjust cost based on age
        if age < 18:
            cost *= self.minor_discount
        
        # Adjust cost based on duration
        if duration <= 30:
            cost += self.duration_fee['up_to_30_days']
        elif duration <= 90:
            cost += self.duration_fee['31_to_90_days']
        else:
            cost += self.duration_fee['more_than_90_days']

        return cost

def main():
    try:
        calculator = RegistrationCostCalculator()
        
        # Example input for multiple individuals
        individuals = [
            {"age": 25, "duration": 60},
            {"age": 17, "duration": 15},
            {"age": 30, "duration": 95},
            {"age": 10, "duration": 30}
        ]

        total_cost = 0

        # Calculate the total cost for all individuals
        for individual in individuals:
            cost = calculator.calculate_cost(individual['age'], individual['duration'])
            total_cost += cost
            print(f"Cost for individual (Age: {individual['age']}, Duration: {individual['duration']} days): {cost:.2f}")

        print(f"Total cost for registration: {total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
