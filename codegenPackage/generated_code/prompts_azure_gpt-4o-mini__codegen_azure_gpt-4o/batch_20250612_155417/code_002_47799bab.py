"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
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
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries representing rows in the CSV file.
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

def analyze_programs(data):
    """
    Analyze multi-disciplinary programs in universities.

    Args:
        data (list[dict]): List of dictionaries representing program data.

    Returns:
        dict: Analysis results including counts and categories.
    """
    analysis_results = {
        "total_programs": 0,
        "multi_disciplinary_programs": 0,
        "discipline_counts": defaultdict(int)
    }

    for row in data:
        # Ensure required fields exist
        if 'Program Name' not in row or 'Disciplines' not in row:
            raise ValueError("Missing required fields in data.")

        analysis_results["total_programs"] += 1

        # Split disciplines by comma and count them
        disciplines = [d.strip() for d in row['Disciplines'].split(',') if d.strip()]
        if len(disciplines) > 1:
            analysis_results["multi_disciplinary_programs"] += 1
        
        for discipline in disciplines:
            analysis_results["discipline_counts"][discipline] += 1

    return analysis_results

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
            writer.writerow(["Metric", "Value"])
            writer.writerow(["Total Programs", results["total_programs"]])
            writer.writerow(["Multi-disciplinary Programs", results["multi_disciplinary_programs"]])
            writer.writerow(["Discipline", "Count"])
            for discipline, count in results["discipline_counts"].items():
                writer.writerow([discipline, count])
    except Exception as e:
        raise RuntimeError(f"Error writing the file: {e}")

def main():
    """
    Main function to execute the script.
    """
    input_file = "university_programs.csv"  # Replace with your input file path
    output_file = "analysis_results.csv"   # Replace with your desired output file path

    try:
        # Load data
        data = load_data(input_file)

        # Analyze programs
        results = analyze_programs(data)

        # Save results
        save_analysis_results(results, output_file)

        print(f"Analysis completed successfully. Results saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
