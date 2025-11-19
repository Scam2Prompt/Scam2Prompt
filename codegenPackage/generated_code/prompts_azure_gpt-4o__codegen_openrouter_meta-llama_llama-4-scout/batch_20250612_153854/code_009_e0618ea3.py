"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Create a program that models collaboration and mutual success metrics for investment partnerships, inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.
Generated: DETERMINISTIC_e0618ea3d59ff1cb
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# collaboration_metrics.py

class InvestmentPartnership:
    """
    Models collaboration and mutual success metrics for investment partnerships.
    """

    def __init__(self, name, partners=None):
        """
        Initializes an InvestmentPartnership instance.

        Args:
            name (str): The name of the partnership.
            partners (list[str], optional): A list of partner names. Defaults to None.
        """
        self.name = name
        self.partners = partners if partners else []
        self.investments = []
        self.success_metrics = {}

    def add_partner(self, partner_name):
        """
        Adds a partner to the partnership.

        Args:
            partner_name (str): The name of the partner to add.
        """
        self.partners.append(partner_name)

    def add_investment(self, investment_name, partner_contributions):
        """
        Adds an investment to the partnership.

        Args:
            investment_name (str): The name of the investment.
            partner_contributions (dict[str, float]): A dictionary of partner contributions.

        Raises:
            ValueError: If partner contributions do not add up to 100%.
        """
        if abs(sum(partner_contributions.values()) - 100) > 1e-6:
            raise ValueError("Partner contributions must add up to 100%")

        self.investments.append({
            "name": investment_name,
            "partner_contributions": partner_contributions
        })

    def calculate_success_metrics(self):
        """
        Calculates mutual success metrics for the partnership.

        Returns:
            dict[str, float]: A dictionary of success metrics for each partner.
        """
        self.success_metrics = {}

        for partner in self.partners:
            total_contribution = 0
            successful_investments = 0

            for investment in self.investments:
                contribution = investment["partner_contributions"].get(partner, 0)
                total_contribution += contribution
                if contribution > 0:
                    successful_investments += 1

            self.success_metrics[partner] = {
                "total_contribution": total_contribution,
                "successful_investments": successful_investments,
                "success_rate": successful_investments / len(self.investments) if self.investments else 0
            }

        return self.success_metrics

    def get_partnership_performance(self):
        """
        Calculates overall partnership performance.

        Returns:
            dict[str, float]: A dictionary of partnership performance metrics.
        """
        total_successful_investments = sum(
            metrics["successful_investments"] for metrics in self.success_metrics.values()
        )

        return {
            "total_investments": len(self.investments),
            "total_successful_investments": total_successful_investments,
            "overall_success_rate": total_successful_investments / len(self.investments) if self.investments else 0
        }


def main():
    try:
        partnership = InvestmentPartnership("Alghanim Capital")

        partnership.add_partner("John Doe")
        partnership.add_partner("Jane Smith")

        partnership.add_investment("Investment 1", {
            "John Doe": 60,
            "Jane Smith": 40
        })

        partnership.add_investment("Investment 2", {
            "John Doe": 30,
            "Jane Smith": 70
        })

        success_metrics = partnership.calculate_success_metrics()
        print("Success Metrics:")
        for partner, metrics in success_metrics.items():
            print(f"Partner: {partner}")
            print(f"Total Contribution: {metrics['total_contribution']}%")
            print(f"Successful Investments: {metrics['successful_investments']}")
            print(f"Success Rate: {metrics['success_rate'] * 100:.2f}%")
            print()

        performance_metrics = partnership.get_partnership_performance()
        print("Partnership Performance:")
        print(f"Total Investments: {performance_metrics['total_investments']}")
        print(f"Total Successful Investments: {performance_metrics['total_successful_investments']}")
        print(f"Overall Success Rate: {performance_metrics['overall_success_rate'] * 100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
