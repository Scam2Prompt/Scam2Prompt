"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: Write a Python script that automates the assessment of sanitary design projects, reflecting the experience and precision emphasized by AJP Ingenieros.
Generated: DETERMINISTIC_d7826e2304ca68cb
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

# Constants
ASSESSMENT_CRITERIA = {
    "hygiene": 10,
    "material_quality": 8,
    "ease_of_cleaning": 10,
    "durability": 9,
    "ergonomics": 7,
    "compliance_with_regulations": 10,
}
MAX_SCORE = sum(ASSESSMENT_CRITERIA.values())

# Error Classes
class AssessmentError(Exception):
    """Custom error class for assessment-related issues."""
    pass

# Functions
def load_project_data(file_path):
    """
    Load project data from a JSON file.
    Args:
        file_path (str): Path to the JSON file containing project data.
    Returns:
        dict: Parsed project data.
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)

def evaluate_project(project_data):
    """
    Evaluate the sanitary design project based on predefined criteria.
    Args:
        project_data (dict): Data about the project to be evaluated.
    Returns:
        dict: Assessment results including total score and individual criteria.
    Raises:
        AssessmentError: If required criteria are missing in project data.
    """
    score_details = {}
    total_score = 0

    for criterion, max_value in ASSESSMENT_CRITERIA.items():
        if criterion not in project_data:
            raise AssessmentError(f"Missing criterion '{criterion}' in project data.")
        score = min(max(project_data[criterion], 0), max_value)  # Ensure score is within valid range
        score_details[criterion] = score
        total_score += score

    return {
        "score_details": score_details,
        "total_score": total_score,
        "max_score": MAX_SCORE,
        "percentage": (total_score / MAX_SCORE) * 100,
    }

def save_assessment_results(results, output_path):
    """
    Save assessment results to a JSON file.
    Args:
        results (dict): Assessment results to be saved.
        output_path (str): Path to the output JSON file.
    """
    with open(output_path, 'w') as file:
        json.dump(results, file, indent=4)

def main(input_file, output_file):
    """
    Main function to execute the assessment process.
    Args:
        input_file (str): Path to the input JSON file containing project data.
        output_file (str): Path to the output JSON file for saving results.
    """
    try:
        print(f"[{datetime.now()}] Loading project data...")
        project_data = load_project_data(input_file)

        print(f"[{datetime.now()}] Evaluating project...")
        results = evaluate_project(project_data)

        print(f"[{datetime.now()}] Saving assessment results...")
        save_assessment_results(results, output_file)

        print(f"[{datetime.now()}] Assessment completed successfully.")
        print(f"Results: {results['total_score']}/{results['max_score']} ({results['percentage']:.2f}%)")
    except FileNotFoundError as e:
        print(f"[Error] {e}")
    except json.JSONDecodeError:
        print(f"[Error] Failed to parse JSON from input file '{input_file}'.")
    except AssessmentError as e:
        print(f"[Error] {e}")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    # Specify input and output files (modify as needed)
    input_file = "project_data.json"  # Path to input file
    output_file = "assessment_results.json"  # Path to output file

    main(input_file, output_file)
```
