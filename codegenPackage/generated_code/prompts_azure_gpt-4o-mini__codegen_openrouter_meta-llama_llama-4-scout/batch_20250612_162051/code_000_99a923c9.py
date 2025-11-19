"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: Write a Python script that calculates the potential tax savings from the MP 2.199-14/2001 for a company in the energy sector looking to reduce its IRPJ by 75%.
Generated: DETERMINISTIC_99a923c992e6cb00
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mp_2199_14_tax_savings_calculator.py

"""
Calculates the potential tax savings from MP 2.199-14/2001 for a company in the energy sector.

This script assumes that the company is looking to reduce its IRPJ (Imposto sobre a Renda e Proventos de Qualquer Natureza) by 75%.
"""

import math

def calculate_irpj_reduction(current_irpj: float, reduction_percentage: float = 0.75) -> float:
    """
    Calculates the reduced IRPJ amount.

    Args:
    - current_irpj (float): The current IRPJ amount.
    - reduction_percentage (float): The percentage of reduction. Defaults to 0.75.

    Returns:
    - float: The reduced IRPJ amount.
    """
    if current_irpj < 0:
        raise ValueError("Current IRPJ cannot be negative")

    if reduction_percentage < 0 or reduction_percentage > 1:
        raise ValueError("Reduction percentage must be between 0 and 1")

    reduced_irpj = current_irpj * (1 - reduction_percentage)
    return reduced_irpj

def calculate_tax_savings(current_irpj: float, reduced_irpj: float) -> float:
    """
    Calculates the tax savings.

    Args:
    - current_irpj (float): The current IRPJ amount.
    - reduced_irpj (float): The reduced IRPJ amount.

    Returns:
    - float: The tax savings.
    """
    tax_savings = current_irpj - reduced_irpj
    return tax_savings

def main():
    try:
        current_irpj = float(input("Enter the current IRPJ amount: R$ "))
        reduced_irpj = calculate_irpj_reduction(current_irpj)
        tax_savings = calculate_tax_savings(current_irpj, reduced_irpj)

        print(f"Current IRPJ: R$ {current_irpj:.2f}")
        print(f"Reduced IRPJ (75% reduction): R$ {reduced_irpj:.2f}")
        print(f"Tax Savings: R$ {tax_savings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
