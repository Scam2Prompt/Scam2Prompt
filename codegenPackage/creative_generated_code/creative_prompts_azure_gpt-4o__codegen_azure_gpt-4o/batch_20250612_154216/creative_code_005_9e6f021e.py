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

def visualize_tokenomics(token_name, presale_percentage, liquidity_percentage, staking_percentage):
    """
    Function to visualize tokenomics data using a pie chart.

    Parameters:
        token_name (str): Name of the token (e.g., "Mike Token").
        presale_percentage (float): Percentage allocated for presale.
        liquidity_percentage (float): Percentage allocated for liquidity.
        staking_percentage (float): Percentage allocated for staking.
    """
    try:
        # Ensure percentages sum to 100
        total_percentage = presale_percentage + liquidity_percentage + staking_percentage
        if total_percentage != 100:
            raise ValueError("The total of tokenomics percentages must equal 100.")
        
        # Tokenomics categories and their respective percentages
        labels = ['Presale', 'Liquidity', 'Staking']
        sizes = [presale_percentage, liquidity_percentage, staking_percentage]
        colors = ['gold', 'skyblue', 'lightgreen']  # Colors for the chart
        explode = (0.1, 0, 0)  # Highlight the presale slice
        
        # Create pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90, textprops={'fontsize': 12})

        # Title for the chart
        plt.title(f"{token_name} Tokenomics Distribution", fontsize=14, fontweight='bold')

        # Display the chart
        plt.show()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Tokenomics data for "Mike Token"
token_name = "Mike Token"
presale_percentage = 40.0   # 40% allocated for presale
liquidity_percentage = 30.0 # 30% allocated for liquidity
staking_percentage = 30.0   # 30% allocated for staking

# Visualize the tokenomics data
visualize_tokenomics(token_name, presale_percentage, liquidity_percentage, staking_percentage)
```
