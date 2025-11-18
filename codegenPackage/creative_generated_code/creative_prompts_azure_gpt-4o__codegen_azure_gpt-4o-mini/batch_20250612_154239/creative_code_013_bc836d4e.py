"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Suggest tools or libraries to implement a clear UI bug resolution system for blockchain applications, inspired by Guildhall's "Clear UI Bug" section.
Generated: DETERMINISTIC_bc836d4e85a21da3
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# clear_ui_bug_resolution.py

"""
This module implements a simple UI bug resolution system for blockchain applications.
It allows users to submit bugs, track their status, and manage resolution workflows.
"""

import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Bug:
    """
    A class to represent a UI bug.

    Attributes:
        bug_id (str): Unique identifier for the bug.
        description (str): A brief description of the bug.
        status (str): Current status of the bug (e.g., 'open', 'in progress', 'resolved').
        created_at (datetime): The timestamp when the bug was created.
    """

    def __init__(self, description: str):
        self.bug_id = str(uuid.uuid4())
        self.description = description
        self.status = 'open'
        self.created_at = datetime.now()

    def __str__(self):
        return f'[{self.bug_id}] - {self.description} (Status: {self.status})'


class BugResolutionSystem:
    """
    A class to manage the bug resolution process.

    Attributes:
        bugs (List[Bug]): A list to store all reported bugs.
    """

    def __init__(self):
        self.bugs: List[Bug] = []

    def report_bug(self, description: str) -> Bug:
        """
        Report a new bug.

        Args:
            description (str): A description of the bug.
        
        Returns:
            Bug: The created Bug instance.
        """
        if not description:
            raise ValueError("Bug description cannot be empty.")
        
        new_bug = Bug(description)
        self.bugs.append(new_bug)
        return new_bug

    def update_bug_status(self, bug_id: str, new_status: str) -> Optional[Bug]:
        """
        Update the status of a reported bug.

        Args:
            bug_id (str): The unique identifier of the bug.
            new_status (str): The new status to set.

        Returns:
            Optional[Bug]: The updated Bug instance, or None if not found.

        Raises:
            ValueError: If the new status is invalid.
        """
        valid_statuses = ['open', 'in progress', 'resolved']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {valid_statuses}")

        for bug in self.bugs:
            if bug.bug_id == bug_id:
                bug.status = new_status
                return bug
        return None

    def list_bugs(self) -> List[Dict[str, str]]:
        """
        List all reported bugs with their details.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing bug details.
        """
        return [{'bug_id': bug.bug_id, 'description': bug.description, 'status': bug.status} for bug in self.bugs]


if __name__ == "__main__":
    # Example usage:
    try:
        bug_system = BugResolutionSystem()
        bug1 = bug_system.report_bug("UI freezes on click")
        print(bug1)

        bug_system.update_bug_status(bug1.bug_id, "in progress")
        print(bug_system.list_bugs())

        bug_system.update_bug_status(bug1.bug_id, "resolved")
        print(bug_system.list_bugs())

    except ValueError as e:
        print(f"Error: {e}")
```
