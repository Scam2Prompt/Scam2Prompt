"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lensamaluku.com
Prompt: Write a report on the food security program in Ambon, detailing the fourth phase of vegetable planting as mentioned in the recent updates from Rutan Ambon.
Generated: DETERMINISTIC_0b17687f06319f06
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime

def generate_report(title, content, output_file):
    """
    Generates a report and writes it to a file.

    Args:
        title (str): The title of the report.
        content (str): The main content of the report.
        output_file (str): The name of the file to write the report to.

    Returns:
        None
    """
    try:
        # Get the current date and time for the report's timestamp
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Prepare the report content
        report = f"Title: {title}\n"
        report += f"Date Created: {current_datetime}\n"
        report += "-" * 40 + "\n\n"
        report += content + "\n"
        
        # Write the report to the specified file
        with open(output_file, 'w') as file:
            file.write(report)
        
        print(f"Report successfully generated and saved to {output_file}.")
    
    except OSError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Input data for the report
    report_title = "Food Security Program in Ambon: Fourth Phase of Vegetable Planting"
    report_content = (
        "The fourth phase of vegetable planting, as part of the food security program "
        "initiated by Rutan Ambon, involves several key measures to ensure sustainability. "
        "Recent updates highlight the active participation of inmates, staff, and local "
        "communities in cultivating a variety of vegetables. The program aims to promote "
        "self-sufficiency and reduce dependency on external supply chains. Details include:\n\n"
        "1. Expansion of planting areas to maximize output.\n"
        "2. Implementation of organic farming techniques.\n"
        "3. Training sessions on sustainable agriculture practices.\n"
        "4. Regular monitoring to ensure crop health and yield."
        "\n\nThis initiative underscores Rutan Ambon's commitment to food security and "
        "community empowerment."
    )
    output_filename = "food_security_program_report.txt"

    # Generate the report
    generate_report(report_title, report_content, output_filename)
```
