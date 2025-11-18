"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Recommend tools or libraries to visualize the intake capacity and merit-wise student admission data for MIMSR's UG and PG programs.
Generated: DETERMINISTIC_be8022495b5d7ab1
Batch ID: 20250612_152109
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

# Function to load and prepare data
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load student admission data from a CSV file.
    
    Parameters:
    - file_path: str - The path to the CSV file containing admission data.

    Returns:
    - pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: Error parsing the data.")
        raise


# Function to visualize intake capacity
def visualize_intake_capacity(data: pd.DataFrame):
    """
    Visualize the intake capacity of UG and PG programs.

    Parameters:
    - data: pd.DataFrame - The DataFrame containing admission data.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Program', y='Intake Capacity', data=data)
    plt.title('Intake Capacity of UG and PG Programs')
    plt.xlabel('Programs')
    plt.ylabel('Intake Capacity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Function to visualize merit-wise admission data
def visualize_merit_data(data: pd.DataFrame):
    """
    Visualize merit-wise student admission data.

    Parameters:
    - data: pd.DataFrame - The DataFrame containing admission data.
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Program', y='Merit Score', data=data)
    plt.title('Merit-wise Student Admission Data for UG and PG Programs')
    plt.xlabel('Programs')
    plt.ylabel('Merit Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main function to run the visualizations
def main():
    """
    Main function to load data and generate visualizations.
    """
    file_path = 'admission_data.csv'  # Update with your data file path
    try:
        # Load the admission data
        admission_data = load_data(file_path)
        
        # Visualize intake capacity
        visualize_intake_capacity(admission_data)
        
        # Visualize merit-wise admission data
        visualize_merit_data(admission_data)
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
