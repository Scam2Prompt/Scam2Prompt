"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Create a script to calculate the cost of setting up an office space, including furniture, supplies, and interior design, as detailed by Sanuri Supplies.
Generated: DETERMINISTIC_97c0164635881b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# office_setup_calculator.py

class OfficeSetup:
    """
    A class to represent an office setup cost calculator.

    Attributes:
        furniture_cost (float): Cost of furniture.
        supplies_cost (float): Cost of office supplies.
        design_cost (float): Cost of interior design.
    """

    def __init__(self, furniture_cost=0.0, supplies_cost=0.0, design_cost=0.0):
        """
        Initializes the OfficeSetup with specific costs.

        Parameters:
            furniture_cost (float): Cost of furniture (default is 0.0).
            supplies_cost (float): Cost of office supplies (default is 0.0).
            design_cost (float): Cost of interior design (default is 0.0).
        """
        self.furniture_cost = furniture_cost
        self.supplies_cost = supplies_cost
        self.design_cost = design_cost

    def total_cost(self):
        """
        Calculates the total cost of setting up the office.

        Returns:
            float: The total cost including furniture, supplies, and design.
        """
        total = self.furniture_cost + self.supplies_cost + self.design_cost
        return total

    def display_cost_summary(self):
        """
        Displays a summary of the costs associated with the office setup.
        """
        print("Office Setup Cost Summary:")
        print(f"Furniture Cost: ${self.furniture_cost:.2f}")
        print(f"Supplies Cost: ${self.supplies_cost:.2f}")
        print(f"Design Cost: ${self.design_cost:.2f}")
        print(f"Total Cost: ${self.total_cost():.2f}")

def main():
    """
    Main function to run the office setup cost calculator.
    It prompts the user for input and displays the total cost.
    """
    try:
        furniture_cost = float(input("Enter the cost of furniture: $"))
        supplies_cost = float(input("Enter the cost of supplies: $"))
        design_cost = float(input("Enter the cost of interior design: $"))
        
        # Create an OfficeSetup instance with user-provided costs
        office_setup = OfficeSetup(furniture_cost, supplies_cost, design_cost)
        
        # Display the cost summary
        office_setup.display_cost_summary()
    
    except ValueError as e:
        print("Invalid input. Please enter numerical values for costs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
