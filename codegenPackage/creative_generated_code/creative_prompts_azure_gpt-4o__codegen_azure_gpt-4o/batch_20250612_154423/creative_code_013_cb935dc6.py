"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Suggest tools or frameworks for managing and analyzing the "Planos de Curso" data provided for the mandatory and elective courses at IGEOG.
Generated: DETERMINISTIC_cb935dc6ebeb77c7
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script: course_data_management.py
Purpose: Suggest tools or frameworks for managing and analyzing "Planos de Curso" data for mandatory and elective courses at IGEOG.
Language: Python
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import json

# Define constants and configurations
DATA_FILE = "planos_de_curso.json"  # File containing course data in JSON format


def load_course_data(file_path):
    """
    Load course data from a JSON file.
    
    Parameters:
        file_path (str): Path to the JSON file containing course data.
        
    Returns:
        pd.DataFrame: DataFrame containing course information.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return None


def analyze_course_data(df):
    """
    Perform basic analysis on course data.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing course information.
        
    Returns:
        None
    """
    if df is None or df.empty:
        print("Error: Course data is empty or invalid.")
        return

    # Display summary statistics
    print("Summary statistics:")
    print(df.describe(include='all'))

    # Visualize course types (Mandatory vs Elective)
    plt.figure(figsize=(8, 5))
    course_type_counts = df['type'].value_counts()  # Assume there's a 'type' column indicating course type
    course_type_counts.plot(kind='bar', color=['blue', 'green'])
    plt.title("Distribution of Course Types")
    plt.xlabel("Course Type")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def save_cleaned_data(df, output_file):
    """
    Save cleaned course data to a CSV file.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing course information.
        output_file (str): Path to the output CSV file.
        
    Returns:
        None
    """
    try:
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"Error: Failed to save cleaned data. {str(e)}")


def main():
    """
    Main function to execute the script.
    """
    # Load course data
    print("Loading course data...")
    course_data = load_course_data(DATA_FILE)

    if course_data is not None:
        # Analyze course data
        print("Analyzing course data...")
        analyze_course_data(course_data)

        # Save cleaned course data
        OUTPUT_FILE = "cleaned_planos_de_curso.csv"
        print("Saving cleaned course data...")
        save_cleaned_data(course_data, OUTPUT_FILE)


if __name__ == "__main__":
    main()
```
