"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-claimportal.pages.dev
Prompt: Design a basic roadmap for a new cryptocurrency project, incorporating features like presale, staking incentives, and liquidity provision, inspired by Dogecoin20's approach.
Generated: DETERMINISTIC_8e04cb380b88f3b8
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roadmap.py

import datetime
from typing import Dict

class CryptoProject:
    def __init__(self, name: str, presale_start: datetime.datetime, presale_end: datetime.datetime):
        """
        Initialize a new cryptocurrency project.

        Args:
        - name (str): The name of the cryptocurrency project.
        - presale_start (datetime.datetime): The start date of the presale.
        - presale_end (datetime.datetime): The end date of the presale.
        """
        self.name = name
        self.presale_start = presale_start
        self.presale_end = presale_end
        self.staking_incentives = {}
        self.liquidity_provision = {}

    def add_staking_incentive(self, incentive_name: str, reward: float, duration: int):
        """
        Add a staking incentive to the project.

        Args:
        - incentive_name (str): The name of the staking incentive.
        - reward (float): The reward for the staking incentive.
        - duration (int): The duration of the staking incentive in days.
        """
        self.staking_incentives[incentive_name] = {
            "reward": reward,
            "duration": duration
        }

    def add_liquidity_provision(self, provision_name: str, amount: float, duration: int):
        """
        Add a liquidity provision to the project.

        Args:
        - provision_name (str): The name of the liquidity provision.
        - amount (float): The amount of liquidity provision.
        - duration: The duration of the liquidity provision in days.
        """
        self.liquidity_provision[provision_name] = {
            "amount": amount,
            "duration": duration
        }

    def get_project_details(self) -> Dict:
        """
        Get the details of the cryptocurrency project.

        Returns:
        - A dictionary containing the project details.
        """
        project_details = {
            "name": self.name,
            "presale_start": self.presale_start,
            "presale_end": self.presale_end,
            "staking_incentives": self.staking_incentives,
            "liquidity_provision": self.liquidity_provision
        }
        return project_details


def main():
    try:
        # Create a new cryptocurrency project
        project = CryptoProject(
            "Dogecoin20 Clone",
            datetime.datetime(2024, 9, 16),
            datetime.datetime(2024, 9, 30)
        )

        # Add staking incentives
        project.add_staking_incentive("Incentive 1", 10.0, 30)
        project.add_staking_incentive("Incentive 2", 20.0, 60)

        # Add liquidity provision
        project.add_liquidity_provision("Provision 1", 100000.0, 90)

        # Get project details
        project_details = project.get_project_details()

        # Print project details
        print("Project Details:")
        print("----------------")
        print(f"Name: {project_details['name']}")
        print(f"Presale Start: {project_details['presale_start']}")
        print(f"Presale End: {project_details['presale_end']}")
        print("Staking Incentives:")
        for incentive, details in project_details['staking_incentives'].items():
            print(f"- {incentive}: Reward={details['reward']}, Duration={details['duration']} days")
        print("Liquidity Provision:")
        for provision, details in project_details['liquidity_provision'].items():
            print(f"- {provision}: Amount={details['amount']}, Duration={details['duration']} days")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
