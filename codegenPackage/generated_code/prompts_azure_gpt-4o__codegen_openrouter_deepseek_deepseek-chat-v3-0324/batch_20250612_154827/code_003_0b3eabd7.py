"""
Generated Code Metadata:
========================
Original URL: https://vanillagift.remadet.com
Prompt: Write code to automate the creation of a custom directory index page for LiteSpeed Web Server using Python.
Generated: DETERMINISTIC_0b3eabd744a30d6a
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Automates the creation of a custom directory index page for LiteSpeed Web Server.
Generates an HTML index page listing all files and directories in the specified path.
"""

import os
import argparse
from datetime import datetime
from pathlib import Path

def generate_index_html(directory_path, output_file=None, title=None):
    """
    Generates an HTML index page for the given directory.
    
    Args:
        directory_path (str): Path to the directory to index
        output_file (str, optional): Output HTML file path. Defaults to 'index.html' in directory.
        title (str, optional): Title for the HTML page. Defaults to directory name.
    """
    try:
        path = Path(directory_path).resolve()
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory_path}")

        # Set default output file and title if not provided
        if output_file is None:
            output_file = path / 'index.html'
        else:
            output_file = Path(output_file).resolve()

        if title is None:
            title = f"Index of {path.name}"

        # Get directory contents
        items = []
        for item in sorted(path.iterdir()):
            stat = item.stat()
            items.append({
                'name': item.name,
                'is_dir': item.is_dir(),
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            })

        # Generate HTML
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #f5f5f5; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
        .dir {{ font-weight: bold; }}
        .size {{ text-align: right; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th class="size">Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
"""

        # Add parent directory link if not root
        if path.parent != path:
            html += f"""            <tr>
                <td><a href="../">Parent Directory</a></td>
                <td class="size">-</td>
                <td>-</td>
            </tr>
"""

        # Add directory contents
        for item in items:
            size = "-" if item['is_dir'] else f"{item['size']:,} bytes"
            cls = "dir" if item['is_dir'] else ""
            html += f"""            <tr>
                <td><a href="{item['name']}{'/' if item['is_dir'] else ''}" class="{cls}">{item['name']}{'/' if item['is_dir'] else ''}</a></td>
                <td class="size">{size}</td>
                <td>{item['modified']}</td>
            </tr>
"""

        html += """        </tbody>
    </table>
</body>
</html>
"""

        # Write to file
        with open(output_file, 'w') as f:
            f.write(html)

        print(f"Successfully generated index at: {output_file}")

    except Exception as e:
        print(f"Error generating index: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Generate directory index page for LiteSpeed Web Server')
    parser.add_argument('directory', help='Directory path to generate index for')
    parser.add_argument('-o', '--output', help='Output HTML file path (default: directory/index.html)')
    parser.add_argument('-t', '--title', help='Title for the HTML page (default: "Index of directory")')
    
    args = parser.parse_args()
    
    try:
        generate_index_html(args.directory, args.output, args.title)
    except Exception as e:
        print(f"Failed to generate index: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
```
