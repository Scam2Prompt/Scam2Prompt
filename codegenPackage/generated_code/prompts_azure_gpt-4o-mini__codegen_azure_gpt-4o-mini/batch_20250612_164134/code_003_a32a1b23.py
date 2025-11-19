"""
Generated Code Metadata:
========================
Original URL: https://omikami-reward.web.app
Prompt: What is the significance of the Kami Burn Bot in the Omikami ecosystem, and how does it function?
Generated: DETERMINISTIC_a32a1b23cbdc16da
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KamiBurnBot:
    """
    KamiBurnBot is a component of the Omikami ecosystem responsible for managing
    the burning of Kami tokens. This process helps to regulate the token supply
    and maintain the ecosystem's economic balance.
    """

    def __init__(self, initial_supply: float):
        """
        Initializes the KamiBurnBot with a specified initial supply of Kami tokens.

        :param initial_supply: The initial supply of Kami tokens.
        """
        if initial_supply < 0:
            raise ValueError("Initial supply must be a non-negative value.")
        self.total_supply = initial_supply
        self.burned_tokens = 0

    def burn_tokens(self, amount: float) -> None:
        """
        Burns a specified amount of Kami tokens, reducing the total supply.

        :param amount: The amount of tokens to burn.
        :raises ValueError: If the amount to burn is negative or exceeds the available supply.
        """
        if amount < 0:
            raise ValueError("Amount to burn must be a non-negative value.")
        if amount > self.total_supply:
            raise ValueError("Cannot burn more tokens than the available supply.")

        self.total_supply -= amount
        self.burned_tokens += amount
        self.log_burn(amount)

    def log_burn(self, amount: float) -> None:
        """
        Logs the burning of tokens for auditing purposes.

        :param amount: The amount of tokens that were burned.
        """
        print(f"Burned {amount} Kami tokens. Total burned: {self.burned_tokens}")

    def get_total_supply(self) -> float:
        """
        Returns the current total supply of Kami tokens.

        :return: The current total supply of Kami tokens.
        """
        return self.total_supply

    def get_burned_tokens(self) -> float:
        """
        Returns the total amount of burned Kami tokens.

        :return: The total amount of burned Kami tokens.
        """
        return self.burned_tokens


# Example usage
if __name__ == "__main__":
    try:
        kami_bot = KamiBurnBot(initial_supply=10000.0)
        print(f"Initial supply: {kami_bot.get_total_supply()}")

        kami_bot.burn_tokens(1000.0)
        print(f"Current supply after burn: {kami_bot.get_total_supply()}")

        kami_bot.burn_tokens(500.0)
        print(f"Current supply after burn: {kami_bot.get_total_supply()}")

    except ValueError as e:
        print(f"Error: {e}")
```
