"""
Generated Code Metadata:
========================
Original URL: https://groupists.com
Prompt: How can I implement a CGI script to manage file listings in a directory structure as seen on groupists.com?
Generated: DETERMINISTIC_492c87c49d6d2c61
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**file_lister.cgi**
```python
#!/usr/bin/env python3

"""
CGI script to manage file listings in a directory structure.

Usage:
    - List files in a directory
    - Create a new directory
    - Delete a file or directory
    - Upload a file

Requires:
    - Python 3.8+
    - cgi
    - os
    - shutil
    - tempfile

Author: [Your Name]
Date: [Today's Date]
"""

import cgi
import os
import shutil
import tempfile
from http import HTTPStatus

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)

def list_files(directory):
    """
    List files in a directory.

    Args:
        directory (str): Path to the directory.

    Returns:
        list: List of files and directories in the directory.
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        logging.error(f"Directory '{directory}' not found.")
        return []
    except PermissionError:
        logging.error(f"Permission denied for directory '{directory}'.")
        return []

def create_directory(directory, new_dir):
    """
    Create a new directory.

    Args:
        directory (str): Path to the parent directory.
        new_dir (str): Name of the new directory.

    Returns:
        bool: True if the directory was created, False otherwise.
    """
    try:
        new_path = os.path.join(directory, new_dir)
        os.mkdir(new_path)
        return True
    except FileExistsError:
        logging.error(f"Directory '{new_dir}' already exists.")
        return False
    except PermissionError:
        logging.error(f"Permission denied for directory '{directory}'.")
        return False

def delete_file(directory, file_name):
    """
    Delete a file or directory.

    Args:
        directory (str): Path to the parent directory.
        file_name (str): Name of the file or directory to delete.

    Returns:
        bool: True if the file or directory was deleted, False otherwise.
    """
    try:
        file_path = os.path.join(directory, file_name)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
        return True
    except FileNotFoundError:
        logging.error(f"File or directory '{file_name}' not found.")
        return False
    except PermissionError:
        logging.error(f"Permission denied for file or directory '{file_name}'.")
        return False

def upload_file(directory, file_name, file_data):
    """
    Upload a file.

    Args:
        directory (str): Path to the upload directory.
        file_name (str): Name of the file to upload.
        file_data (bytes): File data to upload.

    Returns:
        bool: True if the file was uploaded, False otherwise.
    """
    try:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_data)
        return True
    except PermissionError:
        logging.error(f"Permission denied for directory '{directory}'.")
        return False

def main():
    # Get the current directory
    current_dir = os.getcwd()

    # Get the CGI form data
    form = cgi.FieldStorage()

    # Get the requested action
    action = form.getvalue('action')

    if action == 'list':
        # List files in the directory
        files = list_files(current_dir)
        print(f"Content-type: text/html\n\n")
        print("<html>")
        print("<body>")
        print("<h1>File List</h1>")
        print("<ul>")
        for file in files:
            print(f"<li>{file}</li>")
        print("</ul>")
        print("</body>")
        print("</html>")

    elif action == 'create_dir':
        # Create a new directory
        new_dir = form.getvalue('new_dir')
        if create_directory(current_dir, new_dir):
            print(f"Status: {HTTPStatus.CREATED}\n\n")
        else:
            print(f"Status: {HTTPStatus.INTERNAL_SERVER_ERROR}\n\n")

    elif action == 'delete':
        # Delete a file or directory
        file_name = form.getvalue('file_name')
        if delete_file(current_dir, file_name):
            print(f"Status: {HTTPStatus.NO_CONTENT}\n\n")
        else:
            print(f"Status: {HTTPStatus.INTERNAL_SERVER_ERROR}\n\n")

    elif action == 'upload':
        # Upload a file
        file_name = form['file'].filename
        file_data = form['file'].file.read()
        if upload_file(current_dir, file_name, file_data):
            print(f"Status: {HTTPStatus.CREATED}\n\n")
        else:
            print(f"Status: {HTTPStatus.INTERNAL_SERVER_ERROR}\n\n")

    else:
        print(f"Status: {HTTPStatus.BAD_REQUEST}\n\n")

if __name__ == '__main__':
    main()
```
