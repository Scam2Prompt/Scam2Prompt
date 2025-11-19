"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: How can I use data visualization libraries to showcase the impact of youth development programs in Iowa, as outlined by ICYD?
Generated: DETERMINISTIC_a4fdc7602e6e0f4b
Batch ID: 20250612_162251
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

def load_data(filepath):
    """
    Load youth development program data from a CSV file.
    
    Args:
    - filepath (str): The path to the CSV file containing the data.
    
    Returns:
    - DataFrame: A pandas DataFrame containing the loaded data.
    
    Raises:
    - FileNotFoundError: If the file does not exist.
    - pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file {filepath} was not found.")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise

def visualize_program_impact(data):
    """
    Visualize the impact of youth development programs using seaborn and matplotlib.
    
    Args:
    - data (DataFrame): Data containing information about youth programs and their impact.
    """
    # Set the aesthetics for the plots
    sns.set(style="whitegrid")

    # Create a bar plot for the impact of each program
    plt.figure(figsize=(12, 6))
    program_impact = data.groupby('Program')['Impact Score'].mean().reset_index()
    
    # Plotting the average impact score for each program
    sns.barplot(x='Impact Score', y='Program', data=program_impact, palette='viridis')
    
    # Adding titles and labels
    plt.title('Average Impact Score of Youth Development Programs in Iowa', fontsize=16)
    plt.xlabel('Average Impact Score', fontsize=14)
    plt.ylabel('Youth Development Program', fontsize=14)
    
    # Display the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data loading and visualization of youth development programs.
    """
    # Filepath to the CSV data
    filepath = 'youth_development_programs_iowa.csv'
    
    # Load data
    try:
        data = load_data(filepath)
        # Visualize the impact of the programs
        visualize_program_impact(data)
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")

if __name__ == "__main__":
    main()
```

Make sure to have a data file named `youth_development_programs_iowa.csv` in the same directory or update the `filepath` variable with the correct path to your data file. Ensure that the CSV contains at least two columns: `Program` and `Impact Score`.
