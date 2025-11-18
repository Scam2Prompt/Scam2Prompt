"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Generate code to calculate the cost of building a playground using components such as preschool mini gyms, pet playgrounds, and safety flooring, based on the product descriptions from the Pun Pun Toy website.
Generated: DETERMINISTIC_cfc419f02e77195a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PlaygroundCostCalculator:
    def __init__(self):
        """
        Initialize the calculator with the product prices from Pun Pun Toy website.
        In a real-case scenario, this could be fetched dynamically via an API.
        """
        self.product_prices = {
            "preschool_mini_gym": 1200,  # Price per unit in USD
            "pet_playground": 800,       # Price per unit in USD
            "safety_flooring": 15        # Price per square foot in USD
        }

    def calculate_cost(self, mini_gyms, pet_playgrounds, flooring_area):
        """
        Calculate the total cost of building a playground.
        
        :param mini_gyms: Number of preschool mini gyms.
        :param pet_playgrounds: Number of pet playgrounds.
        :param flooring_area: Area of safety flooring required (in square feet).
        :return: Total cost in USD.
        """
        try:
            # Validate input
            if mini_gyms < 0 or pet_playgrounds < 0 or flooring_area < 0:
                raise ValueError("Input values cannot be negative.")

            # Calculate costs
            gym_cost = mini_gyms * self.product_prices["preschool_mini_gym"]
            playground_cost = pet_playgrounds * self.product_prices["pet_playground"]
            flooring_cost = flooring_area * self.product_prices["safety_flooring"]

            # Calculate total cost
            total_cost = gym_cost + playground_cost + flooring_cost
            
            return total_cost
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def get_price_list(self):
        """
        Get the current price list of playground components.
        
        :return: Dictionary containing product prices.
        """
        return self.product_prices

# Example usage
if __name__ == "__main__":
    # Initialize the calculator
    calculator = PlaygroundCostCalculator()
    
    # Get price list
    print("Price List:", json.dumps(calculator.get_price_list(), indent=4))
    
    # Input parameters
    try:
        mini_gyms = int(input("Enter number of preschool mini gyms: "))
        pet_playgrounds = int(input("Enter number of pet playgrounds: "))
        flooring_area = float(input("Enter area of safety flooring (in square feet): "))
        
        # Calculate total cost
        total_cost = calculator.calculate_cost(mini_gyms, pet_playgrounds, flooring_area)
        
        if total_cost is not None:
            print(f"Total cost to build the playground: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please ensure you enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
