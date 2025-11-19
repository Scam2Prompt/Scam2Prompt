"""
Generated Code Metadata:
========================
Original URL: https://contentxlabs.dev
Prompt: "Design a content metadata management system for AI licensing, inspired by ContentXLabs' approach to supporting metadata for mp4 files."
Generated: DETERMINISTIC_5657dd8c2cb09d8c
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_metadata_management_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4
from datetime import datetime
import json

class MetadataType(str, Enum):
    """Types of metadata."""
    TITLE = "title"
    DESCRIPTION = "description"
    TAGS = "tags"
    CATEGORY = "category"
    LICENSE = "license"

@dataclass
class ContentMetadata:
    """Content metadata data class."""
    id: str
    title: str
    description: str
    tags: List[str]
    category: str
    license: str
    created_at: str
    updated_at: str

    @classmethod
    def create(cls, title: str, description: str, tags: List[str], category: str, license: str) -> 'ContentMetadata':
        """Create a new content metadata instance."""
        id = str(uuid4())
        created_at = datetime.now().isoformat()
        updated_at = created_at
        return cls(id, title, description, tags, category, license, created_at, updated_at)

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "category": self.category,
            "license": self.license,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class ContentMetadataManagementSystem:
    """Content metadata management system."""

    def __init__(self):
        self.metadata: Dict[str, ContentMetadata] = {}

    def create_metadata(self, title: str, description: str, tags: List[str], category: str, license: str) -> ContentMetadata:
        """Create a new content metadata."""
        metadata = ContentMetadata.create(title, description, tags, category, license)
        self.metadata[metadata.id] = metadata
        return metadata

    def get_metadata(self, id: str) -> ContentMetadata:
        """Get content metadata by id."""
        try:
            return self.metadata[id]
        except KeyError:
            raise ValueError(f"Metadata with id {id} not found.")

    def update_metadata(self, id: str, title: str = None, description: str = None, tags: List[str] = None, category: str = None, license: str = None) -> ContentMetadata:
        """Update content metadata."""
        metadata = self.get_metadata(id)
        if title:
            metadata.title = title
        if description:
            metadata.description = description
        if tags:
            metadata.tags = tags
        if category:
            metadata.category = category
        if license:
            metadata.license = license
        metadata.updated_at = datetime.now().isoformat()
        self.metadata[id] = metadata
        return metadata

    def delete_metadata(self, id: str) -> None:
        """Delete content metadata."""
        try:
            del self.metadata[id]
        except KeyError:
            raise ValueError(f"Metadata with id {id} not found.")

def main():
    # Example usage
    system = ContentMetadataManagementSystem()

    metadata = system.create_metadata(
        title="Example Video",
        description="This is an example video.",
        tags=["example", "video"],
        category="entertainment",
        license="creative_commons"
    )

    print(json.dumps(metadata.to_dict(), indent=4))

    updated_metadata = system.update_metadata(metadata.id, title="Updated Example Video")
    print(json.dumps(updated_metadata.to_dict(), indent=4))

    system.delete_metadata(metadata.id)

if __name__ == "__main__":
    main()
```
