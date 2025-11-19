"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Develop a tool in Python to recommend mentors and coaches in coworking spaces, using insights from the "Dénichez mentors et coachs dans les espaces de coworking" article on NetCoworking.
Generated: DETERMINISTIC_14a035d9eb9bffc1
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mentor_recommender.py

import json
from typing import Dict, List

class Mentor:
    def __init__(self, id: int, name: str, expertise: List[str]):
        """
        Initialize a Mentor object.

        Args:
        - id (int): Unique identifier for the mentor.
        - name (str): Name of the mentor.
        - expertise (List[str]): List of areas of expertise for the mentor.
        """
        self.id = id
        self.name = name
        self.expertise = expertise

class CoworkingSpace:
    def __init__(self, id: int, name: str, mentors: List[Mentor]):
        """
        Initialize a CoworkingSpace object.

        Args:
        - id (int): Unique identifier for the coworking space.
        - name (str): Name of the coworking space.
        - mentors (List[Mentor]): List of mentors in the coworking space.
        """
        self.id = id
        self.name = name
        self.mentors = mentors

class MentorRecommender:
    def __init__(self, coworking_spaces: List[CoworkingSpace]):
        """
        Initialize a MentorRecommender object.

        Args:
        - coworking_spaces (List[CoworkingSpace]): List of coworking spaces.
        """
        self.coworking_spaces = coworking_spaces

    def recommend_mentors(self, expertise: List[str], coworking_space_id: int = None) -> List[Mentor]:
        """
        Recommend mentors based on expertise and optional coworking space.

        Args:
        - expertise (List[str]): List of areas of expertise to match.
        - coworking_space_id (int): Optional ID of a specific coworking space.

        Returns:
        - List[Mentor]: List of recommended mentors.
        """
        recommended_mentors = []

        if coworking_space_id:
            # Filter mentors by coworking space
            space = next((s for s in self.coworking_spaces if s.id == coworking_space_id), None)
            if space:
                recommended_mentors = [m for m in space.mentors if any(e in m.expertise for e in expertise)]
            else:
                raise ValueError(f"Coworking space with ID {coworking_space_id} not found")
        else:
            # Filter mentors across all coworking spaces
            for space in self.coworking_spaces:
                recommended_mentors.extend([m for m in space.mentors if any(e in m.expertise for e in expertise)])

        # Remove duplicates
        recommended_mentors = list(set(recommended_mentors))

        return recommended_mentors

def load_data(file_path: str) -> Dict:
    """
    Load data from a JSON file.

    Args:
    - file_path (str): Path to the JSON file.

    Returns:
    - Dict: Loaded data.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

def main():
    # Load data from JSON file
    data = load_data('data.json')

    # Create coworking spaces and mentors
    mentors = []
    for mentor_data in data['mentors']:
        mentors.append(Mentor(mentor_data['id'], mentor_data['name'], mentor_data['expertise']))

    coworking_spaces = []
    for space_data in data['coworkingSpaces']:
        space_mentors = [m for m in mentors if m.id in space_data['mentorIds']]
        coworking_spaces.append(CoworkingSpace(space_data['id'], space_data['name'], space_mentors))

    # Create mentor recommender
    recommender = MentorRecommender(coworking_spaces)

    # Recommend mentors
    expertise = ['marketing', 'productivity']
    recommended_mentors = recommender.recommend_mentors(expertise)

    # Print recommended mentors
    for mentor in recommended_mentors:
        print(f"Name: {mentor.name}, Expertise: {mentor.expertise}")

if __name__ == '__main__':
    main()
```

```json
// data.json

{
    "mentors": [
        {
            "id": 1,
            "name": "John Doe",
            "expertise": ["marketing", "productivity"]
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "expertise": ["finance", "leadership"]
        },
        {
            "id": 3,
            "name": "Bob Johnson",
            "expertise": ["marketing", "sales"]
        }
    ],
    "coworkingSpaces": [
        {
            "id": 1,
            "name": "Space 1",
            "mentorIds": [1, 2]
        },
        {
            "id": 2,
            "name": "Space 2",
            "mentorIds": [2, 3]
        }
    ]
}
```
