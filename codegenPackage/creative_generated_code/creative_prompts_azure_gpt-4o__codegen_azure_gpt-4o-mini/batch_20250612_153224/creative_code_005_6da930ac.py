"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tkcjourneys.com
Prompt: Write a script to calculate the total cost for a group of travelers (minimum 5 persons) using the discount offers mentioned on TKC Journeys' website.
Generated: DETERMINISTIC_6da930acf8bf8b09
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TravelCostCalculator:
    def __init__(self, base_cost_per_person, group_size):
        """
        Initializes the TravelCostCalculator with the base cost per person and group size.
        
        :param base_cost_per_person: float, cost for a single person
        :param group_size: int, number of persons in the group
        """
        if group_size < 5:
            raise ValueError("Group size must be at least 5 persons.")
        if base_cost_per_person < 0:
            raise ValueError("Base cost per person must be a non-negative value.")

        self.base_cost_per_person = base_cost_per_person
        self.group_size = group_size

    def calculate_discount(self):
        """
        Calculates the discount based on the group size.
        
        :return: float, discount percentage
        """
        if self.group_size >= 10:
            return 0.20  # 20% discount for 10 or more persons
        elif self.group_size >= 5:
            return 0.10  # 10% discount for 5 to 9 persons
        return 0.0  # No discount for less than 5 persons

    def calculate_total_cost(self):
        """
        Calculates the total cost for the group after applying the discount.
        
        :return: float, total cost after discount
        """
        discount = self.calculate_discount()
        total_cost = self.base_cost_per_person * self.group_size
        discounted_cost = total_cost * (1 - discount)
        return discounted_cost

def main():
    """
    Main function to execute the TravelCostCalculator.
    """
    try:
        # Input base cost per person and group size
        base_cost_per_person = float(input("Enter the base cost per person: "))
        group_size = int(input("Enter the number of persons in the group (minimum 5): "))

        # Create an instance of TravelCostCalculator
        calculator = TravelCostCalculator(base_cost_per_person, group_size)

        # Calculate total cost
        total_cost = calculator.calculate_total_cost()

        # Output the result
        print(f"The total cost for the group of {group_size} persons is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
