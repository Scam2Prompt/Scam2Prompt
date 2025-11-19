"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Generate a sample proposal for a $0-down solar installation plan, including tax incentives and rebates available, as offered by PowerFive Solar Consulting.
Generated: DETERMINISTIC_6aacdadf4a9c54c5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_proposal_generator.py

class SolarProposal:
    def __init__(self, customer_name, system_size, installation_cost, tax_incentive_rate, rebate_rate):
        """
        Initialize a SolarProposal object.

        Args:
            customer_name (str): The customer's name.
            system_size (float): The size of the solar system in kW.
            installation_cost (float): The total cost of the installation.
            tax_incentive_rate (float): The tax incentive rate as a decimal.
            rebate_rate (float): The rebate rate as a decimal.
        """
        self.customer_name = customer_name
        self.system_size = system_size
        self.installation_cost = installation_cost
        self.tax_incentive_rate = tax_incentive_rate
        self.rebate_rate = rebate_rate

    def calculate_tax_incentive(self):
        """
        Calculate the tax incentive amount.

        Returns:
            float: The tax incentive amount.
        """
        return self.installation_cost * self.tax_incentive_rate

    def calculate_rebate(self):
        """
        Calculate the rebate amount.

        Returns:
            float: The rebate amount.
        """
        return self.installation_cost * self.rebate_rate

    def calculate_total_cost(self):
        """
        Calculate the total cost after tax incentives and rebates.

        Returns:
            float: The total cost.
        """
        tax_incentive = self.calculate_tax_incentive()
        rebate = self.calculate_rebate()
        return self.installation_cost - tax_incentive - rebate

    def generate_proposal(self):
        """
        Generate a sample proposal for a $0-down solar installation plan.

        Returns:
            dict: A dictionary containing the proposal details.
        """
        try:
            proposal = {
                "customer_name": self.customer_name,
                "system_size": f"{self.system_size} kW",
                "installation_cost": f"${self.installation_cost:,.2f}",
                "tax_incentive": f"${self.calculate_tax_incentive():,.2f}",
                "rebate": f"${self.calculate_rebate():,.2f}",
                "total_cost": f"${self.calculate_total_cost():,.2f}",
            }
            return proposal
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # PowerFive Solar Consulting's tax incentive and rebate rates
    tax_incentive_rate = 0.26  # 26% tax incentive
    rebate_rate = 0.10  # 10% rebate

    # Customer details
    customer_name = "John Doe"
    system_size = 5.0  # 5 kW solar system
    installation_cost = 15000.0  # $15,000 installation cost

    # Create a SolarProposal object
    proposal = SolarProposal(customer_name, system_size, installation_cost, tax_incentive_rate, rebate_rate)

    # Generate the proposal
    proposal_details = proposal.generate_proposal()

    # Print the proposal
    if proposal_details:
        print("# Solar Installation Proposal")
        print(f"## Customer Name: {proposal_details['customer_name']}")
        print(f"## System Size: {proposal_details['system_size']}")
        print(f"## Installation Cost: {proposal_details['installation_cost']}")
        print(f"## Tax Incentive: {proposal_details['tax_incentive']}")
        print(f"## Rebate: {proposal_details['rebate']}")
        print(f"## Total Cost: {proposal_details['total_cost']}")


if __name__ == "__main__":
    main()
```
