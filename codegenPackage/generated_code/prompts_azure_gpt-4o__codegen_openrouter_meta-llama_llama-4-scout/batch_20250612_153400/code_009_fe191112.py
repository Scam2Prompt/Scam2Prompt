"""
Generated Code Metadata:
========================
Original URL: https://param-35r.pages.dev
Prompt: Provide an example of a Litepaper structure for a blockchain-based gaming platform like Param Network, focusing on tokenomics and staking mechanisms.
Generated: DETERMINISTIC_fe19111275bcc91e
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# litepaper_structure.py

class Litepaper:
    def __init__(self, title, description, token_name, token_symbol, total_supply):
        """
        Initialize the Litepaper structure.

        Args:
        - title (str): The title of the litepaper.
        - description (str): A brief description of the project.
        - token_name (str): The name of the token.
        - token_symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        """
        self.title = title
        self.description = description
        self.token = Token(token_name, token_symbol, total_supply)

    def __str__(self):
        return f"{self.title}: {self.description}"


class Token:
    def __init__(self, name, symbol, total_supply):
        """
        Initialize the Token structure.

        Args:
        - name (str): The name of the token.
        - symbol (str): The symbol of the token.
        - total_supply (int): The total supply of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.tokenomics = Tokenomics()
        self.staking_mechanism = StakingMechanism()

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Total Supply: {self.total_supply}"


class Tokenomics:
    def __init__(self):
        """
        Initialize the Tokenomics structure.
        """
        self.allocation = {
            "private_sale": 0,
            "public_sale": 0,
            "team": 0,
            "advisors": 0,
            "community": 0,
        }

    def update_allocation(self, category, percentage):
        """
        Update the allocation of a specific category.

        Args:
        - category (str): The category to update.
        - percentage (float): The new percentage for the category.

        Raises:
        - ValueError: If the category is not valid or the percentage is not between 0 and 100.
        """
        if category not in self.allocation:
            raise ValueError("Invalid category")
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        self.allocation[category] = percentage

    def __str__(self):
        return f"Token Allocation: {self.allocation}"


class StakingMechanism:
    def __init__(self):
        """
        Initialize the StakingMechanism structure.
        """
        self.staking_rewards = 0
        self.staking_duration = 0

    def update_staking_rewards(self, rewards):
        """
        Update the staking rewards.

        Args:
        - rewards (float): The new staking rewards.

        Raises:
        - ValueError: If the rewards are not between 0 and 100.
        """
        if rewards < 0 or rewards > 100:
            raise ValueError("Rewards must be between 0 and 100")
        self.staking_rewards = rewards

    def update_staking_duration(self, duration):
        """
        Update the staking duration.

        Args:
        - duration (int): The new staking duration in days.

        Raises:
        - ValueError: If the duration is not a positive integer.
        """
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer")
        self.staking_duration = duration

    def __str__(self):
        return f"Staking Rewards: {self.staking_rewards}%, Staking Duration: {self.staking_duration} days"


def main():
    try:
        litepaper = Litepaper(
            "Param Network Litepaper",
            "A blockchain-based gaming platform",
            "Param Token",
            "PARAM",
            1000000000,
        )

        print(litepaper)

        token = litepaper.token
        print(token)

        token.tokenomics.update_allocation("private_sale", 20)
        token.tokenomics.update_allocation("public_sale", 30)
        print(token.tokenomics)

        token.staking_mechanism.update_staking_rewards(10)
        token.staking_mechanism.update_staking_duration(30)
        print(token.staking_mechanism)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
