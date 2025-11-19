"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-renzoprotocol.com
Prompt: Generate code to track user votes and calculate rewards based on a voting proposal, similar to the $REZ Rewards Proposal on the Renzo Protocol site.
Generated: DETERMINISTIC_1cee511b59b9c32c
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class VoteTracker:
    """
    A class to track user votes and calculate rewards based on voting proposals.
    """

    def __init__(self, db_file):
        """
        Initialize the VoteTracker with a database connection.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.

        Args:
            db_file (str): The path to the SQLite database file.

        Returns:
            Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """
        Create a table for storing votes and rewards.
        """
        try:
            sql_create_votes_table = """
            CREATE TABLE IF NOT EXISTS votes (
                id integer PRIMARY KEY,
                user_id text NOT NULL,
                proposal_id text NOT NULL,
                vote_value integer NOT NULL,
                UNIQUE(user_id, proposal_id)
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_votes_table)
        except Error as e:
            print(f"Error creating table: {e}")

    def cast_vote(self, user_id, proposal_id, vote_value):
        """
        Cast a vote for a proposal.

        Args:
            user_id (str): The ID of the user casting the vote.
            proposal_id (str): The ID of the proposal being voted on.
            vote_value (int): The value of the vote (e.g., 1 for approve, -1 for reject).

        Returns:
            str: A message indicating the result of the vote casting.
        """
        try:
            sql_insert_vote = """
            INSERT INTO votes (user_id, proposal_id, vote_value)
            VALUES (?, ?, ?)
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_vote, (user_id, proposal_id, vote_value))
            self.connection.commit()
            return "Vote cast successfully."
        except sqlite3.IntegrityError:
            return "Error: User has already voted on this proposal."
        except Error as e:
            return f"Error casting vote: {e}"

    def calculate_rewards(self, proposal_id):
        """
        Calculate total rewards based on votes for a specific proposal.

        Args:
            proposal_id (str): The ID of the proposal.

        Returns:
            float: The total computed rewards based on the votes for the proposal.
        """
        try:
            sql_total_votes = """
            SELECT SUM(vote_value) FROM votes WHERE proposal_id = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_total_votes, (proposal_id,))
            total_votes = cursor.fetchone()[0] or 0  # Default to 0 if no votes
            rewards = total_votes * 0.1  # Example reward calculation
            return rewards
        except Error as e:
            print(f"Error calculating rewards: {e}")
            return 0.0

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()


# Example usage
if __name__ == "__main__":
    # Initialize the VoteTracker with a database file
    vote_tracker = VoteTracker("votes.db")

    # Cast votes
    print(vote_tracker.cast_vote("user123", "proposalA", 1))
    print(vote_tracker.cast_vote("user456", "proposalA", -1))

    # Calculate rewards for a proposal
    rewards = vote_tracker.calculate_rewards("proposalA")
    print(f"Total rewards for proposalA: {rewards}")

    # Close the connection when done
    vote_tracker.close_connection()
```
