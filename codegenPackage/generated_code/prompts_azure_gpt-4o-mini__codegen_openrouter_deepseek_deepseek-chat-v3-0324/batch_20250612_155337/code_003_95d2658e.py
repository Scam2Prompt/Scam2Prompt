"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Develop a character profile for a member of the Stormwind Rangers, focusing on their perspective on law enforcement and community relations.
Generated: DETERMINISTIC_95d2658e92397489
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CharacterProfile:
    """A class representing a character profile for a Stormwind Ranger."""
    
    def __init__(self, name: str, rank: str, years_of_service: int):
        """
        Initialize the character profile.
        
        Args:
            name (str): The full name of the ranger.
            rank (str): The current rank within the Stormwind Rangers.
            years_of_service (int): Number of years served in the Rangers.
        """
        self.name = name
        self.rank = rank
        self.years_of_service = years_of_service
        self.perspective = {
            'law_enforcement': None,
            'community_relations': None
        }
        
    def set_law_enforcement_perspective(self, perspective: str):
        """
        Set the character's perspective on law enforcement.
        
        Args:
            perspective (str): Description of their views on law enforcement.
            
        Raises:
            ValueError: If perspective is empty or None.
        """
        if not perspective:
            raise ValueError("Perspective cannot be empty")
        self.perspective['law_enforcement'] = perspective
        
    def set_community_relations_perspective(self, perspective: str):
        """
        Set the character's perspective on community relations.
        
        Args:
            perspective (str): Description of their views on community relations.
            
        Raises:
            ValueError: If perspective is empty or None.
        """
        if not perspective:
            raise ValueError("Perspective cannot be empty")
        self.perspective['community_relations'] = perspective
        
    def get_profile(self) -> dict:
        """
        Get the complete character profile.
        
        Returns:
            dict: A dictionary containing all profile information.
        """
        return {
            'name': self.name,
            'rank': self.rank,
            'years_of_service': self.years_of_service,
            'perspectives': self.perspective
        }
        
    def __str__(self) -> str:
        """Return a formatted string representation of the profile."""
        return (
            f"Stormwind Ranger Profile:\n"
            f"Name: {self.name}\n"
            f"Rank: {self.rank}\n"
            f"Years of Service: {self.years_of_service}\n"
            f"Law Enforcement Perspective: {self.perspective['law_enforcement']}\n"
            f"Community Relations Perspective: {self.perspective['community_relations']}"
        )


def create_sample_ranger() -> CharacterProfile:
    """
    Create and return a sample Stormwind Ranger profile with preset values.
    
    Returns:
        CharacterProfile: A populated character profile instance.
    """
    ranger = CharacterProfile(
        name="Captain Alleria Windrunner",
        rank="Captain",
        years_of_service=15
    )
    
    ranger.set_law_enforcement_perspective(
        "Law enforcement should be swift and just, but with compassion. "
        "The law exists to protect citizens, not oppress them."
    )
    
    ranger.set_community_relations_perspective(
        "A ranger must be part of the community they protect. "
        "Building trust through regular interaction and fair treatment "
        "is more effective than brute force."
    )
    
    return ranger


if __name__ == "__main__":
    try:
        sample_ranger = create_sample_ranger()
        print(sample_ranger)
    except Exception as e:
        print(f"Error creating character profile: {e}")
```
