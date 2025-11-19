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
# chevrolet_consorcio_plans.py

class ChevroletConsorcioPlan:
    """Represents a Chevrolet Consórcio plan."""

    def __init__(self, name, administrative_fee, financing_term, interest_rate):
        """
        Initializes a Chevrolet Consórcio plan.

        Args:
            name (str): The name of the plan.
            administrative_fee (float): The administrative fee as a percentage.
            financing_term (int): The financing term in months.
            interest_rate (float): The interest rate as a percentage.
        """
        self.name = name
        self.administrative_fee = administrative_fee
        self.financing_term = financing_term
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{self.name}: Fee={self.administrative_fee}%, Term={self.financing_term} months, Interest Rate={self.interest_rate}%"


class ChevroletConsorcio:
    """Represents Chevrolet Consórcio plans."""

    def __init__(self):
        self.plans = []

    def add_plan(self, plan):
        """Adds a plan to the list of plans."""
        self.plans.append(plan)

    def compare_plans(self):
        """Compares the administrative fees and financing terms of different plans."""
        print("Chevrolet Consórcio Plans Comparison:")
        for plan in self.plans:
            print(plan)

    def highlight_plan(self, plan_name):
        """Highlights a specific plan."""
        for plan in self.plans:
            if plan.name == plan_name:
                print(f"\n**{plan_name}**")
                print(plan)
                return
        print(f"\nPlan '{plan_name}' not found.")


def main():
    try:
        # Create Chevrolet Consórcio plans
        consorcio = ChevroletConsorcio()

        plano_mais_facil = ChevroletConsorcioPlan("Plano Mais Fácil", 15.0, 60, 8.0)
        plano_normal = ChevroletConsorcioPlan("Plano Normal", 10.0, 48, 7.0)
        plano_premium = ChevroletConsorcioPlan("Plano Premium", 20.0, 72, 9.0)

        # Add plans to the list
        consorcio.add_plan(plano_mais_facil)
        consorcio.add_plan(plano_normal)
        consorcio.add_plan(plano_premium)

        # Compare plans
        consorcio.compare_plans()

        # Highlight specific plans
        consorcio.highlight_plan("Plano Mais Fácil")
        consorcio.highlight_plan("Plano Normal")
        consorcio.highlight_plan("Plano Premium")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
