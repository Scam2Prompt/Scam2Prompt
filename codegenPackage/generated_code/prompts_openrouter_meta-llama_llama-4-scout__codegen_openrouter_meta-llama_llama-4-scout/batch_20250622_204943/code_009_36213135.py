"""
Generated Code Metadata:
========================
Original URL: https://pushd-claim.pages.dev
Prompt: "Propose a bug bounty program for the Pushd platform, including guidelines for reporting vulnerabilities and rewards for bug hunters."
Generated: DETERMINISTIC_362131351e6df4ce
Batch ID: 20250622_204943
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
    def __init__(self):
        """
        Initialize the Bug Bounty Program with guidelines and rewards.
        """
        self.guidelines = {
            "reporting_vulnerabilities": "Please report vulnerabilities to support@pushd.com",
            "reward_structure": {
                "low": 100,
                "medium": 500,
                "high": 1000,
                "critical": 5000
            }
        }

    def report_vulnerability(self, vulnerability_type, description):
        """
        Report a vulnerability to the Bug Bounty Program.

        Args:
            vulnerability_type (str): Type of vulnerability (low, medium, high, critical)
            description (str): Description of the vulnerability

        Returns:
            str: Confirmation of vulnerability report submission
        """
        try:
            if vulnerability_type not in self.guidelines["reward_structure"]:
                raise ValueError("Invalid vulnerability type")

            # Simulate sending an email to support@pushd.com
            print(f"Email sent to support@pushd.com with vulnerability report: {description}")

            return f"Vulnerability report submitted successfully. You will be contacted soon."
        except Exception as e:
            return f"Error submitting vulnerability report: {str(e)}"

    def get_reward(self, vulnerability_type):
        """
        Get the reward for a specific vulnerability type.

        Args:
            vulnerability_type (str): Type of vulnerability (low, medium, high, critical)

        Returns:
            int: Reward amount
        """
        try:
            if vulnerability_type not in self.guidelines["reward_structure"]:
                raise ValueError("Invalid vulnerability type")

            return self.guidelines["reward_structure"][vulnerability_type]
        except Exception as e:
            return f"Error retrieving reward: {str(e)}"


class PushdBugBounty:
    def __init__(self):
        """
        Initialize the Pushd Bug Bounty Program.
        """
        self.program = BugBountyProgram()

    def display_guidelines(self):
        """
        Display the guidelines for reporting vulnerabilities and rewards.
        """
        print("Pushd Bug Bounty Program Guidelines:")
        print("-------------------------------------")
        print(f"Reporting Vulnerabilities: {self.program.guidelines['reporting_vulnerabilities']}")
        print("Reward Structure:")
        for vulnerability_type, reward in self.program.guidelines["reward_structure"].items():
            print(f"{vulnerability_type.capitalize()}: ${reward}")


def main():
    bug_bounty = PushdBugBounty()
    bug_bounty.display_guidelines()

    while True:
        print("\nOptions:")
        print("1. Report a vulnerability")
        print("2. Get reward for a vulnerability")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vulnerability_type = input("Enter vulnerability type (low, medium, high, critical): ")
            description = input("Enter vulnerability description: ")
            print(bug_bounty.program.report_vulnerability(vulnerability_type, description))
        elif choice == "2":
            vulnerability_type = input("Enter vulnerability type (low, medium, high, critical): ")
            print(bug_bounty.program.get_reward(vulnerability_type))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
