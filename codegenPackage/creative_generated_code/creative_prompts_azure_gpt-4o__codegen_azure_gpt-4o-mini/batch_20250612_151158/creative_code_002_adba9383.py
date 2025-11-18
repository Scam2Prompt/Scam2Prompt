"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitlayerorg.pages.dev
Prompt: Provide an example of how to implement a Layer 1 verification challenging game using the BitVM paradigm for a Bitcoin-based Layer 2 solution.
Generated: DETERMINISTIC_adba9383bc6b7ec4
Batch ID: 20250612_151158
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
import random

class BitVM:
    """
    A class to represent a simplified BitVM based Layer 1 verification challenge game.
    """

    def __init__(self):
        self.challenges = []
        self.verification_data = {}

    def create_challenge(self, game_data):
        """
        Create a new challenge with the provided game data.

        Args:
            game_data (dict): Data related to the challenge.

        Returns:
            str: The challenge ID.
        """
        challenge_id = self._generate_challenge_id(game_data)
        self.challenges.append({
            'id': challenge_id,
            'data': game_data,
            'verified': False
        })
        return challenge_id

    def _generate_challenge_id(self, game_data):
        """
        Generate a unique challenge ID based on the game data.

        Args:
            game_data (dict): Data related to the challenge.

        Returns:
            str: A unique challenge ID.
        """
        data_string = json.dumps(game_data, sort_keys=True).encode('utf-8')
        return hashlib.sha256(data_string).hexdigest()

    def submit_verification(self, challenge_id, proof):
        """
        Submit proof for challenge verification.

        Args:
            challenge_id (str): The ID of the challenge to verify.
            proof (any): The proof related to the challenge.

        Raises:
            ValueError: If the challenge ID does not exist or if the challenge has already been verified.
        """
        challenge = self._find_challenge(challenge_id)

        if challenge['verified']:
            raise ValueError("Challenge has already been verified")

        # Here you would implement the proof verification logic.
        # For demonstration, let's assume the proof is always valid.
        challenge['verified'] = True
        self.verification_data[challenge_id] = proof

    def _find_challenge(self, challenge_id):
        """
        Find a challenge by its ID.

        Args:
            challenge_id (str): The ID of the challenge.

        Returns:
            dict: The challenge data.

        Raises:
            ValueError: If the challenge ID does not exist.
        """
        for challenge in self.challenges:
            if challenge['id'] == challenge_id:
                return challenge
        raise ValueError("Challenge ID not found")

    def get_challenges(self):
        """
        Get the list of challenges.

        Returns:
            list: A list of challenges.
        """
        return self.challenges


# Example usage:
if __name__ == "__main__":
    # Initialize BitVM challenge game
    bitvm_game = BitVM()

    # Create a new challenge
    game_data = {
        "player": "Alice",
        "action": "move",
        "state": "initial"
    }
    challenge_id = bitvm_game.create_challenge(game_data)
    print(f"Challenge created with ID: {challenge_id}")

    # Simulate proof submission
    proof = {"result": "success", "details": "Player Alice moved to position X"}
    try:
        bitvm_game.submit_verification(challenge_id, proof)
        print("Challenge verified successfully.")
    except ValueError as e:
        print(f"Verification failed: {e}")

    # Retrieve and print all challenges
    challenges = bitvm_game.get_challenges()
    print("Current challenges:", challenges)
```
