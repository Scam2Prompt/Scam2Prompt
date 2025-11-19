"""
Generated Code Metadata:
========================
Original URL: https://claim-beef-meme.pages.dev
Prompt: Create a Python script to calculate the percentage of BEEF Coin distribution across DEX liquidity pools, CEX liquidity pools, and airdrops based on the tokenomics provided.
Generated: DETERMINISTIC_c535a875e98b0978
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BeefCoinDistribution:
    def __init__(self, tokenomics):
        """
        Initialize the BeefCoinDistribution with tokenomics data.

        :param tokenomics: A dictionary containing the distribution data.
        """
        self.tokenomics = tokenomics

    def calculate_distribution(self):
        """
        Calculate the percentage distribution of BEEF Coin across different categories.

        :return: A dictionary with the percentage distribution.
        """
        try:
            total_supply = self.tokenomics.get("total_supply", 0)
            if total_supply <= 0:
                raise ValueError("Total supply must be greater than zero.")

            distribution = {
                "DEX": self.tokenomics.get("dex_liquidity", 0) / total_supply * 100,
                "CEX": self.tokenomics.get("cex_liquidity", 0) / total_supply * 100,
                "Airdrops": self.tokenomics.get("airdrops", 0) / total_supply * 100,
            }

            return distribution
        except Exception as e:
            print(f"Error calculating distribution: {e}")
            return None

def load_tokenomics(file_path):
    """
    Load tokenomics data from a JSON file.

    :param file_path: Path to the JSON file containing tokenomics data.
    :return: A dictionary with tokenomics data.
    """
    try:
        with open(file_path, 'r') as file:
            tokenomics = json.load(file)
            return tokenomics
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def main():
    """
    Main function to execute the distribution calculation.
    """
    # Load tokenomics data from a JSON file
    tokenomics_file = 'tokenomics.json'
    tokenomics = load_tokenomics(tokenomics_file)

    if tokenomics:
        # Create an instance of BeefCoinDistribution
        distribution_calculator = BeefCoinDistribution(tokenomics)

        # Calculate the distribution percentages
        distribution = distribution_calculator.calculate_distribution()

        if distribution:
            # Print the distribution results
            print("BEEF Coin Distribution:")
            for category, percentage in distribution.items():
                print(f"{category}: {percentage:.2f}%")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `tokenomics.json` file exists in the same directory as this script and contains the appropriate structure, including keys like `total_supply`, `dex_liquidity`, `cex_liquidity`, and `airdrops`.
