"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.coin-bubbles.com
Prompt: Write code to create an interactive bubble chart for visualizing cryptocurrency market data, similar to the visualizations described on Coin Bubbles.
Generated: DETERMINISTIC_4d576383442d8dff
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
import seaborn as sns

# Set the style for the plot
sns.set(style="whitegrid")

def fetch_crypto_data():
    """
    Fetch cryptocurrency market data.
    
    Returns:
        DataFrame: A pandas DataFrame containing cryptocurrency data
    """
    try:
        # Sample data for demonstration; replace with actual API call if needed
        data = {
            'name': ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Cardano'],
            'market_cap': [800000000000, 300000000000, 60000000000, 12000000000, 50000000000],
            'price': [42000, 2800, 1.5, 150, 2],
            'volume': [50000000000, 20000000000, 10000000000, 5000000000, 2000000000]
        }
        return pd.DataFrame(data)
    
    except Exception as e:
        print(f"Error fetching cryptocurrency data: {e}")
        return pd.DataFrame()

def plot_bubble_chart(crypto_data):
    """
    Create an interactive bubble chart for visualizing cryptocurrency market data.
    
    Args:
        crypto_data (DataFrame): A DataFrame containing cryptocurrency data
    """
    # Check if data is empty
    if crypto_data.empty:
        print("No data available to plot.")
        return
    
    # Normalize the market cap for bubble sizes
    sizes = np.sqrt(crypto_data['market_cap']) / np.max(np.sqrt(crypto_data['market_cap'])) * 1000

    # Set up the figure and axis
    plt.figure(figsize=(12, 8))
    
    # Create a scatter plot
    scatter = plt.scatter(
        x=crypto_data['price'],
        y=crypto_data['volume'],
        s=sizes,
        alpha=0.5,
        c=crypto_data['market_cap'],
        cmap='viridis',
        norm=Normalize(vmin=crypto_data['market_cap'].min(), vmax=crypto_data['market_cap'].max())
    )

    # Add color bar
    plt.colorbar(scatter, label='Market Cap (in $)')
    
    # Add labels and title
    plt.title('Cryptocurrency Market Data Bubble Chart')
    plt.xlabel('Price (in $)')
    plt.ylabel('Volume (in $)')
    
    # Annotate each bubble
    for i, row in crypto_data.iterrows():
        plt.annotate(row['name'], (row['price'], row['volume']), fontsize=9, ha='center')
    
    # Show plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Fetch data and plot
    crypto_data = fetch_crypto_data()
    plot_bubble_chart(crypto_data)
```
