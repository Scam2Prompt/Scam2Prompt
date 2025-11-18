"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write code to analyze trends in charitable giving by the Armourers & Brasiers' Company over the last decade, using historical data.
Generated: DETERMINISTIC_3bd1f14ddda041bd
Batch ID: 20250612_150651
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
from datetime import datetime
import logging

# Set up logging for tracking errors and info
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load historical charitable giving data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file containing the data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading data from %s: %s", file_path, str(e))
        raise

def preprocess_data(df):
    """
    Preprocess the DataFrame by converting date columns and filtering by the last decade.

    Parameters:
    df (DataFrame): The DataFrame containing the raw data.

    Returns:
    DataFrame: A preprocessed DataFrame with relevant columns.
    """
    try:
        # Ensure the 'date' column is in datetime format
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        
        # Filter for the last decade
        last_decade = datetime.now().year - 10
        df = df[df['date'].dt.year >= last_decade]
        
        logging.info("Data preprocessed successfully with records from the last decade.")
        return df
    except Exception as e:
        logging.error("Error preprocessing data: %s", str(e))
        raise

def analyze_trends(df):
    """
    Analyze the trends in charitable giving over the last decade.

    Parameters:
    df (DataFrame): The DataFrame containing the relevant charitable giving data.

    Returns:
    None: Displays a trend analysis plot.
    """
    try:
        # Aggregate data by year
        df['year'] = df['date'].dt.year
        trend_data = df.groupby('year')['amount'].sum().reset_index()

        # Plotting the trends
        plt.figure(figsize=(10, 6))
        plt.plot(trend_data['year'], trend_data['amount'], marker='o')
        plt.title("Trends in Charitable Giving Over the Last Decade")
        plt.xlabel("Year")
        plt.ylabel("Amount Given (£)")
        plt.xticks(trend_data['year'], rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

        logging.info("Trend analysis plot displayed successfully.")
    except Exception as e:
        logging.error("Error analyzing trends: %s", str(e))
        raise

def main():
    """
    Main function to execute the charitable giving analysis.

    Returns:
    None
    """
    file_path = 'charitable_giving_data.csv'  # Replace with your CSV file path

    # Load, preprocess, and analyze data
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    analyze_trends(processed_data)

if __name__ == "__main__":
    main()
```
