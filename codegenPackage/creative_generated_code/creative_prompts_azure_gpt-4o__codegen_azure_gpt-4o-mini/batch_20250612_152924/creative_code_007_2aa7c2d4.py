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
import json

class FitOutCalculator:
    """A class to calculate the cost of interior fit-outs for coffee shops and restaurants."""

    def __init__(self):
        """Initialize the calculator with service rates."""
        self.service_rates = {
            "design": 50.0,  # Cost per hour for design services
            "construction": 100.0,  # Cost per hour for construction services
            "furniture": 2000.0,  # Base cost for furniture installation
            "decor": 1500.0,  # Base cost for decor installation
        }

    def calculate_cost(self, services):
        """
        Calculate the total cost based on selected services.

        Args:
            services (dict): A dictionary containing the services and their respective hours.

        Returns:
            float: Total cost of the fit-out services.
        """
        total_cost = 0.0
        for service, hours in services.items():
            if service not in self.service_rates:
                raise ValueError(f"Service '{service}' not found in service rates.")
            if hours < 0:
                raise ValueError(f"Hours for service '{service}' cannot be negative.")

            total_cost += self.service_rates[service] * hours
        
        return total_cost

    def load_service_rates(self, file_path):
        """
        Load service rates from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing service rates.

        Returns:
            bool: True if rates were loaded successfully, False otherwise.
        """
        try:
            with open(file_path, 'r') as file:
                self.service_rates = json.load(file)
            return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading service rates: {e}")
            return False

def main():
    """Main function to run the fit-out calculator."""
    calculator = FitOutCalculator()

    # Example service hours (could be modified based on user input)
    services = {
        "design": 10,  # 10 hours for design services
        "construction": 20,  # 20 hours for construction services
        "furniture": 1,  # 1 installation of furniture
        "decor": 1,  # 1 installation of decor
    }

    try:
        total_cost = calculator.calculate_cost(services)
        print(f"Total cost for interior fit-out: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error calculating cost: {e}")

if __name__ == "__main__":
    main()
```
