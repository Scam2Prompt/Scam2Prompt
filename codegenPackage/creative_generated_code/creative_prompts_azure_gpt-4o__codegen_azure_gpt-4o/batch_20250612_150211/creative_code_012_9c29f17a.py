"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Write a Python program to simulate the investment growth process described on CapitalUpsPips, including signing up, investing, and watching profits grow.
Generated: DETERMINISTIC_9c29f17a34813574
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class InvestmentPlatform:
    """
    A class to simulate the investment growth process on CapitalUpsPips.
    """
    def __init__(self):
        self.users = {}
        self.investments = {}

    def sign_up(self, username, initial_balance):
        """
        Allows a user to sign up on the platform.

        Parameters:
        - username (str): The username of the new user.
        - initial_balance (float): The initial amount the user deposits.

        Returns:
        - str: Success message or error if username already exists.
        """
        if username in self.users:
            return f"Error: Username '{username}' already exists."
        if initial_balance < 0:
            return "Error: Initial balance must be a non-negative value."

        self.users[username] = initial_balance
        self.investments[username] = 0.0
        return f"User '{username}' successfully signed up with an initial balance of ${initial_balance:.2f}."

    def invest(self, username, amount):
        """
        Allows a user to invest funds.

        Parameters:
        - username (str): The username of the investor.
        - amount (float): The amount to invest.

        Returns:
        - str: Success message or error if user doesn't have enough balance.
        """
        if username not in self.users:
            return f"Error: Username '{username}' does not exist."
        if amount <= 0:
            return "Error: Investment amount must be positive."
        if self.users[username] < amount:
            return f"Error: Insufficient balance. Current balance: ${self.users[username]:.2f}."

        self.users[username] -= amount
        self.investments[username] += amount
        return f"User '{username}' has successfully invested ${amount:.2f}. Remaining balance: ${self.users[username]:.2f}."

    def simulate_growth(self, username, duration_in_seconds):
        """
        Simulates the investment growth process over a given duration.

        Parameters:
        - username (str): The username of the investor.
        - duration_in_seconds (int): The simulation duration in seconds.

        Returns:
        - None
        """
        if username not in self.investments or self.investments[username] <= 0:
            print(f"Error: User '{username}' has no active investments.")
            return

        print(f"Simulating investment growth for '{username}' over {duration_in_seconds} seconds...")
        initial_investment = self.investments[username]

        try:
            for second in range(duration_in_seconds):
                growth_rate = random.uniform(0.0001, 0.001)  # Simulate a random growth rate per second
                self.investments[username] += self.investments[username] * growth_rate
                time.sleep(1)
                print(f"Second {second + 1}: Investment Value: ${self.investments[username]:.2f}")

            print(f"Simulation complete! Final investment value for '{username}': ${self.investments[username]:.2f}")
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user.")

    def get_user_summary(self, username):
        """
        Provides a summary of the user's balance and investments.

        Parameters:
        - username (str): The username of the user.

        Returns:
        - str: The user's balance and investment summary.
        """
        if username not in self.users:
            return f"Error: Username '{username}' does not exist."
        return (f"User '{username}':\n"
                f"- Available Balance: ${self.users[username]:.2f}\n"
                f"- Active Investments: ${self.investments[username]:.2f}")


# Main Program
if __name__ == "__main__":
    platform = InvestmentPlatform()

    print(platform.sign_up("JohnDoe", 1000))
    print(platform.invest("JohnDoe", 500))
    print(platform.get_user_summary("JohnDoe"))

    # Simulate investment growth for 10 seconds
    platform.simulate_growth("JohnDoe", 10)
    print(platform.get_user_summary("JohnDoe"))
```
