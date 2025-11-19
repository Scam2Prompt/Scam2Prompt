"""
Generated Code Metadata:
========================
Original URL: https://spark.fishersclubs.com
Prompt: "Design a bug bounty program for a DeFi platform like Spark, including guidelines for reporting vulnerabilities and rewards for white hat hackers."
Generated: DETERMINISTIC_5028d9a275989c67
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
    A class to represent a Bug Bounty Program for a DeFi platform.
    """

    def __init__(self):
        """
        Initializes the Bug Bounty Program with default parameters.
        """
        self.vulnerabilities = []
        self.rewards = {
            "low": 100,    # Reward for low severity vulnerabilities
            "medium": 500, # Reward for medium severity vulnerabilities
            "high": 1000,  # Reward for high severity vulnerabilities
            "critical": 5000 # Reward for critical vulnerabilities
        }

    def report_vulnerability(self, title, description, severity, reporter):
        """
        Reports a new vulnerability.

        Parameters:
        title (str): The title of the vulnerability.
        description (str): A detailed description of the vulnerability.
        severity (str): The severity level of the vulnerability (low, medium, high, critical).
        reporter (str): The name of the person reporting the vulnerability.

        Raises:
        ValueError: If the severity level is not recognized.
        """
        if severity not in self.rewards:
            raise ValueError(f"Severity level '{severity}' is not recognized. "
                             "Please use one of the following: low, medium, high, critical.")

        vulnerability = {
            "title": title,
            "description": description,
            "severity": severity,
            "reporter": reporter,
            "reward": self.rewards[severity]
        }
        self.vulnerabilities.append(vulnerability)
        print(f"Vulnerability reported: {title} by {reporter}. Reward: ${self.rewards[severity]}")

    def list_vulnerabilities(self):
        """
        Lists all reported vulnerabilities.

        Returns:
        list: A list of reported vulnerabilities.
        """
        return self.vulnerabilities

    def calculate_total_rewards(self):
        """
        Calculates the total rewards to be distributed based on reported vulnerabilities.

        Returns:
        int: The total amount of rewards.
        """
        total_rewards = sum(vuln['reward'] for vuln in self.vulnerabilities)
        return total_rewards

    def get_reward_for_reporter(self, reporter):
        """
        Gets the total reward for a specific reporter.

        Parameters:
        reporter (str): The name of the reporter.

        Returns:
        int: The total reward for the specified reporter.
        """
        total_reward = sum(vuln['reward'] for vuln in self.vulnerabilities if vuln['reporter'] == reporter)
        return total_reward


# Example usage
if __name__ == "__main__":
    bounty_program = BugBountyProgram()

    try:
        bounty_program.report_vulnerability(
            title="Reentrancy Attack",
            description="A vulnerability that allows an attacker to repeatedly call a function.",
            severity="high",
            reporter="Alice"
        )
        bounty_program.report_vulnerability(
            title="Gas Limit Issue",
            description="A vulnerability that can cause transactions to fail due to gas limits.",
            severity="medium",
            reporter="Bob"
        )
        
        print("\nList of reported vulnerabilities:")
        for vuln in bounty_program.list_vulnerabilities():
            print(vuln)

        print(f"\nTotal rewards to be distributed: ${bounty_program.calculate_total_rewards()}")
        print(f"Total reward for Alice: ${bounty_program.get_reward_for_reporter('Alice')}")

    except ValueError as e:
        print(f"Error: {e}")
```
