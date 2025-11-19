"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Develop a script to visualize the historical production trends of TPCPLC, including key events like nationalization in 1978 and privatization in 1998.
Generated: DETERMINISTIC_f078322205f2a07d
Batch ID: 20250612_154513
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
import matplotlib.dates as mdates
from datetime import datetime

def load_and_prepare_data(filepath):
    """
    Load and prepare the production data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file containing production data.
        
    Returns:
        pandas.DataFrame: Prepared DataFrame with datetime index and production data.
    """
    try:
        # Load data with date parsing
        df = pd.read_csv(filepath, parse_dates=['Date'], dayfirst=True)
        df.set_index('Date', inplace=True)
        df.sort_index(inplace=True)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found at {filepath}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def plot_production_trends(data, title="TPCPLC Historical Production Trends"):
    """
    Plot production trends with key events marked.
    
    Args:
        data (pandas.DataFrame): DataFrame containing production data.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(12, 6))
    
    # Plot production data
    plt.plot(data.index, data['Production'], label='Production', color='blue')
    
    # Add key events
    nationalization_date = datetime(1978, 1, 1)
    privatization_date = datetime(1998, 1, 1)
    
    plt.axvline(x=nationalization_date, color='red', linestyle='--', 
                label='Nationalization (1978)')
    plt.axvline(x=privatization_date, color='green', linestyle='--', 
                label='Privatization (1998)')
    
    # Formatting
    plt.title(title, fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Production (units)', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Format x-axis to show years
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Load data (replace with actual file path)
        data = load_and_prepare_data('tpcplc_production_data.csv')
        
        # Plot trends
        plot_production_trends(data)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
