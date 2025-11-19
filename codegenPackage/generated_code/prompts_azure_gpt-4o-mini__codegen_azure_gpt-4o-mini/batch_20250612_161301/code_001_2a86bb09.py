"""
Generated Code Metadata:
========================
Original URL: https://retik-com.pages.dev
Prompt: Write a function to calculate the total supply and distribution of the RETIK token based on the provided tokenomics data.
Generated: DETERMINISTIC_2a86bb09ffbb9061
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RetikTokenomics:
    def __init__(self, total_supply, distribution):
        """
        Initializes the RetikTokenomics class with total supply and distribution data.

        :param total_supply: Total supply of RETIK tokens (in integer).
        :param distribution: A dictionary containing distribution categories and their respective amounts.
        """
        self.total_supply = total_supply
        self.distribution = distribution

    def calculate_total_distribution(self):
        """
        Calculates the total distribution of RETIK tokens.

        :return: Total distribution amount (in integer).
        """
        total_distribution = sum(self.distribution.values())
        return total_distribution

    def validate_distribution(self):
        """
        Validates the distribution data against the total supply.

        :raises ValueError: If the total distribution exceeds the total supply.
        """
        total_distribution = self.calculate_total_distribution()
        if total_distribution > self.total_supply:
            raise ValueError("Total distribution exceeds total supply of RETIK tokens.")

    def get_distribution_summary(self):
        """
        Returns a summary of the distribution of RETIK tokens.

        :return: A dictionary containing total supply, total distribution, and distribution details.
        """
        try:
            self.validate_distribution()
            total_distribution = self.calculate_total_distribution()
            return {
                "total_supply": self.total_supply,
                "total_distribution": total_distribution,
                "distribution_details": self.distribution
            }
        except ValueError as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Define total supply and distribution data
    total_supply = 1000000  # Total supply of RETIK tokens
    distribution = {
        "team": 200000,
        "marketing": 150000,
        "development": 250000,
        "community": 300000,
        "reserve": 100000
    }

    # Create an instance of RetikTokenomics
    retik_tokenomics = RetikTokenomics(total_supply, distribution)

    # Get the distribution summary
    summary = retik_tokenomics.get_distribution_summary()
    print(summary)
```
