"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcoin.world
Prompt: Write a Python script to calculate the allocation percentages for God Token supply (e.g., 60% for Rewards Pool, 10% for Development) and display the token distribution in a pie chart using Matplotlib.
Generated: DETERMINISTIC_06d666938e4b0ed9
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def calculate_allocation(supply, allocations):
    """
    Calculate the allocation for each category based on the total supply.

    :param supply: Total supply of God Tokens
    :param allocations: Dictionary with allocation percentages
    :return: Dictionary with the allocated token amounts
    """
    allocated_amounts = {}
    for category, percentage in allocations.items():
        if not (0 <= percentage <= 100):
            raise ValueError(f"Allocation percentage for '{category}' must be between 0 and 100.")
        allocated_amounts[category] = (percentage / 100) * supply
    return allocated_amounts

def plot_distribution(allocations):
    """
    Plot a pie chart of the token distribution.

    :param allocations: Dictionary with allocated token amounts
    """
    categories = allocations.keys()
    amounts = allocations.values()
    
    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title('God Token Distribution')
    plt.show()

def main():
    # Total supply of God Tokens
    total_supply = 1000000

    # Define the allocation percentages
    allocation_percentages = {
        'Rewards Pool': 60,
        'Development': 10,
        'Marketing': 15,
        'Community Fund': 5,
        'Reserve': 10
    }

    try:
        # Calculate allocated amounts
        allocations = calculate_allocation(total_supply, allocation_percentages)

        # Plot the distribution
        plot_distribution(allocations)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
