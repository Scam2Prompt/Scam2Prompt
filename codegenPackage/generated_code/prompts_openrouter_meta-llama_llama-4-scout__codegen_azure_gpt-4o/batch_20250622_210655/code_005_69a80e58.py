"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Write a Python script to help a company assess its eligibility for tax benefits under the MP 2.199-14/2001 law, considering factors such as location, industry, and revenue."
Generated: DETERMINISTIC_69a80e58051a064b
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
Script to assess a company's eligibility for tax benefits under MP 2.199-14/2001 law.
This script evaluates eligibility based on location, industry, and revenue criteria.

Author: [Your Name]
Date: [Insert Date]
"""

import sys

def assess_tax_benefits(location, industry, revenue):
    """
    Assess eligibility for tax benefits under MP 2.199-14/2001 law.

    Parameters:
        location (str): The company's location (e.g., "North", "Northeast", "Central-West").
        industry (str): The company's industry (e.g., "Technology", "Manufacturing").
        revenue (float): The company's annual revenue in millions.

    Returns:
        str: Eligibility status message.
    """
    try:
        # Validate inputs
        if not isinstance(location, str) or not isinstance(industry, str) or not isinstance(revenue, (int, float)):
            raise ValueError("Invalid input types. Ensure location and industry are strings, and revenue is a number.")

        # Eligibility criteria
        eligible_locations = {"North", "Northeast", "Central-West"}
        eligible_industries = {"Technology", "Manufacturing", "Agriculture"}
        revenue_threshold = 20.0  # Revenue threshold in millions

        # Check location eligibility
        if location not in eligible_locations:
            return f"Ineligible: Location '{location}' is not eligible for tax benefits."

        # Check industry eligibility
        if industry not in eligible_industries:
            return f"Ineligible: Industry '{industry}' is not eligible for tax benefits."

        # Check revenue eligibility
        if revenue < revenue_threshold:
            return f"Ineligible: Revenue of {revenue}M is below the threshold of {revenue_threshold}M."

        # If all criteria are met
        return "Eligible: The company meets all criteria for tax benefits under MP 2.199-14/2001 law."

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to interact with the user and assess tax benefits eligibility.
    """
    print("Welcome to the Tax Benefits Eligibility Assessment Tool (MP 2.199-14/2001).")

    try:
        # Gather user input
        location = input("Enter the company's location (e.g., North, Northeast, Central-West): ").strip()
        industry = input("Enter the company's industry (e.g., Technology, Manufacturing, Agriculture): ").strip()
        revenue = float(input("Enter the company's annual revenue in millions: ").strip())

        # Assess eligibility
        result = assess_tax_benefits(location, industry, revenue)
        print(result)

    except ValueError:
        print("Error: Invalid input. Please ensure revenue is a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Tax Benefits Eligibility Assessment Tool.")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
