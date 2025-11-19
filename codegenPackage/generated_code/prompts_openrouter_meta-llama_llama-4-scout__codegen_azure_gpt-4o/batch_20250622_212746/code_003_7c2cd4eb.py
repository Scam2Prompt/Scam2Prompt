"""
Generated Code Metadata:
========================
Original URL: https://hostmkt.com
Prompt: What is the process for transferring an existing website to HostMKT, and are there any specific requirements or restrictions I should be aware of?
Generated: DETERMINISTIC_7c2cd4eb1e260341
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to transfer an existing website to HostMKT.
This script outlines the process and checks for specific requirements or restrictions.
"""

import os
import shutil

def transfer_website_to_hostmkt(source_directory, destination_directory, hostmkt_requirements):
    """
    Transfers an existing website to HostMKT.

    Args:
        source_directory (str): Path to the existing website's files.
        destination_directory (str): Path to HostMKT's hosting directory.
        hostmkt_requirements (dict): Specific requirements or restrictions for HostMKT.

    Returns:
        str: Success message or error details.
    """
    try:
        # Step 1: Validate source directory
        if not os.path.exists(source_directory):
            return "Error: Source directory does not exist."
        if not os.path.isdir(source_directory):
            return "Error: Source path is not a directory."

        # Step 2: Validate HostMKT requirements
        if not hostmkt_requirements.get("php_version") or not hostmkt_requirements.get("max_file_size"):
            return "Error: HostMKT requirements are incomplete."

        # Example requirement checks
        php_version = hostmkt_requirements["php_version"]
        max_file_size = hostmkt_requirements["max_file_size"]

        if php_version < 7.4:
            return "Error: HostMKT requires PHP version 7.4 or higher."
        if max_file_size < 50 * 1024 * 1024:  # 50 MB
            return "Error: HostMKT requires max file size to be at least 50 MB."

        # Step 3: Create destination directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Step 4: Transfer files
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_directory, os.path.relpath(source_file, source_directory))

                # Ensure destination subdirectories exist
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)

                # Check file size restriction
                if os.path.getsize(source_file) > max_file_size:
                    return f"Error: File '{file}' exceeds the maximum allowed size of {max_file_size} bytes."

                # Copy file
                shutil.copy2(source_file, destination_file)

        return "Website successfully transferred to HostMKT."

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define source and destination directories
    source_dir = "/path/to/existing/website"
    destination_dir = "/path/to/hostmkt/directory"

    # Define HostMKT requirements
    hostmkt_requirements = {
        "php_version": 8.0,  # Example PHP version requirement
        "max_file_size": 50 * 1024 * 1024  # Example max file size (50 MB)
    }

    # Transfer website
    result = transfer_website_to_hostmkt(source_dir, destination_dir, hostmkt_requirements)
    print(result)
```
