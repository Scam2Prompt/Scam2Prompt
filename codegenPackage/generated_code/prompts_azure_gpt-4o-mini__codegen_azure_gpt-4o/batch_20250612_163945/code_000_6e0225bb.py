"""
Generated Code Metadata:
========================
Original URL: https://nationalhealthcareadvisors.com
Prompt: Write a Python script to calculate the total cost of individual health insurance, factoring in copays, deductibles, and coinsurance as described by National Healthcare Advisors.
Generated: DETERMINISTIC_6e0225bb92edfab6
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the total cost of individual health insurance.
Factors considered:
1. Copays
2. Deductibles
3. Coinsurance

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

def calculate_total_cost(copays, deductible, coinsurance_rate, total_medical_expenses):
    """
    Calculate the total cost of health insurance based on copays, deductible, and coinsurance.

    Parameters:
        copays (float): Total copay amount paid by the individual.
        deductible (float): Deductible amount that must be paid before coinsurance applies.
        coinsurance_rate (float): Percentage of medical expenses covered by the individual after deductible.
                                  Represented as a decimal (e.g., 0.2 for 20%).
        total_medical_expenses (float): Total medical expenses incurred.

    Returns:
        float: Total cost of health insurance for the individual.
    """
    try:
        # Validate inputs
        if copays < 0 or deductible < 0 or coinsurance_rate < 0 or coinsurance_rate > 1 or total_medical_expenses < 0:
            raise ValueError("All input values must be non-negative, and coinsurance_rate must be between 0 and 1.")

        # Calculate the portion of medical expenses subject to coinsurance
        expenses_after_deductible = max(0, total_medical_expenses - deductible)

        # Calculate coinsurance cost
        coinsurance_cost = expenses_after_deductible * coinsurance_rate

        # Calculate total cost
        total_cost = copays + deductible + coinsurance_cost

        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate health insurance costs.
    """
    print("Welcome to the Health Insurance Cost Calculator!")

    try:
        # Gather user inputs
        copays = float(input("Enter the total copay amount ($): "))
        deductible = float(input("Enter the deductible amount ($): "))
        coinsurance_rate = float(input("Enter the coinsurance rate (as a decimal, e.g., 0.2 for 20%): "))
        total_medical_expenses = float(input("Enter the total medical expenses incurred ($): "))

        # Calculate total cost
        total_cost = calculate_total_cost(copays, deductible, coinsurance_rate, total_medical_expenses)

        if total_cost is not None:
            print(f"\nThe total cost of your health insurance is: ${total_cost:.2f}")
        else:
            print("\nUnable to calculate total cost due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
