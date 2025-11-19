"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poc-dao.zetachain.io
Prompt: Write a code snippet that allows members to stake cryptocurrency in a POC-DAO and vote on commitment levels.
Generated: DETERMINISTIC_c7342b7b77178006
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

class DAO:
    def __init__(self):
        # Initialize the DAO database and tables
        self.db = sqlite3.connect("dao.db")
        self.cursor = self.db.cursor()
        self._initialize_database()

    def _initialize_database(self):
        # Create members table to store staking info and voting rights
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stake_amount REAL NOT NULL,
            voting_power REAL NOT NULL
        )
        """)
        
        # Create votes table to store commitment level votes
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            commitment_level TEXT NOT NULL,
            voted_at TIMESTAMP NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members (id)
        )
        """)
        self.db.commit()

    def add_member(self, name, stake_amount):
        """
        Add a new member to the DAO and calculate voting power based on their stake amount.
        
        Voting Power Formula: voting_power = stake_amount * 0.1
        """
        try:
            voting_power = stake_amount * 0.1
            self.cursor.execute("INSERT INTO members (name, stake_amount, voting_power) VALUES (?, ?, ?)",
                                (name, stake_amount, voting_power))
            self.db.commit()
            print(f"Member '{name}' successfully added with voting power {voting_power:.2f}.")
        except sqlite3.Error as e:
            print(f"Error adding member: {e}")

    def cast_vote(self, member_id, commitment_level):
        """
        Allow members to cast a vote on commitment levels (e.g., 'High', 'Medium', 'Low').
        """
        try:
            # Check if member exists
            self.cursor.execute("SELECT * FROM members WHERE id = ?", (member_id,))
            member = self.cursor.fetchone()
            if not member:
                print(f"No member found with ID {member_id}.")
                return
            
            # Record the vote
            voted_at = datetime.now()
            self.cursor.execute("""
            INSERT INTO votes (member_id, commitment_level, voted_at) VALUES (?, ?, ?)
            """, (member_id, commitment_level, voted_at))
            self.db.commit()
            print(f"Vote successfully cast by member ID {member_id} for commitment level '{commitment_level}'.")
        except sqlite3.Error as e:
            print(f"Error casting vote: {e}")

    def get_votes(self):
        """
        Retrieve all votes cast in the DAO.
        """
        try:
            self.cursor.execute("SELECT members.name, votes.commitment_level, votes.voted_at FROM votes JOIN members ON votes.member_id = members.id")
            votes = self.cursor.fetchall()
            if votes:
                print("DAO Votes:")
                for vote in votes:
                    print(f"Member: {vote[0]}, Commitment Level: {vote[1]}, Voted At: {vote[2]}")
            else:
                print("No votes have been cast yet.")
        except sqlite3.Error as e:
            print(f"Error retrieving votes: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.db.close()


# Example usage (uncomment to test)
if __name__ == "__main__":
    dao = DAO()
    dao.add_member("Alice", 1000)  # Add a member with 1000 stake
    dao.add_member("Bob", 500)    # Add a member with 500 stake
    dao.cast_vote(1, "High")      # Alice votes for 'High' commitment level
    dao.cast_vote(2, "Medium")    # Bob votes for 'Medium' commitment level
    dao.get_votes()               # Retrieve and display all votes
    dao.close()
```
