"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Write a Python script to analyze the impact of campaign spending on election outcomes using data from McHenry County, Illinois, as described on Fair Maps Illinois.
Generated: DETERMINISTIC_6ff28388426027fd
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze the impact of campaign spending on election outcomes using data from McHenry County, Illinois.

Author: [Your Name]
Date: [Insert Date]

Dependencies:
    - pandas
    - matplotlib
    - numpy
    
Ensure that you have the required dataset in CSV format (e.g., 'mchenry_campaign_data.csv') 
with the following columns:
    - 'Candidate'
    - 'Campaign_Spending' (in USD)
    - 'Votes_Received'
    - 'Party'
    - 'Election_Year'
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define constants
DATA_FILE = "mchenry_campaign_data.csv"  # Path to the dataset file

def load_data(file_path):
    """
    Load election data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file containing campaign data.

    Returns:
        pd.DataFrame: DataFrame containing the election data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The dataset file is empty.")
        exit(1)
    except pd.errors.ParserError:
        print("Error: The dataset file contains invalid formatting.")
        exit(1)

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and filtering relevant columns.

    Args:
        data (pd.DataFrame): Original election data.

    Returns:
        pd.DataFrame: Preprocessed election data.
    """
    # Drop rows with missing values
    data = data.dropna(subset=['Candidate', 'Campaign_Spending', 'Votes_Received', 'Party', 'Election_Year'])

    # Convert Campaign_Spending and Votes_Received to numeric
    data['Campaign_Spending'] = pd.to_numeric(data['Campaign_Spending'], errors='coerce')
    data['Votes_Received'] = pd.to_numeric(data['Votes_Received'], errors='coerce')

    # Drop rows with invalid numeric entries
    data = data.dropna(subset=['Campaign_Spending', 'Votes_Received'])

    return data

def analyze_spending_vs_outcome(data):
    """
    Analyze the relationship between campaign spending and election outcomes.

    Args:
        data (pd.DataFrame): Preprocessed election data.

    Returns:
        None
    """
    # Group data by Election Year to observe trends over time
    grouped = data.groupby('Election_Year')

    for year, group in grouped:
        print(f"Analyzing data for Election Year: {year}")
        
        # Scatter plot for Campaign Spending vs Votes Received
        plt.figure(figsize=(10, 6))
        plt.scatter(group['Campaign_Spending'], group['Votes_Received'], alpha=0.7, label=f'{year}')
        plt.title(f"Campaign Spending vs Votes Received ({year})")
        plt.xlabel("Campaign Spending (USD)")
        plt.ylabel("Votes Received")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Correlation analysis
        correlation = group['Campaign_Spending'].corr(group['Votes_Received'])
        print(f"Correlation between Campaign Spending and Votes Received in {year}: {correlation:.2f}")

def visualize_spending_distribution(data):
    """
    Visualize the distribution of campaign spending across all candidates.

    Args:
        data (pd.DataFrame): Preprocessed election data.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data['Campaign_Spending'], bins=20, color='blue', alpha=0.7)
    plt.title("Distribution of Campaign Spending")
    plt.xlabel("Campaign Spending (USD)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to execute the script.
    """
    print("Loading data...")
    data = load_data(DATA_FILE)
    
    print("Preprocessing data...")
    data = preprocess_data(data)
    
    print("Analyzing campaign spending vs election outcomes...")
    analyze_spending_vs_outcome(data)
    
    print("Visualizing spending distribution...")
    visualize_spending_distribution(data)

    print("Analysis complete.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
