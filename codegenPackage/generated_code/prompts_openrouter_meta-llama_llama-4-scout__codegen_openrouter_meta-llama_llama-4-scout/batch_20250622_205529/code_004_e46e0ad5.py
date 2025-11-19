"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: How does the Vertiv Incentive Program work and what are the rewards for selling Vertiv products and solutions?
Generated: DETERMINISTIC_e46e0ad59bb922c9
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Vertiv Incentive Program Simulator

class VertivIncentiveProgram:
    """
    Simulates the Vertiv Incentive Program.

    The program rewards partners for selling Vertiv products and solutions.
    """

    def __init__(self):
        # Define the rewards structure
        self.rewards_structure = {
            "product": {
                "bronze": 0.05,  # 5% reward for bronze products
                "silver": 0.10,  # 10% reward for silver products
                "gold": 0.15     # 15% reward for gold products
            },
            "solution": {
                "bronze": 0.10,  # 10% reward for bronze solutions
                "silver": 0.20,  # 20% reward for silver solutions
                "gold": 0.30     # 30% reward for gold solutions
            }
        }

    def calculate_reward(self, sale_type, sale_category, sale_amount):
        """
        Calculates the reward for a sale.

        Args:
            sale_type (str): Type of sale (product or solution)
            sale_category (str): Category of sale (bronze, silver, or gold)
            sale_amount (float): Amount of sale

        Returns:
            float: Reward amount
        """
        try:
            # Check if sale type and category are valid
            if sale_type not in self.rewards_structure:
                raise ValueError("Invalid sale type")
            if sale_category not in self.rewards_structure[sale_type]:
                raise ValueError("Invalid sale category")

            # Calculate reward
            reward_percentage = self.rewards_structure[sale_type][sale_category]
            reward_amount = sale_amount * reward_percentage

            return reward_amount

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def get_rewards_structure(self):
        """
        Returns the rewards structure.

        Returns:
            dict: Rewards structure
        """
        return self.rewards_structure


def main():
    # Create an instance of the Vertiv Incentive Program
    program = VertivIncentiveProgram()

    # Example usage
    sale_type = "product"
    sale_category = "silver"
    sale_amount = 10000.0

    reward_amount = program.calculate_reward(sale_type, sale_category, sale_amount)

    if reward_amount:
        print(f"Reward for {sale_type} {sale_category} sale of ${sale_amount:.2f}: ${reward_amount:.2f}")

    # Print rewards structure
    print("\nRewards Structure:")
    for sale_type, categories in program.get_rewards_structure().items():
        print(f"{sale_type.capitalize()}:")
        for category, reward_percentage in categories.items():
            print(f"  {category.capitalize()}: {reward_percentage*100}%")

if __name__ == "__main__":
    main()
```
