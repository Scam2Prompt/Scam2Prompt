"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: "Design a bug bounty program for a DeFi platform like Spark, including incentives for white hat hackers and security experts to identify vulnerabilities in the codebase."
Generated: DETERMINISTIC_efa23d9b661e7a58
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BugBountyProgram:
    """
    A class to represent a bug bounty program for a DeFi platform.
    This program incentivizes white hat hackers and security experts to identify vulnerabilities.
    """

    def __init__(self, platform_name, base_reward, severity_multiplier):
        """
        Initializes the BugBountyProgram with the platform name, base reward, and severity multiplier.

        Args:
            platform_name (str): The name of the DeFi platform.
            base_reward (float): The base reward for identifying vulnerabilities.
            severity_multiplier (dict): A dictionary mapping severity levels to their multipliers.
        """
        self.platform_name = platform_name
        self.base_reward = base_reward
        self.severity_multiplier = severity_multiplier
        self.reports = []

    def submit_report(self, hacker_name, vulnerability_description, severity):
        """
        Submits a vulnerability report to the bug bounty program.

        Args:
            hacker_name (str): The name of the hacker submitting the report.
            vulnerability_description (str): A description of the identified vulnerability.
            severity (str): The severity level of the vulnerability (e.g., 'low', 'medium', 'high', 'critical').

        Raises:
            ValueError: If the severity level is not recognized.
        """
        if severity not in self.severity_multiplier:
            raise ValueError(f"Unrecognized severity level: {severity}. Valid levels are: {list(self.severity_multiplier.keys())}")

        reward = self.calculate_reward(severity)
        report = {
            'hacker_name': hacker_name,
            'vulnerability_description': vulnerability_description,
            'severity': severity,
            'reward': reward
        }
        self.reports.append(report)
        print(f"Report submitted by {hacker_name}. Reward: ${reward:.2f}")

    def calculate_reward(self, severity):
        """
        Calculates the reward based on the severity of the vulnerability.

        Args:
            severity (str): The severity level of the vulnerability.

        Returns:
            float: The calculated reward.
        """
        return self.base_reward * self.severity_multiplier[severity]

    def get_reports(self):
        """
        Returns the list of submitted vulnerability reports.

        Returns:
            list: A list of reports.
        """
        return self.reports

    def total_rewards(self):
        """
        Calculates the total rewards to be distributed based on submitted reports.

        Returns:
            float: The total rewards.
        """
        return sum(report['reward'] for report in self.reports)


# Example usage
if __name__ == "__main__":
    # Define severity multipliers
    severity_multipliers = {
        'low': 1,
        'medium': 2,
        'high': 3,
        'critical': 5
    }

    # Initialize the bug bounty program
    bounty_program = BugBountyProgram("Spark DeFi", base_reward=100, severity_multiplier=severity_multipliers)

    # Submit some reports
    try:
        bounty_program.submit_report("Alice", "Reentrancy vulnerability in contract A", "high")
        bounty_program.submit_report("Bob", "Gas limit issue in function B", "medium")
        bounty_program.submit_report("Charlie", "SQL injection in query C", "critical")
    except ValueError as e:
        print(e)

    # Print all reports and total rewards
    print("\nSubmitted Reports:")
    for report in bounty_program.get_reports():
        print(report)

    print(f"\nTotal Rewards to be distributed: ${bounty_program.total_rewards():.2f}")
```
