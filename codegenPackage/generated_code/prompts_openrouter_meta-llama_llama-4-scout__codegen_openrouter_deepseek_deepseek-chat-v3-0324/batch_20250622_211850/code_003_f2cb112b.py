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
import heapq
from typing import List, Dict, Set, Tuple
from collections import defaultdict

class Member:
    """Represents a member with interests and connections."""
    def __init__(self, member_id: int, interests: Set[str]):
        self.member_id = member_id
        self.interests = interests
        self.connections: Set[int] = set()

class LikeMindedMembers:
    """Implements a 'like-minded members' connection feature."""
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.interest_index: Dict[str, Set[int]] = defaultdict(set)

    def add_member(self, member_id: int, interests: List[str]) -> None:
        """Add a new member with their interests.
        
        Args:
            member_id: Unique identifier for the member.
            interests: List of interests for the member.
        """
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already exists.")
        
        interests_set = set(interests)
        self.members[member_id] = Member(member_id, interests_set)
        
        for interest in interests_set:
            self.interest_index[interest].add(member_id)

    def add_connection(self, member_id1: int, member_id2: int) -> None:
        """Add a connection between two members.
        
        Args:
            member_id1: ID of the first member.
            member_id2: ID of the second member.
        """
        if member_id1 not in self.members or member_id2 not in self.members:
            raise ValueError("One or both members do not exist.")
        
        self.members[member_id1].connections.add(member_id2)
        self.members[member_id2].connections.add(member_id1)

    def get_recommendations(self, member_id: int, top_n: int = 5) -> List[int]:
        """Get top N like-minded member recommendations for a given member.
        
        Args:
            member_id: ID of the member to get recommendations for.
            top_n: Number of recommendations to return.
        
        Returns:
            List of recommended member IDs sorted by relevance.
        """
        if member_id not in self.members:
            raise ValueError(f"Member {member_id} does not exist.")
        
        member = self.members[member_id]
        interest_scores: Dict[int, int] = defaultdict(int)
        
        # Calculate Jaccard similarity based on shared interests
        for interest in member.interests:
            for other_member_id in self.interest_index[interest]:
                if other_member_id != member_id and other_member_id not in member.connections:
                    interest_scores[other_member_id] += 1
        
        # Normalize by total interests to get Jaccard similarity
        recommendations = []
        for other_member_id, shared_count in interest_scores.items():
            other_member = self.members[other_member_id]
            total_interests = len(member.interests.union(other_member.interests))
            if total_interests > 0:
                jaccard_similarity = shared_count / total_interests
                recommendations.append((-jaccard_similarity, other_member_id))  # Negative for min-heap
        
        # Use heap to get top N recommendations
        heapq.heapify(recommendations)
        top_recommendations = []
        for _ in range(min(top_n, len(recommendations))):
            similarity, recommended_id = heapq.heappop(recommendations)
            top_recommendations.append(recommended_id)
        
        return top_recommendations

# Example usage
if __name__ == "__main__":
    lmm = LikeMindedMembers()
    
    # Add some members with interests
    lmm.add_member(1, ["programming", "python", "machine learning"])
    lmm.add_member(2, ["python", "data science", "statistics"])
    lmm.add_member(3, ["machine learning", "deep learning", "neural networks"])
    lmm.add_member(4, ["cooking", "baking", "food"])
    lmm.add_member(5, ["programming", "python", "web development"])
    
    # Add some connections
    lmm.add_connection(1, 2)
    lmm.add_connection(1, 3)
    
    # Get recommendations
    print("Recommendations for member 1:", lmm.get_recommendations(1))
    print("Recommendations for member 4:", lmm.get_recommendations(4))
```
