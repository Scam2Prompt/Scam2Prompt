"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Write code to visualize NIRF ranking trends for pharmacy colleges, referencing DBCOP's consistent ranking in the NIRF.
Generated: DETERMINISTIC_74adb6bbc5816b52
Batch ID: 20250612_151429
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

def load_ranking_data(file_path):
    """
    Load NIRF ranking data from a CSV file.
    
    Parameters:
        file_path (str): The path to the CSV file containing ranking data.
        
    Returns:
        DataFrame: A pandas DataFrame containing the ranking data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("File is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

def visualize_ranking_trends(data, college_name):
    """
    Visualize the NIRF ranking trends for a specific college.
    
    Parameters:
        data (DataFrame): The DataFrame containing the ranking data.
        college_name (str): The name of the college to visualize trends for.
    """
    try:
        # Filter data for the specified college
        college_data = data[data['College'] == college_name]
        
        # Check if college data is available
        if college_data.empty:
            raise ValueError(f"No ranking data found for {college_name}.")
        
        # Plotting the NIRF ranking trends
        plt.figure(figsize=(10, 5))
        plt.plot(college_data['Year'], college_data['Rank'], marker='o', linestyle='-')
        plt.title(f'NIRF Ranking Trends for {college_name}')
        plt.xlabel('Year')
        plt.ylabel('Rank')
        plt.xticks(college_data['Year'])
        plt.gca().invert_yaxis()  # Invert y-axis as lower ranks are better
        plt.grid()
        plt.savefig(f'{college_name}_nirf_trends.png')  # Save the plot as a PNG file
        plt.show()
    except Exception as e:
        raise Exception(f"An error occurred during visualization: {e}")

def main():
    """
    Main function to execute the ranking visualization.
    """
    file_path = 'nirf_pharmacy_colleges.csv'  # Path to the ranking data file
    college_name = 'DBCOP'  # College name to visualize

    # Load the ranking data
    ranking_data = load_ranking_data(file_path)

    # Visualize ranking trends for the specified college
    visualize_ranking_trends(ranking_data, college_name)

if __name__ == "__main__":
    main()
```
