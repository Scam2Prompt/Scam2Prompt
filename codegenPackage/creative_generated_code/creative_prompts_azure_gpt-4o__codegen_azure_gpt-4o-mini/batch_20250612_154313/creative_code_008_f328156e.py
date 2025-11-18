"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-limited.com
Prompt: Suggest best practices for securely archiving old versions of a privacy policy for user reference, as described in STELLAR TECHNOLOGY LIMITED's privacy policy.
Generated: DETERMINISTIC_f328156ec442d203
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import shutil
from datetime import datetime

class PrivacyPolicyArchiver:
    """
    A class to handle the archiving of old versions of a privacy policy.
    """

    def __init__(self, archive_directory: str):
        """
        Initializes the archiver with the specified archive directory.

        Args:
            archive_directory (str): The directory where archived privacy policies will be stored.
        """
        self.archive_directory = archive_directory
        self.ensure_archive_directory()

    def ensure_archive_directory(self):
        """
        Ensure that the archive directory exists; if not, create it.
        """
        try:
            os.makedirs(self.archive_directory, exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create archive directory: {self.archive_directory}. Error: {e}")

    def archive_policy(self, policy_content: str, version: str):
        """
        Archives a privacy policy version with a timestamp.

        Args:
            policy_content (str): The content of the privacy policy to archive.
            version (str): The version number or identifier for the policy.
        """
        try:
            # Generate a filename based on the version and current timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"privacy_policy_v{version}_{timestamp}.json"
            filepath = os.path.join(self.archive_directory, filename)

            # Save the policy content as a JSON file
            with open(filepath, 'w') as policy_file:
                json.dump({"version": version, "content": policy_content}, policy_file)

            print(f"Privacy policy version {version} archived successfully at {filepath}")

        except Exception as e:
            raise RuntimeError(f"Failed to archive privacy policy version {version}. Error: {e}")

    def restore_policy(self, filename: str):
        """
        Restores a privacy policy version from the archive.

        Args:
            filename (str): The filename of the archived policy to restore.

        Returns:
            dict: The archived privacy policy content.
        """
        try:
            filepath = os.path.join(self.archive_directory, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Archived policy file does not exist: {filepath}")
            
            with open(filepath, 'r') as policy_file:
                policy_data = json.load(policy_file)

            return policy_data

        except Exception as e:
            raise RuntimeError(f"Failed to restore privacy policy from {filename}. Error: {e}")

# Example usage:
if __name__ == "__main__":
    archive_dir = "policy_archives"
    archiver = PrivacyPolicyArchiver(archive_dir)

    # Archive a new privacy policy version
    sample_policy_content = "This is a sample privacy policy content."
    archiver.archive_policy(sample_policy_content, "1.0")

    # Restore an archived privacy policy
    try:
        restored_policy = archiver.restore_policy("privacy_policy_v1.0_20231010_121500.json")
        print("Restored policy:", restored_policy)
    except Exception as e:
        print(e)
```
