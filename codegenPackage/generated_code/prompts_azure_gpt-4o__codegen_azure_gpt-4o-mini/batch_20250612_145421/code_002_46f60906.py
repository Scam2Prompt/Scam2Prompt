"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Generate code using a library like Pandas to visualize data on youth health and social competence, inspired by the objectives of ICYD.org.
Generated: DETERMINISTIC_46f609068e4f236c
Batch ID: 20250612_145421
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

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing youth health and social competence data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None

def visualize_data(data):
    """
    Visualize the youth health and social competence data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to visualize.
    """
    if data is None or data.empty:
        print("No data to visualize.")
        return

    # Create a pairplot to visualize relationships between variables
    try:
        sns.pairplot(data, hue='Social_Competence', diag_kind='kde')
        plt.title('Pairplot of Youth Health and Social Competence')
        plt.show()
    except Exception as e:
        print(f"An error occurred while visualizing data: {e}")

def main():
    """
    Main function to execute the data loading and visualization process.
    """
    # Specify the path to the CSV file
    file_path = 'youth_health_social_competence.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Visualize the data
    visualize_data(data)

if __name__ == "__main__":
    main()
```
