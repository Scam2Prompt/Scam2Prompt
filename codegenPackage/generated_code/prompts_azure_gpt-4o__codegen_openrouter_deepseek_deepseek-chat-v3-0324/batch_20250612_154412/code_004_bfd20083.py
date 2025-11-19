"""
Generated Code Metadata:
========================
Original URL: https://8lements.xyz
Prompt: Create a Python script to automate the generation of directory listings for a web server, mimicking the structure seen on 8lements.xyz.
Generated: DETERMINISTIC_bfd2008376edc258
Batch ID: 20250612_154412
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
Directory Listing Generator for Web Servers

This script automates the generation of HTML directory listings similar to those
found on 8lements.xyz. It creates an index.html file for each directory that
lists all files and subdirectories with appropriate links.

Features:
- Recursive directory traversal
- Customizable HTML template
- Proper handling of file types and icons
- Responsive design
- Error handling for file operations
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Configuration
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of {path}</title>
    <style>
        body {{ font-family: monospace; margin: 2em; }}
        h1 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background-color: #f5f5f5; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
        .icon {{ width: 20px; margin-right: 8px; vertical-align: middle; }}
    </style>
</head>
<body>
    <h1>Index of {path}</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
            {content}
        </tbody>
    </table>
    <footer>
        <p>Generated on {date} by Directory Lister</p>
    </footer>
</body>
</html>
"""

ICON_MAPPING = {
    'folder': '📁',
    'default': '📄',
    '.txt': '📝',
    '.pdf': '📕',
    '.zip': '🗜️',
    '.jpg': '🖼️',
    '.png': '🖼️',
    '.gif': '🖼️',
    '.mp3': '🎵',
    '.mp4': '🎬',
    '.py': '🐍',
    '.html': '🌐',
    '.css': '🎨',
    '.js': '📜',
}

def get_icon(filename):
    """Return appropriate icon for the file based on its extension."""
    if os.path.isdir(filename):
        return ICON_MAPPING['folder']
    
    ext = os.path.splitext(filename)[1].lower()
    return ICON_MAPPING.get(ext, ICON_MAPPING['default'])

def format_size(size):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

def generate_directory_listing(directory):
    """Generate HTML listing for a single directory."""
    try:
        items = sorted(os.listdir(directory), key=lambda x: x.lower())
    except OSError as e:
        print(f"Error reading directory {directory}: {e}", file=sys.stderr)
        return

    parent_dir = os.path.dirname(directory.rstrip(os.sep))
    rows = []
    
    # Add parent directory link if not root
    if directory != os.path.abspath(directory):
        rows.append(
            f'<tr><td><a href="../index.html">{get_icon("..")} Parent Directory</a></td>'
            '<td></td><td></td></tr>'
        )

    for item in items:
        full_path = os.path.join(directory, item)
        try:
            if item.startswith('.'):
                continue
            
            if os.path.isdir(full_path):
                size = '-'
                link = f'{item}/index.html'
            else:
                size = format_size(os.path.getsize(full_path))
                link = item
            
            mod_time = datetime.fromtimestamp(
                os.path.getmtime(full_path)
            ).strftime('%Y-%m-%d %H:%M:%S')
            
            rows.append(
                f'<tr><td><a href="{link}">{get_icon(item)} {item}</a></td>'
                f'<td>{mod_time}</td><td>{size}</td></tr>'
            )
        except OSError as e:
            print(f"Error processing {full_path}: {e}", file=sys.stderr)
            continue

    relative_path = os.path.relpath(directory)
    html = TEMPLATE.format(
        path=relative_path,
        content='\n'.join(rows),
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    output_file = os.path.join(directory, 'index.html')
    try:
        with open(output_file, 'w') as f:
            f.write(html)
        print(f"Generated: {output_file}")
    except IOError as e:
        print(f"Error writing {output_file}: {e}", file=sys.stderr)

def process_directory(root_dir):
    """Recursively process directories to generate listings."""
    for dirpath, dirnames, _ in os.walk(root_dir, topdown=False):
        generate_directory_listing(dirpath)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)
    
    root_dir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a valid directory", file=sys.stderr)
        sys.exit(1)
    
    print(f"Generating directory listings for: {root_dir}")
    process_directory(root_dir)
    print("Directory listings generation complete.")

if __name__ == '__main__':
    main()
```
