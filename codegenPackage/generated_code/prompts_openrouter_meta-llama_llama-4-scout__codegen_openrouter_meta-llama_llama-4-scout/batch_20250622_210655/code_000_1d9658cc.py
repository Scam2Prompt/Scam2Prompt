"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Write a code snippet in Python to calculate the reduction of 75% of IRPJ tax for a company in the Northeast region of Brazil, considering the MP 2.199-14/2001 law."
Generated: DETERMINISTIC_1d9658cca7d41be2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coding: utf-8

"""
Calculates the reduction of 75% of IRPJ tax for a company in the Northeast region of Brazil,
considering the MP2.199-14/2001 law.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_irpj_reduction(tax_value: float, region: str, is_northeast: bool) -> float:
    """
    Calculates the reduction of IRPJ tax.

    Args:
    - tax_value (float): The original IRPJ tax value.
    - region (str): The region where the company is located.
    - is_northeast (bool): Flag indicating if the company is in the Northeast region.

    Returns:
    - float: The reduced IRPJ tax value.

    Raises:
    - ValueError: If the tax value is negative or if the region is not provided.
    """

    # Check if tax value is valid
    if tax_value < 0:
        raise ValueError("Tax value cannot be negative.")

    # Check if region is provided
    if not region:
        raise ValueError("Region must be provided.")

    # Define the reduction percentage
    reduction_percentage = 0.75

    # Check if the company is in the Northeast region
    if is_northeast:
        # Apply the reduction according to MP2.199-14/2001 law
        reduced_tax = tax_value * (1 - reduction_percentage)
        return reduced_tax
    else:
        # No reduction applied
        return tax_value


def main():
    try:
        # Example usage
        tax_value = 10000.0
        region = "Northeast"
        is_northeast = True

        reduced_tax = calculate_irpj_reduction(tax_value, region, is_northeast)
        print(f"Reduced IRPJ tax: R${reduced_tax:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
