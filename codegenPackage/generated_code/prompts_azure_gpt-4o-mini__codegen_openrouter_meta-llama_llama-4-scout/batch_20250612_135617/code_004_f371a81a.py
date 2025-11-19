"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Create a function that checks for the presence of documentation files (.DOC, .RTF, .TXT) in a screen saver package, inspired by the content from Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f371a81a40c0c386
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def check_documentation_files(package_path):
    """
    Checks for the presence of documentation files (.DOC, .RTF, .TXT) in a screen saver package.

    Args:
        package_path (str): The path to the screen saver package.

    Returns:
        dict: A dictionary containing a boolean indicating the presence of documentation files and a list of found files.

    Raises:
        FileNotFoundError: If the package path does not exist.
        NotADirectoryError: If the package path is not a directory.
    """

    # Check if the package path exists
    if not os.path.exists(package_path):
        raise FileNotFoundError(f"The package path '{package_path}' does not exist.")

    # Check if the package path is a directory
    if not os.path.isdir(package_path):
        raise NotADirectoryError(f"The package path '{package_path}' is not a directory.")

    # Initialize a list to store the found documentation files
    documentation_files = []

    # Define the supported documentation file extensions
    supported_extensions = ['.doc', '.rtf', '.txt']

    # Iterate over all files in the package directory
    for root, dirs, files in os.walk(package_path):
        for file in files:
            # Get the file extension
            file_extension = os.path.splitext(file)[1].lower()

            # Check if the file has a supported documentation file extension
            if file_extension in supported_extensions:
                # Add the file to the list of documentation files
                documentation_files.append(os.path.join(root, file))

    # Return a dictionary containing a boolean indicating the presence of documentation files and the list of found files
    return {
        'present': len(documentation_files) > 0,
        'files': documentation_files
    }


def main():
    try:
        package_path = '.'  # Replace with the desired package path
        result = check_documentation_files(package_path)

        print(f"Documentation files present: {result['present']}")
        print("Found files:")
        for file in result['files']:
            print(file)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
