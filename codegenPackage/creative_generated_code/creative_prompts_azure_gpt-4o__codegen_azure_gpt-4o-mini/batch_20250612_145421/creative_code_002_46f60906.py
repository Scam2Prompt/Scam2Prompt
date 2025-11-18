"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Generate code using a library like Pandas to visualize data on youth health and social competence, inspired by the objectives of ICYD.org.
Generated: DETERMINISTIC_46f609068e4f236c
Batch ID: 20250612_145421
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

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Loads data from a CSV file into a Pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

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
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

def visualize_youth_health(data):
    """
    Creates visualizations for youth health and social competence data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to visualize.
    """
    if data is None:
        print("No data to visualize.")
        return
    
    # Check if required columns exist in the DataFrame
    required_columns = ['Age', 'Health_Score', 'Social_Competence_Score']
    for column in required_columns:
        if column not in data.columns:
            print(f"Missing required column: {column}")
            return

    # Set up the figure and axes for the plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Histogram of Health Scores
    sns.histplot(data['Health_Score'], bins=10, ax=axes[0], kde=True)
    axes[0].set_title('Distribution of Youth Health Scores')
    axes[0].set_xlabel('Health Score')
    axes[0].set_ylabel('Frequency')

    # Boxplot of Social Competence Scores by Age
    sns.boxplot(x='Age', y='Social_Competence_Score', data=data, ax=axes[1])
    axes[1].set_title('Social Competence Scores by Age')
    axes[1].set_xlabel('Age')
    axes[1].set_ylabel('Social Competence Score')

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data loading and visualization.
    """
    # Define the path to the data file
    file_path = 'youth_health_data.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Visualize the youth health and social competence data
    visualize_youth_health(data)

if __name__ == "__main__":
    main()
```
