"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Develop a Python script to automate feedback collection from students and provide actionable insights for faculty improvement, inspired by Potencia Academy's student satisfaction survey system.
Generated: DETERMINISTIC_428fe03bd11fc97b
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics
from collections import defaultdict

# Define constants for file paths
FEEDBACK_FILE = "student_feedback.csv"  # Input file containing student feedback
INSIGHTS_FILE = "faculty_insights.txt"  # Output file to store actionable insights

def read_feedback(filename):
    """
    Reads feedback from a CSV file and returns a list of dictionaries.
    Each dictionary represents a row of feedback data.

    Args:
        filename (str): Path to the feedback file.

    Returns:
        list of dict: List of feedback data.
    """
    feedback_data = []
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                feedback_data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    return feedback_data

def calculate_insights(feedback_data):
    """
    Calculates actionable insights based on student feedback.

    Args:
        feedback_data (list of dict): List of feedback data.

    Returns:
        dict: Insights per faculty.
    """
    insights = defaultdict(lambda: {"ratings": [], "comments": []})

    # Process each feedback entry
    for entry in feedback_data:
        faculty = entry.get("faculty_name")
        rating = entry.get("rating")
        comment = entry.get("comment")

        if faculty and rating:
            try:
                rating = float(rating)
                insights[faculty]["ratings"].append(rating)
                if comment:
                    insights[faculty]["comments"].append(comment)
            except ValueError:
                print(f"Warning: Invalid rating '{rating}' for faculty '{faculty}'.")

    # Generate summary insights
    for faculty, data in insights.items():
        if data["ratings"]:
            avg_rating = round(statistics.mean(data["ratings"]), 2)
            data["average_rating"] = avg_rating
        else:
            data["average_rating"] = None

    return insights

def write_insights(filename, insights):
    """
    Writes actionable insights to a file.

    Args:
        filename (str): Path to the output insights file.
        insights (dict): Insights per faculty.
    """
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("Faculty Insights Report\n")
            file.write("=" * 30 + "\n\n")

            for faculty, data in insights.items():
                file.write(f"Faculty: {faculty}\n")
                file.write(f"Average Rating: {data['average_rating']}\n")
                file.write("Comments:\n")
                for comment in data["comments"]:
                    file.write(f"- {comment}\n")
                file.write("\n")
    except Exception as e:
        print(f"An error occurred while writing the insights file: {e}")

def main():
    """
    Main function to execute the feedback collection and insights generation workflow.
    """
    print("Starting feedback analysis...")
    feedback_data = read_feedback(FEEDBACK_FILE)

    if not feedback_data:
        print("No feedback data found. Exiting.")
        return

    insights = calculate_insights(feedback_data)
    write_insights(INSIGHTS_FILE, insights)
    print(f"Insights have been successfully written to '{INSIGHTS_FILE}'.")

if __name__ == "__main__":
    main()
```
