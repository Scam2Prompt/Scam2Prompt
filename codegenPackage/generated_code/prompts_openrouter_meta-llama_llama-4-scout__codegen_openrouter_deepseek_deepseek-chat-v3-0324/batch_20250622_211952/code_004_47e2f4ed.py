"""
Generated Code Metadata:
========================
Original URL: https://presale-app.com
Prompt: Write a Python script to automatically generate a basic webpage with a given directory path and timestamp.
Generated: DETERMINISTIC_47e2f4ed72c56d72
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime

def generate_webpage(directory_path, title="Generated Webpage"):
    """
    Generates a basic HTML webpage with a directory listing and timestamp.
    
    Args:
        directory_path (str): Path to the directory to list in the webpage.
        title (str, optional): Title of the webpage. Defaults to "Generated Webpage".
    
    Returns:
        str: Path to the generated HTML file.
    
    Raises:
        NotADirectoryError: If the provided path is not a directory.
        PermissionError: If there's no permission to read the directory.
    """
    try:
        # Validate directory path
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Path '{directory_path}' is not a directory")
        
        # Get directory contents
        contents = os.listdir(directory_path)
        
        # Generate HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 5px 0; }}
        .timestamp {{ color: #666; font-style: italic; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>Directory: {directory_path}</p>
    <div class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
    <h2>Contents:</h2>
    <ul>
"""

        # Add directory contents to HTML
        for item in contents:
            html_content += f"        <li>{item}</li>\n"
        
        html_content += """    </ul>
</body>
</html>"""
        
        # Create output filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"webpage_{timestamp}.html"
        output_path = os.path.join(directory_path, output_filename)
        
        # Write HTML file
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        return output_path
    
    except PermissionError as e:
        raise PermissionError(f"Permission denied to access directory '{directory_path}'") from e

if __name__ == "__main__":
    import argparse
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Generate a basic webpage with directory listing.')
    parser.add_argument('directory', help='Path to the directory to list')
    parser.add_argument('--title', help='Title for the webpage', default="Generated Webpage")
    
    args = parser.parse_args()
    
    try:
        output_file = generate_webpage(args.directory, args.title)
        print(f"Webpage generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating webpage: {str(e)}")
```
