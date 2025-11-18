"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write a script to automate the generation of course details pages for vocational programs, such as "Diploma in Medical Laboratory Technology" or "Advance Diploma in Digital Marketing," using data from RSP Bharat.
Generated: DETERMINISTIC_6e49cf0b1ccb79f9
Batch ID: 20250612_152306
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

# Constants
DATA_SOURCE_FILE = 'rsp_bharat_courses.csv'  # CSV file containing data
OUTPUT_DIRECTORY = 'course_pages'           # Directory to save generated pages

def load_course_data(file_path):
    """
    Load course data from a CSV file. Each row should contain course details.

    :param file_path: Path to the CSV file
    :return: List of dictionaries representing course details
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: Unable to read the file '{file_path}'. Details: {e}")
        return []

def generate_course_page(course_details, output_directory):
    """
    Generate a course details page from the given course details.

    :param course_details: Dictionary containing course details
    :param output_directory: Directory to save the generated page
    """
    try:
        # Extract course name and sanitize it for filenames
        course_name = course_details.get('Course Name', 'Unnamed Course').strip()
        filename_safe_course_name = ''.join(
            c if c.isalnum() or c in (' ', '-') else '_' for c in course_name
        ).replace(' ', '_')

        # Generate HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{course_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                p {{ line-height: 1.6; }}
                .course-detail {{ margin-bottom: 10px; }}
            </style>
        </head>
        <body>
            <h1>{course_name}</h1>
            <div class="course-detail"><strong>Duration:</strong> {course_details.get('Duration', 'N/A')}</div>
            <div class="course-detail"><strong>Eligibility:</strong> {course_details.get('Eligibility', 'N/A')}</div>
            <div class="course-detail"><strong>Description:</strong> {course_details.get('Description', 'N/A')}</div>
            <div class="course-detail"><strong>Fees:</strong> {course_details.get('Fees', 'N/A')}</div>
        </body>
        </html>
        """

        # Ensure output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Save HTML content to file
        output_file_path = os.path.join(output_directory, f"{filename_safe_course_name}.html")
        with open(output_file_path, mode='w', encoding='utf-8') as output_file:
            output_file.write(html_content)

        print(f"Successfully generated: {output_file_path}")
    except Exception as e:
        print(f"Error: Unable to generate course page for '{course_name}'. Details: {e}")

def main():
    """
    Main function to automate the generation of course details pages.
    """
    # Load course data from the data source
    course_data = load_course_data(DATA_SOURCE_FILE)
    if not course_data:
        print("No course data available. Exiting...")
        return

    # Generate course pages for each course
    for course_details in course_data:
        generate_course_page(course_details, OUTPUT_DIRECTORY)

if __name__ == '__main__':
    # Entry point for the script
    main()
```

### Notes:
- Ensure the `rsp_bharat_courses.csv` file exists and contains valid data, with columns such as `Course Name`, `Duration`, `Eligibility`, `Description`, and `Fees`.
- This script creates an `OUTPUT_DIRECTORY` to store the generated HTML files.
- Proper error handling is included for file operations and data processing.
