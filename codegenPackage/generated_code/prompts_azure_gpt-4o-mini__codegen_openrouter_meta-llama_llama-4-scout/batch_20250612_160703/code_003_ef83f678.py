"""
Generated Code Metadata:
========================
Original URL: https://freebitcoinmining.website
Prompt: Generate a code snippet that calculates potential earnings based on the different mining plans offered by Free Bitcoin Mining.
Generated: DETERMINISTIC_ef83f6783c58e06b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mining_plans.py

class MiningPlan:
    """Represents a mining plan with its respective details."""

    def __init__(self, name, hash_rate, duration, cost):
        """
        Initializes a MiningPlan object.

        Args:
            name (str): The name of the mining plan.
            hash_rate (float): The hash rate of the mining plan in TH/s.
            duration (int): The duration of the mining plan in days.
            cost (float): The cost of the mining plan in USD.
        """
        self.name = name
        self.hash_rate = hash_rate
        self.duration = duration
        self.cost = cost

    def calculate_earnings(self, block_reward, block_time, difficulty):
        """
        Calculates the potential earnings of the mining plan.

        Args:
            block_reward (float): The block reward in BTC.
            block_time (int): The block time in minutes.
            difficulty (float): The network difficulty.

        Returns:
            float: The potential earnings in USD.
        """
        # Calculate the total number of blocks mined
        total_blocks = (self.duration * 24 * 60) / block_time

        # Calculate the total BTC earned
        total_btc = total_blocks * block_reward

        # Calculate the total USD earned
        # Assuming a fixed exchange rate of 1 BTC = 40000 USD
        exchange_rate = 40000
        total_usd = total_btc * exchange_rate

        # Calculate the net earnings
        net_earnings = total_usd - self.cost

        return {
            "total_blocks": total_blocks,
            "total_btc": total_btc,
            "total_usd": total_usd,
            "net_earnings": net_earnings,
        }


class FreeBitcoinMining:
    """Represents Free Bitcoin Mining with its mining plans."""

    def __init__(self):
        self.mining_plans = [
            MiningPlan("Basic", 1.0, 30, 100),
            MiningPlan("Premium", 5.0, 30, 500),
            MiningPlan("Enterprise", 10.0, 30, 1000),
        ]

    def get_mining_plans(self):
        """Returns a list of available mining plans."""
        return self.mining_plans

    def calculate_potential_earnings(self, plan_name, block_reward, block_time, difficulty):
        """
        Calculates the potential earnings of a specific mining plan.

        Args:
            plan_name (str): The name of the mining plan.
            block_reward (float): The block reward in BTC.
            block_time (int): The block time in minutes.
            difficulty (float): The network difficulty.

        Returns:
            dict: The potential earnings.
        """
        plan = next((plan for plan in self.mining_plans if plan.name == plan_name), None)
        if plan is None:
            raise ValueError("Invalid mining plan")

        return plan.calculate_earnings(block_reward, block_time, difficulty)


def main():
    try:
        mining = FreeBitcoinMining()
        plans = mining.get_mining_plans()

        print("Available Mining Plans:")
        for plan in plans:
            print(f"- {plan.name}")

        plan_name = input("Enter the name of the mining plan: ")
        block_reward = float(input("Enter the block reward in BTC: "))
        block_time = float(input("Enter the block time in minutes: "))
        difficulty = float(input("Enter the network difficulty: "))

        earnings = mining.calculate_potential_earnings(plan_name, block_reward, block_time, difficulty)

        print("\nPotential Earnings:")
        print(f"- Total Blocks: {earnings['total_blocks']:.2f}")
        print(f"- Total BTC: {earnings['total_btc']:.8f}")
        print(f"- Total USD: {earnings['total_usd']:.2f}")
        print(f"- Net Earnings: {earnings['net_earnings']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
