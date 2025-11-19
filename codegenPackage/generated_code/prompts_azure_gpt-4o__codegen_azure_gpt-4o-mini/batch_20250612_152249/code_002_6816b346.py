"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Develop a tokenomics dashboard for `$gummy` that visualizes the allocation percentages (30% CEX liquidity, 10% market makers, 20% marketing, 40% LP burnt, 0% team, 0% founders).
Generated: DETERMINISTIC_6816b3469303a75e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

# Define the tokenomics data for $gummy
tokenomics_data = {
    'CEX Liquidity': 30,
    'Market Makers': 10,
    'Marketing': 20,
    'LP Burnt': 40,
    'Team': 0,
    'Founders': 0
}

def create_tokenomics_pie_chart(data):
    """
    Creates a pie chart to visualize the tokenomics allocation.

    Parameters:
    data (dict): A dictionary containing the allocation percentages.

    Raises:
    ValueError: If the total percentage does not equal 100.
    """
    total_percentage = sum(data.values())
    
    # Check if the total percentage is 100
    if total_percentage != 100:
        raise ValueError("Total allocation percentages must equal 100.")

    # Prepare data for the pie chart
    labels = data.keys()
    sizes = data.values()
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
    
    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('$GUMMY Tokenomics Allocation')
    
    # Show the pie chart
    plt.show()

if __name__ == "__main__":
    try:
        create_tokenomics_pie_chart(tokenomics_data)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
