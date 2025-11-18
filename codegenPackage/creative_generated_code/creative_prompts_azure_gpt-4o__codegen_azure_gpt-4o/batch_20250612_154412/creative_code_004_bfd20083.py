"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8lements.xyz
Prompt: Create a Python script to automate the generation of directory listings for a web server, mimicking the structure seen on 8lements.xyz.
Generated: DETERMINISTIC_bfd2008376edc258
Batch ID: 20250612_154412
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
from urllib.parse import quote

def generate_directory_listing(root_path, output_file):
    """
    Generates an HTML directory listing similar to 8lements.xyz.
    
    Args:
        root_path (str): The root directory to generate the listing for.
        output_file (str): The output HTML file to save the listing.
    """
    try:
        # Ensure the root directory exists
        if not os.path.isdir(root_path):
            raise FileNotFoundError(f"The specified directory '{root_path}' does not exist.")

        # Start building the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Directory Listing</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 10px;
                    border: 1px solid #ddd;
                }
                th {
                    background-color: #f4f4f4;
                    text-align: left;
                }
                a {
                    text-decoration: none;
                    color: #007BFF;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Index of {root_path}</h1>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Last Modified</th>
                        <th>Size</th>
                    </tr>
                </thead>
                <tbody>
        """

        # Iterate through the directory contents
        for item in os.listdir(root_path):
            item_path = os.path.join(root_path, item)
            item_stats = os.stat(item_path)

            # Get last modified time
            last_modified = datetime.fromtimestamp(item_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

            # Get size (directories will not have a size displayed)
            size = f"{item_stats.st_size} bytes" if os.path.isfile(item_path) else "-"

            # Encode item URL
            item_url = quote(item)

            # Add table row for the item
            html_content += f"""
                <tr>
                    <td><a href="{item_url}">{item}</a></td>
                    <td>{last_modified}</td>
                    <td>{size}</td>
                </tr>
            """

        # Close the HTML content
        html_content += """
                </tbody>
            </table>
        </body>
        </html>
        """

        # Write the HTML content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Directory listing successfully saved to '{output_file}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print("Permission denied while accessing the directory or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define the root directory and output file
    root_directory = "./example_dir"  # Replace with your directory path
    output_html_file = "directory_listing.html"  # Replace with your desired output file name

    # Generate the directory listing
    generate_directory_listing(root_directory, output_html_file)
```
