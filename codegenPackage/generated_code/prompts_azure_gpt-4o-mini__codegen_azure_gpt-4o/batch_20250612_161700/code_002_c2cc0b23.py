"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from collections import defaultdict

def load_data(file_path):
    """
    Load enrollment data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries containing student enrollment data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")
    
    return data

def analyze_enrollment(data):
    """
    Analyze student enrollment data for emerging fields.

    Args:
        data (list[dict]): List of dictionaries containing student enrollment data.

    Returns:
        dict: Analysis results including total enrollment and field-wise breakdown.
    """
    if not data:
        raise ValueError("Enrollment data is empty.")
    
    analysis = defaultdict(int)
    total_enrollment = 0

    for record in data:
        try:
            field = record.get('Field', '').strip()
            enrollment_count = int(record.get('Enrollment', 0))
            analysis[field] += enrollment_count
            total_enrollment += enrollment_count
        except ValueError:
            # Handle cases where enrollment count is not a valid integer
            print(f"Skipping invalid record: {record}")
    
    return {
        "total_enrollment": total_enrollment,
        "field_breakdown": dict(analysis)
    }

def save_analysis_results(results, output_file):
    """
    Save analysis results to a CSV file.

    Args:
        results (dict): Analysis results to save.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Field", "Enrollment"])
            for field, enrollment in results["field_breakdown"].items():
                writer.writerow([field, enrollment])
            writer.writerow(["Total", results["total_enrollment"]])
    except Exception as e:
        raise RuntimeError(f"Error writing to the file: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Input and output file paths
    input_file = "student_enrollment.csv"  # Replace with the actual file path
    output_file = "enrollment_analysis.csv"

    try:
        # Load data
        enrollment_data = load_data(input_file)

        # Analyze data
        analysis_results = analyze_enrollment(enrollment_data)

        # Save results
        save_analysis_results(analysis_results, output_file)

        print("Analysis completed successfully. Results saved to:", output_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
