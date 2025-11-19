"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write a script that automates the analysis of management consulting case studies similar to those provided by AM Platinum Consulting.
Generated: DETERMINISTIC_fd5cab9771b4d849
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
from collections import Counter
import json
from typing import Dict, List, Tuple

# Define constants
CASE_STUDY_DIRECTORY = "case_studies"  # Directory containing case study files
RESULTS_FILE = "analysis_results.json"  # Output file for analysis results

def read_case_study(file_path: str) -> str:
    """
    Reads the content of a case study file and returns it as a string.
    
    Args:
        file_path (str): Path to the case study file.
        
    Returns:
        str: Content of the case study file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file: {file_path}. Details: {e}")

def extract_keywords(content: str) -> List[str]:
    """
    Extracts keywords (words longer than 3 characters) from the content.
    
    Args:
        content (str): The textual content to extract keywords from.
        
    Returns:
        List[str]: List of extracted keywords.
    """
    # Remove special characters and split into words
    words = re.findall(r'\b[a-zA-Z]{4,}\b', content.lower())
    return words

def analyze_case_studies(directory: str) -> Dict[str, Dict[str, int]]:
    """
    Analyzes all case studies in the specified directory and computes keyword frequencies.
    
    Args:
        directory (str): Path to the directory containing case study files.
        
    Returns:
        Dict[str, Dict[str, int]]: Analysis results containing keyword frequencies for each file.
    """
    analysis_results = {}
    
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            try:
                content = read_case_study(file_path)
                keywords = extract_keywords(content)
                keyword_counts = dict(Counter(keywords))
                analysis_results[file_name] = keyword_counts
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")
    
    return analysis_results

def save_analysis_results(results: Dict[str, Dict[str, int]], output_file: str) -> None:
    """
    Saves the analysis results to a JSON file.
    
    Args:
        results (Dict[str, Dict[str, int]]): Analysis results to save.
        output_file (str): Path to the output file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(results, file, indent=4)
    except Exception as e:
        raise Exception(f"Error saving results to file: {output_file}. Details: {e}")

def main():
    """
    Main function to orchestrate the analysis of management consulting case studies.
    """
    try:
        print("Starting case study analysis...")
        results = analyze_case_studies(CASE_STUDY_DIRECTORY)
        save_analysis_results(results, RESULTS_FILE)
        print(f"Analysis complete. Results saved to {RESULTS_FILE}")
    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
