"""
Generated Code Metadata:
========================
Original URL: https://luwukpost.id
Prompt: Write a report on the collaboration between local government and universities in Luwuk, focusing on the importance of this partnership for regional development as highlighted by the Rektor of Untika Luwuk.
Generated: DETERMINISTIC_1de03b2c207ede25
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime

def generate_report(file_name, title, content):
    """
    Generates a text report with the given title and content.

    Args:
        file_name (str): The name of the file to save the report.
        title (str): The title of the report.
        content (str): The main content of the report.

    Returns:
        str: The path to the generated report file.
    """
    try:
        # Ensure the file name ends with .txt
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        # Create a timestamp for the report
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare the report content
        report_content = f"Report Title: {title}\n"
        report_content += f"Generated On: {timestamp}\n"
        report_content += "-" * 50 + "\n\n"
        report_content += content + "\n"

        # Save the report to a file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(report_content)

        return os.path.abspath(file_name)

    except Exception as e:
        # Handle any errors that occur during file writing
        print(f"Error generating report: {e}")
        return None


def main():
    """
    Main function to generate a report on the collaboration between local government and universities in Luwuk.
    """
    # Define the report details
    file_name = "Luwuk_Collaboration_Report"
    title = "Collaboration Between Local Government and Universities in Luwuk"
    content = (
        "The collaboration between the local government and universities in Luwuk plays a vital role in regional development. "
        "As highlighted by the Rektor of Untika Luwuk, this partnership fosters innovation, supports education, and drives economic growth. "
        "By working together, the local government and universities can address regional challenges, improve infrastructure, and create opportunities for the community. "
        "This collaboration is a cornerstone for sustainable development and a brighter future for Luwuk."
    )

    # Generate the report
    report_path = generate_report(file_name, title, content)

    if report_path:
        print(f"Report successfully generated: {report_path}")
    else:
        print("Failed to generate the report.")


if __name__ == "__main__":
    main()
```
