"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate a Python script to analyze student performance data for a coaching academy like Potencia Academy, focusing on JEE and NEET preparation.
Generated: DETERMINISTIC_ed55983f9662d950
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Define constants for analysis
JEE_SUBJECTS = ['Physics', 'Chemistry', 'Mathematics']
NEET_SUBJECTS = ['Physics', 'Chemistry', 'Biology']
PASS_THRESHOLD = 40  # Minimum passing percentage for each subject

def load_data(file_path):
    """
    Load student performance data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing student data.
        
    Returns:
        pd.DataFrame: DataFrame containing the student data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def validate_data(data):
    """
    Validate the structure and content of the student data.
    
    Args:
        data (pd.DataFrame): DataFrame containing the student data.
        
    Returns:
        bool: True if data is valid, False otherwise.
    """
    required_columns = ['Student_ID', 'Name', 'Exam_Type'] + JEE_SUBJECTS + NEET_SUBJECTS
    missing_columns = [col for col in required_columns if col not in data.columns]
    
    if missing_columns:
        print(f"Error: Missing columns in data: {missing_columns}")
        return False
    
    return True

def analyze_performance(data):
    """
    Analyze student performance based on their exam type (JEE or NEET).
    
    Args:
        data (pd.DataFrame): DataFrame containing the student data.
        
    Returns:
        dict: Dictionary containing analysis results.
    """
    results = {'JEE': {}, 'NEET': {}}
    
    # Filter data by exam type
    jee_data = data[data['Exam_Type'] == 'JEE']
    neet_data = data[data['Exam_Type'] == 'NEET']
    
    # Analyze JEE performance
    if not jee_data.empty:
        results['JEE']['Average_Scores'] = jee_data[JEE_SUBJECTS].mean().to_dict()
        results['JEE']['Pass_Percentage'] = (
            (jee_data[JEE_SUBJECTS] >= PASS_THRESHOLD).all(axis=1).mean() * 100
        )
    
    # Analyze NEET performance
    if not neet_data.empty:
        results['NEET']['Average_Scores'] = neet_data[NEET_SUBJECTS].mean().to_dict()
        results['NEET']['Pass_Percentage'] = (
            (neet_data[NEET_SUBJECTS] >= PASS_THRESHOLD).all(axis=1).mean() * 100
        )
    
    return results

def save_results(results, output_file):
    """
    Save the analysis results to a JSON file.
    
    Args:
        results (dict): Dictionary containing analysis results.
        output_file (str): Path to the output JSON file.
    """
    try:
        import json
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error: Unable to save results to file. {e}")

def main():
    """
    Main function to execute the student performance analysis pipeline.
    """
    # File paths
    input_file = 'student_performance.csv'  # Replace with actual file path
    output_file = 'analysis_results.json'  # Replace with desired output file path
    
    # Load data
    data = load_data(input_file)
    if data is None:
        return
    
    # Validate data
    if not validate_data(data):
        return
    
    # Analyze performance
    results = analyze_performance(data)
    
    # Save results
    save_results(results, output_file)

if __name__ == "__main__":
    main()
```
