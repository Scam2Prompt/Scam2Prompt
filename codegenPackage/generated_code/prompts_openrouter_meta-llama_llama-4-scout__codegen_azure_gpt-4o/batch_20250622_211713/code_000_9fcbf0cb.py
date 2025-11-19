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

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries containing the data.
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

def analyze_selection_process(data):
    """
    Analyze the selection process for professor positions.

    Args:
        data (list[dict]): List of dictionaries containing the data.

    Returns:
        dict: Analysis results with the number of applicants and interviewees per position.
    """
    analysis_results = {}
    
    for entry in data:
        position = entry.get('Position')
        if not position:
            raise ValueError("Missing 'Position' field in data entry.")
        
        applicants = int(entry.get('Applicants', 0))
        interviewees = int(entry.get('Interviewees', 0))
        
        if position not in analysis_results:
            analysis_results[position] = {'Applicants': 0, 'Interviewees': 0}
        
        analysis_results[position]['Applicants'] += applicants
        analysis_results[position]['Interviewees'] += interviewees
    
    return analysis_results

def display_results(results):
    """
    Display the analysis results.

    Args:
        results (dict): Analysis results with the number of applicants and interviewees per position.
    """
    print("Selection Process Analysis Results:")
    print("-" * 40)
    for position, stats in results.items():
        print(f"Position: {position}")
        print(f"  Total Applicants: {stats['Applicants']}")
        print(f"  Total Interviewees: {stats['Interviewees']}")
        print("-" * 40)

def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing the data
    file_path = 'selection_process_data.csv'
    
    try:
        # Load data from the CSV file
        data = load_data(file_path)
        
        # Analyze the selection process
        results = analyze_selection_process(data)
        
        # Display the results
        display_results(results)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(f"Data error: {val_error}")
    except RuntimeError as runtime_error:
        print(f"Runtime error: {runtime_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
