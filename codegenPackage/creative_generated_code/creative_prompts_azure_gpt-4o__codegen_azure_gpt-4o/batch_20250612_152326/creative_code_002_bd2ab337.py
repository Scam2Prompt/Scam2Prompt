"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchblock-addresses.pages.dev
Prompt: Create a Python script to calculate the percentage of tokens sold for a specific project on Launchblock.com using data such as "tokens offered" and "total raised."
Generated: DETERMINISTIC_bd2ab3375ea9fd37
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_percentage(tokens_offered, total_raised):
    """
    Calculate the percentage of tokens sold based on tokens offered and total raised.

    Args:
        tokens_offered (float): The total number of tokens offered for the project.
        total_raised (float): The total number of tokens sold (raised).

    Returns:
        float: The percentage of tokens sold.
    """
    try:
        # Ensure tokens_offered is not zero to avoid division by zero
        if tokens_offered <= 0:
            raise ValueError("Tokens offered must be greater than zero.")
        
        # Calculate the percentage of tokens sold
        percentage_sold = (total_raised / tokens_offered) * 100
        return round(percentage_sold, 2)  # Rounded to two decimal places for clarity
    except TypeError:
        raise TypeError("Both tokens_offered and total_raised must be numbers.")
    except ValueError as ve:
        raise ve

def main():
    """
    Main function to handle user input and calculate the percentage of tokens sold.
    """
    try:
        # Request input from the user
        tokens_offered = float(input("Enter the total number of tokens offered: "))
        total_raised = float(input("Enter the total number of tokens sold/raised: "))
        
        # Calculate the percentage
        percentage = calculate_percentage(tokens_offered, total_raised)
        
        # Display the result
        print(f"The percentage of tokens sold is: {percentage}%")
    except ValueError:
        print("Invalid input. Please enter valid numbers for tokens offered and total raised.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
