"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Write Python code to integrate a document management system for organizing, digitalizing, and securely storing files, referencing solutions similar to those provided by EasyDoc Gestão.
Generated: DETERMINISTIC_cba3854421668a18
Batch ID: 20250612_154306
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
import hashlib
from datetime import datetime

class DocumentManagementSystem:
    """
    A Document Management System (DMS) for organizing, digitalizing, and securely storing files.
    """

    def __init__(self, storage_dir="document_storage"):
        """
        Initialize the DMS with a storage directory.

        :param storage_dir: Directory where files will be securely stored.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)  # Ensure the storage directory exists

    def _generate_file_hash(self, file_path):
        """
        Generate a SHA256 hash for the given file to ensure secure storage.

        :param file_path: Path to the file to generate the hash for.
        :return: Hexadecimal hash value as a string.
        """
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError("The specified file does not exist.")
        except Exception as e:
            raise Exception(f"Error generating file hash: {e}")

    def add_file(self, file_path, category="general"):
        """
        Add a file to the document management system.

        :param file_path: Path to the file to be added.
        :param category: Category to store the file under (e.g., 'invoices', 'reports').
        :return: New file path in the storage directory.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file does not exist.")

        try:
            # Generate unique hash for the file
            file_hash = self._generate_file_hash(file_path)

            # Create category directory if it doesn't exist
            category_dir = os.path.join(self.storage_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            # Get file extension and create new filename
            _, file_extension = os.path.splitext(file_path)
            new_filename = f"{file_hash}{file_extension}"

            # Copy file to storage directory
            new_file_path = os.path.join(category_dir, new_filename)
            shutil.copy2(file_path, new_file_path)

            return new_file_path
        except Exception as e:
            raise Exception(f"Error adding file to DMS: {e}")

    def retrieve_files_by_category(self, category):
        """
        Retrieve all files stored under a specific category.

        :param category: Category name to retrieve files from.
        :return: List of file paths.
        """
        category_dir = os.path.join(self.storage_dir, category)
        if not os.path.exists(category_dir):
            raise FileNotFoundError("The specified category does not exist.")

        try:
            return [os.path.join(category_dir, file) for file in os.listdir(category_dir)]
        except Exception as e:
            raise Exception(f"Error retrieving files: {e}")

    def delete_file(self, category, filename):
        """
        Delete a specific file from the DMS.

        :param category: Category name where the file resides.
        :param filename: Name of the file to delete.
        """
        file_path = os.path.join(self.storage_dir, category, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError("The specified file does not exist.")

        try:
            os.remove(file_path)
        except Exception as e:
            raise Exception(f"Error deleting file: {e}")

    def backup_storage(self, backup_dir="document_backup"):
        """
        Create a backup of the entire storage directory.

        :param backup_dir: Directory where the backup will be stored.
        """
        try:
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
            shutil.copytree(self.storage_dir, backup_path)
        except Exception as e:
            raise Exception(f"Error creating backup: {e}")


# Example usage
if __name__ == "__main__":
    try:
        dms = DocumentManagementSystem()

        # Add a file to the system
        added_file_path = dms.add_file("example_document.pdf", category="invoices")
        print(f"File added at: {added_file_path}")

        # Retrieve files from a category
        files = dms.retrieve_files_by_category("invoices")
        print(f"Files in 'invoices': {files}")

        # Delete a file
        filename_to_delete = os.path.basename(added_file_path)
        dms.delete_file("invoices", filename_to_delete)
        print(f"Deleted file: {filename_to_delete}")

        # Backup storage
        dms.backup_storage()
        print("Backup created successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
