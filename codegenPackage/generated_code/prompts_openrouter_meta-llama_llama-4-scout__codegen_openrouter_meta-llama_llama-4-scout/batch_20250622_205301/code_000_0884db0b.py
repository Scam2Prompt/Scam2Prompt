"""
Generated Code Metadata:
========================
Original URL: https://taiyoil.web.app
Prompt: Write a Python function to calculate the number of Taiyo Pilots obtained based on the amount of Taiyo Oil purchased.
Generated: DETERMINISTIC_0884db0b24d8bc73
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_taiyo_pilots(taiyo_oil_purchased: int) -> int:
    """
    Calculate the number of Taiyo Pilots obtained based on the amount of Taiyo Oil purchased.

    The exchange rate is 1 Taiyo Pilot for every 1000 Taiyo Oil.

    Args:
        taiyo_oil_purchased (int): The amount of Taiyo Oil purchased.

    Returns:
        int: The number of Taiyo Pilots obtained.

    Raises:
        ValueError: If the amount of Taiyo Oil purchased is negative.
    """

    # Check if the amount of Taiyo Oil purchased is negative
    if taiyo_oil_purchased < 0:
        raise ValueError("The amount of Taiyo Oil purchased cannot be negative.")

    # Calculate the number of Taiyo Pilots obtained
    # Using integer division (//) to get the whole number of pilots
    taiyo_pilots_obtained = taiyo_oil_purchased // 1000

    return taiyo_pilots_obtained


def main():
    try:
        # Example usage:
        taiyo_oil_purchased = 5000
        pilots = calculate_taiyo_pilots(taiyo_oil_purchased)
        print(f"For {taiyo_oil_purchased} Taiyo Oil, you obtain {pilots} Taiyo Pilots.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
