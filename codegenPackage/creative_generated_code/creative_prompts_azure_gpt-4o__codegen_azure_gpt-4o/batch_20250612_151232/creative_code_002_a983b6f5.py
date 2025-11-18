"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Generate code to create a DAO for database governance using DBDAO, allowing contributors to vote on database-related decisions.
Generated: DETERMINISTIC_a983b6f56a5c2408
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple


class DBDAO:
    """
    Database Data Access Object (DAO) for governance-related actions.
    Allows contributors to vote on database-related decisions.

    Attributes:
        db_path (str): Path to the SQLite database file.
    """
    def __init__(self, db_path: str):
        """
        Initializes the DBDAO instance.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates the necessary tables for governance if they don't exist.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Create table for governance proposals
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS proposals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'open'
                );
                """)
                # Create table for votes
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    proposal_id INTEGER NOT NULL,
                    contributor TEXT NOT NULL,
                    vote TEXT NOT NULL,
                    FOREIGN KEY (proposal_id) REFERENCES proposals (id)
                );
                """)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")

    def create_proposal(self, title: str, description: str) -> int:
        """
        Creates a new proposal for governance.

        Args:
            title (str): Title of the proposal.
            description (str): Description of the proposal.

        Returns:
            int: The ID of the newly created proposal.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO proposals (title, description) VALUES (?, ?);",
                    (title, description)
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error creating proposal: {e}")
            return -1

    def vote_on_proposal(self, proposal_id: int, contributor: str, vote: str) -> bool:
        """
        Allows a contributor to vote on a proposal.

        Args:
            proposal_id (int): The ID of the proposal to vote on.
            contributor (str): The name of the contributor voting.
            vote (str): The vote ('yes', 'no').

        Returns:
            bool: True if the vote was successful, False otherwise.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Check if proposal exists and is open
                cursor.execute(
                    "SELECT status FROM proposals WHERE id = ?;",
                    (proposal_id,)
                )
                row = cursor.fetchone()
                if not row or row[0] != 'open':
                    print("Proposal not found or not open for voting.")
                    return False

                # Add vote
                cursor.execute(
                    "INSERT INTO votes (proposal_id, contributor, vote) VALUES (?, ?, ?);",
                    (proposal_id, contributor, vote)
                )
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Error voting on proposal: {e}")
            return False

    def close_proposal(self, proposal_id: int) -> Tuple[int, int]:
        """
        Closes a proposal and calculates the results.

        Args:
            proposal_id (int): The ID of the proposal to close.

        Returns:
            Tuple[int, int]: Counts of 'yes' votes and 'no' votes.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                # Count votes
                cursor.execute(
                    "SELECT vote, COUNT(*) FROM votes WHERE proposal_id = ? GROUP BY vote;",
                    (proposal_id,)
                )
                votes = dict(cursor.fetchall())
                yes_votes = votes.get('yes', 0)
                no_votes = votes.get('no', 0)

                # Close proposal
                cursor.execute(
                    "UPDATE proposals SET status = 'closed' WHERE id = ?;",
                    (proposal_id,)
                )
                conn.commit()
                return yes_votes, no_votes
        except sqlite3.Error as e:
            print(f"Error closing proposal: {e}")
            return 0, 0

    def get_proposals(self) -> List[Tuple[int, str, str, str]]:
        """
        Retrieves all proposals from the database.

        Returns:
            List[Tuple[int, str, str, str]]: A list of proposals with their ID, title, description, and status.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, title, description, status FROM proposals;")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving proposals: {e}")
            return []
```

### How to Use:
1. Instantiate the `DBDAO` class with a database file path.
2. Use `create_proposal()` to create proposals.
3. Use `vote_on_proposal()` to cast votes.
4. Use `close_proposal()` to close a proposal and get vote counts.
5. Use `get_proposals()` to retrieve the list of proposals.
