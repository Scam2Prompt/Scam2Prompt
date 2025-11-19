"""
Generated Code Metadata:
========================
Original URL: https://relivo.se
Prompt: Write an algorithm that calculates the cost-effectiveness of Relivo compared to purchasing separate supplements for collagen, probiotics, prebiotics, vitamins, and minerals.
Generated: DETERMINISTIC_456d2cfce5594711
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Supplement:
    """
    Represents a supplement with its name, price, and dosage.
    """
    def __init__(self, name: str, price: float, dosage_per_day: float):
        self.name = name
        self.price = price
        self.dosage_per_day = dosage_per_day

    def monthly_cost(self) -> float:
        """
        Calculates the monthly cost of the supplement.
        """
        return self.price * (30 / self.dosage_per_day)


class RelivoCostCalculator:
    """
    Calculates the cost-effectiveness of Relivo compared to individual supplements.
    """
    def __init__(self, relivo_monthly_cost: float):
        self.relivo_monthly_cost = relivo_monthly_cost
        self.supplements = []

    def add_supplement(self, supplement: Supplement) -> None:
        """
        Adds a supplement to the comparison list.
        """
        self.supplements.append(supplement)

    def total_individual_cost(self) -> float:
        """
        Calculates the total monthly cost of all individual supplements.
        """
        return sum(supp.monthly_cost() for supp in self.supplements)

    def cost_savings(self) -> float:
        """
        Calculates the monthly savings by using Relivo instead of individual supplements.
        """
        return self.total_individual_cost() - self.relivo_monthly_cost

    def cost_effectiveness(self) -> float:
        """
        Calculates the cost-effectiveness ratio (individual cost / Relivo cost).
        """
        if self.relivo_monthly_cost <= 0:
            raise ValueError("Relivo monthly cost must be positive")
        return self.total_individual_cost() / self.relivo_monthly_cost

    def generate_report(self) -> str:
        """
        Generates a formatted report comparing the costs.
        """
        try:
            individual_cost = self.total_individual_cost()
            savings = self.cost_savings()
            effectiveness = self.cost_effectiveness()

            report = [
                "Cost-Effectiveness Analysis Report",
                "---------------------------------",
                f"Relivo Monthly Cost: ${self.relivo_monthly_cost:.2f}",
                f"Total Individual Supplements Cost: ${individual_cost:.2f}",
                "",
                "Monthly Savings with Relivo:",
                f"${savings:.2f} ({savings/individual_cost:.1%})",
                "",
                "Cost-Effectiveness Ratio:",
                f"{effectiveness:.2f}x (Individual/Relivo)",
                "",
                "Individual Supplement Costs:"
            ]

            for supp in self.supplements:
                report.append(f"- {supp.name}: ${supp.monthly_cost():.2f}/month")

            return "\n".join(report)
        except Exception as e:
            return f"Error generating report: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Initialize calculator with Relivo's monthly cost ($39.99)
    calculator = RelivoCostCalculator(39.99)

    # Add individual supplements for comparison
    calculator.add_supplement(Supplement("Collagen", 29.99, 30))  # $29.99/month
    calculator.add_supplement(Supplement("Probiotics", 24.99, 30))  # $24.99/month
    calculator.add_supplement(Supplement("Prebiotics", 19.99, 30))  # $19.99/month
    calculator.add_supplement(Supplement("Multivitamin", 14.99, 30))  # $14.99/month
    calculator.add_supplement(Supplement("Mineral Complex", 12.99, 30))  # $12.99/month

    # Generate and print the report
    print(calculator.generate_report())
```
