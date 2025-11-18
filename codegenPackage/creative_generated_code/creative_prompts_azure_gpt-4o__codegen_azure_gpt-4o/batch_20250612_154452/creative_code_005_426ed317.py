"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Develop a Python script to analyze student performance data from a coaching center like Retina and generate insights for improving preparation strategies.
Generated: DETERMINISTIC_426ed31767939f18
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Define constants for grade thresholds
GRADE_THRESHOLDS = {"A": 90, "B": 80, "C": 70, "D": 60}

def load_data(file_path):
    """
    Load student performance data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing student performance data.
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

def calculate_statistics(data):
    """
    Calculate statistics on student performance.

    Args:
        data (pd.DataFrame): DataFrame containing student performance data.
    
    Returns:
        dict: Dictionary containing calculated statistics.
    """
    try:
        stats = {
            "average_score": np.mean(data["Score"]),
            "median_score": np.median(data["Score"]),
            "max_score": np.max(data["Score"]),
            "min_score": np.min(data["Score"]),
            "standard_deviation": np.std(data["Score"])
        }
        return stats
    except KeyError:
        print("Error: 'Score' column not found in the data.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def assign_grades(data):
    """
    Assign grades to students based on their scores.

    Args:
        data (pd.DataFrame): DataFrame containing student performance data.
    
    Returns:
        pd.DataFrame: DataFrame with an added 'Grade' column.
    """
    def grade(score):
        for grade, threshold in GRADE_THRESHOLDS.items():
            if score >= threshold:
                return grade
        return "F"

    try:
        data["Grade"] = data["Score"].apply(grade)
        return data
    except KeyError:
        print("Error: 'Score' column not found in the data.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def identify_improvement_areas(data):
    """
    Identify areas of improvement based on performance data.

    Args:
        data (pd.DataFrame): DataFrame containing student performance data.
    
    Returns:
        dict: Dictionary containing improvement insights.
    """
    try:
        subject_avg = data.groupby("Subject")["Score"].mean()
        low_performance_subjects = subject_avg[subject_avg < 70]  # Subjects below 70 average
        return {
            "low_performance_subjects": low_performance_subjects.to_dict(),
            "overall_average": np.mean(data["Score"]),
        }
    except KeyError:
        print("Error: Required columns ('Subject', 'Score') not found in the data.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def generate_report(file_path):
    """
    Generate a performance analysis report.

    Args:
        file_path (str): Path to the CSV file containing student data.
    """
    # Load data
    data = load_data(file_path)
    if data is None:
        return
    
    # Calculate statistics
    stats = calculate_statistics(data)
    if stats:
        print("\nPerformance Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    
    # Assign grades
    data_with_grades = assign_grades(data)
    if data_with_grades is not None:
        print("\nStudent Grades Assigned:")
        print(data_with_grades[["Student", "Score", "Grade"]])

    # Identify improvement areas
    insights = identify_improvement_areas(data)
    if insights:
        print("\nImprovement Insights:")
        print("Low Performance Subjects:")
        for subject, avg in insights["low_performance_subjects"].items():
            print(f"{subject}: Avg Score = {avg}")
        print(f"Overall Average Score: {insights['overall_average']}")

# Main execution
if __name__ == "__main__":
    # File path to the CSV containing student data
    FILE_PATH = "student_performance.csv"
    generate_report(FILE_PATH)
```
