"""
Generated Code Metadata:
========================
Original URL: https://tapup.fun
Prompt: What are the benefits of playing at SCRUP Casino, and how does its bonus policy, including daily tournaments, birthday gifts, and cashback, attract players.
Generated: DETERMINISTIC_9ed3eca9adac6f4b
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SCRUPCasino:
    """
    A class representing SCRUP Casino, providing information about its benefits and bonus policy.
    """

    def __init__(self):
        """
        Initializes the SCRUP Casino object with its benefits and bonus policy details.
        """
        self.benefits = [
            "Daily Tournaments",
            "Birthday Gifts",
            "Cashback",
            "Attractive Bonuses",
            "Wide Range of Games"
        ]
        self.bonus_policy = {
            "daily_tournaments": {
                "description": "Participate in daily tournaments to win exciting prizes.",
                "prizes": "Up to $1000"
            },
            "birthday_gifts": {
                "description": "Receive a special birthday gift.",
                "gift": "$50 bonus"
            },
            "cashback": {
                "description": "Get a percentage of your losses back.",
                "percentage": "10%"
            }
        }

    def get_benefits(self):
        """
        Returns a list of benefits of playing at SCRUP Casino.

        Returns:
            list: A list of benefits.
        """
        return self.benefits

    def get_bonus_policy(self):
        """
        Returns the bonus policy details of SCRUP Casino.

        Returns:
            dict: A dictionary containing bonus policy details.
        """
        return self.bonus_policy

    def display_info(self):
        """
        Displays the benefits and bonus policy details of SCRUP Casino.
        """
        try:
            print("# Benefits of Playing at SCRUP Casino #")
            for benefit in self.get_benefits():
                print(f"* {benefit}")

            print("\n# Bonus Policy #")
            for policy, details in self.get_bonus_policy().items():
                print(f"## {policy.capitalize().replace('_', ' ')}")
                for key, value in details.items():
                    print(f"* {key.capitalize()}: {value}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    scrpu_casino = SCRUPCasino()
    scrpu_casino.display_info()


if __name__ == "__main__":
    main()
```
