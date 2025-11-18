"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python program to compare the administrative fees and financing terms of different Chevrolet Consórcio plans, highlighting the "Plano Mais Fácil," "Plano Normal," and "Plano Premium" options.
Generated: DETERMINISTIC_450eedac259b25b7
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ConsorcioPlan:
    """
    A class to represent a Chevrolet Consórcio plan.
    """
    def __init__(self, name, admin_fee_percentage, financing_term_months):
        """
        Initializes a ConsorcioPlan instance.

        :param name: Name of the plan (e.g., "Plano Mais Fácil", "Plano Normal", "Plano Premium").
        :param admin_fee_percentage: Administrative fee in percentage.
        :param financing_term_months: Financing term in months.
        """
        self.name = name
        self.admin_fee_percentage = admin_fee_percentage
        self.financing_term_months = financing_term_months

    def __str__(self):
        """
        Returns a string representation of the plan.
        """
        return f"{self.name}: Administrative Fee = {self.admin_fee_percentage}% | Financing Term = {self.financing_term_months} months"


def compare_consorcio_plans(plans):
    """
    Compares consórcio plans based on administrative fees and financing terms.

    :param plans: List of ConsorcioPlan objects.
    :return: Tuple containing the plan with the lowest admin fee and the plan with the longest financing term.
    """
    if not plans:
        raise ValueError("Plan list is empty. Please provide valid plans for comparison.")

    # Find the plan with the lowest administrative fee
    plan_with_lowest_fee = min(plans, key=lambda plan: plan.admin_fee_percentage)

    # Find the plan with the longest financing term
    plan_with_longest_term = max(plans, key=lambda plan: plan.financing_term_months)

    return plan_with_lowest_fee, plan_with_longest_term


def main():
    """
    Main function to compare Chevrolet Consórcio plans.
    """
    try:
        # Create instances of the ConsorcioPlan representing different plans
        plano_mais_facil = ConsorcioPlan(name="Plano Mais Fácil", admin_fee_percentage=10, financing_term_months=60)
        plano_normal = ConsorcioPlan(name="Plano Normal", admin_fee_percentage=12, financing_term_months=72)
        plano_premium = ConsorcioPlan(name="Plano Premium", admin_fee_percentage=8, financing_term_months=84)

        # Collect the plans into a list
        plans = [plano_mais_facil, plano_normal, plano_premium]

        # Perform comparison
        lowest_fee_plan, longest_term_plan = compare_consorcio_plans(plans)

        # Display the results
        print("Comparison of Chevrolet Consórcio Plans:")
        print("Plans:")
        for plan in plans:
            print(plan)

        print("\nHighlights:")
        print(f"Plan with the Lowest Administrative Fee: {lowest_fee_plan}")
        print(f"Plan with the Longest Financing Term: {longest_term_plan}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
