"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grants-archive-cf.webflow.io
Prompt: Write a script in R or Python to compare the number of grantees across Gitcoin Grants rounds and generate a bar chart visualization.
Generated: DETERMINISTIC_5019faf691cea775
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script to compare the number of grantees across Gitcoin Grants rounds and generate a bar chart visualization:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data and handle errors
def load_data(file_path):
    """
    Load data from a CSV file and handle potential errors.
    :param file_path: Path to the CSV file
    :return: DataFrame containing the data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

# Function to validate and preprocess data
def preprocess_data(data):
    """
    Validate and preprocess the data.
    :param data: DataFrame containing the data
    :return: Preprocessed DataFrame
    """
    required_columns = ['round', 'grantee']
    for column in required_columns:
        if column not in data.columns:
            print(f"Error: Missing required column '{column}' in the data")
            exit(1)

    # Ensure there are no missing values in required columns
    if data[required_columns].isnull().any().any():
        print("Error: Data contains missing values in required columns")
        exit(1)

    return data

# Function to visualize the number of grantees per round
def visualize_grantees(data):
    """
    Generate a bar chart comparing the number of grantees across Gitcoin Grants rounds.
    :param data: DataFrame containing the data
    """
    # Aggregate data to count grantees per round
    grantee_counts = data.groupby('round')['grantee'].nunique()

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    grantee_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Number of Grantees Across Gitcoin Grants Rounds', fontsize=16)
    plt.xlabel('Round', fontsize=14)
    plt.ylabel('Number of Grantees', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the chart to a file
    plt.savefig('grantees_per_round.png')
    plt.show()

# Main function
def main():
    """
    Main function to execute the script.
    """
    # Replace 'gitcoin_grants_data.csv' with the actual path to your data file
    file_path = 'gitcoin_grants_data.csv'

    # Load and preprocess the data
    data = load_data(file_path)
    data = preprocess_data(data)

    # Generate the visualization
    visualize_grantees(data)

# Entry point of the script
if __name__ == '__main__':
    main()
```

Ensure you have a CSV file named `gitcoin_grants_data.csv` with the following columns:
- `round` (representing the Gitcoin Grants round)
- `grantee` (unique identifier for each grantee)

You can modify the `file_path` variable to match the location of your dataset.
