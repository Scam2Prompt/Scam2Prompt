"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Write a Python script to calculate the percentage increase in value for antique coins based on auction data, using examples like the "1908 Austria 100 Corona Gold Coin" from Premium Coin's website.
Generated: DETERMINISTIC_64f47a0d9491e9bd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_percentage_increase(initial_value, final_value):
    """
    Calculate the percentage increase between two values.

    Parameters:
        initial_value (float): The initial value of the coin.
        final_value (float): The final auction value of the coin.

    Returns:
        float: The percentage increase, rounded to two decimal places.
    """
    if initial_value <= 0:
        raise ValueError("Initial value must be greater than zero.")
    if final_value <= 0:
        raise ValueError("Final value must be greater than zero.")

    percentage_increase = ((final_value - initial_value) / initial_value) * 100
    return round(percentage_increase, 2)


def main():
    """
    Main function to calculate percentage increase for antique coins based on user input.
    """
    try:
        print("Antique Coin Percentage Increase Calculator")
        
        # Use the 1908 Austria 100 Corona Gold Coin example for demonstration
        # Initial value obtained from historical price data
        initial_value = float(input("Enter the initial value of the coin (e.g., 1200.00): "))
        
        # Final value obtained from recent auction price data
        final_value = float(input("Enter the final value of the coin (e.g., 1500.00): "))

        # Calculate the percentage increase
        percentage_increase = calculate_percentage_increase(initial_value, final_value)
        
        print(f"The percentage increase in value is {percentage_increase}%.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
