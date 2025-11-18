"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Write a script to visualize tokenomics data for Mike Token, including presale allocation, liquidity, and staking percentages, using Python and Matplotlib.
Generated: DETERMINISTIC_9e6f021ed63156d8
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def visualize_tokenomics(presale_allocation, liquidity, staking):
    """
    Visualizes the tokenomics data of Mike Token.

    Parameters:
    presale_allocation (float): Percentage of tokens allocated for presale.
    liquidity (float): Percentage of tokens allocated for liquidity.
    staking (float): Percentage of tokens allocated for staking.

    Raises:
    ValueError: If any percentage is negative or if the total exceeds 100%.
    """
    # Validate inputs
    if any(x < 0 for x in [presale_allocation, liquidity, staking]):
        raise ValueError("All percentages must be non-negative.")
    if presale_allocation + liquidity + staking > 100:
        raise ValueError("Total percentage cannot exceed 100.")

    # Data for visualization
    labels = ['Presale Allocation', 'Liquidity', 'Staking']
    sizes = [presale_allocation, liquidity, staking]
    colors = ['#FF9999', '#66B3FF', '#99FF99']
    explode = (0.1, 0, 0)  # explode the 1st slice (Presale Allocation)

    # Create pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Tokenomics of Mike Token')
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is a circle.

    # Display the plot
    plt.show()

if __name__ == "__main__":
    # Example tokenomics data for Mike Token
    presale_allocation = 40.0  # 40% for presale
    liquidity = 30.0           # 30% for liquidity
    staking = 30.0             # 30% for staking

    try:
        visualize_tokenomics(presale_allocation, liquidity, staking)
    except ValueError as e:
        print(f"Error: {e}")
```
