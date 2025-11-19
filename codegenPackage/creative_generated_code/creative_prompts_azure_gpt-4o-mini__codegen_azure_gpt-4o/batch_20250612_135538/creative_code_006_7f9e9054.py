"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective.events
Prompt: How can I utilize Dropbox's version history and recovery features in my file management system?
Generated: DETERMINISTIC_7f9e905428e66b06
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code utilizing Dropbox's SDK to access version history and recovery features. It adheres to your requirements.

```python
import dropbox
from dropbox.exceptions import ApiError

# Access Token for the Dropbox account
ACCESS_TOKEN = 'your_access_token_here'

class DropboxManager:
    """
    DropboxManager provides methods to interact with Dropbox API for version history
    and file recovery features.
    """

    def __init__(self, access_token):
        """
        Initialize DropboxManager with an access token.

        :param access_token: The OAuth access token for the Dropbox account.
        """
        self.dbx = dropbox.Dropbox(access_token)

    def list_versions(self, file_path):
        """
        List all available versions (revisions) of a given file.

        :param file_path: Path to the file in Dropbox.
        :return: A list of file revisions with metadata.
        """
        try:
            revisions = self.dbx.files_list_revisions(file_path, mode=dropbox.files.ListRevisionsMode.PATH, limit=100)
            return revisions.entries
        except ApiError as e:
            print(f"Error retrieving version history: {e}")
            return []

    def restore_version(self, file_path, revision_id):
        """
        Restore a specific version of a file based on its revision ID.

        :param file_path: Path to the file in Dropbox.
        :param revision_id: The revision ID of the version to restore.
        :return: Metadata of the restored file.
        """
        try:
            restored_file = self.dbx.files_restore(file_path, revision_id)
            return restored_file
        except ApiError as e:
            print(f"Error restoring file version: {e}")
            return None


def main():
    """
    Example usage of DropboxManager:
    1. List available versions of a file.
    2. Restore a specific version.
    """
    # Initialize DropboxManager with your access token
    dropbox_manager = DropboxManager(ACCESS_TOKEN)

    # File path in Dropbox (update this path to an actual file)
    file_path = '/path/to/your/file.txt'

    # Step 1: List available versions (revisions) of the file
    print("Fetching version history...")
    versions = dropbox_manager.list_versions(file_path)
    if not versions:
        print("No versions found or an error occurred.")
        return

    print("Available versions:")
    for i, version in enumerate(versions):
        print(f"{i + 1}. Revision ID: {version.rev}, Modified: {version.server_modified}")

    # Step 2: Prompt user to select a version to restore
    try:
        choice = int(input(f"Enter the number of the version to restore (1-{len(versions)}): "))
        if 1 <= choice <= len(versions):
            revision_to_restore = versions[choice - 1].rev
            print(f"Restoring version: {revision_to_restore}...")
            restored_file = dropbox_manager.restore_version(file_path, revision_to_restore)
            if restored_file:
                print(f"File restored successfully! Metadata: {restored_file}")
            else:
                print("Failed to restore the file.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
```

**NOTE**: Replace `'your_access_token_here'` with a valid access token obtained from Dropbox API. You will need to install the Dropbox Python SDK (`pip install dropbox`) before running this script.
