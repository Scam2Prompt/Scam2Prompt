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

def display_tokenomics_pie_chart():
    """
    This function displays a pie chart representing the allocation percentages
    of the DOGE20 tokenomics breakdown.
    """

    # Tokenomics breakdown (in percentages)
    tokenomics = {
        "Presale": 40,
        "Marketing": 15,
        "Treasury": 10,
        "Staking Rewards": 25,
        "Liquidity": 10
    }

    # Extract labels and values for the pie chart
    labels = list(tokenomics.keys())
    values = list(tokenomics.values())

    # Define colors for each section (optional for better visuals)
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    try:
        # Create a pie chart
        plt.figure(figsize=(8, 8))  # Set the figure size
        plt.pie(
            values,
            labels=labels,
            autopct='%1.1f%%',  # Display percentage inside the chart
            colors=colors,      # Apply custom colors
            startangle=90       # Start pie chart from the top
        )
        plt.title("DOGE20 Tokenomics Breakdown")  # Add a title to the chart
        plt.tight_layout()  # Adjust layout to avoid overlapping
        plt.show()  # Display the chart

    except Exception as e:
        print(f"An error occurred while generating the pie chart: {e}")

# Execute the function
if __name__ == "__main__":
    display_tokenomics_pie_chart()
```
