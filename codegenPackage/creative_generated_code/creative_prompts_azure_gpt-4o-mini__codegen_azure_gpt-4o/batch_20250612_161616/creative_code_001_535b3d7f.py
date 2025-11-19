"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milli-dog.vercel.app
Prompt: Write a function that calculates the tokenomics distribution for $MILLI based on the provided percentages.
Generated: DETERMINISTIC_535b3d7f687840e5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tokenomics.py

def calculate_tokenomics_distribution(total_supply, distribution_percentages):
    """
    Calculates tokenomics distribution for $MILLI based on given percentages.

    Args:
        total_supply (int): The total supply of tokens.
        distribution_percentages (dict): A dictionary with the distribution categories as keys
                                         and their respective percentages as values.

    Returns:
        dict: A dictionary with the distribution categories as keys and the number of tokens allocated as values.

    Raises:
        ValueError: If the total percentage exceeds or is less than 100%.
        TypeError: If invalid data types are provided.
    """
    # Input validation
    if not isinstance(total_supply, (int, float)) or total_supply <= 0:
        raise TypeError("Total supply must be a positive number.")
    if not isinstance(distribution_percentages, dict):
        raise TypeError("Distribution percentages must be provided as a dictionary.")
    if not all(isinstance(key, str) and isinstance(value, (int, float)) for key, value in distribution_percentages.items()):
        raise TypeError("All keys in distribution percentages must be strings and values must be numbers.")

    total_percentage = sum(distribution_percentages.values())
    if total_percentage != 100:
        raise ValueError("The total percentage of distributions must equal 100%.")

    # Calculate token distribution
    token_distribution = {}
    for category, percentage in distribution_percentages.items():
        token_distribution[category] = round(total_supply * (percentage / 100))

    return token_distribution


# Example usage
if __name__ == "__main__":
    try:
        # Total supply of $MILLI tokens
        total_supply = 1_000_000_000  # 1 billion tokens

        # Tokenomics distribution percentages
        distribution_percentages = {
            "Team": 15.0,              # 15%
            "Marketing": 10.0,         # 10%
            "Community": 40.0,         # 40%
            "Development": 25.0,       # 25%
            "Reserve": 10.0            # 10%
        }

        # Calculate and display the distribution
        distribution = calculate_tokenomics_distribution(total_supply, distribution_percentages)
        print("Tokenomics Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens} tokens")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
