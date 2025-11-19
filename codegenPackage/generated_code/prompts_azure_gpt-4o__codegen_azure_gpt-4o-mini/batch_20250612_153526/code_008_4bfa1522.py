"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Using the DOGE20 tokenomics breakdown, write a script to display the allocation percentages (e.g., presale, marketing, treasury, staking rewards, liquidity) in a pie chart using Python's Matplotlib library.
Generated: DETERMINISTIC_4bfa15227de80d27
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

# Define the tokenomics breakdown for DOGE20
tokenomics = {
    'Presale': 20,        # Percentage allocated for presale
    'Marketing': 15,      # Percentage allocated for marketing
    'Treasury': 10,       # Percentage allocated for treasury
    'Staking Rewards': 25, # Percentage allocated for staking rewards
    'Liquidity': 30        # Percentage allocated for liquidity
}

def plot_tokenomics(tokenomics):
    """
    Plots a pie chart of the DOGE20 tokenomics allocation.

    Parameters:
    tokenomics (dict): A dictionary containing the allocation percentages.

    Raises:
    ValueError: If the total percentage does not equal 100.
    """
    # Calculate total percentage
    total_percentage = sum(tokenomics.values())
    
    # Check if the total percentage is valid
    if total_percentage != 100:
        raise ValueError(f"Total percentage must equal 100, but got {total_percentage}.")

    # Prepare data for plotting
    labels = tokenomics.keys()
    sizes = tokenomics.values()
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']  # Custom colors for each section
    explode = (0.1, 0, 0, 0, 0)  # explode the first slice (Presale)

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    # Equal aspect ratio ensures that pie chart is a circle
    plt.axis('equal')  
    plt.title('DOGE20 Tokenomics Allocation')
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

# Run the function to plot the tokenomics
if __name__ == "__main__":
    try:
        plot_tokenomics(tokenomics)
    except ValueError as e:
        print(f"Error: {e}")
```
