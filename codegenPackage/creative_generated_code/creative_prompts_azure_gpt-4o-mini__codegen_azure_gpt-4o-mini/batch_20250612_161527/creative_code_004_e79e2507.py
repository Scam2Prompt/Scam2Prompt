"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Illustrate how to implement a case management system for litigation briefs, utilizing concepts from the Ramdays litigation services.
Generated: DETERMINISTIC_e79e250791c7f340
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Optional, Dict

class LitigationBrief:
    """
    Represents a litigation brief in the case management system.
    """
    
    def __init__(self, title: str, description: str, case_number: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the brief
        self.title = title  # Title of the litigation brief
        self.description = description  # Description of the brief
        self.case_number = case_number  # Associated case number
        self.created_at = datetime.now()  # Timestamp when the brief was created

    def __repr__(self):
        return f"LitigationBrief(id={self.id}, title={self.title}, case_number={self.case_number})"


class CaseManagementSystem:
    """
    Manages litigation briefs for various cases.
    """

    def __init__(self):
        self.briefs: List[LitigationBrief] = []  # List to store litigation briefs

    def add_brief(self, title: str, description: str, case_number: str) -> LitigationBrief:
        """
        Adds a new litigation brief to the system.

        Args:
            title (str): Title of the litigation brief.
            description (str): Description of the brief.
            case_number (str): Associated case number.

        Returns:
            LitigationBrief: The created litigation brief.
        """
        if not title or not description or not case_number:
            raise ValueError("Title, description, and case number cannot be empty.")

        brief = LitigationBrief(title, description, case_number)
        self.briefs.append(brief)
        return brief

    def get_brief(self, brief_id: str) -> Optional[LitigationBrief]:
        """
        Retrieves a litigation brief by ID.

        Args:
            brief_id (str): The ID of the litigation brief.

        Returns:
            Optional[LitigationBrief]: The requested litigation brief or None if not found.
        """
        for brief in self.briefs:
            if brief.id == brief_id:
                return brief
        return None  # Brief not found

    def delete_brief(self, brief_id: str) -> bool:
        """
        Deletes a litigation brief by ID.

        Args:
            brief_id (str): The ID of the litigation brief to delete.

        Returns:
            bool: True if the brief was deleted, False if it did not exist.
        """
        for brief in self.briefs:
            if brief.id == brief_id:
                self.briefs.remove(brief)
                return True
        return False  # Brief not found

    def list_all_briefs(self) -> List[Dict]:
        """
        Lists all litigation briefs in a structured format.

        Returns:
            List[Dict]: A list of dictionaries representing all briefs.
        """
        return [vars(brief) for brief in self.briefs]


# Example usage:
if __name__ == "__main__":
    cms = CaseManagementSystem()

    # Adding briefs
    try:
        brief1 = cms.add_brief("Brief 1", "This is the first litigation brief.", "12345")
        print(f"Added: {brief1}")
        
        brief2 = cms.add_brief("Brief 2", "This is the second litigation brief.", "12346")
        print(f"Added: {brief2}")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing all briefs
    print("All briefs:", cms.list_all_briefs())

    # Retrieving a brief
    retrieved_brief = cms.get_brief(brief1.id)
    print("Retrieved brief:", retrieved_brief)

    # Deleting a brief
    deleted = cms.delete_brief(brief1.id)
    print("Deleted brief:", deleted)

    # Listing all briefs after deletion
    print("All briefs after deletion:", cms.list_all_briefs())
```
