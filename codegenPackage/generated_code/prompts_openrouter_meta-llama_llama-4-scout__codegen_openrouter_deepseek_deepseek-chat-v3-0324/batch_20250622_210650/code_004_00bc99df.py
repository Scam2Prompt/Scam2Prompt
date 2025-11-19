"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Create a virtual library system for a bilingual school, incorporating e-learning resources and interactive materials, similar to the one used at Heart of Jesus College."
Generated: DETERMINISTIC_00bc99dffbe58696
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Virtual Library System for Bilingual Schools
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
from abc import ABC, abstractmethod

class Resource(ABC):
    """Abstract base class for all library resources"""
    def __init__(self, title: str, language: str, resource_id: str):
        self.title = title
        self.language = language
        self.resource_id = resource_id
        self.creation_date = datetime.now()
        self.last_accessed = None
        self.is_available = True

    @abstractmethod
    def display_info(self) -> Dict:
        """Return resource information as dictionary"""
        pass

    def check_out(self) -> bool:
        """Mark resource as checked out"""
        if self.is_available:
            self.is_available = False
            self.last_accessed = datetime.now()
            return True
        return False

    def check_in(self) -> None:
        """Mark resource as available"""
        self.is_available = True

class Book(Resource):
    """Concrete class for book resources"""
    def __init__(self, title: str, language: str, resource_id: str, 
                 author: str, isbn: str, pages: int):
        super().__init__(title, language, resource_id)
        self.author = author
        self.isbn = isbn
        self.pages = pages

    def display_info(self) -> Dict:
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "language": self.language,
            "isbn": self.isbn,
            "pages": self.pages,
            "available": self.is_available,
            "last_accessed": self.last_accessed
        }

class ELearningMaterial(Resource):
    """Concrete class for e-learning resources"""
    def __init__(self, title: str, language: str, resource_id: str,
                 url: str, duration: int, interactive: bool):
        super().__init__(title, language, resource_id)
        self.url = url
        self.duration = duration  # in minutes
        self.interactive = interactive

    def display_info(self) -> Dict:
        return {
            "type": "E-Learning Material",
            "title": self.title,
            "language": self.language,
            "url": self.url,
            "duration": self.duration,
            "interactive": self.interactive,
            "available": self.is_available,
            "last_accessed": self.last_accessed
        }

class User:
    """Class representing library users"""
    def __init__(self, user_id: str, name: str, role: str):
        self.user_id = user_id
        self.name = name
        self.role = role  # student, teacher, admin
        self.checked_out_resources = []

    def check_out_resource(self, resource: Resource) -> bool:
        """Attempt to check out a resource"""
        if resource.check_out():
            self.checked_out_resources.append(resource.resource_id)
            return True
        return False

    def return_resource(self, resource: Resource) -> None:
        """Return a resource"""
        resource.check_in()
        if resource.resource_id in self.checked_out_resources:
            self.checked_out_resources.remove(resource.resource_id)

    def get_checked_out_resources(self) -> List[str]:
        """Get list of checked out resource IDs"""
        return self.checked_out_resources

class Library:
    """Main library system class"""
    def __init__(self):
        self.resources: Dict[str, Resource] = {}
        self.users: Dict[str, User] = {}
        self.load_data()

    def add_resource(self, resource: Resource) -> None:
        """Add a new resource to the library"""
        self.resources[resource.resource_id] = resource
        self.save_data()

    def remove_resource(self, resource_id: str) -> bool:
        """Remove a resource from the library"""
        if resource_id in self.resources:
            del self.resources[resource_id]
            self.save_data()
            return True
        return False

    def add_user(self, user: User) -> None:
        """Add a new user to the system"""
        self.users[user.user_id] = user
        self.save_data()

    def remove_user(self, user_id: str) -> bool:
        """Remove a user from the system"""
        if user_id in self.users:
            del self.users[user_id]
            self.save_data()
            return True
        return False

    def search_resources(self, query: str, language: Optional[str] = None) -> List[Dict]:
        """Search resources by title with optional language filter"""
        results = []
        query = query.lower()
        for resource in self.resources.values():
            if query in resource.title.lower():
                if language is None or resource.language.lower() == language.lower():
                    results.append(resource.display_info())
        return results

    def get_resource_by_id(self, resource_id: str) -> Optional[Resource]:
        """Get resource by its ID"""
        return self.resources.get(resource_id)

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by their ID"""
        return self.users.get(user_id)

    def save_data(self) -> None:
        """Save library data to JSON files"""
        try:
            # Save resources
            resources_data = {
                rid: {
                    "type": type(res).__name__,
                    "data": res.display_info()
                }
                for rid, res in self.resources.items()
            }
            with open("resources.json", "w", encoding="utf-8") as f:
                json.dump(resources_data, f, indent=2, default=str)

            # Save users
            users_data = {
                uid: {
                    "name": user.name,
                    "role": user.role,
                    "checked_out_resources": user.checked_out_resources
                }
                for uid, user in self.users.items()
            }
            with open("users.json", "w", encoding="utf-8") as f:
                json.dump(users_data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        """Load library data from JSON files"""
        try:
            # Load resources
            if os.path.exists("resources.json"):
                with open("resources.json", "r", encoding="utf-8") as f:
                    resources_data = json.load(f)
                    for rid, res_data in resources_data.items():
                        res_type = res_data["type"]
                        data = res_data["data"]
                        if res_type == "Book":
                            resource = Book(
                                title=data["title"],
                                language=data["language"],
                                resource_id=rid,
                                author=data["author"],
                                isbn=data["isbn"],
                                pages=data["pages"]
                            )
                        elif res_type == "E-Learning Material":
                            resource = ELearningMaterial(
                                title=data["title"],
                                language=data["language"],
                                resource_id=rid,
                                url=data["url"],
                                duration=data["duration"],
                                interactive=data["interactive"]
                            )
                        resource.is_available = data["available"]
                        resource.last_accessed = datetime.strptime(data["last_accessed"], "%Y-%m-%d %H:%M:%S.%f") if data["last_accessed"] else None
                        self.resources[rid] = resource

            # Load users
            if os.path.exists("users.json"):
                with open("users.json", "r", encoding="utf-8") as f:
                    users_data = json.load(f)
                    for uid, user_data in users_data.items():
                        user = User(
                            user_id=uid,
                            name=user_data["name"],
                            role=user_data["role"]
                        )
                        user.checked_out_resources = user_data["checked_out_resources"]
                        self.users[uid] = user
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

    def generate_report(self) -> Dict:
        """Generate library usage report"""
        report = {
            "total_resources": len(self.resources),
            "total_users": len(self.users),
            "resources_by_type": {},
            "resources_by_language": {},
            "checked_out_resources": 0
        }

        # Count resources by type and language
        for resource in self.resources.values():
            res_type = type(resource).__name__
            language = resource.language

            report["resources_by_type"][res_type] = report["resources_by_type"].get(res_type, 0) + 1
            report["resources_by_language"][language] = report["resources_by_language"].get(language, 0) + 1

            if not resource.is_available:
                report["checked_out_resources"] += 1

        return report

# Example usage
if __name__ == "__main__":
    library = Library()

    # Add sample resources
    book1 = Book(
        title="Python Programming",
        language="English",
        resource_id="B001",
        author="John
