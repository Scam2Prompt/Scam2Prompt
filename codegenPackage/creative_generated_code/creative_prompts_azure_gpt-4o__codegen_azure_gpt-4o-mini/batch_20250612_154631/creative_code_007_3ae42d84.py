"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ivrtuals.io
Prompt: Generate code for an AI agent that curates and scores user experiences using the ERM framework described on Virtuals.io.
Generated: DETERMINISTIC_3ae42d841db31d9a
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Set up logging for the application
logging.basicConfig(level=logging.INFO)

class Experience:
    """Represents a user experience with its associated attributes."""
    def __init__(self, user_id: str, feedback: str, score: float):
        self.user_id = user_id
        self.feedback = feedback
        self.score = score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Experience object to a dictionary."""
        return {
            "user_id": self.user_id,
            "feedback": self.feedback,
            "score": self.score
        }

class ExperienceCurator:
    """Curates and scores user experiences using the ERM framework."""
    
    def __init__(self):
        self.experiences: List[Experience] = []

    def add_experience(self, user_id: str, feedback: str, score: float) -> None:
        """Add a new user experience to the curator."""
        if not self.validate_score(score):
            logging.error(f"Invalid score: {score}. It must be between 0 and 10.")
            raise ValueError("Score must be between 0 and 10.")
        
        experience = Experience(user_id, feedback, score)
        self.experiences.append(experience)
        logging.info(f"Experience added: {experience.to_dict()}")

    def validate_score(self, score: float) -> bool:
        """Validate if the score is within the accepted range."""
        return 0 <= score <= 10

    def get_average_score(self) -> float:
        """Calculate the average score of all recorded experiences."""
        if not self.experiences:
            logging.warning("No experiences to calculate the average score.")
            return 0.0

        total_score = sum(exp.score for exp in self.experiences)
        average_score = total_score / len(self.experiences)
        logging.info(f"Average score calculated: {average_score}")
        return average_score

    def save_experiences(self, file_path: str) -> None:
        """Save experiences to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump([exp.to_dict() for exp in self.experiences], f, indent=4)
            logging.info(f"Experiences saved to {file_path}")
        except IOError as e:
            logging.error(f"Error saving experiences to {file_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    curator = ExperienceCurator()
    
    # Example of adding experiences
    try:
        curator.add_experience("user1", "Great experience!", 9.5)
        curator.add_experience("user2", "Satisfactory experience.", 7.0)
        curator.add_experience("user3", "Could be better.", 5.0)

        # Calculate and print the average score
        average_score = curator.get_average_score()
        print(f"Average Score: {average_score}")

        # Save experiences to a file
        curator.save_experiences("user_experiences.json")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
