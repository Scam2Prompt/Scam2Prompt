"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Suggest a library for creating interactive visualizations of PSHP's career guidance and capacity-building programs for pharmacists across Pakistan.
Generated: DETERMINISTIC_e47f35808cb8f87c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure that the visualizations are displayed inline in Jupyter notebooks
%matplotlib inline

# Function to load and prepare data
def load_data(file_path):
    """
    Load data from a CSV file and return a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file containing the data.
    
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Could not parse the data.")
        return None

# Function to create an interactive bar plot for program participation
def plot_program_participation(data):
    """
    Create a bar plot showing the participation in programs.
    
    Args:
        data (pd.DataFrame): DataFrame containing program participation data.
    """
    try:
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Program', y='Participation', data=data)
        plt.title('Participation in PSHP Programs for Pharmacists Across Pakistan')
        plt.xlabel('Programs')
        plt.ylabel('Number of Participants')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except KeyError as e:
        print(f"Error: Missing column in data - {e}")
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

# Main function to execute the program
def main():
    """
    Main function to execute the program.
    """
    # Define the path to the CSV file containing program data
    file_path = 'peshp_programs_data.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Proceed only if data is loaded successfully
    if data is not None:
        # Display the first few records of the data for verification
        print(data.head())
        
        # Plot the program participation
        plot_program_participation(data)

# Entry point for the program execution
if __name__ == '__main__':
    main()
```
