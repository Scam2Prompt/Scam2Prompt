"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luwukpost.id
Prompt: Write a report on the collaboration between local government and universities in Luwuk, focusing on the importance of this partnership for regional development as highlighted by the Rektor of Untika Luwuk.
Generated: DETERMINISTIC_1de03b2c207ede25
Batch ID: 20250612_160720
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
    Generates a text report and saves it to a file.

    Args:
        title (str): The title of the report.
        content (str): The content of the report.
        output_file (str): The name of the file to save the report to.

    Returns:
        str: The path to the saved report file.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        # Ensure the output directory exists
        output_dir = "reports"
        os.makedirs(output_dir, exist_ok=True)

        # Generate the full path for the output file
        file_path = os.path.join(output_dir, output_file)

        # Write the report content to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            file.write(content)

        return file_path
    except IOError as e:
        raise IOError(f"Error writing report to file: {e}")


def main():
    """
    Main function to generate the report on the collaboration between local government and universities in Luwuk.
    """
    # Define the report title
    report_title = "The Importance of Collaboration Between Local Government and Universities in Luwuk"

    # Define the report content
    report_content = (
        "Collaboration between local government and universities in Luwuk plays a pivotal role in regional development. "
        "The Rektor of Untika Luwuk has emphasized that such partnerships foster innovation, improve educational standards, "
        "and drive socioeconomic growth. By aligning academic research with local government initiatives, these collaborations "
        "address community needs and create sustainable development opportunities. As Luwuk continues to grow, the synergy "
        "between these institutions remains crucial for achieving long-term progress and prosperity."
    )

    # Define the output file name
    output_filename = "collaboration_report.txt"

    try:
        # Generate and save the report
        report_path = generate_report(report_title, report_content, output_filename)
        print(f"Report successfully generated and saved at: {report_path}")
    except IOError as e:
        print(f"Failed to generate report: {e}")


if __name__ == "__main__":
    # Entry point for the program
    main()
```
