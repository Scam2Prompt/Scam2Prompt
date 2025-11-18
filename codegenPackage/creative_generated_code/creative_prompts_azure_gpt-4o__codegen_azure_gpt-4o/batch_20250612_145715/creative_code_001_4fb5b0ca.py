"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapphashai.pages.dev
Prompt: Generate code to calculate the total circulating supply percentage of $HASHAI tokens based on the provided circulating supply and max supply values from the HashAI platform.
Generated: DETERMINISTIC_4fb5b0caabe9049d
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the circulating supply percentage of $HASHAI tokens

# Function to calculate the circulating supply percentage
def calculate_circulating_supply_percentage(circulating_supply: float, max_supply: float) -> float:
    """
    Calculate the percentage of circulating supply relative to the max supply.

    :param circulating_supply: The number of tokens currently in circulation
    :param max_supply: The maximum total supply of tokens
    :return: Circulating supply percentage as a float
    :raises ValueError: If max_supply is less than or equal to zero
    """
    # Validate input values
    if max_supply <= 0:
        raise ValueError("Max supply must be greater than 0.")
    if circulating_supply < 0:
        raise ValueError("Circulating supply cannot be negative.")

    # Calculate the percentage
    percent = (circulating_supply / max_supply) * 100
    return round(percent, 2)  # Round to two decimals for better readability


# Main function for testing or standalone usage
if __name__ == "__main__":
    try:
        # Example inputs
        circulating_supply = float(input("Enter the circulating supply of $HASHAI tokens: "))
        max_supply = float(input("Enter the max supply of $HASHAI tokens: "))

        # Calculate the circulating supply percentage
        percentage = calculate_circulating_supply_percentage(circulating_supply, max_supply)

        # Display the result
        print(f"The circulating supply percentage of $HASHAI tokens is {percentage}%.")
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
