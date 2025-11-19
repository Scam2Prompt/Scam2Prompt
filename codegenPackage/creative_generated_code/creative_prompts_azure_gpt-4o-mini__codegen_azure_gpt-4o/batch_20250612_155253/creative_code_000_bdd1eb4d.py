"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Write a Python script that analyzes the impact of campaign spending on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_bdd1eb4da1978304
Batch ID: 20250612_155253
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
import seaborn as sns
import os

def load_data(file_path):
    """
    Load campaign spending and election outcome data from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: DataFrame containing the loaded data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File at {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File at {file_path} could not be parsed. Ensure it is a properly formatted CSV.")
        return None

def preprocess_data(data):
    """
    Preprocess the data for analysis. This includes handling missing values and renaming columns.
    
    :param data: DataFrame containing the raw data
    :return: Cleaned DataFrame
    """
    # Drop rows where important fields are missing
    data = data.dropna(subset=['Campaign Spending', 'Votes Received', 'Outcome'])
    
    # Convert columns to appropriate data types
    try:
        data['Campaign Spending'] = pd.to_numeric(data['Campaign Spending'], errors='coerce')
        data['Votes Received'] = pd.to_numeric(data['Votes Received'], errors='coerce')
    except Exception as e:
        print(f"Error during data type conversion: {e}")
        return None
    
    # Remove rows with invalid data
    data = data.dropna(subset=['Campaign Spending', 'Votes Received'])
    
    # Standardize column names (if necessary)
    data.rename(columns={
        'Campaign Spending': 'campaign_spending',
        'Votes Received': 'votes_received',
        'Outcome': 'outcome'
    }, inplace=True)
    
    return data

def analyze_data(data):
    """
    Analyze the relationship between campaign spending and election outcomes.

    :param data: Preprocessed DataFrame
    :return: Summary statistics and visualization
    """
    # Generate summary statistics
    summary = data.groupby('outcome')['campaign_spending'].mean()
    print("Average Campaign Spending by Outcome:")
    print(summary)
    
    # Visualization: Scatter plot of Campaign Spending vs Votes Received
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='campaign_spending', y='votes_received', hue='outcome', data=data)
    plt.title('Impact of Campaign Spending on Votes Received')
    plt.xlabel('Campaign Spending ($)')
    plt.ylabel('Votes Received')
    plt.legend(title='Outcome')
    plt.show()

def main():
    """
    Main function to drive the script.
    """
    # Define the file path for the dataset
    file_path = 'mchenry_county_election_data.csv'
    
    # Ensure the file exists before proceeding
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please provide a valid file.")
        return
    
    # Load the data
    data = load_data(file_path)
    if data is None:
        return
    
    # Preprocess the data
    cleaned_data = preprocess_data(data)
    if cleaned_data is None:
        return
    
    # Analyze the data
    analyze_data(cleaned_data)

if __name__ == "__main__":
    main()
```
