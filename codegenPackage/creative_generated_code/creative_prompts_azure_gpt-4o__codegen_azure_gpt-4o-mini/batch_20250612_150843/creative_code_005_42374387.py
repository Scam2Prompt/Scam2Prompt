"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.org
Prompt: Create a Python program to simulate a mentorship matching system where users are paired with investment experts based on their learning goals, inspired by LucraBot GPT's approach.
Generated: DETERMINISTIC_4237438778cc6f04
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Optional

class Mentor:
    """A class representing a mentor with a name and expertise."""
    
    def __init__(self, name: str, expertise: List[str]):
        self.name = name
        self.expertise = expertise

    def __repr__(self):
        return f'Mentor(name={self.name}, expertise={self.expertise})'


class Mentee:
    """A class representing a mentee with a name and learning goals."""
    
    def __init__(self, name: str, goals: List[str]):
        self.name = name
        self.goals = goals

    def __repr__(self):
        return f'Mentee(name={self.name}, goals={self.goals})'


class MentorshipMatcher:
    """A class to match mentees with mentors based on their goals and expertise."""
    
    def __init__(self):
        self.mentors: List[Mentor] = []
        self.mentees: List[Mentee] = []

    def add_mentor(self, mentor: Mentor):
        """Add a mentor to the matching system."""
        self.mentors.append(mentor)

    def add_mentee(self, mentee: Mentee):
        """Add a mentee to the matching system."""
        self.mentees.append(mentee)

    def match_mentees(self) -> Dict[Mentee, Optional[Mentor]]:
        """Match mentees with mentors based on their goals and expertise."""
        matches: Dict[Mentee, Optional[Mentor]] = {}

        for mentee in self.mentees:
            # Filter mentors based on mentee's goals
            suitable_mentors = [mentor for mentor in self.mentors if any(goal in mentor.expertise for goal in mentee.goals)]
            
            if suitable_mentors:
                # Randomly select a mentor from the list of suitable mentors
                selected_mentor = random.choice(suitable_mentors)
                matches[mentee] = selected_mentor
            else:
                # No suitable mentor found
                matches[mentee] = None
            
        return matches


def main():
    """Main function to run the mentorship matching system."""
    try:
        # Create the matcher
        matcher = MentorshipMatcher()

        # Example mentors and their expertise
        mentors = [
            Mentor("Alice", ["Investment Strategies", "Risk Management"]),
            Mentor("Bob", ["Stock Market", "Technical Analysis"]),
            Mentor("Charlie", ["Real Estate", "Portfolio Management"]),
        ]

        # Add mentors to the matcher
        for mentor in mentors:
            matcher.add_mentor(mentor)

        # Example mentees and their learning goals
        mentees = [
            Mentee("David", ["Investment Strategies"]),
            Mentee("Eve", ["Stock Market"]),
            Mentee("Frank", ["Real Estate", "Risk Management"]),
        ]

        # Add mentees to the matcher
        for mentee in mentees:
            matcher.add_mentee(mentee)

        # Match mentees to mentors
        matches = matcher.match_mentees()

        # Display the matches
        for mentee, mentor in matches.items():
            if mentor:
                print(f'{mentee.name} is matched with mentor {mentor.name}.')
            else:
                print(f'{mentee.name} has no suitable mentor.')

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    main()
```
