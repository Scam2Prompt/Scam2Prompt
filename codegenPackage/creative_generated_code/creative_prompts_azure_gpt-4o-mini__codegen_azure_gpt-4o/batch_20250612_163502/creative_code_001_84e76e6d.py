"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tornado.army
Prompt: Can you provide a code snippet for visualizing tornado data using a specific library mentioned on tornado.army?
Generated: DETERMINISTIC_84e76e6d21663dd3
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tornado Data Visualization using matplotlib and pandas

This script visualizes tornado data using Python.
It assumes data is provided in CSV format and includes fields like 
latitude, longitude, magnitude, and date.

Make sure you have matplotlib and pandas installed: `pip install matplotlib pandas`
Replace 'your_tornado_data.csv' with the actual CSV file path.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Function to load and process tornado data
def load_tornado_data(file_path):
    """
    Load tornado data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing tornado data.

    Returns:
        pd.DataFrame: Processed dataframe.
    """
    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Ensure required columns exist
        required_columns = ['latitude', 'longitude', 'magnitude', 'date']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")
        
        # Convert date column to datetime format
        df['date'] = pd.to_datetime(df['date'])

        return df
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        raise
    except Exception as e:
        print(f"Error loading tornado data: {e}")
        raise

# Function to visualize tornado data
def visualize_tornado_data(data):
    """
    Visualizes tornado data on a scatter plot.

    Args:
        data (pd.DataFrame): Tornado data containing latitude, longitude, and magnitude.
    """
    try:
        # Create a scatter plot of tornado locations, color-coded by magnitude
        plt.figure(figsize=(10, 8))
        scatter = plt.scatter(
            data['longitude'], 
            data['latitude'], 
            c=data['magnitude'], 
            cmap='viridis', 
            s=50, 
            alpha=0.75
        )
        plt.colorbar(scatter, label='Magnitude')
        plt.title('Tornado Data Visualization')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)

        # Display the plot
        plt.show()
    except KeyError as e:
        print(f"Error: Missing required column for visualization: {e}")
        raise
    except Exception as e:
        print(f"Error visualizing tornado data: {e}")
        raise

def main():
    """
    Main function to execute the tornado data visualization.
    """
    # Path to the CSV file containing tornado data
    file_path = 'your_tornado_data.csv'
    
    # Load tornado data
    tornado_data = load_tornado_data(file_path)
    
    # Visualize tornado data
    visualize_tornado_data(tornado_data)

if __name__ == "__main__":
    main()
```
