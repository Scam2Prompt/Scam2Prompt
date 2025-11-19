"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories from "Bismillah Gems," write a program to generate a visual catalog that organizes gemstones by type, weight, and price.
Generated: DETERMINISTIC_8090b26c066a3243
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define a class to represent a gemstone
class Gemstone:
    def __init__(self, name, category, weight, price):
        """
        Initialize a Gemstone object.

        :param name: str - The name of the gemstone
        :param category: str - The category of the gemstone (e.g., Ruby, Sapphire)
        :param weight: float - The weight of the gemstone in carats
        :param price: float - The price of the gemstone in USD
        """
        self.name = name
        self.category = category
        self.weight = weight
        self.price = price

# Function to create a visual catalog of gemstones
def create_gemstone_catalog(gemstones):
    """
    Create a visual catalog of gemstones organized by type, weight, and price.

    :param gemstones: list of Gemstone - A list of Gemstone objects
    """
    # Convert the list of gemstones into a DataFrame for easier manipulation
    df = pd.DataFrame([{
        'Name': gem.name,
        'Category': gem.category,
        'Weight (carats)': gem.weight,
        'Price (USD)': gem.price
    } for gem in gemstones])

    # Group by category and calculate average weight and price
    grouped_df = df.groupby('Category').agg({
        'Weight (carats)': 'mean',
        'Price (USD)': 'mean'
    }).reset_index()

    # Plotting the average weight and price of gemstones by category
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Create a bar plot for average weight
    ax1.bar(grouped_df['Category'], grouped_df['Weight (carats)'], color='b', alpha=0.6, label='Average Weight (carats)')
    ax1.set_xlabel('Gemstone Category')
    ax1.set_ylabel('Average Weight (carats)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second y-axis for average price
    ax2 = ax1.twinx()
    ax2.plot(grouped_df['Category'], grouped_df['Price (USD)'], color='r', marker='o', label='Average Price (USD)')
    ax2.set_ylabel('Average Price (USD)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    # Adding title and legends
    plt.title('Gemstone Catalog: Average Weight and Price by Category')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Sample gemstone data
        gemstones = [
            Gemstone("Ruby", "Ruby", 1.2, 3000),
            Gemstone("Sapphire", "Sapphire", 1.5, 2500),
            Gemstone("Emerald", "Emerald", 1.0, 4000),
            Gemstone("Diamond", "Diamond", 0.5, 5000),
            Gemstone("Topaz", "Topaz", 2.0, 1500),
            Gemstone("Ruby", "Ruby", 1.0, 2800),
            Gemstone("Sapphire", "Sapphire", 1.8, 2700),
        ]

        # Create the gemstone catalog
        create_gemstone_catalog(gemstones)

    except Exception as e:
        print(f"An error occurred: {e}")
```
