"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Generate code to create a bonus system for an online gaming platform like Pelangi189, where users can claim rewards after specific milestones.
Generated: DETERMINISTIC_57efaa2c8332c4d3
Batch ID: 20250612_153246
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

# Bonus system implementation for an online gaming platform

class BonusSystem:
    """A class to manage the bonus system for users."""
    
    def __init__(self, db_path='bonus_system.db'):
        """
        Initializes the bonus system with a connection to the database.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """Initializes the database with necessary tables if they don't exist."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    total_points INTEGER DEFAULT 0,
                    last_claimed_bonus TIMESTAMP DEFAULT NULL
                )
            ''')
            
            # Create bonuses table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bonuses (
                    bonus_id INTEGER PRIMARY KEY,
                    milestone_points INTEGER NOT NULL,
                    reward_description TEXT NOT NULL,
                    reward_amount REAL NOT NULL
                )
            ''')
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_user(self, username):
        """
        Adds a new user to the database.
        
        Args:
            username (str): The username of the new user.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO users (username) VALUES (?)
            ''', (username,))
            
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Username '{username}' already exists.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
        finally:
            conn.close()

    def add_bonus(self, milestone_points, reward_description, reward_amount):
        """
        Adds a new bonus milestone to the database.
        
        Args:
            milestone_points (int): Points required to reach the bonus milestone.
            reward_description (str): Description of the reward.
            reward_amount (float): Value of the reward.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO bonuses (milestone_points, reward_description, reward_amount)
                VALUES (?, ?, ?)
            ''', (milestone_points, reward_description, reward_amount))
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding bonus: {e}")
        finally:
            conn.close()

    def claim_bonus(self, username):
        """
        Allows a user to claim a bonus if they hit a milestone.
        
        Args:
            username (str): The username of the user claiming the bonus.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Fetch user data
            cursor.execute('SELECT user_id, total_points, last_claimed_bonus FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            
            if not user:
                print(f"User '{username}' not found.")
                return
            
            user_id, total_points, last_claimed_bonus = user
            
            # Fetch eligible bonuses
            cursor.execute('''
                SELECT bonus_id, milestone_points, reward_description, reward_amount
                FROM bonuses
                WHERE milestone_points <= ? AND bonus_id > IFNULL(
                    (SELECT MAX(bonus_id) FROM bonuses WHERE bonus_id IN (
                        SELECT bonus_id FROM claim_history WHERE user_id = ?
                    )), 0)
            ''', (total_points, user_id))
            
            bonuses = cursor.fetchall()
            
            if not bonuses:
                print("No bonuses available for claim.")
                return
            
            # Claim bonuses
            for bonus_id, milestone_points, reward_description, reward_amount in bonuses:
                print(f"Claiming Bonus: {reward_description} - Value: {reward_amount}")
                cursor.execute('''
                    INSERT INTO claim_history (user_id, bonus_id, claimed_at)
                    VALUES (?, ?, ?)
                ''', (user_id, bonus_id, datetime.now()))
            
            conn.commit()
            print("Bonuses claimed successfully.")
        except sqlite3.Error as e:
            print(f"Error claiming bonus: {e}")
        finally:
            conn.close()

    def update_user_points(self, username, points):
        """
        Updates the user's total points in the database.
        
        Args:
            username (str): The username of the user.
            points (int): Points to add to the user's total.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE users
                SET total_points = total_points + ?
                WHERE username = ?
            ''', (points, username))
            
            conn.commit()
            print(f"Updated points for user '{username}'.")
        except sqlite3.Error as e:
            print(f"Error updating user points: {e}")
        finally:
            conn.close()


# Sample code to use the BonusSystem
if __name__ == "__main__":
    bonus_system = BonusSystem()

    # Initialize sample data
    bonus_system.add_user("Player1")
    bonus_system.add_bonus(100, "Small Bonus", 10.0)
    bonus_system.add_bonus(500, "Medium Bonus", 50.0)
    bonus_system.add_bonus(1000, "Large Bonus", 100.0)

    # Update player points and claim bonus
    bonus_system.update_user_points("Player1", 600)
    bonus_system.claim_bonus("Player1")
```
