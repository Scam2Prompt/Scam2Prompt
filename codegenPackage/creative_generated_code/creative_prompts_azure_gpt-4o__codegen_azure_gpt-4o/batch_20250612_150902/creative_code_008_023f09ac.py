"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Write code to analyze and visualize data from occupational health examinations, including psychological evaluations and electromyography results, as outlined on Medicid IPS's website.
Generated: DETERMINISTIC_023f09ac40b83d5e
Batch ID: 20250612_150902
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


def load_data(file_path):
    """
    Loads data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file containing occupational health examination data.
    
    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please check the contents.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def preprocess_data(data):
    """
    Cleans and preprocesses the data for analysis.
    
    Args:
        data (pd.DataFrame): The DataFrame containing occupational health examination data.
    
    Returns:
        pd.DataFrame: A cleaned and preprocessed DataFrame.
    """
    if data is None:
        print("Error: Data is None. Preprocessing skipped.")
        return None
    
    # Dropping rows with missing values
    data = data.dropna()
    
    # Ensuring proper data types for columns
    if 'Age' in data.columns:
        data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
    if 'Electromyography_Result' in data.columns:
        data['Electromyography_Result'] = pd.to_numeric(data['Electromyography_Result'], errors='coerce')
    
    # Dropping rows with invalid data
    data = data.dropna()
    
    return data


def visualize_data(data):
    """
    Visualizes the data using plots.
    
    Args:
        data (pd.DataFrame): The DataFrame containing occupational health examination data.
    """
    if data is None or data.empty:
        print("Error: Data is None or empty. Visualization skipped.")
        return
    
    # Visualizing age distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'], bins=20, kde=True, color='blue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Visualizing electromyography results
    if 'Electromyography_Result' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data['Electromyography_Result'], bins=20, kde=True, color='green')
        plt.title('Electromyography Result Distribution')
        plt.xlabel('Electromyography Result')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    # Visualizing psychological evaluation scores
    if 'Psychological_Evaluation_Score' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data['Psychological_Evaluation_Score'], color='orange')
        plt.title('Psychological Evaluation Score Distribution')
        plt.xlabel('Score')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    """
    Main function to execute data analysis and visualization.
    """
    # Specify the path to the data file (update this to the actual path)
    file_path = "occupational_health_examination_data.csv"
    
    # Step 1: Load the data
    data = load_data(file_path)
    
    if data is None:
        return
    
    # Step 2: Preprocess the data
    data = preprocess_data(data)
    
    if data is None or data.empty:
        print("Error: Preprocessed data is None or empty. Exiting.")
        return
    
    # Step 3: Visualize the data
    visualize_data(data)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
