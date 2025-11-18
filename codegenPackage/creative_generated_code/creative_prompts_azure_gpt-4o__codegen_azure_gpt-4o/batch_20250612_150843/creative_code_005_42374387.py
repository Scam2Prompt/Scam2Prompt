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
import logging

# Configure logging for error handling and program status
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Mentor:
    """
    Represents an investment expert available for mentorship.
    """
    def __init__(self, name, expertise_areas):
        self.name = name
        self.expertise_areas = expertise_areas

    def __str__(self):
        return f"Mentor: {self.name}, Expertise: {', '.join(self.expertise_areas)}"


class User:
    """
    Represents a user looking for mentorship.
    """
    def __init__(self, name, learning_goals):
        self.name = name
        self.learning_goals = learning_goals

    def __str__(self):
        return f"User: {self.name}, Learning Goals: {', '.join(self.learning_goals)}"


class MentorshipMatchingSystem:
    """
    Handles the mentorship matching process.
    """
    def __init__(self):
        self.mentors = []
        self.users = []

    def add_mentor(self, mentor):
        """
        Adds a mentor to the system.
        """
        if not isinstance(mentor, Mentor):
            logging.error("Invalid mentor object.")
            raise TypeError("Expected an instance of Mentor.")
        self.mentors.append(mentor)
        logging.info(f"Mentor {mentor.name} added to the system.")

    def add_user(self, user):
        """
        Adds a user to the system.
        """
        if not isinstance(user, User):
            logging.error("Invalid user object.")
            raise TypeError("Expected an instance of User.")
        self.users.append(user)
        logging.info(f"User {user.name} added to the system.")

    def find_mentor_for_user(self, user):
        """
        Finds the best mentor match for a user based on their learning goals.
        """
        if not isinstance(user, User):
            logging.error("Invalid user object passed for matching.")
            raise TypeError("Expected an instance of User.")

        logging.info(f"Matching user {user.name} with a mentor...")
        best_match = None
        max_overlap = 0

        for mentor in self.mentors:
            # Calculate overlap between user's learning goals and mentor's expertise
            overlap = len(set(user.learning_goals) & set(mentor.expertise_areas))
            if overlap > max_overlap:
                best_match = mentor
                max_overlap = overlap

        if best_match:
            logging.info(f"User {user.name} matched with mentor {best_match.name}.")
        else:
            logging.warning(f"No suitable mentor found for user {user.name}.")
        return best_match

    def match_all_users(self):
        """
        Matches all users in the system with a mentor.
        """
        matches = {}
        for user in self.users:
            matches[user.name] = self.find_mentor_for_user(user)
        return matches


# Example usage
if __name__ == "__main__":
    try:
        # Create the mentorship system
        mentorship_system = MentorshipMatchingSystem()

        # Add mentors
        mentorship_system.add_mentor(Mentor("Alice", ["stocks", "real estate", "crypto"]))
        mentorship_system.add_mentor(Mentor("Bob", ["ETFs", "mutual funds", "bonds"]))
        mentorship_system.add_mentor(Mentor("Charlie", ["crypto", "options", "futures"]))

        # Add users
        mentorship_system.add_user(User("John", ["crypto", "stocks"]))
        mentorship_system.add_user(User("Jane", ["bonds", "ETFs"]))
        mentorship_system.add_user(User("Mike", ["real estate", "options"]))

        # Match users with mentors
        matches = mentorship_system.match_all_users()

        # Display matches
        for user_name, mentor in matches.items():
            if mentor:
                print(f"{user_name} is matched with {mentor.name}")
            else:
                print(f"No suitable mentor found for {user_name}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
