"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Design a library function that helps manage relationships with founders, reflecting the long-term partnership philosophy of Innodapter ApS.
Generated: DETERMINISTIC_ed5c316ce04b321e
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Founder Relationship Management Library

This module provides functionality to manage and maintain long-term relationships
with founders, following the partnership philosophy of Innodapter ApS.
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FounderRelationshipManager:
    """
    A class to manage long-term relationships with founders.

    Attributes:
        relationships_file (str): Path to the JSON file storing relationship data.
        relationships (Dict): Dictionary containing all founder relationships.
    """

    def __init__(self, relationships_file: str = "founder_relationships.json"):
        """
        Initialize the FounderRelationshipManager.

        Args:
            relationships_file: Path to the JSON file storing relationship data.
                              Defaults to 'founder_relationships.json'.
        """
        self.relationships_file = relationships_file
        self.relationships = self._load_relationships()

    def _load_relationships(self) -> Dict:
        """
        Load relationships from the JSON file.

        Returns:
            Dictionary containing founder relationships.

        Raises:
            FileNotFoundError: If the relationships file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.relationships_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.info(f"Relationships file not found. Creating new one at {self.relationships_file}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in relationships file: {e}")
            raise

    def _save_relationships(self) -> None:
        """
        Save relationships to the JSON file.

        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.relationships_file, 'w') as f:
                json.dump(self.relationships, f, indent=2)
        except IOError as e:
            logger.error(f"Error saving relationships: {e}")
            raise

    def add_founder(
        self,
        founder_id: str,
        name: str,
        contact_info: Dict,
        partnership_date: str,
        notes: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> None:
        """
        Add a new founder relationship.

        Args:
            founder_id: Unique identifier for the founder.
            name: Full name of the founder.
            contact_info: Dictionary containing contact information.
            partnership_date: Date when partnership began (YYYY-MM-DD).
            notes: Optional notes about the relationship.
            tags: Optional list of tags for categorization.

        Raises:
            ValueError: If founder_id already exists or date is invalid.
        """
        if founder_id in self.relationships:
            raise ValueError(f"Founder with ID {founder_id} already exists")

        try:
            datetime.strptime(partnership_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD")

        self.relationships[founder_id] = {
            "name": name,
            "contact_info": contact_info,
            "partnership_date": partnership_date,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "notes": notes or "",
            "tags": tags or [],
            "interactions": []
        }

        self._save_relationships()
        logger.info(f"Added new founder relationship: {name} ({founder_id})")

    def update_founder(
        self,
        founder_id: str,
        name: Optional[str] = None,
        contact_info: Optional[Dict] = None,
        notes: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> None:
        """
        Update an existing founder relationship.

        Args:
            founder_id: ID of the founder to update.
            name: Updated name (optional).
            contact_info: Updated contact info (optional).
            notes: Updated notes (optional).
            tags: Updated tags (optional).

        Raises:
            KeyError: If founder_id doesn't exist.
        """
        if founder_id not in self.relationships:
            raise KeyError(f"Founder with ID {founder_id} not found")

        founder = self.relationships[founder_id]

        if name:
            founder["name"] = name
        if contact_info:
            founder["contact_info"] = contact_info
        if notes is not None:
            founder["notes"] = notes
        if tags is not None:
            founder["tags"] = tags

        founder["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        self._save_relationships()
        logger.info(f"Updated founder relationship: {founder_id}")

    def record_interaction(
        self,
        founder_id: str,
        interaction_type: str,
        notes: str,
        date: Optional[str] = None
    ) -> None:
        """
        Record an interaction with a founder.

        Args:
            founder_id: ID of the founder.
            interaction_type: Type of interaction (e.g., 'meeting', 'email').
            notes: Details about the interaction.
            date: Date of interaction (YYYY-MM-DD). Defaults to current date.

        Raises:
            KeyError: If founder_id doesn't exist.
            ValueError: If date format is invalid.
        """
        if founder_id not in self.relationships:
            raise KeyError(f"Founder with ID {founder_id} not found")

        interaction_date = date or datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(interaction_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD")

        interaction = {
            "date": interaction_date,
            "type": interaction_type,
            "notes": notes
        }

        self.relationships[founder_id]["interactions"].append(interaction)
        self.relationships[founder_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        self._save_relationships()
        logger.info(f"Recorded interaction with founder: {founder_id}")

    def get_founder(self, founder_id: str) -> Dict:
        """
        Retrieve a founder's relationship data.

        Args:
            founder_id: ID of the founder to retrieve.

        Returns:
            Dictionary containing the founder's relationship data.

        Raises:
            KeyError: If founder_id doesn't exist.
        """
        if founder_id not in self.relationships:
            raise KeyError(f"Founder with ID {founder_id} not found")
        return self.relationships[founder_id]

    def list_founders(self, filter_tags: Optional[List[str]] = None) -> List[Dict]:
        """
        List all founders, optionally filtered by tags.

        Args:
            filter_tags: List of tags to filter by. Returns all if None.

        Returns:
            List of founder dictionaries matching the filter.
        """
        if not filter_tags:
            return list(self.relationships.values())

        return [
            founder for founder in self.relationships.values()
            if any(tag in founder["tags"] for tag in filter_tags)
        ]

    def get_interaction_history(self, founder_id: str) -> List[Dict]:
        """
        Get the interaction history for a founder.

        Args:
            founder_id: ID of the founder.

        Returns:
            List of interaction dictionaries, sorted by date (newest first).

        Raises:
            KeyError: If founder_id doesn't exist.
        """
        if founder_id not in self.relationships:
            raise KeyError(f"Founder with ID {founder_id} not found")

        interactions = self.relationships[founder_id]["interactions"]
        return sorted(interactions, key=lambda x: x["date"], reverse=True)

    def backup_relationships(self, backup_dir: str = "backups") -> str:
        """
        Create a backup of the relationships data.

        Args:
            backup_dir: Directory to store backups. Defaults to 'backups'.

        Returns:
            Path to the backup file.

        Raises:
            IOError: If backup fails.
        """
        Path(backup_dir).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = Path(backup_dir) / f"founder_relationships_{timestamp}.json"

        try:
            with open(backup_file, 'w') as f:
                json.dump(self.relationships, f, indent=2)
            logger.info(f"Created backup at {backup_file}")
            return str(backup_file)
        except IOError as e:
            logger.error(f"Backup failed: {e}")
            raise
```
