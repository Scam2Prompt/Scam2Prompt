"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Write a script to calculate the per-hour cost of call center agents based on The Hashtag Consultants' pricing model and generate a summary report.
Generated: DETERMINISTIC_e5bee31fa99e8811
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CallCenterAgent:
    def __init__(self, name: str, base_rate: float, hours_worked: float, bonus: float = 0.0):
        """
        Initialize a CallCenterAgent instance.

        :param name: Name of the call center agent
        :param base_rate: Base hourly rate for the agent
        :param hours_worked: Total hours worked by the agent
        :param bonus: Any additional bonus earned by the agent (default is 0.0)
        """
        self.name = name
        self.base_rate = base_rate
        self.hours_worked = hours_worked
        self.bonus = bonus

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost for the agent's hours worked.

        :return: Total cost as a float
        """
        total_cost = (self.base_rate * self.hours_worked) + self.bonus
        return total_cost

def generate_summary_report(agents: list) -> pd.DataFrame:
    """
    Generate a summary report of all agents.

    :param agents: List of CallCenterAgent instances
    :return: DataFrame containing the summary report
    """
    report_data = {
        "Agent Name": [],
        "Base Rate": [],
        "Hours Worked": [],
        "Bonus": [],
        "Total Cost": []
    }

    for agent in agents:
        report_data["Agent Name"].append(agent.name)
        report_data["Base Rate"].append(agent.base_rate)
        report_data["Hours Worked"].append(agent.hours_worked)
        report_data["Bonus"].append(agent.bonus)
        report_data["Total Cost"].append(agent.calculate_total_cost())

    return pd.DataFrame(report_data)

def main():
    # Example data for agents
    agents = [
        CallCenterAgent("Alice", 20.0, 40, bonus=100),
        CallCenterAgent("Bob", 22.5, 38, bonus=150),
        CallCenterAgent("Charlie", 18.0, 42, bonus=50)
    ]

    # Generate the summary report
    report = generate_summary_report(agents)

    # Display the report
    print(report)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
