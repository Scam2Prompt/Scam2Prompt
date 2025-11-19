"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: "Develop a basic calculator script to determine the potential income from selling processed EPS Styrofoam, given the weight of the Styrofoam and the market price per pound."
Generated: DETERMINISTIC_a91ddfb9e8247e10
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
EPS Styrofoam Income Calculator

Calculates the potential income from selling processed EPS Styrofoam based on its weight and market price per pound.
"""

def calculate_income(weight_in_pounds: float, market_price_per_pound: float) -> float:
    """
    Calculates the potential income from selling processed EPS Styrofoam.

    Args:
        weight_in_pounds (float): The weight of the Styrofoam in pounds.
        market_price_per_pound (float): The market price per pound of Styrofoam.

    Returns:
        float: The potential income from selling the Styrofoam.

    Raises:
        ValueError: If the weight or market price is negative.
    """
    if weight_in_pounds < 0 or market_price_per_pound < 0:
        raise ValueError("Weight and market price must be non-negative.")

    income = weight_in_pounds * market_price_per_pound
    return income


def main():
    try:
        weight_in_pounds = float(input("Enter the weight of the Styrofoam in pounds: "))
        market_price_per_pound = float(input("Enter the market price per pound of Styrofoam: $"))

        income = calculate_income(weight_in_pounds, market_price_per_pound)

        print(f"The potential income from selling {weight_in_pounds} pounds of Styrofoam at ${market_price_per_pound:.2f} per pound is: ${income:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
