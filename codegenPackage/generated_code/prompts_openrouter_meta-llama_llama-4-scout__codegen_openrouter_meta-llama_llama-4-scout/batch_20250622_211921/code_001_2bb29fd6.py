"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a Python script to calculate the Impuesto General a las Ventas (IGV) for a given amount in Peru, considering the current tax rates and regulations."
Generated: DETERMINISTIC_2bb29fd6749975db
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# igv_calculator.py

"""
Calculates the Impuesto General a las Ventas (IGV) for a given amount in Peru.

The IGV is a tax applied to the consumption of goods and services. In Peru, 
the current IGV rate is 18%.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_igv(amount: float, igv_rate: float = 0.18) -> float:
    """
    Calculates the IGV for a given amount.

    Args:
    - amount (float): The base amount to calculate the IGV.
    - igv_rate (float, optional): The IGV tax rate. Defaults to 0.18 (18%).

    Returns:
    - float: The calculated IGV amount.

    Raises:
    - ValueError: If the amount or igv_rate is negative.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if igv_rate < 0:
        raise ValueError("IGV rate cannot be negative.")

    # Calculate IGV
    igv = amount * igv_rate

    return igv

def calculate_total_amount(amount: float, igv_rate: float = 0.18) -> float:
    """
    Calculates the total amount including IGV.

    Args:
    - amount (float): The base amount.
    - igv_rate (float, optional): The IGV tax rate. Defaults to 0.18 (18%).

    Returns:
    - float: The total amount including IGV.

    Raises:
    - ValueError: If the amount or igv_rate is negative.
    """
    igv = calculate_igv(amount, igv_rate)
    total_amount = amount + igv

    return total_amount

def main():
    try:
        amount = float(input("Enter the amount: "))
        igv = calculate_igv(amount)
        total_amount = calculate_total_amount(amount)

        print(f"IGV (18%): S/ {igv:.2f}")
        print(f"Total Amount: S/ {total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
