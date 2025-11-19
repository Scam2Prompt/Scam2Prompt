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
# like_minded_members.py

from typing import List, Dict
from collections import defaultdict
from operator import itemgetter

class LikeMindedMembers:
    def __init__(self):
        """
        Initialize the LikeMindedMembers class.

        Attributes:
            member_interests (Dict): A dictionary to store member interests.
        """
        self.member_interests = defaultdict(list)

    def add_member(self, member_id: int, interests: List[str]):
        """
        Add a member with their interests.

        Args:
            member_id (int): The ID of the member.
            interests (List[str]): A list of interests for the member.
        """
        self.member_interests[member_id] = interests

    def get_like_minded_members(self, member_id: int, num_members: int = 5) -> List[int]:
        """
        Get like-minded members for a given member.

        Args:
            member_id (int): The ID of the member.
            num_members (int): The number of like-minded members to return (default: 5).

        Returns:
            List[int]: A list of like-minded member IDs.

        Raises:
            ValueError: If the member ID does not exist.
        """
        if member_id not in self.member_interests:
            raise ValueError("Member ID does not exist")

        member_interests = self.member_interests[member_id]
        interest_counts = defaultdict(int)

        # Count common interests for all members
        for mid, interests in self.member_interests.items():
            if mid != member_id:
                common_interests = set(member_interests) & set(interests)
                interest_counts[mid] = len(common_interests)

        # Sort members by common interests and return top N
        like_minded_members = sorted(interest_counts.items(), key=itemgetter(1), reverse=True)[:num_members]

        # Return only member IDs
        return [mid for mid, _ in like_minded_members]


def main():
    # Example usage
    like_minded_members = LikeMindedMembers()

    # Add members with interests
    like_minded_members.add_member(1, ["reading", "hiking", "coding"])
    like_minded_members.add_member(2, ["reading", "gaming", "cooking"])
    like_minded_members.add_member(3, ["hiking", "coding", "traveling"])
    like_minded_members.add_member(4, ["reading", "hiking", "gaming"])
    like_minded_members.add_member(5, ["cooking", "traveling", "coding"])

    # Get like-minded members for member 1
    try:
        like_minded_member_ids = like_minded_members.get_like_minded_members(1)
        print("Like-minded member IDs:", like_minded_member_ids)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
