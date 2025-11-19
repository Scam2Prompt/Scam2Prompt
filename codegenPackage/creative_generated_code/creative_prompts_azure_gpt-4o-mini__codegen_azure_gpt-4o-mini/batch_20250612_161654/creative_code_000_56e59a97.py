"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benenergie-dz.com
Prompt: Generate a code snippet to create an index page similar to the one found at benenergie-dz.com, including file size and last modified date.
Generated: DETERMINISTIC_56e59a97304bd225
Batch ID: 20250612_161654
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

def generate_index_page(directory: str, output_file: str) -> None:
    """
    Generate an index HTML page for the specified directory.
    
    Args:
        directory (str): The path to the directory to index.
        output_file (str): The path to the output HTML file.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        Exception: For any general exceptions that occur during processing.
    """
    try:
        # Verify that the specified directory exists
        if not os.path.exists(directory) or not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        # Start building the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Index of {directory}</title>
            <style>
                body { font-family: Arial, sans-serif; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Index of {directory}</h1>
            <table>
                <tr>
                    <th>Filename</th>
                    <th>Filesize (bytes)</th>
                    <th>Last Modified</th>
                </tr>
        """.replace("{directory}", directory)

        # Iterate over the files in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                # Get file size and last modified date
                filesize = os.path.getsize(item_path)
                last_modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')
                
                # Append a row to the HTML table
                html_content += f"""
                <tr>
                    <td>{item}</td>
                    <td>{filesize}</td>
                    <td>{last_modified}</td>
                </tr>
                """

        # Closing the table and HTML tags
        html_content += """
            </table>
        </body>
        </html>
        """

        # Write the HTML content to the output file
        with open(output_file, 'w') as file:
            file.write(html_content)

        print(f"Index page generated successfully at {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    generate_index_page("path/to/your/directory", "index.html")
```

Make sure to replace `"path/to/your/directory"` with the actual directory you want to index before running the script.
