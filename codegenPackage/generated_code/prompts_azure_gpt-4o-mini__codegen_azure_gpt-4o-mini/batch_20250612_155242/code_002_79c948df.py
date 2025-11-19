"""
Generated Code Metadata:
========================
Original URL: https://initia.co
Prompt: Can you provide an example of how to unlock value in an app using Initia's aligned economics?
Generated: DETERMINISTIC_79c948df999d6baf
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InitiaEconomics:
    """
    A class to represent Initia's aligned economics for unlocking value in an application.
    """

    def __init__(self, user_investment: float, app_value: float):
        """
        Initializes the InitiaEconomics instance.

        :param user_investment: The amount invested by the user in the app.
        :param app_value: The current value of the app.
        """
        if user_investment < 0 or app_value < 0:
            raise ValueError("Investment and app value must be non-negative.")

        self.user_investment = user_investment
        self.app_value = app_value

    def calculate_user_equity(self) -> float:
        """
        Calculates the user's equity in the app based on their investment.

        :return: The user's equity percentage in the app.
        """
        if self.app_value == 0:
            raise ZeroDivisionError("App value cannot be zero when calculating equity.")

        user_equity = (self.user_investment / self.app_value) * 100
        return user_equity

    def unlock_value(self, additional_investment: float) -> float:
        """
        Unlocks additional value in the app based on further user investment.

        :param additional_investment: The additional amount the user invests.
        :return: The new app value after the additional investment.
        """
        if additional_investment < 0:
            raise ValueError("Additional investment must be non-negative.")

        self.user_investment += additional_investment
        self.app_value += additional_investment * 1.5  # Assuming a multiplier effect
        return self.app_value

    def get_app_status(self) -> dict:
        """
        Returns the current status of the app including user investment and app value.

        :return: A dictionary containing user investment and app value.
        """
        return {
            "user_investment": self.user_investment,
            "app_value": self.app_value,
            "user_equity": self.calculate_user_equity()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the InitiaEconomics with user investment and app value
        initia = InitiaEconomics(user_investment=1000, app_value=5000)

        # Unlock value through additional investment
        new_app_value = initia.unlock_value(additional_investment=500)

        # Get the current status of the app
        app_status = initia.get_app_status()

        # Print the results
        print(f"New App Value: {new_app_value}")
        print(f"App Status: {app_status}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
