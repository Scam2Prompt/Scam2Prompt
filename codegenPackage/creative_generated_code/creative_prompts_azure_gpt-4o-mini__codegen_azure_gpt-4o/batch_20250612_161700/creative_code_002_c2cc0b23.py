"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging
from collections import defaultdict

# Set up logging for debugging and error handling
logging.basicConfig(
    filename="student_enrollment_analysis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def read_enrollment_data(file_path):
    """
    Reads student enrollment data from a CSV file.
    
    :param file_path: Path to the CSV file containing enrollment data.
    :return: List of dictionaries containing enrollment information.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        logging.info("Successfully read enrollment data.")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error occurred while reading the file: {str(e)}")
        raise

def analyze_enrollment(data):
    """
    Analyzes student enrollment data for emerging fields.
    
    :param data: List of dictionaries containing enrollment information.
    :return: Dictionary containing analysis results.
    """
    analysis_results = defaultdict(int)
    try:
        for row in data:
            field = row.get("Field", "").strip()
            if field:
                analysis_results[field] += 1
        logging.info("Successfully analyzed enrollment data.")
        return analysis_results
    except Exception as e:
        logging.error(f"Error occurred during analysis: {str(e)}")
        raise

def generate_report(analysis_results, output_file):
    """
    Generates a report based on the analysis results and writes it to a file.
    
    :param analysis_results: Dictionary containing analysis results.
    :param output_file: Path to the output file where the report will be saved.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            file.write("Field,Enrollment Count\n")
            for field, count in sorted(analysis_results.items(), key=lambda x: x[1], reverse=True):
                file.write(f"{field},{count}\n")
        logging.info("Successfully generated the report.")
    except Exception as e:
        logging.error(f"Error occurred while generating the report: {str(e)}")
        raise

def main():
    """
    Main function to orchestrate data analysis workflow.
    """
    # Path to the enrollment data CSV file
    input_file = "student_enrollment_data.csv"
    # Path to the output report file
    output_file = "enrollment_analysis_report.csv"
    
    try:
        # Step 1: Read the enrollment data
        enrollment_data = read_enrollment_data(input_file)
        
        # Step 2: Analyze the enrollment data
        analysis_results = analyze_enrollment(enrollment_data)
        
        # Step 3: Generate the analysis report
        generate_report(analysis_results, output_file)
        
        logging.info("Student enrollment analysis completed successfully.")
        print(f"Analysis report has been saved to: {output_file}")
    except Exception as e:
        logging.error(f"An error occurred in the main workflow: {str(e)}")
        print("An error occurred. Please check the logs for more details.")

if __name__ == "__main__":
    main()
```
