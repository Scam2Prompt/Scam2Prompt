"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Generate code to calculate cleaning service costs based on the type of cleaning (e.g., deep cleaning, post-renovation cleaning) and add-ons like fridge or oven cleaning. Include a feature for generating a free estimate.
Generated: DETERMINISTIC_2a2dc534a9fbc234
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CleaningService:
    def __init__(self):
        # Base prices for different cleaning types
        self.cleaning_types = {
            "standard_cleaning": 100,
            "deep_cleaning": 150,
            "post_renovation_cleaning": 200
        }
        
        # Prices for add-ons
        self.add_ons = {
            "fridge_cleaning": 20,
            "oven_cleaning": 25,
            "window_cleaning": 30
        }
    
    def calculate_cost(self, cleaning_type, selected_add_ons):
        """
        Calculate the total cost of the cleaning service based on cleaning type and add-ons.
        
        :param cleaning_type: str - Type of cleaning service
        :param selected_add_ons: list - List of selected add-ons
        :return: float - Total cost
        """
        # Validate cleaning type
        if cleaning_type not in self.cleaning_types:
            raise ValueError(f"Invalid cleaning type: {cleaning_type}")

        # Validate add-ons
        for add_on in selected_add_ons:
            if add_on not in self.add_ons:
                raise ValueError(f"Invalid add-on: {add_on}")

        # Base cost of cleaning type
        total_cost = self.cleaning_types[cleaning_type]

        # Add cost of selected add-ons
        for add_on in selected_add_ons:
            total_cost += self.add_ons[add_on]

        return total_cost
    
    def generate_estimate(self, cleaning_type, selected_add_ons):
        """
        Generate a free cost estimate for the cleaning service.
        
        :param cleaning_type: str - Type of cleaning service
        :param selected_add_ons: list - List of selected add-ons
        :return: str - Estimate message
        """
        try:
            estimated_cost = self.calculate_cost(cleaning_type, selected_add_ons)
            return f"Estimated total cost for {cleaning_type} with selected add-ons: ${estimated_cost:.2f}"
        except ValueError as e:
            return str(e)


# Main function to demonstrate the functionality
def main():
    try:
        # Create service instance
        service = CleaningService()

        # User input for cleaning type
        cleaning_type = input("Enter cleaning type (standard_cleaning, deep_cleaning, post_renovation_cleaning): ").strip()

        # User input for add-ons (comma-separated)
        add_ons_input = input("Enter add-ons (fridge_cleaning, oven_cleaning, window_cleaning) separated by commas: ").strip()
        selected_add_ons = [add_on.strip() for add_on in add_ons_input.split(",") if add_on.strip()]

        # Generate and display estimate
        estimate = service.generate_estimate(cleaning_type, selected_add_ons)
        print(estimate)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


# Entry point
if __name__ == "__main__":
    main()
```
