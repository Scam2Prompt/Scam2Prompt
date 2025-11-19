"""
Generated Code Metadata:
========================
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Generate a visualization of Mike Token's token allocation and liquidity strategies using a suitable data visualization library.
Generated: DETERMINISTIC_b7befebd1ba66fb8
Batch ID: 20250622_211514
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
import seaborn as sns
from typing import Dict, List

# Configuration for visualization
plt.style.use('seaborn')
sns.set_palette("husl")

# Sample data for Mike Token's allocation and liquidity strategies
TOKEN_ALLOCATION = {
    "Team": 20,
    "Advisors": 5,
    "Ecosystem Development": 30,
    "Liquidity Provision": 25,
    "Community Rewards": 10,
    "Reserves": 10
}

LIQUIDITY_STRATEGIES = {
    "Uniswap": 40,
    "Sushiswap": 20,
    "Balancer": 15,
    "Curve": 15,
    "Other DEXs": 10
}

def plot_pie_chart(data: Dict[str, float], title: str, explode: List[float] = None):
    """
    Plot a pie chart for the given data.
    
    Args:
        data: Dictionary with labels as keys and values as sizes
        title: Title of the chart
        explode: List of values to explode slices (if any)
    """
    if explode is None:
        explode = [0] * len(data)
    
    labels = list(data.keys())
    sizes = list(data.values())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=140,
        textprops={'fontsize': 12}
    )
    ax.set_title(title, fontsize=16, pad=20)
    ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
    
    plt.tight_layout()
    plt.show()

def plot_bar_chart(data: Dict[str, float], title: str, xlabel: str, ylabel: str):
    """
    Plot a bar chart for the given data.
    
    Args:
        data: Dictionary with labels as keys and values as heights
        title: Title of the chart
        xlabel: Label for x-axis
        ylabel: Label for y-axis
    """
    df = pd.DataFrame(list(data.items()), columns=[xlabel, ylabel])
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=xlabel, y=ylabel, data=df)
    plt.title(title, fontsize=16, pad=20)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to generate visualizations."""
    try:
        # Token Allocation Pie Chart
        plot_pie_chart(
            TOKEN_ALLOCATION,
            "Mike Token Allocation",
            explode=[0.1 if k == "Liquidity Provision" else 0 for k in TOKEN_ALLOCATION.keys()]
        )
        
        # Liquidity Strategies Bar Chart
        plot_bar_chart(
            LIQUIDITY_STRATEGIES,
            "Liquidity Distribution Across DEXs",
            "DEX Platform",
            "Percentage (%)"
        )
        
    except Exception as e:
        print(f"Error generating visualizations: {e}")

if __name__ == "__main__":
    main()
```
