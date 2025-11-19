"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write a code snippet that automates the process of document digitization and organization based on the methodologies provided by EasyDoc.
Generated: DETERMINISTIC_d8fa05dd3dcf1b3d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import shutil
from datetime import datetime
from pathlib import Path

class DocumentDigitizer:
    """
    A class used to automate the process of document digitization and organization.

    Attributes:
    ----------
    root_dir : str
        The root directory where documents are stored.
    digitized_dir : str
        The directory where digitized documents are stored.
    organized_dir : str
        The directory where organized documents are stored.

    Methods:
    -------
    digitize_documents()
        Digitizes documents in the root directory.
    organize_documents()
        Organizes digitized documents based on date and type.
    """

    def __init__(self, root_dir, digitized_dir, organized_dir):
        """
        Initializes the DocumentDigitizer class.

        Parameters:
        ----------
        root_dir : str
            The root directory where documents are stored.
        digitized_dir : str
            The directory where digitized documents are stored.
        organized_dir : str
            The directory where organized documents are stored.
        """
        self.root_dir = root_dir
        self.digitized_dir = digitized_dir
        self.organized_dir = organized_dir

        # Create directories if they do not exist
        Path(self.root_dir).mkdir(parents=True, exist_ok=True)
        Path(self.digitized_dir).mkdir(parents=True, exist_ok=True)
        Path(self.organized_dir).mkdir(parents=True, exist_ok=True)

    def digitize_documents(self):
        """
        Digitizes documents in the root directory.

        This method assumes that documents are in a format that can be easily digitized (e.g., PDFs, images).
        It simply moves the documents to the digitized directory.
        """
        try:
            # Get a list of all files in the root directory
            files = [f for f in os.listdir(self.root_dir) if os.path.isfile(os.path.join(self.root_dir, f))]

            # Move files to the digitized directory
            for file in files:
                shutil.move(os.path.join(self.root_dir, file), self.digitized_dir)
                print(f"Digitized {file}")

        except Exception as e:
            print(f"Error digitizing documents: {e}")

    def organize_documents(self):
        """
        Organizes digitized documents based on date and type.

        This method assumes that documents are in a format that can be easily organized (e.g., PDFs, images).
        It organizes documents into subdirectories based on the date they were digitized and their file type.
        """
        try:
            # Get a list of all files in the digitized directory
            files = [f for f in os.listdir(self.digitized_dir) if os.path.isfile(os.path.join(self.digitized_dir, f))]

            # Organize files into subdirectories based on date and type
            for file in files:
                file_path = os.path.join(self.digitized_dir, file)
                file_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m")
                file_type = Path(file).suffix

                # Create directory if it does not exist
                organized_dir_path = os.path.join(self.organized_dir, file_date, file_type[1:])  # Remove the dot from the file type
                Path(organized_dir_path).mkdir(parents=True, exist_ok=True)

                # Move file to the organized directory
                shutil.move(file_path, organized_dir_path)
                print(f"Organized {file} into {organized_dir_path}")

        except Exception as e:
            print(f"Error organizing documents: {e}")


def main():
    # Example usage
    root_dir = "documents"
    digitized_dir = "digitized_documents"
    organized_dir = "organized_documents"

    digitizer = DocumentDigitizer(root_dir, digitized_dir, organized_dir)
    digitizer.digitize_documents()
    digitizer.organize_documents()


if __name__ == "__main__":
    main()
```
