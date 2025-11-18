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
# Function to calculate tariff rates for Balaji Tours & Travels
def calculate_tariff(car_model, kilometers):
    """
    Calculate the tariff rates based on car model and kilometers traveled.
    
    Parameters:
        car_model (str): The car model (e.g., 'Innova', 'Tavera', 'Tempo Traveler').
        kilometers (float): The number of kilometers traveled.
        
    Returns:
        float: The total tariff cost.
        
    Raises:
        ValueError: If the car model is invalid or kilometers are negative.
    """

    # Tariff rates per kilometer for each car model
    tariff_rates = {
        "Innova": 12.0,         # Rate per km for Innova
        "Tavera": 10.0,         # Rate per km for Tavera
        "Tempo Traveler": 15.0  # Rate per km for Tempo Traveler
    }

    # Validate input
    if car_model not in tariff_rates:
        raise ValueError(f"Invalid car model: {car_model}. Valid options are: {', '.join(tariff_rates.keys())}")
    if kilometers < 0:
        raise ValueError("Kilometers traveled cannot be negative.")
    
    # Calculate and return the tariff cost
    cost_per_km = tariff_rates[car_model]
    total_cost = cost_per_km * kilometers
    return total_cost


# Example usage:
if __name__ == "__main__":
    try:
        # Input data
        car = "Innova"
        km_traveled = 150
        
        # Calculate tariff
        result = calculate_tariff(car, km_traveled)
        print(f"The total tariff for {car} traveling {km_traveled} km is: ₹{result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
