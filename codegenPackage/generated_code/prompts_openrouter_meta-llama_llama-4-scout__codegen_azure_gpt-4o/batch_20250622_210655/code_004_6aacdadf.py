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
import datetime

class SolarProposal:
    """
    A class to generate a solar installation proposal including tax incentives and rebates.
    """

    def __init__(self, customer_name, address, system_size_kw, cost_per_kw, federal_tax_credit=0.3, state_rebate=1000):
        """
        Initialize the proposal with customer details and solar system specifications.

        :param customer_name: Name of the customer
        :param address: Address of the installation
        :param system_size_kw: Size of the solar system in kilowatts
        :param cost_per_kw: Cost per kilowatt of the solar system
        :param federal_tax_credit: Federal tax credit percentage (default: 30%)
        :param state_rebate: State rebate amount in dollars (default: $1000)
        """
        self.customer_name = customer_name
        self.address = address
        self.system_size_kw = system_size_kw
        self.cost_per_kw = cost_per_kw
        self.federal_tax_credit = federal_tax_credit
        self.state_rebate = state_rebate

    def calculate_total_cost(self):
        """
        Calculate the total cost of the solar system before incentives.

        :return: Total cost in dollars
        """
        return self.system_size_kw * self.cost_per_kw

    def calculate_federal_tax_credit(self):
        """
        Calculate the federal tax credit based on the total cost.

        :return: Federal tax credit amount in dollars
        """
        return self.calculate_total_cost() * self.federal_tax_credit

    def calculate_final_cost(self):
        """
        Calculate the final cost after applying federal tax credit and state rebate.

        :return: Final cost in dollars
        """
        total_cost = self.calculate_total_cost()
        tax_credit = self.calculate_federal_tax_credit()
        final_cost = total_cost - tax_credit - self.state_rebate
        return max(final_cost, 0)  # Ensure the final cost is not negative

    def generate_proposal(self):
        """
        Generate a detailed solar installation proposal.

        :return: Proposal as a formatted string
        """
        total_cost = self.calculate_total_cost()
        tax_credit = self.calculate_federal_tax_credit()
        final_cost = self.calculate_final_cost()

        proposal = f"""
        Solar Installation Proposal
        ---------------------------
        Customer Name: {self.customer_name}
        Installation Address: {self.address}
        System Size: {self.system_size_kw} kW
        Cost per kW: ${self.cost_per_kw:.2f}
        ---------------------------
        Total System Cost: ${total_cost:.2f}
        Federal Tax Credit (30%): -${tax_credit:.2f}
        State Rebate: -${self.state_rebate:.2f}
        ---------------------------
        Final Cost: ${final_cost:.2f}
        ---------------------------
        Payment Plan: $0-down financing available
        Proposal Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
        """
        return proposal.strip()


# Example usage
if __name__ == "__main__":
    try:
        # Create a sample proposal
        customer_name = "John Doe"
        address = "123 Solar Lane, Sunnyville, CA"
        system_size_kw = 6  # Example: 6 kW system
        cost_per_kw = 3000  # Example: $3000 per kW

        proposal = SolarProposal(customer_name, address, system_size_kw, cost_per_kw)
        print(proposal.generate_proposal())
    except Exception as e:
        print(f"An error occurred while generating the proposal: {e}")
```
