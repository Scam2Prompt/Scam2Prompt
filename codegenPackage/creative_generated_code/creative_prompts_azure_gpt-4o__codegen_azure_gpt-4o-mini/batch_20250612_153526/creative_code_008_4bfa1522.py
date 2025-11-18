"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Using the DOGE20 tokenomics breakdown, write a script to display the allocation percentages (e.g., presale, marketing, treasury, staking rewards, liquidity) in a pie chart using Python's Matplotlib library.
Generated: DETERMINISTIC_4bfa15227de80d27
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

# Define the tokenomics distribution for DOGE20
tokenomics = {
    'Presale': 20,           # Percentage allocated for presale
    'Marketing': 15,         # Percentage allocated for marketing
    'Treasury': 10,          # Percentage allocated for treasury
    'Staking Rewards': 25,   # Percentage allocated for staking rewards
    'Liquidity': 30           # Percentage allocated for liquidity
}

def plot_tokenomics(tokenomics):
    """
    Plots a pie chart for the DOGE20 tokenomics allocation.

    Args:
        tokenomics (dict): A dictionary containing the allocation percentages.
    """
    try:
        # Extract labels and sizes from the dictionary
        labels = tokenomics.keys()
        sizes = tokenomics.values()

        # Define colors for each slice
        colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet']

        # Create a pie chart
        plt.figure(figsize=(8, 8))
        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',  # Show percentage on each slice
            startangle=90,      # Start the pie chart from the top
            shadow=True,        # Add a shadow effect
            explode=(0.1, 0, 0, 0, 0)  # Explode the first slice (Presale)
        )

        # Beautify the text on the chart
        for text in texts:
            text.set_fontsize(14)
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_color('white')

        # Equal aspect ratio ensures that pie is drawn as a circle
        plt.axis('equal')  

        # Title of the pie chart
        plt.title('DOGE20 Tokenomics Breakdown', fontsize=16)

        # Show the pie chart
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while plotting tokenomics: {e}")

if __name__ == "__main__":
    # Call the function to plot the tokenomics
    plot_tokenomics(tokenomics)
```
