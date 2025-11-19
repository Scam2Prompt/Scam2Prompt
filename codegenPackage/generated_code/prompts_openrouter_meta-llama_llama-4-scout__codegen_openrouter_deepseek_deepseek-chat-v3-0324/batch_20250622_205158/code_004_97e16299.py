"""
Generated Code Metadata:
========================
Original URL: https://braavos.rs
Prompt: What are some best practices for architectural firms to showcase their projects and collaborate with fellow architects using tools like the Études Architect App?
Generated: DETERMINISTIC_97e162993a51704b
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Études Architect App - Project Showcase and Collaboration Module

import os
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from pathlib import Path
from dataclasses import dataclass
import hashlib
import json
from PIL import Image
import shutil

class ProjectVisibility(Enum):
    PRIVATE = "private"
    TEAM = "team"
    PUBLIC = "public"

class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    MODEL = "3d_model"

@dataclass
class ProjectMember:
    user_id: str
    role: str
    joined_at: datetime

@dataclass
class ProjectMedia:
    media_id: str
    file_path: str
    media_type: MediaType
    upload_date: datetime
    description: Optional[str] = None
    tags: Optional[List[str]] = None

@dataclass
class ProjectComment:
    comment_id: str
    user_id: str
    content: str
    timestamp: datetime
    replies: List['ProjectComment'] = None

class Project:
    def __init__(self, project_id: str, name: str, owner_id: str):
        self.project_id = project_id
        self.name = name
        self.owner_id = owner_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.visibility = ProjectVisibility.PRIVATE
        self.description = ""
        self.tags = []
        self.members = []
        self.media = []
        self.comments = []
        self.version_history = []

    def add_member(self, user_id: str, role: str) -> bool:
        if any(member.user_id == user_id for member in self.members):
            return False
        
        new_member = ProjectMember(
            user_id=user_id,
            role=role,
            joined_at=datetime.now()
        )
        self.members.append(new_member)
        self.updated_at = datetime.now()
        return True

    def upload_media(self, file_path: str, media_type: MediaType, description: str = None) -> Optional[ProjectMedia]:
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError("File does not exist")
            
            # Generate unique media ID
            media_id = str(uuid.uuid4())
            
            # Create media directory if it doesn't exist
            media_dir = f"projects/{self.project_id}/media"
            os.makedirs(media_dir, exist_ok=True)
            
            # Process and store the file
            file_ext = Path(file_path).suffix
            new_filename = f"{media_id}{file_ext}"
            new_path = f"{media_dir}/{new_filename}"
            
            # Handle different media types appropriately
            if media_type == MediaType.IMAGE:
                self._process_image(file_path, new_path)
            else:
                shutil.copy2(file_path, new_path)
            
            media = ProjectMedia(
                media_id=media_id,
                file_path=new_path,
                media_type=media_type,
                upload_date=datetime.now(),
                description=description
            )
            
            self.media.append(media)
            self.updated_at = datetime.now()
            return media
            
        except Exception as e:
            print(f"Error uploading media: {e}")
            return None

    def _process_image(self, source_path: str, dest_path: str):
        """Process and optimize image before saving"""
        try:
            img = Image.open(source_path)
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            # Resize if too large
            if max(img.size) > 2000:
                img.thumbnail((2000, 2000))
            img.save(dest_path, quality=85, optimize=True)
        except Exception as e:
            raise Exception(f"Image processing failed: {e}")

    def add_comment(self, user_id: str, content: str) -> ProjectComment:
        comment = ProjectComment(
            comment_id=str(uuid.uuid4()),
            user_id=user_id,
            content=content,
            timestamp=datetime.now()
        )
        self.comments.append(comment)
        self.updated_at = datetime.now()
        return comment

    def reply_to_comment(self, comment_id: str, user_id: str, content: str) -> Optional[ProjectComment]:
        parent_comment = next((c for c in self.comments if c.comment_id == comment_id), None)
        if not parent_comment:
            return None
            
        reply = ProjectComment(
            comment_id=str(uuid.uuid4()),
            user_id=user_id,
            content=content,
            timestamp=datetime.now()
        )
        
        if parent_comment.replies is None:
            parent_comment.replies = []
        parent_comment.replies.append(reply)
        self.updated_at = datetime.now()
        return reply

    def to_dict(self) -> Dict:
        return {
            "project_id": self.project_id,
            "name": self.name,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "visibility": self.visibility.value,
            "description": self.description,
            "tags": self.tags,
            "members": [{
                "user_id": m.user_id,
                "role": m.role,
                "joined_at": m.joined_at.isoformat()
            } for m in self.members],
            "media_count": len(self.media),
            "comments_count": len(self.comments)
        }

class ProjectManager:
    def __init__(self):
        self.projects = {}
        self.users = {}
        
    def create_project(self, name: str, owner_id: str) -> Project:
        project_id = str(uuid.uuid4())
        project = Project(project_id, name, owner_id)
        self.projects[project_id] = project
        project.add_member(owner_id, "owner")
        return project
    
    def get_project(self, project_id: str) -> Optional[Project]:
        return self.projects.get(project_id)
    
    def get_user_projects(self, user_id: str) -> List[Project]:
        return [
            p for p in self.projects.values() 
            if p.owner_id == user_id or 
            any(m.user_id == user_id for m in p.members)
        ]
    
    def export_project_data(self, project_id: str, output_dir: str) -> bool:
        project = self.get_project(project_id)
        if not project:
            return False
            
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            # Save project metadata
            metadata_path = os.path.join(output_dir, "project_metadata.json")
            with open(metadata_path, 'w') as f:
                json.dump(project.to_dict(), f, indent=2)
            
            # Save media files
            media_dir = os.path.join(output_dir, "media")
            os.makedirs(media_dir, exist_ok=True)
            
            for media in project.media:
                shutil.copy2(media.file_path, os.path.join(media_dir, os.path.basename(media.file_path)))
            
            return True
        except Exception as e:
            print(f"Error exporting project: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    project = manager.create_project("Urban Renewal Project", "user123")
    project.description = "A comprehensive urban renewal plan for downtown district"
    project.tags = ["urban", "renewal", "mixed-use"]
    project.visibility = ProjectVisibility.TEAM
    
    # Add team members
    project.add_member("user456", "architect")
    project.add_member("user789", "designer")
    
    # Upload project media
    project.upload_media("sample_blueprint.jpg", MediaType.IMAGE, "Initial design concept")
    project.upload_media("project_brief.pdf", MediaType.DOCUMENT)
    
    # Add comments
    project.add_comment("user456", "The initial concept looks promising!")
    project.reply_to_comment(project.comments[0].comment_id, "user789", "I agree, but we should consider more green spaces.")
    
    # Export project data
    manager.export_project_data(project.project_id, "exported_project")
```
