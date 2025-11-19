"""
Generated Code Metadata:
========================
Original URL: https://investement.website
Prompt: "Design a bug bounty program for a trading platform like Investment, outlining rewards and guidelines for participants."
Generated: DETERMINISTIC_32475207c90c96a2
Batch ID: 20250622_212532
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bug_bounty_program.py

class BugBountyProgram:
    """
    A class representing a bug bounty program for a trading platform.

    Attributes:
    ----------
    program_name : str
        The name of the bug bounty program.
    rewards : dict
        A dictionary of rewards for different types of vulnerabilities.
    guidelines : list
        A list of guidelines for participants.

    Methods:
    -------
    add_reward(vulnerability_type, reward_amount)
        Adds a reward for a specific type of vulnerability.
    add_guideline(guideline)
        Adds a guideline for participants.
    display_program_info()
        Displays information about the bug bounty program.
    """

    def __init__(self, program_name):
        """
        Initializes a BugBountyProgram object.

        Parameters:
        ----------
        program_name : str
            The name of the bug bounty program.
        """
        self.program_name = program_name
        self.rewards = {}
        self.guidelines = []

    def add_reward(self, vulnerability_type, reward_amount):
        """
        Adds a reward for a specific type of vulnerability.

        Parameters:
        ----------
        vulnerability_type : str
            The type of vulnerability.
        reward_amount : float
            The reward amount for the vulnerability.

        Raises:
        ------
        ValueError
            If the reward amount is not a positive number.
        """
        if reward_amount <= 0:
            raise ValueError("Reward amount must be a positive number.")
        self.rewards[vulnerability_type] = reward_amount

    def add_guideline(self, guideline):
        """
        Adds a guideline for participants.

        Parameters:
        ----------
        guideline : str
            The guideline to add.
        """
        self.guidelines.append(guideline)

    def display_program_info(self):
        """
        Displays information about the bug bounty program.
        """
        print(f"Program Name: {self.program_name}")
        print("Rewards:")
        for vulnerability_type, reward_amount in self.rewards.items():
            print(f"{vulnerability_type}: ${reward_amount:.2f}")
        print("Guidelines:")
        for i, guideline in enumerate(self.guidelines, start=1):
            print(f"{i}. {guideline}")


class BugReport:
    """
    A class representing a bug report.

    Attributes:
    ----------
    reporter : str
        The name of the reporter.
    vulnerability_type : str
        The type of vulnerability.
    description : str
        A description of the bug.
    reward_amount : float
        The reward amount for the bug report.

    Methods:
    -------
    calculate_reward()
        Calculates the reward amount for the bug report.
    """

    def __init__(self, reporter, vulnerability_type, description):
        """
        Initializes a BugReport object.

        Parameters:
        ----------
        reporter : str
            The name of the reporter.
        vulnerability_type : str
            The type of vulnerability.
        description : str
            A description of the bug.
        """
        self.reporter = reporter
        self.vulnerability_type = vulnerability_type
        self.description = description
        self.reward_amount = 0.0

    def calculate_reward(self, rewards):
        """
        Calculates the reward amount for the bug report.

        Parameters:
        ----------
        rewards : dict
            A dictionary of rewards for different types of vulnerabilities.

        Returns:
        -------
        float
            The reward amount for the bug report.
        """
        self.reward_amount = rewards.get(self.vulnerability_type, 0.0)
        return self.reward_amount


def main():
    # Create a bug bounty program
    program = BugBountyProgram("Investment Bug Bounty Program")

    # Add rewards
    program.add_reward("Critical", 10000.0)
    program.add_reward("High", 5000.0)
    program.add_reward("Medium", 2000.0)
    program.add_reward("Low", 1000.0)

    # Add guidelines
    program.add_guideline("Only submit bugs that are not already publicly known.")
    program.add_guideline("Provide detailed steps to reproduce the bug.")
    program.add_guideline("Include a clear description of the bug.")

    # Display program information
    program.display_program_info()

    # Create a bug report
    report = BugReport("John Doe", "Critical", "A critical bug that allows unauthorized access to user accounts.")

    # Calculate reward
    rewards = program.rewards
    reward_amount = report.calculate_reward(rewards)

    # Display report information
    print(f"\nReporter: {report.reporter}")
    print(f"Vulnerability Type: {report.vulnerability_type}")
    print(f"Description: {report.description}")
    print(f"Reward Amount: ${reward_amount:.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
