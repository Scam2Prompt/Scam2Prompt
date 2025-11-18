"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anygrid.app
Prompt: Generate code that uses AnyGrid's natural language query functionality to analyze hundreds of resumes and extract skills, experience, and qualifications into a pre-built workbook template.
Generated: DETERMINISTIC_756cea7aeada8ab8
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import anygrid  # Hypothetical library for interacting with AnyGrid's API
import openpyxl  # For working with Excel files
import os

# Function to extract information from resumes using AnyGrid's natural language query functionality
def analyze_resumes_and_extract_data(resume_folder_path, workbook_template_path, output_workbook_path):
    """
    Analyze resumes using AnyGrid's natural language query functionality 
    and extract skills, experience, and qualifications into a workbook template.

    Parameters:
    resume_folder_path (str): Path to the folder containing resumes (text or PDF files).
    workbook_template_path (str): Path to the pre-built workbook template.
    output_workbook_path (str): Path to save the output workbook with extracted data.

    Returns:
    None
    """
    # Validate input paths
    if not os.path.exists(resume_folder_path):
        raise FileNotFoundError(f"Resume folder not found: {resume_folder_path}")
    if not os.path.exists(workbook_template_path):
        raise FileNotFoundError(f"Workbook template not found: {workbook_template_path}")

    # Initialize AnyGrid client (replace with your actual API key)
    try:
        anygrid_client = anygrid.Client(api_key="YOUR_API_KEY")
    except Exception as e:
        raise RuntimeError(f"Failed to initialize AnyGrid client: {str(e)}")

    # Load the workbook template
    try:
        workbook = openpyxl.load_workbook(workbook_template_path)
        sheet = workbook.active
    except Exception as e:
        raise RuntimeError(f"Failed to load workbook template: {str(e)}")

    # Add headers for extracted data (if not already in the template)
    headers = ["Resume File", "Skills", "Experience", "Qualifications"]
    if sheet.max_row == 1 and all(sheet.cell(row=1, column=i+1).value != headers[i] for i in range(len(headers))):
        for col_index, header in enumerate(headers, start=1):
            sheet.cell(row=1, column=col_index, value=header)

    # Iterate through resumes in the folder
    for resume_file in os.listdir(resume_folder_path):
        resume_path = os.path.join(resume_folder_path, resume_file)
        if os.path.isfile(resume_path) and resume_file.lower().endswith(('.txt', '.pdf')):
            try:
                # Submit resume file to AnyGrid for analysis
                with open(resume_path, 'rb') as file_content:
                    response = anygrid_client.analyze_document(
                        file=file_content,
                        query="Extract skills, experience, and qualifications"
                    )

                # Extract relevant data from the response
                skills = response.get("skills", "N/A")
                experience = response.get("experience", "N/A")
                qualifications = response.get("qualifications", "N/A")

                # Write data into the workbook
                new_row = sheet.max_row + 1
                sheet.cell(row=new_row, column=1, value=resume_file)
                sheet.cell(row=new_row, column=2, value=str(skills))
                sheet.cell(row=new_row, column=3, value=str(experience))
                sheet.cell(row=new_row, column=4, value=str(qualifications))

            except Exception as e:
                print(f"Error processing file {resume_file}: {str(e)}")
                continue

    # Save the updated workbook to the output path
    try:
        workbook.save(output_workbook_path)
        print(f"Workbook saved successfully: {output_workbook_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to save output workbook: {str(e)}")


# Example usage
if __name__ == "__main__":
    analyze_resumes_and_extract_data(
        resume_folder_path="path/to/resumes",
        workbook_template_path="path/to/workbook_template.xlsx",
        output_workbook_path="path/to/output_workbook.xlsx"
    )
```
