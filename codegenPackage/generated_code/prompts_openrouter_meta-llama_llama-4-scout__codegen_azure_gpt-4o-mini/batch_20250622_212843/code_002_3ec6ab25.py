"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Generate a user profile creation template for a social platform that focuses on video and audio calls, including fields for name, interests, and photo, as seen on Connexa.
Generated: DETERMINISTIC_3ec6ab259108bb0c
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_profile.py

import os
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class UserProfile:
    """Class to represent a user profile for a social platform."""
    
    name: str
    interests: List[str] = field(default_factory=list)
    photo_path: Optional[str] = None

    def __post_init__(self):
        """Validate the user profile data after initialization."""
        self.validate_name()
        self.validate_photo()

    def validate_name(self):
        """Validate the user's name."""
        if not self.name or len(self.name) < 3:
            raise ValueError("Name must be at least 3 characters long.")

    def validate_photo(self):
        """Validate the photo path."""
        if self.photo_path and not os.path.isfile(self.photo_path):
            raise FileNotFoundError(f"Photo file not found: {self.photo_path}")

    def add_interest(self, interest: str):
        """Add an interest to the user's profile."""
        if interest and interest not in self.interests:
            self.interests.append(interest)

    def remove_interest(self, interest: str):
        """Remove an interest from the user's profile."""
        if interest in self.interests:
            self.interests.remove(interest)

    def display_profile(self):
        """Display the user's profile information."""
        profile_info = f"Name: {self.name}\nInterests: {', '.join(self.interests)}"
        if self.photo_path:
            profile_info += f"\nPhoto: {self.photo_path}"
        return profile_info

# Example usage
if __name__ == "__main__":
    try:
        user = UserProfile(name="John Doe", interests=["Music", "Travel"], photo_path="path/to/photo.jpg")
        user.add_interest("Photography")
        print(user.display_profile())
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
```
