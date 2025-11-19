"""
Generated Code Metadata:
========================
Original URL: https://bloxwhitelist.pages.dev
Prompt: Design a Blox-like tokenomics system for a new cryptocurrency project, including a sustainable financial model and a balanced ecosystem.
Generated: DETERMINISTIC_06756d961ca0e168
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    """
    A class to represent the tokenomics of a cryptocurrency project.
    This includes the distribution, utility, and sustainability of the token.
    """

    def __init__(self, total_supply: int):
        """
        Initializes the Tokenomics with a total supply of tokens.

        :param total_supply: Total number of tokens to be created.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.distribution = {
            "team": 0.15,  # 15% for the team
            "investors": 0.25,  # 25% for early investors
            "community": 0.30,  # 30% for community rewards
            "development": 0.20,  # 20% for development
            "reserve": 0.10  # 10% for reserve
        }
        self.token_distribution = self.calculate_distribution()

    def calculate_distribution(self):
        """
        Calculates the distribution of tokens based on the defined percentages.

        :return: A dictionary with the number of tokens allocated to each category.
        """
        distribution_amounts = {}
        for category, percentage in self.distribution.items():
            distribution_amounts[category] = int(self.total_supply * percentage)
        return distribution_amounts

    def get_distribution(self):
        """
        Returns the current token distribution.

        :return: A dictionary with the token distribution.
        """
        return self.token_distribution

    def utility(self):
        """
        Defines the utility of the token within the ecosystem.

        :return: A string describing the utility of the token.
        """
        return ("The token can be used for transaction fees, staking rewards, "
                "governance voting, and accessing premium features within the ecosystem.")

    def sustainability_model(self):
        """
        Outlines the sustainability model for the token.

        :return: A string describing the sustainability model.
        """
        return ("The sustainability model includes transaction fees that are "
                "reinvested into the ecosystem, regular buybacks, and a portion "
                "of the rewards allocated to a development fund.")

    def display_info(self):
        """
        Displays the complete information about the tokenomics.

        :return: None
        """
        print("Total Supply:", self.total_supply)
        print("Token Distribution:", self.get_distribution())
        print("Utility:", self.utility())
        print("Sustainability Model:", self.sustainability_model())


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply
        tokenomics = Tokenomics(total_supply)
        tokenomics.display_info()
    except ValueError as e:
        print(f"Error: {e}")
```
