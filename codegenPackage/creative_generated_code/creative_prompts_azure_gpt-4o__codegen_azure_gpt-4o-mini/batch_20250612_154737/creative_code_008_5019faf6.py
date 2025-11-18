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

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_grant_data(file_path):
    """
    Load grant data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing grant data.

    Returns:
    pd.DataFrame: A DataFrame containing the grant data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def count_grantees_per_round(data):
    """
    Count the number of grantees for each grant round.

    Parameters:
    data (pd.DataFrame): The DataFrame containing grant data.

    Returns:
    pd.Series: A Series with the count of grantees indexed by grant round.
    """
    if 'round' not in data.columns or 'grantee' not in data.columns:
        raise ValueError("Data must contain 'round' and 'grantee' columns.")
    
    # Group by 'round' and count unique 'grantee' entries
    return data.groupby('round')['grantee'].nunique()

def plot_grantee_counts(grantee_counts):
    """
    Plot a bar chart of the number of grantees per grant round.

    Parameters:
    grantee_counts (pd.Series): The counts of grantees indexed by round.
    """
    plt.figure(figsize=(10, 6))
    grantee_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Grantees per Gitcoin Grant Round')
    plt.xlabel('Grant Round')
    plt.ylabel('Number of Grantees')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grantee_counts.png')  # Save the figure for production use
    plt.show()

def main():
    # Path to the CSV file containing the grant data
    file_path = 'gitcoin_grants.csv'
    
    # Load grant data
    grant_data = load_grant_data(file_path)
    
    # Count the number of grantees per round
    grantee_counts = count_grantees_per_round(grant_data)
    
    # Plot the results
    plot_grantee_counts(grantee_counts)

if __name__ == "__main__":
    main()
```
