"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeg-group.com
Prompt: Write a program to generate quotes for custom swimming pool designs, factoring in features and services offered by Outdoor Environments Group.
Generated: DETERMINISTIC_048af5daf4bce520
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SwimmingPoolQuoteGenerator:
    """
    A class to generate quotes for custom swimming pool designs.
    Includes options for features and services offered by Outdoor Environments Group.
    """

    def __init__(self):
        # Base cost for a swimming pool before additional features/services
        self.base_cost = 20000

        # Dictionary to store additional features and their associated costs
        self.features = {
            "waterfall": 5000,
            "hot_tub": 8000,
            "lighting": 3000,
            "slide": 4000,
            "heating_system": 6000,
        }

        # Dictionary to store additional services and their associated costs
        self.services = {
            "landscaping": 7000,
            "pool_maintenance_plan": 1500,
            "smart_pool_system": 3500,
        }

    def display_options(self):
        """
        Displays the available features and services with their costs.
        """
        print("\nAvailable Features:")
        for feature, cost in self.features.items():
            print(f"  {feature.capitalize()}: ${cost:,}")

        print("\nAvailable Services:")
        for service, cost in self.services.items():
            print(f"  {service.capitalize()}: ${cost:,}")

    def calculate_quote(self, selected_features, selected_services):
        """
        Calculates the total quote based on selected features and services.
        
        Parameters:
            selected_features (list): List of selected features.
            selected_services (list): List of selected services.

        Returns:
            int: Total cost of the quote.
        """
        try:
            # Start with the base cost
            total_cost = self.base_cost

            # Add cost for selected features
            for feature in selected_features:
                if feature in self.features:
                    total_cost += self.features[feature]
                else:
                    raise ValueError(f"Invalid feature: {feature}")

            # Add cost for selected services
            for service in selected_services:
                if service in self.services:
                    total_cost += self.services[service]
                else:
                    raise ValueError(f"Invalid service: {service}")

            return total_cost
        
        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    """
    Main function to execute the Swimming Pool Quote Generator program.
    """
    quote_generator = SwimmingPoolQuoteGenerator()

    print("\nWelcome to Outdoor Environments Group - Swimming Pool Quote Generator")
    print("Base cost for a swimming pool: $20,000")

    # Display available features and services
    quote_generator.display_options()

    # Get user input for selected features
    selected_features = input("\nEnter the desired features, separated by commas (e.g., waterfall, slide): ").strip().lower().split(",")
    selected_features = [feature.strip() for feature in selected_features]

    # Get user input for selected services
    selected_services = input("\nEnter the desired services, separated by commas (e.g., landscaping, smart_pool_system): ").strip().lower().split(",")
    selected_services = [service.strip() for service in selected_services]

    # Calculate the total quote
    total_quote = quote_generator.calculate_quote(selected_features, selected_services)

    if total_quote is not None:
        print(f"\nTotal cost for your custom swimming pool design: ${total_quote:,}")
    else:
        print("\nFailed to calculate the quote due to invalid input.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
