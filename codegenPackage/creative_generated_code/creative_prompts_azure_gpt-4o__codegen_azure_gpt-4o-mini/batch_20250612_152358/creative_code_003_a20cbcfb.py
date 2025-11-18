"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Create a leaderboard tracking system using ChainGPT or similar tools for participants in the $PLENA Quest campaign.
Generated: DETERMINISTIC_a20cbcfb51c34efc
Batch ID: 20250612_152358
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
from typing import List, Dict

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Leaderboard:
    def __init__(self):
        # Initialize leaderboard with an empty list of participants
        self.participants: List[Dict[str, str]] = []

    def add_participant(self, name: str, score: int) -> None:
        """
        Add a participant to the leaderboard.

        :param name: The name of the participant.
        :param score: The score of the participant.
        """
        if score < 0:
            logging.error("Score cannot be negative")
            raise ValueError("Score cannot be negative")
        if any(participant['name'] == name for participant in self.participants):
            logging.error("Participant already exists")
            raise ValueError("Participant already exists")

        participant = {"name": name, "score": score}
        self.participants.append(participant)
        logging.info(f"Added participant: {participant}")

    def update_score(self, name: str, new_score: int) -> None:
        """
        Update the score of an existing participant.

        :param name: The name of the participant.
        :param new_score: The new score for the participant.
        """
        if new_score < 0:
            logging.error("New score cannot be negative")
            raise ValueError("New score cannot be negative")

        for participant in self.participants:
            if participant['name'] == name:
                participant['score'] = new_score
                logging.info(f"Updated score for {name} to {new_score}")
                return

        logging.error("Participant not found")
        raise ValueError("Participant not found")

    def get_leaderboard(self) -> List[Dict[str, str]]:
        """
        Retrieve a sorted list of participants based on their scores.

        :return: A list of participants sorted by score in descending order.
        """
        sorted_participants = sorted(self.participants, key=lambda x: x['score'], reverse=True)
        logging.info("Retrieved leaderboard")
        return sorted_participants

    def save_to_file(self, file_path: str) -> None:
        """
        Save the current leaderboard to a JSON file.

        :param file_path: The file path to save the leaderboard.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.participants, file, indent=4)
            logging.info(f"Leaderboard saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save leaderboard: {e}")
            raise

    def load_from_file(self, file_path: str) -> None:
        """
        Load the leaderboard from a JSON file.

        :param file_path: The file path to load the leaderboard from.
        """
        try:
            with open(file_path, 'r') as file:
                self.participants = json.load(file)
            logging.info(f"Leaderboard loaded from {file_path}")
        except IOError as e:
            logging.error(f"Failed to load leaderboard: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON: {e}")
            raise

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding participants
    try:
        leaderboard.add_participant("Alice", 100)
        leaderboard.add_participant("Bob", 200)
    except ValueError as e:
        logging.error(e)

    # Updating a participant's score
    try:
        leaderboard.update_score("Alice", 150)
    except ValueError as e:
        logging.error(e)

    # Retrieving leaderboard
    print(leaderboard.get_leaderboard())

    # Saving to a file
    leaderboard.save_to_file("leaderboard.json")

    # Loading from a file
    leaderboard.load_from_file("leaderboard.json")
```
