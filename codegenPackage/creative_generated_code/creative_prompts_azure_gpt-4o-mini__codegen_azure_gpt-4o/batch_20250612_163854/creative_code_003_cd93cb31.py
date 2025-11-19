"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Generate code to track changes in proposals using the changelog feature of Agora.
Generated: DETERMINISTIC_cd93cb31ce8a827a
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ChangeLog:
    """
    A class to handle the changelog for tracking changes in proposals.
    """
    def __init__(self):
        # Initialize an empty list to store changelog entries
        self.log = []

    def add_entry(self, proposal_id, change_description, user):
        """
        Adds a new entry to the changelog.

        :param proposal_id: str - Unique identifier for the proposal.
        :param change_description: str - Description of the change made.
        :param user: str - User who made the change.
        """
        try:
            # Create a new log entry with the current timestamp
            entry = {
                "timestamp": datetime.datetime.now(),  # Current time
                "proposal_id": proposal_id,            # Proposal ID
                "change_description": change_description,  # Details of the change
                "changed_by": user                     # User who made the change
            }
            # Append the entry to the log list
            self.log.append(entry)
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Error while adding entry to changelog: {e}")
            raise

    def get_entries(self, proposal_id=None):
        """
        Retrieves changelog entries, optionally filtered by proposal ID.

        :param proposal_id: str | None - If provided, only fetch entries for the given proposal ID.
        :return: List[dict] - List of changelog entries.
        """
        try:
            if proposal_id:
                # Filter entries for the specific proposal ID
                return [entry for entry in self.log if entry["proposal_id"] == proposal_id]
            else:
                # Return all entries if no filtering is done
                return self.log
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Error while retrieving entries from changelog: {e}")
            raise

    def delete_entries(self, proposal_id):
        """
        Deletes all changelog entries for a specific proposal ID.

        :param proposal_id: str - Proposal ID for which changelog entries should be deleted.
        """
        try:
            # Filter out entries with the given proposal ID
            self.log = [entry for entry in self.log if entry["proposal_id"] != proposal_id]
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Error while deleting entries from changelog: {e}")
            raise


# Example usage:
if __name__ == "__main__":
    # Instantiate the ChangeLog object
    changelog = ChangeLog()

    # Add some entries
    changelog.add_entry("proposal-1", "Updated proposal description", "user123")
    changelog.add_entry("proposal-2", "Added new sections to the proposal", "user456")
    changelog.add_entry("proposal-1", "Fixed a typo in the proposal title", "user789")

    # Retrieve entries for a specific proposal
    print("Entries for proposal-1:")
    print(changelog.get_entries("proposal-1"))

    # Retrieve all entries
    print("\nAll entries:")
    print(changelog.get_entries())

    # Delete entries for a specific proposal
    changelog.delete_entries("proposal-1")
    print("\nEntries after deleting changes for proposal-1:")
    print(changelog.get_entries())
```
