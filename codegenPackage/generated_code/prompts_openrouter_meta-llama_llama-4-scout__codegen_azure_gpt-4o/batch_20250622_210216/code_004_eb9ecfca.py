"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Create a token distribution plan for a new cryptocurrency project, inspired by AI Trader's tokenomics, including allocations for public goods funding, ecosystem fund, and user airdrops.
Generated: DETERMINISTIC_eb9ecfcabe2fb32f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TokenDistribution:
    """
    A class to define and manage the token distribution plan for a cryptocurrency project.
    Inspired by AI Trader's tokenomics.
    """

    def __init__(self, total_supply):
        """
        Initialize the token distribution plan.

        :param total_supply: Total supply of tokens for the project.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution_plan = {}

    def allocate_tokens(self, category, percentage):
        """
        Allocate tokens to a specific category.

        :param category: Name of the category (e.g., 'Public Goods Funding').
        :param percentage: Percentage of total supply to allocate to the category.
        """
        if category in self.distribution_plan:
            raise ValueError(f"Category '{category}' already exists in the distribution plan.")
        if percentage <= 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        allocated_tokens = (percentage / 100) * self.total_supply
        self.distribution_plan[category] = allocated_tokens

    def get_distribution_plan(self):
        """
        Get the current token distribution plan.

        :return: A dictionary containing the distribution plan.
        """
        return self.distribution_plan

    def save_distribution_plan(self, file_path):
        """
        Save the distribution plan to a JSON file.

        :param file_path: Path to the file where the distribution plan will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.distribution_plan, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save distribution plan to file: {e}")

    def load_distribution_plan(self, file_path):
        """
        Load a distribution plan from a JSON file.

        :param file_path: Path to the file containing the distribution plan.
        """
        try:
            with open(file_path, 'r') as file:
                self.distribution_plan = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load distribution plan from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the token distribution plan with a total supply of 1,000,000 tokens
        total_supply = 1_000_000
        token_distribution = TokenDistribution(total_supply)

        # Allocate tokens to various categories
        token_distribution.allocate_tokens("Public Goods Funding", 20)  # 20% of total supply
        token_distribution.allocate_tokens("Ecosystem Fund", 50)        # 50% of total supply
        token_distribution.allocate_tokens("User Airdrops", 30)         # 30% of total supply

        # Print the distribution plan
        print("Token Distribution Plan:")
        print(json.dumps(token_distribution.get_distribution_plan(), indent=4))

        # Save the distribution plan to a file
        token_distribution.save_distribution_plan("distribution_plan.json")
        print("Distribution plan saved to 'distribution_plan.json'.")

        # Load the distribution plan from the file (for demonstration purposes)
        token_distribution.load_distribution_plan("distribution_plan.json")
        print("Loaded Distribution Plan:")
        print(json.dumps(token_distribution.get_distribution_plan(), indent=4))

    except Exception as e:
        print(f"Error: {e}")
```
