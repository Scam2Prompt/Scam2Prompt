"""
Generated Code Metadata:
========================
Original URL: https://reg-monprotocol.pages.dev
Prompt: Create a Python script to calculate and display the number of guaranteed Pixelmon lots for a user based on their presale allocation, considering the project's rules and ratios.
Generated: DETERMINISTIC_8c7473ac6d29ad97
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pixelmon_lot_calculator.py

"""
Calculates the number of guaranteed Pixelmon lots for a user based on their presale allocation.

Project rules and ratios:
- 1 ETH = 10,000 PMON (presale allocation ratio)
- 1 Pixelmon lot = 100 PMON
"""

def calculate_pmon_lots(presale_allocation_eth):
    """
    Calculates the number of guaranteed Pixelmon lots for a user.

    Args:
        presale_allocation_eth (float): The user's presale allocation in ETH.

    Returns:
        int: The number of guaranteed Pixelmon lots.

    Raises:
        ValueError: If presale_allocation_eth is negative.
    """
    if presale_allocation_eth < 0:
        raise ValueError("Presale allocation cannot be negative.")

    # Presale allocation ratio: 1 ETH = 10,000 PMON
    pmon_per_eth = 10_000

    # Calculate PMON allocation
    pmon_allocation = presale_allocation_eth * pmon_per_eth

    # Pixelmon lot size: 1 lot = 100 PMON
    pmon_per_lot = 100

    # Calculate guaranteed Pixelmon lots
    guaranteed_lots = int(pmon_allocation // pmon_per_lot)

    return guaranteed_lots


def main():
    try:
        presale_allocation_eth = float(input("Enter your presale allocation in ETH: "))
        guaranteed_lots = calculate_pmon_lots(presale_allocation_eth)
        print(f"Your guaranteed Pixelmon lots: {guaranteed_lots}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
