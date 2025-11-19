"""
Generated Code Metadata:
========================
Original URL: https://viafuar.com
Prompt: Suggest a library for visualizing visitor statistics for events like the Tuzla Boat Show, emphasizing data from multiple countries and years.
Generated: DETERMINISTIC_bb7e568bded412c9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for better visualization
sns.set(style="whitegrid")

def load_and_prepare_data(file_path):
    """
    Load and prepare the visitor statistics data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing visitor data.
        
    Returns:
        pd.DataFrame: Cleaned and prepared DataFrame.
    """
    try:
        # Load data
        df = pd.read_csv(file_path)
        
        # Convert date column to datetime if exists
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        
        # Ensure necessary columns exist
        required_columns = ['country', 'year', 'visitors']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Required column '{col}' not found in data")
                
        return df
    
    except FileNotFoundError:
        raise FileNotFoundError("Data file not found. Please check the file path.")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def plot_visitor_statistics(df, output_file=None):
    """
    Generate visualizations for visitor statistics by country and year.
    
    Args:
        df (pd.DataFrame): Prepared DataFrame with visitor data.
        output_file (str, optional): Path to save the plot. If None, plot is displayed.
    """
    try:
        # Create figure with subplots
        plt.figure(figsize=(15, 8))
        
        # Plot 1: Total visitors by country
        plt.subplot(1, 2, 1)
        sns.barplot(
            x='visitors', 
            y='country', 
            data=df.groupby('country')['visitors'].sum().reset_index().sort_values('visitors', ascending=False),
            palette='viridis'
        )
        plt.title('Total Visitors by Country')
        plt.xlabel('Total Visitors')
        plt.ylabel('Country')
        
        # Plot 2: Visitors by country and year
        plt.subplot(1, 2, 2)
        sns.lineplot(
            x='year', 
            y='visitors', 
            hue='country', 
            data=df,
            marker='o',
            palette='tab20',
            linewidth=2.5
        )
        plt.title('Visitor Trends by Country and Year')
        plt.xlabel('Year')
        plt.ylabel('Visitors')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, bbox_inches='tight', dpi=300)
            print(f"Plot saved to {output_file}")
        else:
            plt.show()
            
    except Exception as e:
        raise Exception(f"Error generating plots: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Load and prepare data
        data = load_and_prepare_data("visitor_statistics.csv")
        
        # Generate and save visualization
        plot_visitor_statistics(data, output_file="visitor_stats_visualization.png")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
