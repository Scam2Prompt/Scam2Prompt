"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Python function to automate the generation of circulars or announcements, such as those published by the Politécnico Municipal de Cali, including details like dates, topics, and downloadable links.
Generated: DETERMINISTIC_a9a573636d75d27a
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import uuid


@dataclass
class Circular:
    """Data class representing a circular/announcement."""
    id: str
    title: str
    content: str
    publication_date: str
    effective_date: str
    topics: List[str]
    download_links: List[str]
    author: str
    is_active: bool = True

    def to_dict(self) -> Dict:
        """Convert Circular object to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "publication_date": self.publication_date,
            "effective_date": self.effective_date,
            "topics": self.topics,
            "download_links": self.download_links,
            "author": self.author,
            "is_active": self.is_active
        }


class CircularGenerator:
    """Class to generate and manage circulars/announcements."""
    
    def __init__(self, storage_path: str = "circulars_data"):
        """Initialize with storage path for circulars."""
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
    
    def _generate_id(self) -> str:
        """Generate a unique ID for each circular."""
        return str(uuid.uuid4())
    
    def _get_current_date(self) -> str:
        """Get current date in YYYY-MM-DD format."""
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    def _validate_input(self, title: str, content: str, topics: List[str]) -> bool:
        """Validate required fields for circular creation."""
        if not title or not content or not topics:
            return False
        return True
    
    def create_circular(
        self,
        title: str,
        content: str,
        topics: List[str],
        download_links: List[str],
        author: str,
        effective_date: Optional[str] = None
    ) -> Optional[Circular]:
        """Create a new circular with given details."""
        if not self._validate_input(title, content, topics):
            return None
        
        publication_date = self._get_current_date()
        effective_date = effective_date if effective_date else publication_date
        
        circular = Circular(
            id=self._generate_id(),
            title=title,
            content=content,
            publication_date=publication_date,
            effective_date=effective_date,
            topics=topics,
            download_links=download_links,
            author=author
        )
        
        self._save_circular(circular)
        return circular
    
    def _save_circular(self, circular: Circular) -> None:
        """Save circular to JSON file."""
        file_path = os.path.join(self.storage_path, f"{circular.id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(circular.to_dict(), f, ensure_ascii=False, indent=4)
    
    def get_circular(self, circular_id: str) -> Optional[Circular]:
        """Retrieve a circular by its ID."""
        file_path = os.path.join(self.storage_path, f"{circular_id}.json")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return Circular(**data)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def get_all_circulars(self) -> List[Circular]:
        """Retrieve all circulars from storage."""
        circulars = []
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                circular = self.get_circular(filename[:-5])  # Remove .json extension
                if circular:
                    circulars.append(circular)
        return circulars
    
    def update_circular(self, circular_id: str, **kwargs) -> Optional[Circular]:
        """Update an existing circular with new data."""
        circular = self.get_circular(circular_id)
        if not circular:
            return None
        
        for key, value in kwargs.items():
            if hasattr(circular, key):
                setattr(circular, key, value)
        
        self._save_circular(circular)
        return circular
    
    def deactivate_circular(self, circular_id: str) -> bool:
        """Deactivate a circular (mark as inactive)."""
        circular = self.get_circular(circular_id)
        if not circular:
            return False
        
        circular.is_active = False
        self._save_circular(circular)
        return True
    
    def generate_html(self, circular: Circular) -> str:
        """Generate HTML representation of a circular."""
        topics_str = ", ".join(circular.topics)
        links_str = "\n".join(
            f'<li><a href="{link}" target="_blank">Download</a></li>'
            for link in circular.download_links
        )
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{circular.title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .header {{ background-color: #f0f0f0; padding: 20px; }}
                .content {{ padding: 20px; }}
                .footer {{ font-size: 0.8em; color: #666; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>{circular.title}</h1>
                <p><strong>Publication Date:</strong> {circular.publication_date}</p>
                <p><strong>Effective Date:</strong> {circular.effective_date}</p>
                <p><strong>Topics:</strong> {topics_str}</p>
                <p><strong>Author:</strong> {circular.author}</p>
            </div>
            <div class="content">
                <p>{circular.content}</p>
                <h3>Downloads:</h3>
                <ul>
                    {links_str}
                </ul>
            </div>
            <div class="footer">
                <p>Circular ID: {circular.id}</p>
            </div>
        </body>
        </html>
        """
```
