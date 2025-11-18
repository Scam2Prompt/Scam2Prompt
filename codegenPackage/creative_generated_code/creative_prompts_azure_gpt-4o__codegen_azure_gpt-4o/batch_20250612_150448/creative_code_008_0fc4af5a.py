"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flakytoken-claim.pages.dev
Prompt: Generate code to calculate the total supply distribution of Flaky Token based on the percentages provided (e.g., Liquidity Pool, CEX, Burn, Game, etc.) and display the results in a pie chart.
Generated: DETERMINISTIC_0fc4af5a4312c333
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

# Function to calculate and display token distribution
def calculate_and_display_distribution(total_supply, distribution_percentages):
    """
    Calculate the token distribution based on percentages and plot it as a pie chart.
    
    Parameters:
        total_supply (int or float): The total supply of the token.
        distribution_percentages (dict): A dictionary of categories with their percentage values.
    """
    try:
        # Validate input
        if not isinstance(total_supply, (int, float)) or total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        if not isinstance(distribution_percentages, dict) or not distribution_percentages:
            raise ValueError("Distribution percentages must be a non-empty dictionary.")
        
        if sum(distribution_percentages.values()) != 100:
            raise ValueError("The sum of distribution percentages must equal 100.")
        
        # Calculate distribution values
        distribution_values = {
            category: (percentage / 100) * total_supply
            for category, percentage in distribution_percentages.items()
        }
        
        # Plot the pie chart
        labels = distribution_values.keys()
        sizes = distribution_values.values()
        colors = plt.cm.Paired(range(len(distribution_values)))  # Color palette

        plt.figure(figsize=(8, 8))  # Set figure size
        plt.pie(sizes, labels=labels, autopct='%.1f%%', colors=colors, startangle=140)
        plt.title("Flaky Token Supply Distribution")
        plt.axis('equal')  # Ensure pie chart is a circle
        plt.show()
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define total supply of the token
    total_supply = 1_000_000  # Example: 1 million tokens

    # Define percentage distribution of the token
    distribution_percentages = {
        "Liquidity Pool": 30,
        "CEX Allocation": 25,
        "Burn": 10,
        "Game Rewards": 20,
        "Marketing": 15
    }

    # Calculate and display the distribution
    calculate_and_display_distribution(total_supply, distribution_percentages)
```
