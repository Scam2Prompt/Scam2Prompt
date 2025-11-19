"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Develop a Python script to analyze student performance data from a coaching center like Retina and generate insights for improving preparation strategies.
Generated: DETERMINISTIC_426ed31767939f18
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_performance_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load student performance data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

def analyze_performance(data):
    """
    Analyze student performance data.

    Args:
        data (pd.DataFrame): Student performance data.

    Returns:
        dict: Insights and statistics.
    """
    insights = {}

    # Calculate overall pass percentage
    total_students = len(data)
    passed_students = len(data[data['result'] == 'pass'])
    pass_percentage = (passed_students / total_students) * 100
    insights['pass_percentage'] = pass_percentage

    # Calculate average score
    average_score = data['score'].mean()
    insights['average_score'] = average_score

    # Identify top 3 subjects with highest average scores
    subject_avg_scores = data.groupby('subject')['score'].mean().sort_values(ascending=False).head(3)
    insights['top_subjects'] = subject_avg_scores

    # Identify bottom 3 subjects with lowest average scores
    bottom_subjects = data.groupby('subject')['score'].mean().sort_values(ascending=True).head(3)
    insights['bottom_subjects'] = bottom_subjects

    return insights

def visualize_performance(data):
    """
    Visualize student performance data.

    Args:
        data (pd.DataFrame): Student performance data.
    """
    # Plot histogram of scores
    plt.hist(data['score'], bins=10, edgecolor='black')
    plt.title('Distribution of Scores')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.show()

    # Plot bar chart of subject-wise average scores
    subject_avg_scores = data.groupby('subject')['score'].mean()
    plt.bar(subject_avg_scores.index, subject_avg_scores.values)
    plt.title('Subject-wise Average Scores')
    plt.xlabel('Subject')
    plt.ylabel('Average Score')
    plt.show()

def main():
    file_path = 'student_performance_data.csv'  # replace with your file path
    data = load_data(file_path)

    if data is not None:
        insights = analyze_performance(data)
        print("Insights:")
        print(f"Pass Percentage: {insights['pass_percentage']:.2f}%")
        print(f"Average Score: {insights['average_score']:.2f}")
        print("Top 3 Subjects with Highest Average Scores:")
        print(insights['top_subjects'])
        print("Bottom 3 Subjects with Lowest Average Scores:")
        print(insights['bottom_subjects'])

        visualize_performance(data)

if __name__ == "__main__":
    main()
```
