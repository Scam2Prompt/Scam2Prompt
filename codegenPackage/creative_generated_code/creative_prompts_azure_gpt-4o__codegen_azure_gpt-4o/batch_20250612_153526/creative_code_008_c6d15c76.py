"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brett-dvf.pages.dev
Prompt: Write a Python script to calculate the percentage allocation of BRETT tokenomics (LP, Treasury, CEX Wallet) and display it in a pie chart using Matplotlib.
Generated: DETERMINISTIC_c6d15c768451a4e3
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def calculate_percentage(allocation):
    """
    Calculate the percentage allocation for each category.

    Parameters:
        allocation (dict): A dictionary with token allocation categories as keys and their values as amounts.

    Returns:
        dict: A dictionary containing the percentage allocation for each category.
    """
    try:
        total = sum(allocation.values())
        # Avoid division by zero
        if total == 0:
            raise ValueError("Total allocation cannot be zero.")
        
        percentage_allocation = {key: (value / total) * 100 for key, value in allocation.items()}
        return percentage_allocation
    except TypeError as e:
        raise TypeError("Allocation values must be numeric.") from e


def display_pie_chart(data):
    """
    Display a pie chart for the given data.

    Parameters:
        data (dict): A dictionary containing categories and their percentage allocation.
    """
    try:
        labels = data.keys()
        sizes = data.values()
        colors = ['#ff9999', '#66b3ff', '#99ff99']  # Custom colors for the pie chart
        explode = [0.1] * len(data)  # Slightly "explode" each section for better visibility

        # Create pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode, colors=colors)
        plt.title("BRETT Tokenomics Allocation")
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.show()
    except Exception as e:
        print(f"An error occurred while displaying the pie chart: {e}")


if __name__ == "__main__":
    # Token allocation data (example values; replace with actual tokenomics data)
    token_allocation = {
        "LP": 5000,        # Liquidity Pool allocation
        "Treasury": 3000,  # Treasury allocation
        "CEX Wallet": 2000 # Centralized Exchange wallet allocation
    }
    
    try:
        # Calculate percentage allocation
        percentage_data = calculate_percentage(token_allocation)
        
        # Display the pie chart
        display_pie_chart(percentage_data)
    except Exception as err:
        print(f"An error occurred: {err}")
```
