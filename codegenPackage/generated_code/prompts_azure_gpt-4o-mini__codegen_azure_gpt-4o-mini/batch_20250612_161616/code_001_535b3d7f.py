"""
Generated Code Metadata:
========================
Original URL: https://milli-dog.vercel.app
Prompt: Write a function that calculates the tokenomics distribution for $MILLI based on the provided percentages.
Generated: DETERMINISTIC_535b3d7f687840e5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsDistribution:
    def __init__(self, total_supply: float):
        """
        Initializes the TokenomicsDistribution with a total supply of tokens.

        :param total_supply: Total number of tokens to distribute.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

    def calculate_distribution(self, percentages: dict) -> dict:
        """
        Calculates the token distribution based on the provided percentages.

        :param percentages: A dictionary where keys are categories and values are the corresponding percentages.
        :return: A dictionary with the calculated token amounts for each category.
        """
        if not isinstance(percentages, dict):
            raise TypeError("Percentages must be provided as a dictionary.")
        
        total_percentage = sum(percentages.values())
        if total_percentage != 100:
            raise ValueError("Total percentages must equal 100.")

        distribution = {}
        for category, percentage in percentages.items():
            if percentage < 0:
                raise ValueError(f"Percentage for {category} cannot be negative.")
            distribution[category] = (percentage / 100) * self.total_supply

        return distribution


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply
        tokenomics = TokenomicsDistribution(total_supply)

        # Define the distribution percentages
        percentages = {
            "Team": 20,
            "Marketing": 15,
            "Development": 25,
            "Liquidity": 30,
            "Reserve": 10
        }

        # Calculate the distribution
        distribution = tokenomics.calculate_distribution(percentages)
        print("Tokenomics Distribution:", distribution)

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
