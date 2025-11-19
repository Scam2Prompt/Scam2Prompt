"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Provide an example of how to set up a DAO for music influencers using the GrooveUP model as a reference.
Generated: DETERMINISTIC_6be91a32fa59f6b9
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing


class MusicInfluencer:
    """Class representing a music influencer."""
    def __init__(self, influencer_id, name, genre, followers):
        self.influencer_id = influencer_id
        self.name = name
        self.genre = genre
        self.followers = followers


class MusicInfluencerDAO:
    """Data Access Object for Music Influencers."""
    
    def __init__(self, db_name='music_influencers.db'):
        """
        Initializes the DAO with a database connection.
        
        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Create the influencers table if it does not exist."""
        with closing(self._get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS influencers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    followers INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def _get_connection(self):
        """Establishes a connection to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def add_influencer(self, influencer):
        """Adds a new influencer to the database.
        
        :param influencer: An instance of MusicInfluencer to add
        :raises Exception: If the database operation fails
        """
        try:
            with closing(self._get_connection()) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO influencers (name, genre, followers) 
                    VALUES (?, ?, ?)
                ''', (influencer.name, influencer.genre, influencer.followers))
                conn.commit()
        except Exception as e:
            print(f"Error adding influencer: {e}")
            raise

    def get_all_influencers(self):
        """Retrieves all influencers from the database.
        
        :return: List of MusicInfluencer instances
        """
        influencers = []
        try:
            with closing(self._get_connection()) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, name, genre, followers FROM influencers')
                rows = cursor.fetchall()
                for row in rows:
                    influencer = MusicInfluencer(*row)
                    influencers.append(influencer)
        except Exception as e:
            print(f"Error retrieving influencers: {e}")
            raise
        return influencers

    def get_influencer_by_id(self, influencer_id):
        """Retrieves a single influencer by ID.
        
        :param influencer_id: ID of the influencer to retrieve
        :return: An instance of MusicInfluencer or None if not found
        """
        try:
            with closing(self._get_connection()) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id, name, genre, followers FROM influencers WHERE id = ?', (influencer_id,))
                row = cursor.fetchone()
                if row:
                    return MusicInfluencer(*row)
                return None
        except Exception as e:
            print(f"Error retrieving influencer by ID: {e}")
            raise

    def update_influencer(self, influencer):
        """Updates an existing influencer in the database.
        
        :param influencer: An instance of MusicInfluencer to update
        :raises Exception: If the database operation fails
        """
        try:
            with closing(self._get_connection()) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE influencers 
                    SET name = ?, genre = ?, followers = ? 
                    WHERE id = ?
                ''', (influencer.name, influencer.genre, influencer.followers, influencer.influencer_id))
                conn.commit()
        except Exception as e:
            print(f"Error updating influencer: {e}")
            raise

    def delete_influencer(self, influencer_id):
        """Deletes an influencer from the database by ID.
        
        :param influencer_id: ID of the influencer to delete
        :raises Exception: If the database operation fails
        """
        try:
            with closing(self._get_connection()) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM influencers WHERE id = ?', (influencer_id,))
                conn.commit()
        except Exception as e:
            print(f"Error deleting influencer: {e}")
            raise


# Example usage
if __name__ == '__main__':
    # Create DAO instance
    influencer_dao = MusicInfluencerDAO()

    # Create a new influencer
    new_influencer = MusicInfluencer(None, 'John Doe', 'Pop', 150000)
    influencer_dao.add_influencer(new_influencer)

    # Retrieve all influencers
    influencers = influencer_dao.get_all_influencers()
    for influencer in influencers:
        print(f"{influencer.influencer_id}: {influencer.name}, Genre: {influencer.genre}, Followers: {influencer.followers}")

    # Update an influencer
    influencer_to_update = influencers[0]
    influencer_to_update.followers += 5000  # Increment followers
    influencer_dao.update_influencer(influencer_to_update)

    # Delete an influencer
    influencer_dao.delete_influencer(influencer_to_update.influencer_id)
```
