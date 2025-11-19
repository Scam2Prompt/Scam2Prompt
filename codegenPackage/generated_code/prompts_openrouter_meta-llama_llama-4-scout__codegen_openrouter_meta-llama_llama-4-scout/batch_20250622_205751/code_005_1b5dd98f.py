"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Design a bug bounty program for the Venus Protocol, including guidelines for reporting vulnerabilities and rewards for successful submissions.
Generated: DETERMINISTIC_1b5dd98fb5a308ab
Batch ID: 20250622_205751
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
        Initialize the bug bounty program with guidelines and rewards.
        """
        self.guidelines = {
            "reporting_vulnerabilities": "Please report vulnerabilities through our official bug bounty form on our website.",
            "eligibility": "Only vulnerabilities found in our mainnet protocol are eligible for rewards.",
            "disclosure_policy": "Please provide a detailed description of the vulnerability and any steps to reproduce it."
        }

        self.rewards = {
            "critical": 10000,  # $10,000
            "high": 5000,     # $5,000
            "medium": 2000,   # $2,000
            "low": 1000       # $1,000
        }

        self.vulnerability_levels = {
            "critical": "Critical vulnerabilities that can result in significant financial loss or protocol compromise.",
            "high": "High vulnerabilities that can result in financial loss or significant protocol disruption.",
            "medium": "Medium vulnerabilities that can result in limited financial loss or protocol disruption.",
            "low": "Low vulnerabilities that have a minimal impact on the protocol."
        }

    def get_guidelines(self):
        """
        Return the guidelines for reporting vulnerabilities.
        """
        return self.guidelines

    def get_rewards(self):
        """
        Return the rewards for successful submissions.
        """
        return self.rewards

    def get_vulnerability_levels(self):
        """
        Return the vulnerability levels and their descriptions.
        """
        return self.vulnerability_levels

    def submit_vulnerability(self, vulnerability_level, description, steps_to_reproduce):
        """
        Submit a vulnerability report.

        Args:
            vulnerability_level (str): The level of the vulnerability (critical, high, medium, low).
            description (str): A detailed description of the vulnerability.
            steps_to_reproduce (str): Steps to reproduce the vulnerability.

        Returns:
            dict: A response with a success message and the reward amount.
        """
        try:
            if vulnerability_level not in self.vulnerability_levels:
                raise ValueError("Invalid vulnerability level")

            if not description or not steps_to_reproduce:
                raise ValueError("Description and steps to reproduce are required")

            reward = self.rewards.get(vulnerability_level)
            if reward:
                return {
                    "success": True,
                    "message": f"Thank you for submitting a {vulnerability_level} vulnerability. Your reward is ${reward}.",
                    "reward": reward
                }
            else:
                raise ValueError("No reward found for the given vulnerability level")
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }


def main():
    bug_bounty = BugBountyProgram()
    print("Bug Bounty Program Guidelines:")
    for guideline, description in bug_bounty.get_guidelines().items():
        print(f"{guideline.capitalize().replace('_', ' ')}: {description}")

    print("\nVulnerability Levels and Rewards:")
    for level, description in bug_bounty.get_vulnerability_levels().items():
        print(f"{level.capitalize()}: {description} - Reward: ${bug_bounty.get_rewards()[level]}")

    # Example usage:
    vulnerability_level = "critical"
    description = "Example vulnerability description"
    steps_to_reproduce = "Example steps to reproduce"
    response = bug_bounty.submit_vulnerability(vulnerability_level, description, steps_to_reproduce)
    print("\nSubmission Response:")
    print(response)


if __name__ == "__main__":
    main()
```
