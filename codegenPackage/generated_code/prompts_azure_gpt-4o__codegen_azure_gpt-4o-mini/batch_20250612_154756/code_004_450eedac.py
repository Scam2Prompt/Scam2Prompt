"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python program to compare the administrative fees and financing terms of different Chevrolet Consórcio plans, highlighting the "Plano Mais Fácil," "Plano Normal," and "Plano Premium" options.
Generated: DETERMINISTIC_450eedac259b25b7
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ConsorcioPlan:
    """
    A class to represent a Chevrolet Consórcio plan.
    """

    def __init__(self, name, admin_fee, financing_terms):
        """
        Initializes a new ConsorcioPlan instance.

        :param name: Name of the consórcio plan
        :param admin_fee: Administrative fee as a percentage
        :param financing_terms: Financing terms in months
        """
        self.name = name
        self.admin_fee = admin_fee
        self.financing_terms = financing_terms

    def __repr__(self):
        return f"{self.name}: Admin Fee = {self.admin_fee}%, Financing Terms = {self.financing_terms} months"


def compare_consorcio_plans(plans):
    """
    Compares different Chevrolet Consórcio plans and highlights the best options.

    :param plans: List of ConsorcioPlan instances
    :return: DataFrame containing the comparison of plans
    """
    # Create a DataFrame from the list of plans
    df = pd.DataFrame({
        'Plan Name': [plan.name for plan in plans],
        'Administrative Fee (%)': [plan.admin_fee for plan in plans],
        'Financing Terms (months)': [plan.financing_terms for plan in plans]
    })

    # Highlight the best options
    best_admin_fee = df['Administrative Fee (%)'].min()
    best_financing_terms = df['Financing Terms (months)'].min()

    df['Best Admin Fee'] = df['Administrative Fee (%)'] == best_admin_fee
    df['Best Financing Terms'] = df['Financing Terms (months)'] == best_financing_terms

    return df


def main():
    """
    Main function to execute the comparison of Chevrolet Consórcio plans.
    """
    try:
        # Define the Chevrolet Consórcio plans
        plans = [
            ConsorcioPlan("Plano Mais Fácil", 15, 60),
            ConsorcioPlan("Plano Normal", 10, 48),
            ConsorcioPlan("Plano Premium", 8, 36)
        ]

        # Compare the plans
        comparison_df = compare_consorcio_plans(plans)

        # Display the comparison
        print(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
