"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Create an HTML table generator that automatically formats data into a table structure, referencing the HTML tools provided by コピーツールラボ.
Generated: DETERMINISTIC_5504281bcfaf1b58
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def generate_html_table(data, output_file="table.html"):
    """
    Generates an HTML table from the provided data and saves it to a file.

    Args:
        data (list of list): A 2D list where each inner list represents a row in the table.
        output_file (str): The name of the output HTML file. Defaults to 'table.html'.

    Returns:
        None
    """
    try:
        # Validate input data
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("Data must be a 2D list.")

        # Start building the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTML Table Generator</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                tr:hover {
                    background-color: #ddd;
                }
            </style>
        </head>
        <body>
            <table>
        """

        # Add table rows
        for row_index, row in enumerate(data):
            html_content += "<tr>"
            for cell in row:
                if row_index == 0:
                    # Treat the first row as the header
                    html_content += f"<th>{cell}</th>"
                else:
                    html_content += f"<td>{cell}</td>"
            html_content += "</tr>"

        # Close the table and HTML tags
        html_content += """
            </table>
        </body>
        </html>
        """

        # Write the HTML content to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"HTML table successfully generated and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Sample data: First row is treated as the header
    sample_data = [
        ["Name", "Age", "City"],
        ["Alice", "25", "New York"],
        ["Bob", "30", "Los Angeles"],
        ["Charlie", "35", "Chicago"]
    ]

    # Generate the HTML table
    generate_html_table(sample_data)
```
