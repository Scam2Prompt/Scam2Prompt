"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenafex.com
Prompt: Generate code to visualize Zenafex's market liquidity and fee structure for different prediction categories.
Generated: DETERMINISTIC_a53f83858ecacfb0
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd

def visualize_market_liquidity_and_fee_structure(data):
    """
    Visualizes Zenafex's market liquidity and fee structure for different prediction categories.

    Args:
        data (pd.DataFrame): A DataFrame containing columns 'Category', 'Liquidity', and 'Fee'.

        Example DataFrame structure:
            Category       Liquidity    Fee
            Sports         10000        0.02
            Politics       7500         0.015
            Finance        12000        0.03
    """
    # Input validation
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Expected input data to be a pandas DataFrame.")
    required_columns = {'Category', 'Liquidity', 'Fee'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

    # Set up the plot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar plot for Liquidity
    color_liquidity = 'tab:blue'
    ax1.bar(data['Category'], data['Liquidity'], color=color_liquidity, alpha=0.7, label='Liquidity')
    ax1.set_xlabel('Prediction Category', fontsize=12)
    ax1.set_ylabel('Liquidity (USD)', color=color_liquidity, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color_liquidity)
    ax1.set_title("Market Liquidity and Fee Structure by Category", fontsize=14)

    # Overlay line plot for Fees
    ax2 = ax1.twinx()
    color_fee = 'tab:orange'
    ax2.plot(data['Category'], data['Fee'], color=color_fee, marker='o', label='Fee Structure')
    ax2.set_ylabel('Fee (%)', color=color_fee, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color_fee)

    # Add legends to the plot
    ax1.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)

    # Finalize and show the visual
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create example data
    example_data = pd.DataFrame({
        'Category': ['Sports', 'Politics', 'Finance', 'Entertainment'],
        'Liquidity': [10000, 7500, 12000, 5000],
        'Fee': [0.02, 0.015, 0.03, 0.025]
    })

    try:
        visualize_market_liquidity_and_fee_structure(example_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```
