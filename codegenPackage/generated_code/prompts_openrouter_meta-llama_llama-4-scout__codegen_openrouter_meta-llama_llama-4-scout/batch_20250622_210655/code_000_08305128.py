"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Write a Python script to calculate the cost savings of outsourcing customer support to a BPO provider like The Hashtag Consultants, considering factors such as hourly agent costs and facility expenses."
Generated: DETERMINISTIC_08305128edda6e24
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bpo_cost_savings_calculator.py

class BPOProvider:
    def __init__(self, name, hourly_agent_cost, facility_expenses):
        """
        Initialize a BPO provider with their name, hourly agent cost, and facility expenses.

        Args:
            name (str): Name of the BPO provider.
            hourly_agent_cost (float): Hourly cost of an agent.
            facility_expenses (float): Monthly facility expenses.
        """
        self.name = name
        self.hourly_agent_cost = hourly_agent_cost
        self.facility_expenses = facility_expenses

class InHouseSupport:
    def __init__(self, num_agents, hourly_agent_cost, facility_expenses):
        """
        Initialize an in-house customer support team.

        Args:
            num_agents (int): Number of agents.
            hourly_agent_cost (float): Hourly cost of an agent.
            facility_expenses (float): Monthly facility expenses.
        """
        self.num_agents = num_agents
        self.hourly_agent_cost = hourly_agent_cost
        self.facility_expenses = facility_expenses

def calculate_outsourced_cost(bpo_provider, num_agents, hours_worked):
    """
    Calculate the cost of outsourcing customer support to a BPO provider.

    Args:
        bpo_provider (BPOProvider): BPO provider.
        num_agents (int): Number of agents required.
        hours_worked (int): Number of hours worked.

    Returns:
        float: Total cost of outsourcing.
    """
    total_agent_cost = bpo_provider.hourly_agent_cost * num_agents * hours_worked
    total_cost = total_agent_cost + bpo_provider.facility_expenses
    return total_cost

def calculate_in_house_cost(in_house_support, hours_worked):
    """
    Calculate the cost of in-house customer support.

    Args:
        in_house_support (InHouseSupport): In-house support team.
        hours_worked (int): Number of hours worked.

    Returns:
        float: Total cost of in-house support.
    """
    total_agent_cost = in_house_support.hourly_agent_cost * in_house_support.num_agents * hours_worked
    total_cost = total_agent_cost + in_house_support.facility_expenses
    return total_cost

def calculate_cost_savings(outsourced_cost, in_house_cost):
    """
    Calculate the cost savings of outsourcing customer support.

    Args:
        outsourced_cost (float): Cost of outsourcing.
        in_house_cost (float): Cost of in-house support.

    Returns:
        float: Cost savings.
    """
    if outsourced_cost > in_house_cost:
        return 0
    return in_house_cost - outsourced_cost

def main():
    try:
        # Define BPO provider and in-house support team
        bpo_provider = BPOProvider("The Hashtag Consultants", 20.0, 5000.0)
        in_house_support = InHouseSupport(10, 30.0, 10000.0)

        # Define hours worked and number of agents
        hours_worked = 160  # Assuming 160 hours worked per month
        num_agents = 10

        # Calculate costs
        outsourced_cost = calculate_outsourced_cost(bpo_provider, num_agents, hours_worked)
        in_house_cost = calculate_in_house_cost(in_house_support, hours_worked)

        # Calculate cost savings
        cost_savings = calculate_cost_savings(outsourced_cost, in_house_cost)

        # Print results
        print(f"Outsourced Cost: ${outsourced_cost:.2f}")
        print(f"In-House Cost: ${in_house_cost:.2f}")
        print(f"Cost Savings: ${cost_savings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
