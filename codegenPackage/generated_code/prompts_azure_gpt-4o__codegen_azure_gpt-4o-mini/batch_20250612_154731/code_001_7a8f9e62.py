"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: Create a function in Python to calculate the tariff rates for Balaji Tours & Travels based on car models like Innova, Tavera, and Tempo Traveler, and the number of kilometers traveled.
Generated: DETERMINISTIC_7a8f9e628c4d9f6d
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TariffCalculator:
    """
    A class to calculate the tariff rates for Balaji Tours & Travels based on car models and kilometers traveled.
    """

    # Tariff rates per kilometer for different car models
    TARIF_RATES = {
        'Innova': 10.0,  # Rate per kilometer for Innova
        'Tavera': 8.0,   # Rate per kilometer for Tavera
        'Tempo Traveler': 12.0  # Rate per kilometer for Tempo Traveler
    }

    @staticmethod
    def calculate_tariff(car_model: str, kilometers: float) -> float:
        """
        Calculate the tariff based on the car model and kilometers traveled.

        :param car_model: The model of the car (Innova, Tavera, Tempo Traveler)
        :param kilometers: The number of kilometers traveled
        :return: The total tariff cost
        :raises ValueError: If the car model is not recognized or kilometers is negative
        """
        # Validate input
        if car_model not in TariffCalculator.TARIF_RATES:
            raise ValueError(f"Unrecognized car model: {car_model}. Valid options are: {', '.join(TariffCalculator.TARIF_RATES.keys())}.")
        
        if kilometers < 0:
            raise ValueError("Kilometers traveled cannot be negative.")

        # Calculate the tariff
        rate_per_km = TariffCalculator.TARIF_RATES[car_model]
        total_tariff = rate_per_km * kilometers
        
        return total_tariff


# Example usage
if __name__ == "__main__":
    try:
        car_model_input = 'Innova'
        kilometers_input = 150.0
        total_cost = TariffCalculator.calculate_tariff(car_model_input, kilometers_input)
        print(f"The total tariff for {car_model_input} for {kilometers_input} kilometers is: ₹{total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
