"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write a Python script to analyze demographic data and identify trends in youth engagement programs, referencing initiatives like those described by ICYD.org.
Generated: DETERMINISTIC_2f45426282a34326
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
from typing import List

# Function to load demographic data from a CSV file
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load demographic data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty. Please provide a valid CSV file.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

# Function to clean the data
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the demographic data by removing missing values and duplicates.

    Args:
        data (pd.DataFrame): The raw demographic data.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    data = data.dropna()  # Remove rows with missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    return data

# Function to analyze trends in youth engagement programs
def analyze_trends(data: pd.DataFrame, age_range: List[int]) -> pd.DataFrame:
    """
    Analyze trends in youth engagement based on age demographics.

    Args:
        data (pd.DataFrame): The cleaned demographic data.
        age_range (List[int]): Age range to filter data (e.g., [10, 24]).

    Returns:
        pd.DataFrame: Filtered data for the specified age range.
    """
    # Ensure the data contains the required columns
    if 'Age' not in data.columns or 'Program Participation' not in data.columns:
        raise KeyError("Required columns 'Age' and 'Program Participation' not found in the data.")
    
    # Filter data for the specified age range
    filtered_data = data[(data['Age'] >= age_range[0]) & (data['Age'] <= age_range[1])]
    
    # Group by Program Participation and count occurrences
    trends = filtered_data.groupby('Program Participation').size().reset_index(name='Count')
    return trends

# Function to visualize trends
def visualize_trends(trends: pd.DataFrame, title: str):
    """
    Visualize trends in youth engagement as a bar chart.

    Args:
        trends (pd.DataFrame): Data containing program participation trends.
        title (str): Title for the chart.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(trends['Program Participation'], trends['Count'], color='skyblue')
    plt.title(title, fontsize=16)
    plt.xlabel('Program Participation', fontsize=14)
    plt.ylabel('Number of Participants', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()

# Main function to execute the script
def main():
    """
    Main function to run the demographic data analysis and trend identification.
    """
    try:
        # File path to the demographic data CSV
        file_path = 'demographic_data.csv'
        
        # Load the data
        raw_data = load_data(file_path)
        
        # Clean the data
        cleaned_data = clean_data(raw_data)
        
        # Analyze trends for youth age range (e.g., 10 to 24 years old)
        age_range = [10, 24]
        trends = analyze_trends(cleaned_data, age_range)
        
        # Display trends
        print("Youth Engagement Trends:")
        print(trends)
        
        # Visualize trends
        visualize_trends(trends, title="Youth Engagement Program Trends")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
