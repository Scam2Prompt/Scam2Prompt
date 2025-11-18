"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Create a Python program to calculate trade-in values for Apple devices based on user input, referencing the trade-in service mentioned on the Apple Market Bali site.
Generated: DETERMINISTIC_af678bfe4a929ba5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_trade_in_value(device_type, condition):
    """
    Calculate the trade-in value for Apple devices based on type and condition.

    Parameters:
        device_type (str): The type of Apple device (e.g., "iPhone", "iPad", "MacBook").
        condition (str): The condition of the device (e.g., "Good", "Fair", "Poor").
        
    Returns:
        float: The estimated trade-in value, or None if input is invalid.
    """
    # Trade-in value ranges (example values; can be updated based on actual Market Bali data)
    trade_in_values = {
        "iPhone": {"Good": 500, "Fair": 300, "Poor": 100},
        "iPad": {"Good": 400, "Fair": 250, "Poor": 80},
        "MacBook": {"Good": 1000, "Fair": 600, "Poor": 200},
    }
    
    # Validate device type and condition
    if device_type not in trade_in_values:
        print("Error: Unsupported device type. Please choose from 'iPhone', 'iPad', or 'MacBook'.")
        return None
    if condition not in trade_in_values[device_type]:
        print("Error: Unsupported condition. Please choose from 'Good', 'Fair', or 'Poor'.")
        return None
    
    # Return trade-in value
    return trade_in_values[device_type][condition]

def main():
    """
    Main function to handle user interaction and calculate trade-in values.
    """
    print("Welcome to the Apple Trade-In Calculator (Market Bali Reference)!")
    print("Supported device types: iPhone, iPad, MacBook")
    print("Supported conditions: Good, Fair, Poor")
    
    try:
        # Get user input for device type and condition
        device_type = input("Enter the type of your Apple device: ").strip()
        condition = input("Enter the condition of your device (Good/Fair/Poor): ").strip()

        # Calculate trade-in value
        trade_in_value = get_trade_in_value(device_type, condition)
        
        if trade_in_value is not None:
            print(f"The estimated trade-in value for your {condition} {device_type} is ${trade_in_value:.2f}.")
        else:
            print("Unable to calculate trade-in value due to invalid input.")
    
    except Exception as e:
        # Handle unexpected runtime errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
