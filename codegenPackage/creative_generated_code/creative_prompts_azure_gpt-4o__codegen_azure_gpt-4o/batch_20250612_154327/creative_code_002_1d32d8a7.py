"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakehelp.com
Prompt: Generate Python code to analyze ESG data provided by Medipal Holdings Co., Ltd. and create visualizations for sustainability reporting.
Generated: DETERMINISTIC_1d32d8a73332fc0b
Batch ID: 20250612_154327
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
    Load ESG data from a CSV file.
    :param file_path: Path to the ESG data file.
    :return: Pandas DataFrame containing the data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")

def validate_data(data, required_columns):
    """
    Validate that the required columns are present in the DataFrame.
    :param data: Pandas DataFrame containing the ESG data.
    :param required_columns: List of required column names.
    :return: None
    """
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

def create_visualizations(data):
    """
    Create visualizations for ESG sustainability reporting.
    :param data: Pandas DataFrame containing the ESG data.
    :return: None
    """
    # Visualization: ESG Score Over Time
    if 'Year' in data and 'ESG_Score' in data:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Year', y='ESG_Score', data=data)
        plt.title('ESG Score Over Time')
        plt.xlabel('Year')
        plt.ylabel('ESG Score')
        plt.grid(True)
        plt.savefig('esg_score_over_time.png')
        plt.show()
    else:
        print("Skipping ESG Score Over Time visualization due to missing columns.")

    # Visualization: Distribution of Carbon Emissions
    if 'Carbon_Emissions' in data:
        plt.figure(figsize=(10, 6))
        sns.histplot(data['Carbon_Emissions'], kde=True, bins=20, color='green')
        plt.title('Distribution of Carbon Emissions')
        plt.xlabel('Carbon Emissions')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig('carbon_emissions_distribution.png')
        plt.show()
    else:
        print("Skipping Distribution of Carbon Emissions visualization due to missing column.")

    # Visualization: Breakdown of Energy Usage by Source
    energy_columns = [col for col in data.columns if col.startswith('Energy_')]
    if energy_columns:
        energy_usage = data[energy_columns].mean()
        plt.figure(figsize=(10, 6))
        energy_usage.plot(kind='bar', color='blue')
        plt.title('Average Energy Usage by Source')
        plt.xlabel('Energy Source')
        plt.ylabel('Usage')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.savefig('energy_usage_by_source.png')
        plt.show()
    else:
        print("Skipping Energy Usage visualization due to missing columns.")

def main():
    """
    Main function to load, validate, analyze, and visualize ESG data for Medipal Holdings Co., Ltd.
    :return: None
    """
    # File path to the ESG data CSV file
    file_path = 'medipal_esg_data.csv'

    # Required columns for analysis
    required_columns = ['Year', 'ESG_Score', 'Carbon_Emissions']

    try:
        # Load ESG data
        esg_data = load_data(file_path)

        # Validate loaded data
        validate_data(esg_data, required_columns)

        # Create visualizations for sustainability reporting
        create_visualizations(esg_data)

        print("Visualizations created successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
