"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate code to calculate cleaning service costs based on the type of cleaning (e.g., deep cleaning, post-renovation cleaning) and add-ons like fridge or oven cleaning. Include a feature for generating a free estimate.
Generated: DETERMINISTIC_2a2dc534a9fbc234
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningService:
    """
    A class to represent a cleaning service and calculate costs based on the type of cleaning and add-ons.
    """

    # Base prices for different types of cleaning services
    BASE_PRICES = {
        'standard': 100,
        'deep': 150,
        'post_renovation': 200
    }

    # Prices for add-ons
    ADD_ON_PRICES = {
        'fridge_cleaning': 30,
        'oven_cleaning': 25,
        'window_cleaning': 20
    }

    def __init__(self, cleaning_type, add_ons=None):
        """
        Initializes the CleaningService with a specific cleaning type and optional add-ons.

        :param cleaning_type: Type of cleaning service (e.g., 'standard', 'deep', 'post_renovation')
        :param add_ons: List of add-ons (e.g., ['fridge_cleaning', 'oven_cleaning'])
        """
        self.cleaning_type = cleaning_type
        self.add_ons = add_ons if add_ons else []

    def calculate_cost(self):
        """
        Calculates the total cost of the cleaning service based on the type and add-ons.

        :return: Total cost of the cleaning service
        :raises ValueError: If the cleaning type is invalid
        """
        if self.cleaning_type not in self.BASE_PRICES:
            raise ValueError(f"Invalid cleaning type: {self.cleaning_type}. Valid options are: {list(self.BASE_PRICES.keys())}")

        total_cost = self.BASE_PRICES[self.cleaning_type]

        for add_on in self.add_ons:
            if add_on in self.ADD_ON_PRICES:
                total_cost += self.ADD_ON_PRICES[add_on]
            else:
                raise ValueError(f"Invalid add-on: {add_on}. Valid options are: {list(self.ADD_ON_PRICES.keys())}")

        return total_cost

    def generate_estimate(self):
        """
        Generates a free estimate for the cleaning service.

        :return: A string containing the estimate details
        """
        try:
            total_cost = self.calculate_cost()
            estimate_details = (
                f"Cleaning Type: {self.cleaning_type.capitalize()}\n"
                f"Add-Ons: {', '.join(self.add_ons).capitalize() if self.add_ons else 'None'}\n"
                f"Total Estimate Cost: ${total_cost:.2f}"
            )
            return estimate_details
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    try:
        cleaning_service = CleaningService(cleaning_type='deep', add_ons=['fridge_cleaning', 'oven_cleaning'])
        estimate = cleaning_service.generate_estimate()
        print(estimate)
    except Exception as e:
        print(f"An error occurred: {e}")
```
