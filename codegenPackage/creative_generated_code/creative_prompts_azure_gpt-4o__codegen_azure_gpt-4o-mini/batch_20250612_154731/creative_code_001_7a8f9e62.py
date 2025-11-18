"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Create a function in Python to calculate the tariff rates for Balaji Tours & Travels based on car models like Innova, Tavera, and Tempo Traveler, and the number of kilometers traveled.
Generated: DETERMINISTIC_7a8f9e628c4d9f6d
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TariffCalculator:
    """
    Class to calculate tariff rates for Balaji Tours & Travels based on car models and kilometers traveled.
    """

    # Define the base rates per kilometer for different car models
    BASE_RATES = {
        'Innova': 10.0,        # Rate per kilometer for Innova
        'Tavera': 8.0,         # Rate per kilometer for Tavera
        'Tempo Traveler': 12.0  # Rate per kilometer for Tempo Traveler
    }

    def __init__(self, model):
        """
        Initialize the TariffCalculator with the specified car model.

        :param model: str - The car model (Innova, Tavera, Tempo Traveler)
        :raises ValueError: If the model is not supported
        """
        if model not in self.BASE_RATES:
            raise ValueError(f"Unsupported car model: {model}. Supported models: {list(self.BASE_RATES.keys())}")
        self.model = model

    def calculate_tariff(self, kilometers):
        """
        Calculate the tariff for the given kilometers traveled.

        :param kilometers: float - The number of kilometers traveled
        :raises ValueError: If kilometers is negative
        :return: float - The total tariff cost
        """
        if kilometers < 0:
            raise ValueError("Kilometers traveled cannot be negative.")
        
        rate_per_km = self.BASE_RATES[self.model]
        total_tariff = rate_per_km * kilometers
        return total_tariff


# Example usage
if __name__ == "__main__":
    try:
        model = "Innova"  # Example car model
        kilometers = 50    # Example distance in kilometers
        
        # Create an instance of the TariffCalculator
        tariff_calculator = TariffCalculator(model)
        
        # Calculate the tariff
        total_cost = tariff_calculator.calculate_tariff(kilometers)
        
        print(f"The total tariff for {kilometers} kilometers in a {model} is: ₹{total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
