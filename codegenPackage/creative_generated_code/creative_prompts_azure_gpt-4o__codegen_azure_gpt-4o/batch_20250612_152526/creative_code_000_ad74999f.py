"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Python script to generate a report template for tracking institutional achievements, such as bilingualism recognition or environmental practices, similar to those highlighted by the Institución Educativa Politécnico Municipal de Cali.
Generated: DETERMINISTIC_ad74999f46e59a78
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

def generate_report_template(file_name, institution_name, achievements):
    """
    Generates a report template for tracking institutional achievements.

    Args:
        file_name (str): The name of the file to save the report template.
        institution_name (str): Name of the institution.
        achievements (list): List of achievements to track.
    
    Returns:
        None
    """
    try:
        # Validate input types
        if not isinstance(file_name, str):
            raise ValueError("File name must be a string.")
        if not isinstance(institution_name, str):
            raise ValueError("Institution name must be a string.")
        if not isinstance(achievements, list):
            raise ValueError("Achievements must be provided as a list.")

        # Ensure file name ends with .txt
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        # Prepare report content
        report_lines = [
            f"Institution Name: {institution_name}",
            f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "Achievements Tracking Report",
            "-" * 40,
            "Achievements:",
        ]

        # Add achievements to the report
        for index, achievement in enumerate(achievements, start=1):
            report_lines.append(f"{index}. {achievement}")
        
        report_lines.append("-" * 40)
        report_lines.append("End of Report")

        # Create or overwrite the report file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))
        
        print(f"Report template successfully generated: {file_name}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error generating report template: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Define institution name and achievements
    institution = "Institución Educativa Politécnico Municipal de Cali"
    achievements_list = [
        "Bilingualism Recognition",
        "Environmental Sustainability Practices",
        "Community Outreach Programs"
    ]
    
    # Generate the report template
    generate_report_template("institution_report", institution, achievements_list)
```
