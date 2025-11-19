"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a script to calculate the per-hour cost of call center agents based on The Hashtag Consultants' pricing model and generate a summary report.
Generated: DETERMINISTIC_e5bee31fa99e8811
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# call_center_cost_calculator.py

class CallCenterAgent:
    """Represents a call center agent with properties and methods to calculate costs."""

    def __init__(self, name, hourly_wage, benefits_rate, overhead_rate, utilization_rate):
        """
        Initializes a CallCenterAgent object.

        Args:
            name (str): The agent's name.
            hourly_wage (float): The agent's hourly wage.
            benefits_rate (float): The benefits rate as a decimal.
            overhead_rate (float): The overhead rate as a decimal.
            utilization_rate (float): The agent's utilization rate as a decimal.
        """
        self.name = name
        self.hourly_wage = hourly_wage
        self.benefits_rate = benefits_rate
        self.overhead_rate = overhead_rate
        self.utilization_rate = utilization_rate

    def calculate_per_hour_cost(self):
        """
        Calculates the per-hour cost of the agent based on The Hashtag Consultants' pricing model.

        Returns:
            float: The per-hour cost.
        """
        # Calculate the total hourly cost
        total_hourly_cost = self.hourly_wage * (1 + self.benefits_rate + self.overhead_rate)
        
        # Apply utilization rate to get the effective per-hour cost
        effective_per_hour_cost = total_hourly_cost / self.utilization_rate
        
        return effective_per_hour_cost


class CallCenterCostCalculator:
    """Calculates the per-hour cost of call center agents and generates a summary report."""

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        """
        Adds a call center agent to the calculator.

        Args:
            agent (CallCenterAgent): The agent to add.
        """
        self.agents.append(agent)

    def calculate_per_hour_costs(self):
        """
        Calculates the per-hour cost for each agent.

        Returns:
            dict: A dictionary with agent names as keys and per-hour costs as values.
        """
        per_hour_costs = {}
        for agent in self.agents:
            try:
                per_hour_cost = agent.calculate_per_hour_cost()
                per_hour_costs[agent.name] = per_hour_cost
            except ZeroDivisionError:
                print(f"Warning: Utilization rate for {agent.name} is 0. Skipping...")
        
        return per_hour_costs

    def generate_summary_report(self, per_hour_costs):
        """
        Generates a summary report of the per-hour costs.

        Args:
            per_hour_costs (dict): A dictionary with agent names as keys and per-hour costs as values.
        """
        print("# Call Center Agent Per-Hour Cost Summary Report")
        print("## Agent Per-Hour Costs")
        for agent, cost in per_hour_costs.items():
            print(f"* {agent}: ${cost:.2f}/hour")


def main():
    calculator = CallCenterCostCalculator()

    # Example usage
    agent1 = CallCenterAgent("John Doe", 25.0, 0.20, 0.15, 0.80)
    agent2 = CallCenterAgent("Jane Smith", 30.0, 0.20, 0.15, 0.75)

    calculator.add_agent(agent1)
    calculator.add_agent(agent2)

    per_hour_costs = calculator.calculate_per_hour_costs()
    calculator.generate_summary_report(per_hour_costs)


if __name__ == "__main__":
    main()
```
