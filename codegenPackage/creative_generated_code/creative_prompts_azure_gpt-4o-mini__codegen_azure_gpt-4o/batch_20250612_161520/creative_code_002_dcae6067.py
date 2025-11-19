"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Create a function that calculates the trade-in value of a used Suzuki car based on the Suzuki Certified Used Car Program guidelines mentioned on the Suzuki Capital Motors site.
Generated: DETERMINISTIC_dcae60673f0840fe
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the trade-in value of a Suzuki car based on Suzuki Certified Used Car Program guidelines

def calculate_trade_in_value(car_age, mileage, base_value, condition):
    """
    Calculate the trade-in value of a used Suzuki car.
    
    Parameters:
        car_age (int): Age of the car in years.
        mileage (int): Total mileage of the car in kilometers.
        base_value (float): Initial base value of the car when new.
        condition (str): Condition of the car (options: "Excellent", "Good", "Fair", "Poor").
        
    Returns:
        float: Calculated trade-in value of the car.
    """
    
    # Validate inputs
    if not (isinstance(car_age, int) and car_age >= 0):
        raise ValueError("Car age must be a non-negative integer.")
    if not (isinstance(mileage, int) and mileage >= 0):
        raise ValueError("Mileage must be a non-negative integer.")
    if not (isinstance(base_value, (int, float)) and base_value >= 0):
        raise ValueError("Base value must be a non-negative number.")
    if condition not in ["Excellent", "Good", "Fair", "Poor"]:
        raise ValueError("Condition must be one of: 'Excellent', 'Good', 'Fair', 'Poor'.")
    
    # Constants for depreciation
    AGE_DEPRECIATION_RATE = 0.05  # 5% depreciation per year
    MILEAGE_DEPRECIATION_RATE = 0.0001  # 0.01% depreciation per kilometer
    CONDITION_MULTIPLIER = {
        "Excellent": 1.0,  # No deduction for excellent condition
        "Good": 0.9,       # 10% deduction for good condition
        "Fair": 0.7,       # 30% deduction for fair condition
        "Poor": 0.5        # 50% deduction for poor condition
    }
    
    # Calculate depreciation based on age
    age_depreciation = base_value * (AGE_DEPRECIATION_RATE * car_age)
    
    # Calculate depreciation based on mileage
    mileage_depreciation = base_value * (MILEAGE_DEPRECIATION_RATE * mileage)
    
    # Apply condition multiplier
    condition_multiplier = CONDITION_MULTIPLIER[condition]
    
    # Calculate final trade-in value
    trade_in_value = base_value - age_depreciation - mileage_depreciation
    trade_in_value *= condition_multiplier
    
    # Ensure the trade-in value is not negative
    trade_in_value = max(trade_in_value, 0.0)
    
    return trade_in_value


# Example usage:
if __name__ == "__main__":
    try:
        # Inputs
        car_age = 5  # Car is 5 years old
        mileage = 60000  # Car has 60,000 km mileage
        base_value = 20000.0  # Initial base value of the car
        condition = "Good"  # Condition of the car
        
        # Calculate trade-in value
        value = calculate_trade_in_value(car_age, mileage, base_value, condition)
        
        # Print the result
        print(f"The trade-in value of the car is: ${value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
