"""
Generated Code Metadata:
========================
Original URL: https://gift-mantra.net
Prompt: "Design a basic algorithm for a 'like-minded members' connection feature, similar to what is described on the Stumble! ® website."
Generated: DETERMINISTIC_f2cb112bc34ce646
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class Member:
    """Class representing a member in the connection feature."""
    
    def __init__(self, member_id: int, interests: List[str]):
        """
        Initialize a new member with an ID and a list of interests.
        
        :param member_id: Unique identifier for the member.
        :param interests: List of interests associated with the member.
        """
        self.member_id = member_id
        self.interests = interests

class ConnectionFeature:
    """Class to handle the connection feature for like-minded members."""
    
    def __init__(self):
        """Initialize the connection feature with an empty member list."""
        self.members: List[Member] = []

    def add_member(self, member: Member) -> None:
        """
        Add a new member to the connection feature.
        
        :param member: Member instance to be added.
        """
        self.members.append(member)

    def find_like_minded_members(self, member_id: int) -> List[Dict[str, Any]]:
        """
        Find members with similar interests to the specified member.
        
        :param member_id: ID of the member for whom to find connections.
        :return: List of dictionaries containing member IDs and their interests.
        """
        # Find the member by ID
        target_member = next((m for m in self.members if m.member_id == member_id), None)
        
        if not target_member:
            raise ValueError(f"Member with ID {member_id} not found.")
        
        # Find like-minded members based on shared interests
        like_minded_members = []
        for member in self.members:
            if member.member_id != target_member.member_id:
                shared_interests = set(target_member.interests) & set(member.interests)
                if shared_interests:
                    like_minded_members.append({
                        'member_id': member.member_id,
                        'shared_interests': list(shared_interests)
                    })
        
        return like_minded_members

# Example usage
if __name__ == "__main__":
    # Create a connection feature instance
    connection_feature = ConnectionFeature()
    
    # Add members with interests
    connection_feature.add_member(Member(1, ['music', 'travel', 'food']))
    connection_feature.add_member(Member(2, ['travel', 'sports', 'movies']))
    connection_feature.add_member(Member(3, ['music', 'art', 'food']))
    connection_feature.add_member(Member(4, ['technology', 'sports', 'food']))
    
    # Find like-minded members for member with ID 1
    try:
        like_minded = connection_feature.find_like_minded_members(1)
        print("Like-minded members for member 1:", like_minded)
    except ValueError as e:
        print(e)
```
