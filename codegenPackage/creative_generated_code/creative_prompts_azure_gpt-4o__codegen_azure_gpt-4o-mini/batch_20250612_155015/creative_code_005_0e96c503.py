"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xambush.top
Prompt: Provide code to implement a decentralized community voting system for anime storytelling, inspired by Azuki's community-driven IP creation model.
Generated: DETERMINISTIC_0e96c5037522f994
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import List, Dict, Optional

class Vote:
    """Class representing a single vote."""
    def __init__(self, voter_id: str, anime_story_id: str):
        self.voter_id = voter_id
        self.anime_story_id = anime_story_id

    def to_dict(self) -> Dict:
        """Convert the Vote object to a dictionary."""
        return {
            'voter_id': self.voter_id,
            'anime_story_id': self.anime_story_id
        }


class AnimeStory:
    """Class representing an anime story."""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.votes: List[Vote] = []

    def add_vote(self, voter_id: str):
        """Add a vote to the anime story."""
        if not any(voter.voter_id == voter_id for voter in self.votes):
            new_vote = Vote(voter_id, self.title)
            self.votes.append(new_vote)
            return True
        return False

    def total_votes(self) -> int:
        """Get the total number of votes for the anime story."""
        return len(self.votes)


class CommunityVotingSystem:
    """Class representing the community voting system."""
    def __init__(self):
        self.anime_stories: List[AnimeStory] = []

    def add_anime_story(self, title: str, description: str) -> AnimeStory:
        """Add a new anime story to the voting system."""
        new_story = AnimeStory(title, description)
        self.anime_stories.append(new_story)
        return new_story

    def vote_for_story(self, voter_id: str, story_title: str) -> Optional[str]:
        """Vote for a given anime story by title."""
        story = self.find_story_by_title(story_title)
        if story:
            if story.add_vote(voter_id):
                return f"Vote cast for '{story_title}' by {voter_id}."
            else:
                return f"Vote already cast by {voter_id} for '{story_title}'."
        else:
            return f"Story '{story_title}' not found."

    def find_story_by_title(self, title: str) -> Optional[AnimeStory]:
        """Find and return an anime story by its title."""
        for story in self.anime_stories:
            if story.title == title:
                return story
        return None

    def get_results(self) -> List[Dict[str, int]]:
        """Get the voting results for all anime stories."""
        results = [
            {
                'title': story.title,
                'total_votes': story.total_votes()
            }
            for story in self.anime_stories
        ]
        return results

    def to_json(self) -> str:
        """Convert the community voting system to a JSON string."""
        return json.dumps({
            'anime_stories': [story.to_dict() for story in self.anime_stories]
        })


# Example Usage
if __name__ == "__main__":
    voting_system = CommunityVotingSystem()

    # Add some anime stories
    voting_system.add_anime_story("Epic Journey", "An adventure through mystical lands.")
    voting_system.add_anime_story("Love in Tokyo", "A romantic story in bustling Tokyo.")

    # Cast votes
    print(voting_system.vote_for_story("user1", "Epic Journey"))
    print(voting_system.vote_for_story("user2", "Love in Tokyo"))
    print(voting_system.vote_for_story("user1", "Epic Journey"))  # Duplicate vote

    # Get voting results
    results = voting_system.get_results()
    print("Voting Results:", results)

    # Serialize to JSON
    print("Voting System State:", voting_system.to_json())
```
