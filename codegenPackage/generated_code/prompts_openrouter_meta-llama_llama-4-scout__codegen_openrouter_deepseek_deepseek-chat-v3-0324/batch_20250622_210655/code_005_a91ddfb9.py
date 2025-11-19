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
def calculate_income(weight: float, price_per_pound: float) -> float:
    """
    Calculate the potential income from selling processed EPS Styrofoam.

    Args:
        weight (float): Weight of the Styrofoam in pounds.
        price_per_pound (float): Market price per pound in dollars.

    Returns:
        float: Total potential income from the sale.

    Raises:
        ValueError: If either weight or price_per_pound is negative.
    """
    if weight < 0 or price_per_pound < 0:
        raise ValueError("Weight and price per pound must be non-negative.")
    
    return weight * price_per_pound


def main():
    """Main function to handle user input and display results."""
    print("EPS Styrofoam Income Calculator")
    print("-------------------------------")
    
    try:
        weight = float(input("Enter the weight of Styrofoam (in pounds): "))
        price = float(input("Enter the market price per pound (in dollars): "))
        
        income = calculate_income(weight, price)
        print(f"\nPotential income: ${income:.2f}")
    
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
