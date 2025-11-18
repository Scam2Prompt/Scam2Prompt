"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dclinvest-sa.com
Prompt: Develop a program to track and visualize global investment trends in transformative technologies, reflecting DCL Invest SA's focus on directing assets toward innovation and sustainable development.
Generated: DETERMINISTIC_d72eb236cab03fd8
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/global_investment_trends.csv": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Constants
DATA_SOURCE_URL = "https://example.com/global_investment_trends.csv"  # Replace with the actual data source URL
OUTPUT_FILE = "investment_trends.csv"

# Function to fetch and load investment data
def fetch_investment_data(url):
    """
    Fetches investment data from the specified URL.

    Parameters:
        url (str): The URL to fetch the CSV data from.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the investment data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        with open(OUTPUT_FILE, 'wb') as file:
            file.write(response.content)
        
        # Load the data into a DataFrame
        df = pd.read_csv(OUTPUT_FILE)
        return df
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to clean and preprocess the data
def preprocess_data(df):
    """
    Cleans and preprocesses the investment data.

    Parameters:
        df (pd.DataFrame): Raw investment data.

    Returns:
        pd.DataFrame: Preprocessed investment data.
    """
    try:
        # Remove any rows with missing values
        df = df.dropna()

        # Ensure date column is in the correct format
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df = df.dropna(subset=['Date'])  # Remove rows with invalid dates

        # Filter relevant columns (e.g., Date, Region, Sector, Investment Amount)
        relevant_columns = ['Date', 'Region', 'Sector', 'Investment_Amount']
        df = df[relevant_columns]

        return df
    except KeyError as e:
        print(f"Missing expected column: {e}")
        return None
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Function to visualize the data
def visualize_trends(df):
    """
    Generates visualizations for investment trends.

    Parameters:
        df (pd.DataFrame): Preprocessed investment data.

    Returns:
        None
    """
    try:
        # Group by sector and sum investments for visualization
        sector_data = df.groupby('Sector')['Investment_Amount'].sum().sort_values(ascending=False)

        # Create a bar chart for sector-wise investment
        plt.figure(figsize=(10, 6))
        sector_data.plot(kind='bar', color='skyblue')
        plt.title('Global Investment Trends by Sector')
        plt.xlabel('Sector')
        plt.ylabel('Investment Amount (in USD)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating visualization: {e}")

# Main program
def main():
    """
    Main function to execute the investment tracking and visualization program.

    Returns:
        None
    """
    print("Fetching investment data...")
    data = fetch_investment_data(DATA_SOURCE_URL)

    if data is not None:
        print("Preprocessing data...")
        clean_data = preprocess_data(data)

        if clean_data is not None:
            print("Visualizing trends...")
            visualize_trends(clean_data)
        else:
            print("Failed to preprocess data.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
```
