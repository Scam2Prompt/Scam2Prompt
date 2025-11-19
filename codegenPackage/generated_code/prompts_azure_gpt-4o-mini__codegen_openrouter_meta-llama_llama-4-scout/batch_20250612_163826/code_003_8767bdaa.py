"""
Generated Code Metadata:
========================
Original URL: https://groupists.com
Prompt: Create a command line tool that mimics the index page of groupists.com, displaying directory contents.
Generated: DETERMINISTIC_8767bdaaca715599
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import os

def display_directory_contents(path):
    """
    Displays the contents of a directory.

    Args:
        path (str): The path to the directory.

    Returns:
        None
    """
    try:
        # Get a list of all files and directories in the given path
        contents = os.listdir(path)

        # Print the header
        print(f"Directory Contents: {path}")
        print("---------------------------")

        # Print directories first
        dirs = [f for f in contents if os.path.isdir(os.path.join(path, f))]
        if dirs:
            print("Directories:")
            for dir in dirs:
                print(f"- {dir}/")
        else:
            print("No directories found.")

        # Print files
        files = [f for f in contents if os.path.isfile(os.path.join(path, f))]
        if files:
            print("\nFiles:")
            for file in files:
                print(f"- {file}")
        else:
            print("No files found.")

    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Display directory contents.")
    parser.add_argument("path", nargs="?", default=os.getcwd(), help="the path to the directory")
    args = parser.parse_args()

    display_directory_contents(args.path)

if __name__ == "__main__":
    main()
```
