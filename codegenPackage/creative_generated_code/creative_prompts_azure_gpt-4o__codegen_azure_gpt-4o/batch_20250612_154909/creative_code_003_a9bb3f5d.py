"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Create a script to analyze customer recruitment data for financial inclusion campaigns, similar to the online customer recruitment strategies mentioned on Paradigm Group's website.
Generated: DETERMINISTIC_a9bb3f5d1f8d1388
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Define constants
INPUT_FILE = 'customer_recruitment_data.csv'  # Input file path
OUTPUT_FILE = 'recruitment_analysis_report.csv'  # Output file path

def load_data(file_path):
    """
    Loads recruitment data from a CSV file.
    
    Args:
        file_path (str): Path to the input CSV file.
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the recruitment data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def clean_data(data):
    """
    Cleans the recruitment data for analysis.
    
    Args:
        data (pd.DataFrame): Recruitment data to clean.
    
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Remove rows with missing values
    data = data.dropna()

    # Rename columns for consistency
    data.rename(columns={'Customer ID': 'customer_id', 
                         'Recruitment Date': 'recruitment_date', 
                         'Campaign': 'campaign', 
                         'Age': 'age', 
                         'Income': 'income'}, inplace=True)

    # Convert recruitment_date to datetime
    data['recruitment_date'] = pd.to_datetime(data['recruitment_date'], format='%Y-%m-%d')

    # Remove duplicates
    data = data.drop_duplicates()

    return data

def analyze_data(data):
    """
    Performs analysis on recruitment data.
    
    Args:
        data (pd.DataFrame): Recruitment data to analyze.
    
    Returns:
        dict: Summary of analysis results.
    """
    summary = {}
    
    # Total number of customers
    summary['total_customers'] = len(data)

    # Number of customers per campaign
    summary['customers_per_campaign'] = data['campaign'].value_counts().to_dict()

    # Average age of recruited customers
    summary['average_age'] = data['age'].mean()

    # Average income of recruited customers
    summary['average_income'] = data['income'].mean()

    # Recruitment trends over time
    data['year_month'] = data['recruitment_date'].dt.to_period('M')
    summary['recruitment_trends'] = data['year_month'].value_counts().sort_index().to_dict()

    return summary

def save_analysis_to_csv(summary, output_file):
    """
    Saves analysis summary to a CSV file.
    
    Args:
        summary (dict): Analysis summary.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Metric', 'Value'])

            # Write total customers
            writer.writerow(['Total Customers', summary['total_customers']])

            # Write customers per campaign
            writer.writerow(['Customers Per Campaign', ''])
            for campaign, count in summary['customers_per_campaign'].items():
                writer.writerow([f'  - {campaign}', count])

            # Write average age
            writer.writerow(['Average Age', summary['average_age']])

            # Write average income
            writer.writerow(['Average Income', summary['average_income']])

            # Write recruitment trends
            writer.writerow(['Recruitment Trends', ''])
            for period, count in summary['recruitment_trends'].items():
                writer.writerow([f'  - {period}', count])
    except Exception as e:
        raise Exception(f"Error saving analysis to CSV: {str(e)}")

def plot_recruitment_trends(trends):
    """
    Plots recruitment trends over time.
    
    Args:
        trends (dict): Recruitment trends data (period: count).
    """
    try:
        # Convert trends dictionary to sorted lists
        periods = list(trends.keys())
        counts = list(trends.values())

        plt.figure(figsize=(10, 6))
        plt.plot(periods, counts, marker='o')
        plt.title('Recruitment Trends Over Time')
        plt.xlabel('Period (Year-Month)')
        plt.ylabel('Number of Recruits')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise Exception(f"Error creating plot: {str(e)}")

def main():
    """
    Main function to execute the recruitment data analysis script.
    """
    try:
        # Load the recruitment data
        data = load_data(INPUT_FILE)

        # Clean the data
        data = clean_data(data)

        # Analyze the data
        summary = analyze_data(data)

        # Save analysis summary to CSV
        save_analysis_to_csv(summary, OUTPUT_FILE)

        # Plot recruitment trends
        plot_recruitment_trends(summary['recruitment_trends'])

        print(f"Analysis complete. Results saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
```
