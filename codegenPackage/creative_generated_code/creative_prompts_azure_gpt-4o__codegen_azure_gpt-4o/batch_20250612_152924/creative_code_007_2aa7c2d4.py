"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Create a Python script to calculate the cost of interior fit-outs for coffee shops and restaurants, based on the services described on Amazing Interior's website.
Generated: DETERMINISTIC_2aa7c2d4866f5f41
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InteriorFitOutEstimator:
    """
    A class to estimate the cost of interior fit-outs for coffee shops and restaurants.
    """

    def __init__(self):
        # Unit costs for various services (cost per square meter)
        self.services_cost = {
            "design_consultation": 100,  # Cost for design consultation
            "flooring": 75,             # Cost for flooring installation
            "lighting": 50,             # Cost for lighting installation
            "furniture": 150,           # Cost for furniture installation
            "painting": 40,             # Cost for painting
            "plumbing": 60,             # Cost for plumbing installation
            "electrical": 80            # Cost for electrical installation
        }

    def calculate_cost(self, area, selected_services):
        """
        Calculate the total cost based on area and selected services.

        Parameters:
            area (float): The area of the shop or restaurant in square meters.
            selected_services (list): The list of services to be performed.

        Returns:
            float: The total estimated cost of the interior fit-out.
        """
        total_cost = 0

        for service in selected_services:
            if service not in self.services_cost:
                raise ValueError(f"Service '{service}' is not available.")
            total_cost += self.services_cost[service] * area

        return total_cost


def get_user_input():
    """
    Get inputs from the user for area and selected services.
    
    Returns:
        float: The area of the shop or restaurant.
        list: The selected services for fit-out.
    """
    try:
        # Get the area input from the user
        area = float(input("Enter the area of the shop/restaurant in square meters: "))
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        
        # Display available services
        print("\nAvailable services:")
        print("1. Design Consultation")
        print("2. Flooring")
        print("3. Lighting")
        print("4. Furniture")
        print("5. Painting")
        print("6. Plumbing")
        print("7. Electrical")
        
        # Get selected services input from the user
        services_input = input("\nEnter the services you want (comma-separated): ").strip().lower()
        selected_services = [s.strip() for s in services_input.split(",")]
        
        return area, selected_services
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def main():
    """
    Main function to execute the script.
    """
    try:
        # Initialize the estimator
        estimator = InteriorFitOutEstimator()

        # Get user input
        area, selected_services = get_user_input()

        # Calculate the cost
        total_cost = estimator.calculate_cost(area, selected_services)

        # Display the result
        print(f"\nTotal estimated cost for interior fit-out: ${total_cost:,.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
