"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Write code to upload and organize photos and media files in a genealogy database, referencing the media attachment system described on the Meyer/Seim family website.
Generated: DETERMINISTIC_fce6826baa2e8be2
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from datetime import datetime

class GenealogyMediaManager:
    """
    This class manages the upload and organization of photos and media files
    in a genealogy database. Files are organized by family name and date.
    """

    def __init__(self, base_directory="genealogy_media"):
        """
        Initializes the media manager with a base directory.

        Args:
            base_directory (str): The root directory where media files will be stored.
        """
        self.base_directory = base_directory
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

    def upload_media(self, file_path, family_name):
        """
        Uploads and organizes a media file for a specific family.

        Args:
            file_path (str): Path to the local file to upload.
            family_name (str): The family name for organizing the media file.

        Returns:
            str: The final path of the uploaded file in the genealogy database.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        # Ensure the family directory exists
        family_directory = os.path.join(self.base_directory, family_name)
        if not os.path.exists(family_directory):
            os.makedirs(family_directory)

        # Subdirectory for the current date
        date_directory = os.path.join(family_directory, datetime.now().strftime("%Y-%m-%d"))
        if not os.path.exists(date_directory):
            os.makedirs(date_directory)

        # Generate final file path
        file_name = os.path.basename(file_path)
        final_file_path = os.path.join(date_directory, file_name)

        # Handle duplicate file names
        counter = 1
        while os.path.exists(final_file_path):
            name, ext = os.path.splitext(file_name)
            final_file_path = os.path.join(date_directory, f"{name}_{counter}{ext}")
            counter += 1

        # Copy the file to the final destination
        shutil.copy2(file_path, final_file_path)

        return final_file_path

    def list_media(self, family_name):
        """
        Lists all media files for a specific family.

        Args:
            family_name (str): The family name whose media files to list.

        Returns:
            list: A list of all file paths for the specified family.
        """
        family_directory = os.path.join(self.base_directory, family_name)
        if not os.path.exists(family_directory):
            raise FileNotFoundError(f"The family directory '{family_name}' does not exist.")

        media_files = []
        for root, _, files in os.walk(family_directory):
            for file in files:
                media_files.append(os.path.join(root, file))

        return media_files

    def delete_media(self, file_path):
        """
        Deletes a specific media file.

        Args:
            file_path (str): The path to the file to delete.

        Returns:
            bool: True if the file was deleted successfully, False otherwise.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
            return False


# Sample usage (if this were part of a script)
if __name__ == "__main__":
    manager = GenealogyMediaManager()

    try:
        # Example: Upload a media file
        uploaded_path = manager.upload_media("example.jpg", "Meyer_Seim")
        print(f"Uploaded to: {uploaded_path}")

        # Example: List media files for a family
        media_files = manager.list_media("Meyer_Seim")
        print("Media files:", media_files)

        # Example: Delete a media file
        if media_files:
            success = manager.delete_media(media_files[0])
            print(f"File deletion successful: {success}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
