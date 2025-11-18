"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaddow.co
Prompt: Write code to analyze historical monthly volume data from the Shadow Exchange and visualize trends using a graphing library like Matplotlib.
Generated: DETERMINISTIC_25b9e104d4db19f0
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load historical monthly volume data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing data.

    Returns:
        pd.DataFrame: A DataFrame containing the historical monthly volume data.
    """
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        
        # Validate required columns are present
        if 'Date' not in data.columns or 'Volume' not in data.columns:
            raise ValueError("CSV file must contain 'Date' and 'Volume' columns.")
        
        # Convert 'Date' column to datetime
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        
        # Drop rows with invalid or missing dates
        data = data.dropna(subset=['Date'])
        
        # Ensure 'Volume' column contains numeric data
        data['Volume'] = pd.to_numeric(data['Volume'], errors='coerce')
        
        # Drop rows with invalid or missing volume
        data = data.dropna(subset=['Volume'])
        
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def plot_volume_trends(data: pd.DataFrame):
    """
    Visualize trends in the historical monthly volume data using Matplotlib.

    Args:
        data (pd.DataFrame): DataFrame containing 'Date' and 'Volume' columns.
    """
    try:
        # Sort data by date to ensure proper visualization
        data = data.sort_values(by='Date')
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        plt.plot(data['Date'], data['Volume'], marker='o', label='Volume Trend', color='blue')
        
        # Add labels, title, and legend
        plt.title("Historical Monthly Volume Trends (Shadow Exchange)", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Volume", fontsize=14)
        plt.legend(loc='upper left', fontsize=12)
        
        # Improve date formatting on the x-axis
        plt.xticks(rotation=45)
        
        # Add gridlines for better readability
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # Display the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating plot: {e}")
        raise

def main():
    """
    Main function to load data, analyze trends, and visualize results.
    """
    # File path to the CSV containing historical monthly volume data
    file_path = "historical_volume_data.csv"  # Replace with the actual file path
    
    try:
        # Load the data
        data = load_data(file_path)
        
        # Visualize the trends
        plot_volume_trends(data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
