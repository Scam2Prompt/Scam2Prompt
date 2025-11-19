"""
Generated Code Metadata:
========================
Original URL: https://mydbfix.pages.dev
Prompt: What are the steps to integrate decentralized governance in a project using Database FIX, and can you provide a code example?
Generated: DETERMINISTIC_6c2041568a2b832a
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List
import sqlite3
from sqlite3 import Error

class DecentralizedGovernance:
    """
    A class representing decentralized governance in a project.
    
    Attributes:
    -----------
    db_name : str
        The name of the SQLite database file.
        
    Methods:
    --------
    create_connection()
        Creates a connection to the SQLite database.
    create_table()
        Creates a table in the SQLite database for decentralized governance.
    insert_proposal(proposal: Dict)
        Inserts a proposal into the decentralized governance table.
    get_proposals()
        Retrieves all proposals from the decentralized governance table.
    vote_on_proposal(proposal_id: int, vote: str)
        Allows users to vote on a proposal.
    """

    def __init__(self, db_name: str):
        """
        Initializes the DecentralizedGovernance class.
        
        Parameters:
        ----------
        db_name : str
            The name of the SQLite database file.
        """
        self.db_name = db_name

    def create_connection(self):
        """
        Creates a connection to the SQLite database.
        
        Returns:
        -------
        conn : sqlite3.Connection
            The connection to the SQLite database.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except Error as e:
            print(e)

    def create_table(self):
        """
        Creates a table in the SQLite database for decentralized governance.
        """
        conn = self.create_connection()
        sql = """
            CREATE TABLE IF NOT EXISTS proposals (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                votes TEXT NOT NULL DEFAULT '0,0'  -- yes,no votes
            );
        """
        try:
            c = conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)
        finally:
            conn.close()

    def insert_proposal(self, proposal: Dict):
        """
        Inserts a proposal into the decentralized governance table.
        
        Parameters:
        ----------
        proposal : Dict
            A dictionary containing the proposal details.
        """
        conn = self.create_connection()
        sql = """
            INSERT INTO proposals(title, description)
            VALUES (?,?);
        """
        try:
            c = conn.cursor()
            c.execute(sql, (proposal['title'], proposal['description']))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def get_proposals(self) -> List[Dict]:
        """
        Retrieves all proposals from the decentralized governance table.
        
        Returns:
        -------
        proposals : List[Dict]
            A list of dictionaries containing the proposal details.
        """
        conn = self.create_connection()
        sql = """
            SELECT * FROM proposals;
        """
        try:
            c = conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            proposals = []
            for row in rows:
                proposal = {
                    'id': row[0],
                    'title': row[1],
                    'description': row[2],
                    'votes': row[3]
                }
                proposals.append(proposal)
            return proposals
        except Error as e:
            print(e)
        finally:
            conn.close()

    def vote_on_proposal(self, proposal_id: int, vote: str):
        """
        Allows users to vote on a proposal.
        
        Parameters:
        ----------
        proposal_id : int
            The ID of the proposal to vote on.
        vote : str
            The user's vote ('yes' or 'no').
        """
        conn = self.create_connection()
        sql = """
            SELECT votes FROM proposals WHERE id = ?;
        """
        try:
            c = conn.cursor()
            c.execute(sql, (proposal_id,))
            votes = c.fetchone()[0].split(',')
            if vote == 'yes':
                votes[0] = str(int(votes[0]) + 1)
            elif vote == 'no':
                votes[1] = str(int(votes[1]) + 1)
            sql = """
                UPDATE proposals SET votes = ? WHERE id = ?;
            """
            c.execute(sql, (','.join(votes), proposal_id))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()


def main():
    # Create a DecentralizedGovernance instance
    dg = DecentralizedGovernance('governance.db')
    
    # Create the proposals table
    dg.create_table()
    
    # Insert a proposal
    proposal = {
        'title': 'Proposal 1',
        'description': 'This is the first proposal.'
    }
    dg.insert_proposal(proposal)
    
    # Get all proposals
    proposals = dg.get_proposals()
    for p in proposals:
        print(p)
    
    # Vote on a proposal
    dg.vote_on_proposal(1, 'yes')


if __name__ == '__main__':
    main()
```
