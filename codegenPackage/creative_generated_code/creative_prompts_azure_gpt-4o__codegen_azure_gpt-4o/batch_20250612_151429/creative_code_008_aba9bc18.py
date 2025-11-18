"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Generate a Python script to process feedback analysis reports for pharmacy education quality improvement, inspired by DBCOP's Feedback Mechanism.
Generated: DETERMINISTIC_aba9bc189f42cc20
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import json
from statistics import mean

# Define constants
INPUT_FOLDER = "feedback_reports"
OUTPUT_FILE = "processed_feedback_summary.json"

def process_feedback(input_folder, output_file):
    """
    Process feedback analysis reports and generate a summary JSON file.
    
    Args:
        input_folder (str): Path to the folder containing feedback CSV files.
        output_file (str): Path to save the processed feedback summary file (JSON).
    
    Returns:
        None
    """
    feedback_data = {}
    
    try:
        # Check if the input folder exists
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Input folder '{input_folder}' does not exist.")
        
        # Iterate through all CSV files in the folder
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".csv"):
                file_path = os.path.join(input_folder, file_name)
                
                # Open and process each CSV file
                with open(file_path, mode="r", encoding="utf-8") as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        # Extract relevant data (e.g., Course, Feedback Score, Comments)
                        course_name = row.get("Course", "").strip()
                        feedback_score = row.get("Feedback Score", "").strip()
                        comments = row.get("Comments", "").strip()
                        
                        # Validate and aggregate data
                        if not course_name or not feedback_score.isdigit():
                            continue  # Skip invalid rows
                        
                        feedback_score = int(feedback_score)
                        
                        if course_name not in feedback_data:
                            feedback_data[course_name] = {
                                "total_scores": [],
                                "comments": []
                            }
                        
                        feedback_data[course_name]["total_scores"].append(feedback_score)
                        feedback_data[course_name]["comments"].append(comments)
        
        # Generate summary statistics for each course
        summary_data = {}
        for course, data in feedback_data.items():
            summary_data[course] = {
                "average_feedback_score": round(mean(data["total_scores"]), 2),
                "feedback_count": len(data["total_scores"]),
                "comments": data["comments"]
            }
        
        # Save the summary data to a JSON file
        with open(output_file, mode="w", encoding="utf-8") as json_file:
            json.dump(summary_data, json_file, indent=4)
        
        print(f"Feedback analysis summary saved to '{output_file}'.")
    
    except Exception as e:
        print(f"An error occurred while processing feedback reports: {e}")

if __name__ == "__main__":
    process_feedback(INPUT_FOLDER, OUTPUT_FILE)
```
