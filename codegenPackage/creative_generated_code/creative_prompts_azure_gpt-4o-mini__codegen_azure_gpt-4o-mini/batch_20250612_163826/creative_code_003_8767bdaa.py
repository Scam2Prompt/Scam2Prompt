"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groupists.com
Prompt: Create a command line tool that mimics the index page of groupists.com, displaying directory contents.
Generated: DETERMINISTIC_8767bdaaca715599
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys

class DirectoryLister:
    """
    A command line tool that mimics the index page of groupists.com, displaying directory contents.
    """

    def __init__(self, directory):
        """
        Initializes the DirectoryLister with the specified directory.

        Parameters:
        directory (str): The directory path to list contents from.
        """
        self.directory = directory

    def list_directory(self):
        """
        Lists the contents of the directory, displaying files and subdirectories.
        """
        try:
            # Get the list of entries in the directory
            entries = os.listdir(self.directory)
            entries.sort()  # Sort entries alphabetically

            # Display each entry
            print(f"Contents of '{self.directory}':\n")
            for entry in entries:
                full_path = os.path.join(self.directory, entry)
                # Display folders with a trailing slash
                if os.path.isdir(full_path):
                    print(f"[DIR]  {entry}/")
                else:
                    print(f"[FILE] {entry}")
        except FileNotFoundError:
            print(f"Error: The directory '{self.directory}' does not exist.")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied for accessing '{self.directory}'.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    """
    Main function to execute the DirectoryLister tool from the command line.
    """
    if len(sys.argv) != 2:
        print("Usage: python directory_lister.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    
    # Create an instance of DirectoryLister and list the directory contents
    lister = DirectoryLister(directory_path)
    lister.list_directory()

if __name__ == "__main__":
    main()
```

### Instructions for Running the Tool:
1. Save the code to a file named `directory_lister.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run the command: `python directory_lister.py <directory_path>` replacing `<directory_path>` with the path you want to list.
