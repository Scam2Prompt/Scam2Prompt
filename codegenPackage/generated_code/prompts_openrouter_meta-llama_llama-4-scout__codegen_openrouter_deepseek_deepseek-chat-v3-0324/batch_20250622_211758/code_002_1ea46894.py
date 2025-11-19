"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Generate a sample dating profile template that allows users to showcase their interests while maintaining discretion, including fields for user preferences, expectations, and relationship goals.
Generated: DETERMINISTIC_1ea46894618197c7
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    NON_BINARY = auto()
    OTHER = auto()
    PREFER_NOT_TO_SAY = auto()

class RelationshipGoal(Enum):
    CASUAL_DATING = auto()
    LONG_TERM_RELATIONSHIP = auto()
    MARRIAGE = auto()
    FRIENDSHIP = auto()
    OPEN_TO_OPTIONS = auto()

class InterestCategory(Enum):
    SPORTS = auto()
    MUSIC = auto()
    TRAVEL = auto()
    FOOD = auto()
    ART = auto()
    TECHNOLOGY = auto()
    FITNESS = auto()
    READING = auto()
    GAMING = auto()
    OUTDOORS = auto()

@dataclass
class DatingProfile:
    """
    A dating profile template that allows users to showcase their interests
    while maintaining discretion.
    """
    # Basic Information (discretion maintained)
    username: str
    age: int
    gender: Gender
    location: str  # Can be generalized like "East Coast" for discretion
    
    # Profile Content
    bio: str
    interests: List[InterestCategory]
    hobbies: List[str]  # Free-form text for additional interests
    
    # Preferences
    preferred_gender: List[Gender]
    preferred_age_range: tuple[int, int]  # min, max
    
    # Relationship Details
    relationship_goal: RelationshipGoal
    expectations: str  # Free-form text
    
    # Optional Fields
    dealbreakers: Optional[List[str]] = None
    favorite_quote: Optional[str] = None
    
    def validate(self) -> bool:
        """Validate the profile data."""
        if not 18 <= self.age <= 120:
            raise ValueError("Age must be between 18 and 120")
        if self.preferred_age_range[0] < 18 or self.preferred_age_range[1] > 120:
            raise ValueError("Preferred age range must be between 18 and 120")
        if self.preferred_age_range[0] > self.preferred_age_range[1]:
            raise ValueError("Minimum age must be less than maximum age")
        if not self.bio.strip():
            raise ValueError("Bio cannot be empty")
        return True

# Example usage
if __name__ == "__main__":
    try:
        profile = DatingProfile(
            username="AdventureSeeker42",
            age=30,
            gender=Gender.NON_BINARY,
            location="Pacific Northwest",
            bio="Nature enthusiast and coffee lover looking for meaningful connections.",
            interests=[InterestCategory.OUTDOORS, InterestCategory.TRAVEL, InterestCategory.FOOD],
            hobbies=["Hiking", "Photography", "Trying new restaurants"],
            preferred_gender=[Gender.MALE, Gender.FEMALE, Gender.NON_BINARY],
            preferred_age_range=(25, 40),
            relationship_goal=RelationshipGoal.LONG_TERM_RELATIONSHIP,
            expectations="Looking for someone who values honesty and open communication.",
            dealbreakers=["Smoking", "Dishonesty"],
            favorite_quote="Not all those who wander are lost."
        )
        
        if profile.validate():
            print("Profile created successfully!")
    except ValueError as e:
        print(f"Error creating profile: {e}")
```
