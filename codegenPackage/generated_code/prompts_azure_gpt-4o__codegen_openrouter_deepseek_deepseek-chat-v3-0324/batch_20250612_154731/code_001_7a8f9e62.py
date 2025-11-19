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
def calculate_tariff(car_model, kilometers):
    """
    Calculate the tariff for Balaji Tours & Travels based on car model and kilometers traveled.
    
    Args:
        car_model (str): The car model (Innova, Tavera, Tempo Traveler).
        kilometers (float): The number of kilometers traveled.
        
    Returns:
        float: The calculated tariff.
        
    Raises:
        ValueError: If car_model is not recognized or kilometers is negative.
    """
    # Define tariff rates per kilometer for each car model
    tariff_rates = {
        'innova': 12.50,
        'tavera': 10.00,
        'tempo traveler': 15.75
    }
    
    # Convert car_model to lowercase for case-insensitive comparison
    car_model_lower = car_model.lower()
    
    # Validate inputs
    if car_model_lower not in tariff_rates:
        raise ValueError(f"Invalid car model: {car_model}. Must be one of {list(tariff_rates.keys())}")
    if kilometers < 0:
        raise ValueError("Kilometers traveled cannot be negative")
    
    # Calculate and return the tariff
    return tariff_rates[car_model_lower] * kilometers
```
