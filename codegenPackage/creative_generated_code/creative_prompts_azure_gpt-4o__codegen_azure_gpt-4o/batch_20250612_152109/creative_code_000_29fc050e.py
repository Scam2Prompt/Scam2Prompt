"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Write Python code to analyze the admission timetables for MBBS and MD/MS courses at MIMSR for the academic years 2023-2025, and extract key dates and deadlines.
Generated: DETERMINISTIC_29fc050ef007c737
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

def extract_key_dates(timetable_text):
    """
    Extracts key dates and deadlines from the admission timetable text.

    Args:
        timetable_text (str): The raw text containing admission timetable details.

    Returns:
        dict: A dictionary with course names as keys and their respective key dates as lists of dictionaries.
    """
    # Regular expression to extract dates in the format DD/MM/YYYY or DD-MM-YYYY
    date_pattern = r"\b(\d{2}[/-]\d{2}[/-]\d{4})\b"
    
    # Regular expression to extract course names (e.g., MBBS, MD/MS)
    course_pattern = r"(MBBS|MD/MS)"

    # Dictionary to store extracted data
    extracted_dates = {}

    try:
        # Split the text into lines for processing
        lines = timetable_text.splitlines()
        
        # Iterate over each line to find courses and dates
        for line in lines:
            # Check for the course name in the line
            course_match = re.search(course_pattern, line)
            
            if course_match:
                course_name = course_match.group(0)
                
                # Extract all dates associated with the course
                dates = re.findall(date_pattern, line)
                
                # Convert dates to a standardized format and store them
                standardized_dates = []
                for date in dates:
                    try:
                        standardized_date = datetime.strptime(date.replace('-', '/'), "%d/%m/%Y")
                        standardized_dates.append({"original": date, "standardized": standardized_date.strftime("%Y-%m-%d")})
                    except ValueError:
                        # Skip invalid dates without crashing
                        continue
                
                # Add course and its dates to the dictionary
                if course_name not in extracted_dates:
                    extracted_dates[course_name] = []
                
                extracted_dates[course_name].extend(standardized_dates)

    except Exception as e:
        print(f"An error occurred while extracting key dates: {e}")

    return extracted_dates


def main():
    """
    Entry point for the program. Reads the timetable text file, analyzes it, and outputs key dates and deadlines.
    """
    # File containing admission timetable details
    timetable_file = "admission_timetable_2023_2025.txt"

    try:
        # Read the timetable text file
        with open(timetable_file, 'r') as file:
            timetable_text = file.read()
        
        # Extract key dates and deadlines
        key_dates = extract_key_dates(timetable_text)
        
        # Output the results
        print("Key Dates and Deadlines:")
        for course, dates in key_dates.items():
            print(f"\n{course}:")
            for date_info in dates:
                print(f"  - Original: {date_info['original']}, Standardized: {date_info['standardized']}")

    except FileNotFoundError:
        print(f"Error: File '{timetable_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
