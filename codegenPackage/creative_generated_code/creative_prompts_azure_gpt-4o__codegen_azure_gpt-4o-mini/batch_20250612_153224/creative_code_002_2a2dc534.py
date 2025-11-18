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
class CleaningService:
    """
    Represents a cleaning service that calculates costs based on service type
    and additional options.
    """
    
    # Base prices for different cleaning types
    BASE_PRICES = {
        "standard": 100,
        "deep": 200,
        "post_renovation": 300
    }

    # Prices for add-on services
    ADD_ON_PRICES = {
        "fridge_cleaning": 30,
        "oven_cleaning": 40,
        "window_cleaning": 50
    }
    
    def __init__(self, cleaning_type: str, add_ons: list = None):
        """
        Initializes the CleaningService with a specific cleaning type and optional add-ons.

        :param cleaning_type: Type of cleaning service ('standard', 'deep', 'post_renovation')
        :param add_ons: List of additional services selected by the user
        """
        self.cleaning_type = cleaning_type
        self.add_ons = add_ons if add_ons else []

    def validate_cleaning_type(self):
        """
        Validates the cleaning type against the predefined options.
        
        :raises ValueError: If the cleaning type is not valid
        """
        if self.cleaning_type not in self.BASE_PRICES:
            raise ValueError(f"Invalid cleaning type: {self.cleaning_type}. "
                             f"Valid options are: {', '.join(self.BASE_PRICES.keys())}")

    def validate_add_ons(self):
        """
        Validates the selected add-ons against the predefined options.
        
        :raises ValueError: If any add-on is not valid
        """
        for add_on in self.add_ons:
            if add_on not in self.ADD_ON_PRICES:
                raise ValueError(f"Invalid add-on: {add_on}. "
                                 f"Valid options are: {', '.join(self.ADD_ON_PRICES.keys())}")

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the cleaning service based on selected type and add-ons.

        :return: Total cost as a float
        """
        self.validate_cleaning_type()
        self.validate_add_ons()
        
        total_cost = self.BASE_PRICES[self.cleaning_type]
        
        for add_on in self.add_ons:
            total_cost += self.ADD_ON_PRICES[add_on]
        
        return total_cost

    def generate_estimate(self):
        """
        Generates a free estimate of the cleaning service.

        :return: Estimated cost as a formatted string
        """
        try:
            total_cost = self.calculate_total_cost()
            return f"Your estimated cost for {self.cleaning_type} cleaning with add-ons {self.add_ons} is: ${total_cost:.2f}"
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    try:
        # Create a cleaning service instance
        service = CleaningService(cleaning_type="deep", add_ons=["fridge_cleaning", "oven_cleaning"])
        
        # Generate and print the estimate
        estimate = service.generate_estimate()
        print(estimate)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
