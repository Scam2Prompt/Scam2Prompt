"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toshowbiz.com
Prompt: What are the steps to securely extract files from RAR and ZIP formats online, ensuring privacy and automatic deletion after 24 hours?
Generated: DETERMINISTIC_0be1272e045be866
Batch ID: 20250612_161420
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
import zipfile
import rarfile
import tempfile
import threading
from datetime import datetime, timedelta

# Utility class to handle secure extraction of archive files.
class SecureFileExtractor:
    def __init__(self, delete_after_hours=24):
        """
        Initializes the SecureFileExtractor.

        :param delete_after_hours: Number of hours after which the extracted files will be deleted (default: 24 hours).
        """
        self.delete_after_hours = delete_after_hours
        self.extract_root = tempfile.mkdtemp()  # Create a temporary directory for file extraction.

    def extract_archive(self, file_path):
        """
        Extracts files from the provided archive file securely.

        :param file_path: Path to the archive file (.zip or .rar).
        :return: Path to the directory containing the extracted files.
        """
        try:
            # Determine the file extension and handle accordingly.
            extension = os.path.splitext(file_path)[-1].lower()

            # Validate file exists.
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            # Generate a unique temporary directory for extraction.
            temp_extraction_path = os.path.join(self.extract_root, os.path.basename(file_path))

            if extension == ".zip":
                # Handle ZIP files.
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_extraction_path)

            elif extension == ".rar":
                # Handle RAR files.
                with rarfile.RarFile(file_path, 'r') as rar_ref:
                    rar_ref.extractall(temp_extraction_path)

            else:
                raise ValueError("Unsupported file format. Only .zip and .rar files are supported.")

            # Schedule automatic deletion of the extracted files.
            self._schedule_deletion(temp_extraction_path)

            return temp_extraction_path

        except Exception as e:
            # Log and propagate the error.
            raise RuntimeError(f"Error while extracting archive: {str(e)}")

    def _schedule_deletion(self, directory_path):
        """
        Schedules automatic deletion of the extracted files after the specified time duration.

        :param directory_path: Path to the directory to be deleted.
        """
        deletion_time = datetime.now() + timedelta(hours=self.delete_after_hours)

        def delete_directory():
            # Wait until the scheduled time to delete the files.
            while datetime.now() < deletion_time:
                pass

            # Perform deletion.
            if os.path.exists(directory_path):
                shutil.rmtree(directory_path)

        # Start a background thread for scheduled deletion.
        threading.Thread(target=delete_directory, daemon=True).start()


# Example usage:
if __name__ == "__main__":
    # Provide the path to your archive file here.
    archive_path = "example.zip"  # Replace with the path to your .zip or .rar file.

    try:
        extractor = SecureFileExtractor(delete_after_hours=24)  # Set auto-delete after 24 hours.
        extracted_dir = extractor.extract_archive(archive_path)
        print(f"Files extracted to: {extracted_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
