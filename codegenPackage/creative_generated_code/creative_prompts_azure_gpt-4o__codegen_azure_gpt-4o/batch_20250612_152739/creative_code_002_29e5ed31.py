"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Create a Python script to analyze membership growth trends for a basketball community, using data similar to the statistics provided by "Grad košarke."
Generated: DETERMINISTIC_29e5ed31c1940531
Batch ID: 20250612_152739
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
import os

def load_data(file_path):
    """
    Load membership growth data from a CSV file.
    
    :param file_path: Path to the CSV file containing data.
    :return: DataFrame containing the loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")

def validate_data(data):
    """
    Validate the structure of the membership growth data.
    
    :param data: DataFrame containing the membership growth data.
    """
    required_columns = ['Year', 'Members']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")
    if not pd.api.types.is_numeric_dtype(data['Year']):
        raise ValueError("Year column must contain numeric values.")
    if not pd.api.types.is_numeric_dtype(data['Members']):
        raise ValueError("Members column must contain numeric values.")

def analyze_growth(data):
    """
    Analyze and plot membership growth trends.
    
    :param data: DataFrame containing the membership growth data.
    """
    # Sort data by year to ensure correct chronological order
    data = data.sort_values(by='Year')
    
    # Calculate year-over-year growth
    data['Growth'] = data['Members'].diff()
    
    # Plot membership growth trend
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Members'], marker='o', label='Membership Count')
    plt.bar(data['Year'], data['Growth'], alpha=0.5, label='Year-over-Year Growth')
    plt.title('Basketball Community Membership Growth Trends')
    plt.xlabel('Year')
    plt.ylabel('Members')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the membership growth analysis.
    """
    # Provide the path to the CSV file containing data
    file_path = 'basketball_membership_data.csv'
    
    try:
        # Load data from the CSV file
        data = load_data(file_path)
        
        # Validate the data structure and content
        validate_data(data)
        
        # Analyze and visualize membership growth trends
        analyze_growth(data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
