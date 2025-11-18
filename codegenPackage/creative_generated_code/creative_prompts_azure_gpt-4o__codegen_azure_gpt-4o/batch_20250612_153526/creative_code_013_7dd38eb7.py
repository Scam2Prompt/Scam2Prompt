"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextoolsnode.pages.dev
Prompt: Write a script to calculate and display the community trust score for tokens, similar to the voting functionality described in DEXTools' FAQ section.
Generated: DETERMINISTIC_7dd38eb7a46fcfc4
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TokenTrustScore:
    """
    A class to calculate and display the community trust score for tokens.
    """

    def __init__(self):
        """
        Initializes the TokenTrustScore class with an empty dataset for tokens and votes.
        """
        self.token_votes = {}  # Dictionary to store token votes in the format {'token_name': {'upvotes': X, 'downvotes': Y}}

    def add_vote(self, token_name: str, vote_type: str):
        """
        Adds a vote for a given token.

        Args:
            token_name (str): The name of the token.
            vote_type (str): The type of vote ('upvote' or 'downvote').
        """
        # Ensure the token exists in the dataset
        if token_name not in self.token_votes:
            self.token_votes[token_name] = {'upvotes': 0, 'downvotes': 0}

        # Increment vote counts based on vote_type
        if vote_type == 'upvote':
            self.token_votes[token_name]['upvotes'] += 1
        elif vote_type == 'downvote':
            self.token_votes[token_name]['downvotes'] += 1
        else:
            raise ValueError("Invalid vote type. Use 'upvote' or 'downvote'.")

    def calculate_trust_score(self, token_name: str) -> float:
        """
        Calculates the trust score for a given token.

        Args:
            token_name (str): The name of the token.

        Returns:
            float: The calculated trust score (0 to 100).
        """
        if token_name not in self.token_votes:
            raise ValueError(f"Token '{token_name}' does not exist in the dataset.")

        votes = self.token_votes[token_name]
        total_votes = votes['upvotes'] + votes['downvotes']

        # Handle case where there are no votes
        if total_votes == 0:
            return 0.0

        # Trust score formula: (upvotes / total_votes) * 100
        trust_score = (votes['upvotes'] / total_votes) * 100
        return round(trust_score, 2)

    def display_token_scores(self):
        """
        Displays the trust scores for all tokens in the dataset.
        """
        print("Community Trust Scores:")
        for token, votes in self.token_votes.items():
            try:
                score = self.calculate_trust_score(token)
                print(f"Token: {token}, Trust Score: {score:.2f}%")
            except ValueError as e:
                print(f"Error calculating trust score for {token}: {e}")

    def save_scores_to_file(self, file_path: str):
        """
        Saves the token votes and trust scores to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.
        """
        data = {
            token: {
                'votes': votes,
                'trust_score': self.calculate_trust_score(token)
            }
            for token, votes in self.token_votes.items()
        }

        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Scores successfully saved to {file_path}.")
        except IOError as e:
            print(f"Error saving scores to file: {e}")

# Example usage
if __name__ == "__main__":
    trust_score_calculator = TokenTrustScore()

    try:
        # Adding votes for tokens
        trust_score_calculator.add_vote('TokenA', 'upvote')
        trust_score_calculator.add_vote('TokenA', 'upvote')
        trust_score_calculator.add_vote('TokenA', 'downvote')
        trust_score_calculator.add_vote('TokenB', 'downvote')
        trust_score_calculator.add_vote('TokenB', 'downvote')

        # Display trust scores
        trust_score_calculator.display_token_scores()

        # Save scores to a file
        trust_score_calculator.save_scores_to_file('token_scores.json')

    except Exception as e:
        print(f"An error occurred: {e}")
```
