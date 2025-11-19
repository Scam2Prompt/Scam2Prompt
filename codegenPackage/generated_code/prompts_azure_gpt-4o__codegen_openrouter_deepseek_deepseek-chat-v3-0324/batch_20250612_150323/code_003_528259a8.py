"""
Generated Code Metadata:
========================
Original URL: https://openseal.ch
Prompt: Create a checklist management system inspired by the Inspect tool from Openseal.ch, using Python and a suitable library.
Generated: DETERMINISTIC_528259a85cf44c68
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid
from datetime import datetime

class ChecklistItemStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()

@dataclass
class ChecklistItem:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str = ""
    status: ChecklistItemStatus = ChecklistItemStatus.NOT_STARTED
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def update_status(self, new_status: ChecklistItemStatus):
        self.status = new_status
        self.updated_at = datetime.now()

@dataclass
class Checklist:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str = ""
    items: List[ChecklistItem] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def add_item(self, item: ChecklistItem):
        self.items.append(item)
        self.updated_at = datetime.now()

    def remove_item(self, item_id: str) -> bool:
        for i, item in enumerate(self.items):
            if item.id == item_id:
                self.items.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def get_item(self, item_id: str) -> Optional[ChecklistItem]:
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update_item_status(self, item_id: str, new_status: ChecklistItemStatus) -> bool:
        item = self.get_item(item_id)
        if item:
            item.update_status(new_status)
            self.updated_at = datetime.now()
            return True
        return False

class ChecklistManager:
    def __init__(self, storage_path: str = "checklists.json"):
        self.storage_path = storage_path
        self.checklists: Dict[str, Checklist] = {}
        self._load_checklists()

    def _load_checklists(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r") as f:
                    data = json.load(f)
                    self.checklists = {
                        checklist_id: Checklist(
                            id=checklist_id,
                            title=checklist_data["title"],
                            description=checklist_data["description"],
                            items=[
                                ChecklistItem(
                                    id=item_data["id"],
                                    title=item_data["title"],
                                    description=item_data["description"],
                                    status=ChecklistItemStatus[item_data["status"]],
                                    created_at=datetime.fromisoformat(item_data["created_at"]),
                                    updated_at=datetime.fromisoformat(item_data["updated_at"])
                                )
                                for item_data in checklist_data["items"]
                            ],
                            created_at=datetime.fromisoformat(checklist_data["created_at"]),
                            updated_at=datetime.fromisoformat(checklist_data["updated_at"])
                        )
                        for checklist_id, checklist_data in data.items()
                    }
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                raise ValueError(f"Failed to load checklists: {str(e)}")

    def _save_checklists(self):
        try:
            with open(self.storage_path, "w") as f:
                json.dump(
                    {
                        checklist.id: {
                            "title": checklist.title,
                            "description": checklist.description,
                            "items": [
                                {
                                    "id": item.id,
                                    "title": item.title,
                                    "description": item.description,
                                    "status": item.status.name,
                                    "created_at": item.created_at.isoformat(),
                                    "updated_at": item.updated_at.isoformat()
                                }
                                for item in checklist.items
                            ],
                            "created_at": checklist.created_at.isoformat(),
                            "updated_at": checklist.updated_at.isoformat()
                        }
                        for checklist in self.checklists.values()
                    },
                    f,
                    indent=2
                )
        except (IOError, TypeError) as e:
            raise ValueError(f"Failed to save checklists: {str(e)}")

    def create_checklist(self, title: str, description: str = "") -> Checklist:
        checklist = Checklist(title=title, description=description)
        self.checklists[checklist.id] = checklist
        self._save_checklists()
        return checklist

    def get_checklist(self, checklist_id: str) -> Optional[Checklist]:
        return self.checklists.get(checklist_id)

    def update_checklist(self, checklist_id: str, title: str = None, description: str = None) -> bool:
        checklist = self.get_checklist(checklist_id)
        if not checklist:
            return False
        
        if title is not None:
            checklist.title = title
        if description is not None:
            checklist.description = description
        
        checklist.updated_at = datetime.now()
        self._save_checklists()
        return True

    def delete_checklist(self, checklist_id: str) -> bool:
        if checklist_id in self.checklists:
            del self.checklists[checklist_id]
            self._save_checklists()
            return True
        return False

    def add_item_to_checklist(self, checklist_id: str, item: ChecklistItem) -> bool:
        checklist = self.get_checklist(checklist_id)
        if checklist:
            checklist.add_item(item)
            self._save_checklists()
            return True
        return False

    def remove_item_from_checklist(self, checklist_id: str, item_id: str) -> bool:
        checklist = self.get_checklist(checklist_id)
        if checklist:
            success = checklist.remove_item(item_id)
            if success:
                self._save_checklists()
            return success
        return False

    def update_item_status_in_checklist(self, checklist_id: str, item_id: str, new_status: ChecklistItemStatus) -> bool:
        checklist = self.get_checklist(checklist_id)
        if checklist:
            success = checklist.update_item_status(item_id, new_status)
            if success:
                self._save_checklists()
            return success
        return False

    def list_checklists(self) -> List[Checklist]:
        return list(self.checklists.values())

if __name__ == "__main__":
    # Example usage
    manager = ChecklistManager()
    
    # Create a new checklist
    checklist = manager.create_checklist("Security Audit", "Checklist for security audit procedures")
    
    # Add items to the checklist
    item1 = ChecklistItem(title="Check firewall rules", description="Verify all firewall rules are properly configured")
    item2 = ChecklistItem(title="Review user permissions", description="Ensure least privilege principle is followed")
    
    manager.add_item_to_checklist(checklist.id, item1)
    manager.add_item_to_checklist(checklist.id, item2)
    
    # Update item status
    manager.update_item_status_in_checklist(checklist.id, item1.id, ChecklistItemStatus.COMPLETED)
    
    # List all checklists
    for cl in manager.list_checklists():
        print(f"Checklist: {cl.title}")
        for item in cl.items:
            print(f" - {item.title} [{item.status.name}]")
```
