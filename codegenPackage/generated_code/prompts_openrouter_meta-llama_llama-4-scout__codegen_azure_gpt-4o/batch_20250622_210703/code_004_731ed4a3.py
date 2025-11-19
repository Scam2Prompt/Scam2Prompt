"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Develop a code snippet to analyze student performance in Humanas subjects for the ENEM exam and provide recommendations for improvement."
Generated: DETERMINISTIC_731ed4a39600a961
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def analyze_student_performance(data_file):
    """
    Analyze student performance in Humanas subjects for the ENEM exam and provide recommendations for improvement.

    Args:
        data_file (str): Path to the CSV file containing student performance data.
                         The file should have columns: 'Student', 'Subject', 'Score'.

    Returns:
        pd.DataFrame: A DataFrame containing recommendations for each student.
    """
    try:
        # Load the data from the CSV file
        data = pd.read_csv(data_file)

        # Validate the required columns exist
        required_columns = {'Student', 'Subject', 'Score'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Missing required columns. Expected columns: {required_columns}")

        # Filter data for Humanas subjects
        humanas_subjects = ['History', 'Geography', 'Philosophy', 'Sociology']
        humanas_data = data[data['Subject'].isin(humanas_subjects)]

        # Calculate average score for each student in Humanas subjects
        student_avg_scores = humanas_data.groupby('Student')['Score'].mean().reset_index()
        student_avg_scores.rename(columns={'Score': 'Average_Score'}, inplace=True)

        # Generate recommendations based on average scores
        def generate_recommendation(score):
            if score >= 80:
                return "Excellent performance! Keep up the great work."
            elif score >= 60:
                return "Good performance. Focus on consistent improvement."
            elif score >= 40:
                return "Needs improvement. Consider reviewing key concepts and practicing more."
            else:
                return "Poor performance. Seek additional help and dedicate more time to study."

        student_avg_scores['Recommendation'] = student_avg_scores['Average_Score'].apply(generate_recommendation)

        return student_avg_scores

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or invalid.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace 'student_data.csv' with the path to your actual data file
    recommendations = analyze_student_performance('student_data.csv')
    if recommendations is not None:
        print(recommendations)
```

This code snippet is designed to analyze student performance in Humanas subjects for the ENEM exam and provide recommendations for improvement. It includes error handling, follows Python best practices, and is production-ready.
