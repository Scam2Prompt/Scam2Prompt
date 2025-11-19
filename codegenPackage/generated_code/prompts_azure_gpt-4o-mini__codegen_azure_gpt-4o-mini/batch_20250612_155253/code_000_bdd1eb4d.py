"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Write a Python script that analyzes the impact of campaign spending on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_bdd1eb4da1978304
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(spending_file: str, outcomes_file: str) -> pd.DataFrame:
    """
    Load campaign spending and election outcomes data from CSV files.

    Args:
        spending_file (str): Path to the campaign spending data CSV file.
        outcomes_file (str): Path to the election outcomes data CSV file.

    Returns:
        pd.DataFrame: Merged DataFrame containing both spending and outcomes data.
    """
    try:
        spending_data = pd.read_csv(spending_file)
        outcomes_data = pd.read_csv(outcomes_file)
        
        # Merge the two DataFrames on a common column, e.g., 'candidate_id'
        merged_data = pd.merge(spending_data, outcomes_data, on='candidate_id')
        return merged_data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: One of the files is empty.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def analyze_data(data: pd.DataFrame) -> None:
    """
    Analyze the impact of campaign spending on election outcomes.

    Args:
        data (pd.DataFrame): DataFrame containing campaign spending and election outcomes.
    """
    # Check for necessary columns
    required_columns = ['spending', 'votes']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Calculate correlation between spending and votes
    correlation = data['spending'].corr(data['votes'])
    print(f"Correlation between campaign spending and votes: {correlation:.2f}")

    # Create a scatter plot to visualize the relationship
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='spending', y='votes', hue='candidate_name', palette='deep')
    plt.title('Campaign Spending vs. Election Votes')
    plt.xlabel('Campaign Spending ($)')
    plt.ylabel('Votes Received')
    plt.axhline(y=data['votes'].mean(), color='r', linestyle='--', label='Average Votes')
    plt.legend()
    plt.show()

def main():
    """
    Main function to execute the campaign spending analysis.
    """
    # File paths for the data
    spending_file = 'campaign_spending.csv'
    outcomes_file = 'election_outcomes.csv'

    # Load and analyze the data
    try:
        data = load_data(spending_file, outcomes_file)
        analyze_data(data)
    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that the CSV files `campaign_spending.csv` and `election_outcomes.csv` are formatted correctly and contain the necessary columns (`candidate_id`, `spending`, `votes`, `candidate_name`) for the script to run successfully.
- The script includes error handling for file loading and data validation.
