"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write a Python script to analyze the selection process for professor positions at the Instituto de Geografia, Universidade do Estado do Rio de Janeiro (UERJ), including calculating the number of applicants and interviewees for each position.
Generated: DETERMINISTIC_9fcbf0cb94a38c9b
Batch ID: 20250622_211713
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

def analyze_professor_selection(input_file, output_file):
    """
    Analyzes the selection process for professor positions at UERJ's Instituto de Geografia.
    Calculates the number of applicants and interviewees for each position.

    Args:
        input_file (str): Path to the CSV file containing the selection process data.
        output_file (str): Path to save the analysis results as a CSV file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the input file is not a valid CSV or has incorrect format.
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        # Initialize data structures
        position_stats = defaultdict(lambda: {'applicants': 0, 'interviewees': 0})

        # Read and process the input file
        with open(input_file, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Validate required fields
            required_fields = ['position_id', 'position_name', 'applicant_status']
            if not all(field in reader.fieldnames for field in required_fields):
                raise ValueError("Input CSV is missing required fields. Expected fields: position_id, position_name, applicant_status")
            
            for row in reader:
                position_id = row['position_id']
                position_stats[position_id]['position_name'] = row['position_name']
                position_stats[position_id]['applicants'] += 1
                
                if row['applicant_status'].lower() == 'interviewed':
                    position_stats[position_id]['interviewees'] += 1

        # Write the results to output file
        with open(output_file, mode='w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['position_id', 'position_name', 'applicants', 'interviewees']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for position_id, stats in position_stats.items():
                writer.writerow({
                    'position_id': position_id,
                    'position_name': stats['position_name'],
                    'applicants': stats['applicants'],
                    'interviewees': stats['interviewees']
                })

    except Exception as e:
        raise Exception(f"An error occurred during analysis: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_csv = "professor_selection_data.csv"
    output_csv = "professor_selection_analysis.csv"
    
    try:
        analyze_professor_selection(input_csv, output_csv)
        print(f"Analysis completed successfully. Results saved to {output_csv}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
