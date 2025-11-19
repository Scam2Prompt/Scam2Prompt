"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Write a Python script that calculates the total cost in ETH for purchasing multiple lots during a presale, given the price per lot is ETH 0.096.
Generated: DETERMINISTIC_d393622756b05507
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# presale_cost_calculator.py

def calculate_total_cost(lots: int, price_per_lot: float = 0.096) -> float:
    """
    Calculate the total cost in ETH for purchasing multiple lots during a presale.

    Parameters:
    lots (int): The number of lots to purchase.
    price_per_lot (float): The price of a single lot in ETH. Default is 0.096 ETH.

    Returns:
    float: The total cost in ETH.

    Raises:
    ValueError: If the number of lots is negative or not an integer.
    """
    if not isinstance(lots, int) or lots < 0:
        raise ValueError("The number of lots must be a non-negative integer.")

    total_cost = lots * price_per_lot
    return total_cost

def main():
    """Main function to execute the presale cost calculation."""
    try:
        # Prompt user for the number of lots
        lots_input = input("Enter the number of lots you wish to purchase: ")

        # Convert input to integer
        lots = int(lots_input)

        # Calculate total cost
        total_cost = calculate_total_cost(lots)

        # Display the result
        print(f"The total cost for purchasing {lots} lot(s) is: {total_cost:.6f} ETH")

    except ValueError as e:
        # Handle errors in input or calculation
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
