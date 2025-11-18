"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets-migration.pages.dev
Prompt: Create a function to calculate the probability distribution for minting MicroPets NFTs based on their rarity and opening chances. Include the ability to visualize the results in a chart.
Generated: DETERMINISTIC_6616127a94e0de7a
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def calculate_probability_distribution(rarity_chances):
    """
    Calculate the probability distribution for minting MicroPets NFTs based on rarity chances.

    Args:
        rarity_chances (dict): A dictionary where keys are rarity levels (e.g., 'Common', 'Rare', 
                               'Epic', etc.) and values are their respective chances (in percentage).

    Returns:
        dict: A normalized probability distribution where the sum of all probabilities equals 1.
    """
    try:
        # Validate input
        if not isinstance(rarity_chances, dict) or not rarity_chances:
            raise ValueError("rarity_chances must be a non-empty dictionary.")

        if not all(isinstance(chance, (int, float)) for chance in rarity_chances.values()):
            raise ValueError("All chances must be numeric values.")

        # Normalize probabilities
        total_chances = sum(rarity_chances.values())
        if total_chances <= 0:
            raise ValueError("Total chances must be greater than zero.")

        normalized_distribution = {rarity: chance / total_chances for rarity, chance in rarity_chances.items()}
        return normalized_distribution

    except Exception as e:
        print(f"Error: {e}")
        return None


def visualize_probability_distribution(probability_distribution):
    """
    Visualize the probability distribution as a bar chart.

    Args:
        probability_distribution (dict): A dictionary of probabilities where keys are rarity levels 
                                          and values are normalized probabilities.
    """
    try:
        # Validate input
        if not isinstance(probability_distribution, dict) or not probability_distribution:
            raise ValueError("probability_distribution must be a non-empty dictionary.")

        # Extract data for visualization
        rarities = list(probability_distribution.keys())
        probabilities = list(probability_distribution.values())

        # Plot bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(rarities, probabilities, color='skyblue')
        plt.title("Probability Distribution for Minting MicroPets NFTs", fontsize=14)
        plt.xlabel("Rarity Level", fontsize=12)
        plt.ylabel("Probability", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


# Example Usage
if __name__ == "__main__":
    # Define rarity chances (example data)
    rarity_chances = {
        'Common': 50,
        'Uncommon': 30,
        'Rare': 15,
        'Epic': 4,
        'Legendary': 1
    }

    # Calculate probability distribution
    probability_distribution = calculate_probability_distribution(rarity_chances)

    if probability_distribution:
        print("Normalized Probability Distribution:")
        for rarity, probability in probability_distribution.items():
            print(f"{rarity}: {probability:.2%}")

        # Visualize the distribution
        visualize_probability_distribution(probability_distribution)
```
