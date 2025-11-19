"""
Generated Code Metadata:
========================
Original URL: https://altprotocol.pages.dev
Prompt: Create a data analysis script to visualize the tokenomics of $AIT, including token distribution and burn rate, using libraries like Pandas and Matplotlib.
Generated: DETERMINISTIC_aa3b5d0b8df56233
Batch ID: 20250622_211342
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
from matplotlib.ticker import PercentFormatter

# Constants
DATA_FILE = 'ait_tokenomics.csv'
OUTPUT_DIR = 'output/'

def load_data(file_path):
    """
    Load tokenomics data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded tokenomics data.
    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise pd.errors.EmptyDataError("The file is empty.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def validate_data(df):
    """
    Validate the tokenomics data structure.
    Args:
        df (pd.DataFrame): Tokenomics data to validate.
    Raises:
        ValueError: If required columns are missing.
    """
    required_columns = ['category', 'percentage', 'burn_rate']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

def plot_token_distribution(df):
    """
    Plot token distribution pie chart.
    Args:
        df (pd.DataFrame): Tokenomics data with 'category' and 'percentage' columns.
    """
    plt.figure(figsize=(10, 8))
    plt.pie(
        df['percentage'],
        labels=df['category'],
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired.colors
    )
    plt.title('$AIT Token Distribution', fontsize=16)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}token_distribution.png')
    plt.close()

def plot_burn_rate(df):
    """
    Plot burn rate bar chart.
    Args:
        df (pd.DataFrame): Tokenomics data with 'category' and 'burn_rate' columns.
    """
    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    df_sorted = df.sort_values('burn_rate', ascending=False)
    bars = ax.bar(
        df_sorted['category'],
        df_sorted['burn_rate'],
        color='firebrick'
    )
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    plt.title('$AIT Burn Rate by Category', fontsize=16)
    plt.ylabel('Burn Rate (%)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{height:.1%}',
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords='offset points',
            ha='center',
            va='bottom'
        )
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}burn_rate.png')
    plt.close()

def main():
    """
    Main function to execute the tokenomics analysis.
    """
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    try:
        # Load and validate data
        df = load_data(DATA_FILE)
        validate_data(df)
        
        # Generate visualizations
        plot_token_distribution(df)
        plot_burn_rate(df)
        
        print(f"Visualizations saved to {OUTPUT_DIR}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == '__main__':
    main()
```
