"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Recommend tools or APIs for implementing a loyalty program with rewards like tickets, discounts, and special prizes, similar to DominoBet's program.
Generated: DETERMINISTIC_5250c1bc2970f7f5
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a simple implementation of a loyalty program
using Python. It provides the structure for managing user accounts, 
tracking points, and redeeming rewards. The code is designed to be 
modular, reusable, and extensible, making it production-ready.

Dependencies:
- `sqlite3`: for database interactions
- `flask`: for API implementation (optional, if needed)
"""

import sqlite3


class LoyaltyProgram:
    """A class to manage a loyalty program with user points and redeemable rewards."""
    
    def __init__(self, db_name="loyalty_program.db"):
        """
        Initialize the database connection and set up the necessary tables.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """
        Create necessary tables for the loyalty program if they don't exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Create 'users' table to store user information and points
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    points INTEGER DEFAULT 0
                )
            """)
            
            # Create 'rewards' table to store available rewards
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rewards (
                    reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    points_required INTEGER NOT NULL
                )
            """)
            
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    def add_user(self, name, email):
        """
        Add a new user to the loyalty program.

        Args:
            name (str): User's name.
            email (str): User's email address.

        Returns:
            str: Success or error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            return "User added successfully."
        except sqlite3.IntegrityError:
            return "Error: Email already exists."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            if conn:
                conn.close()

    def add_reward(self, name, description, points_required):
        """
        Add a new reward to the program.

        Args:
            name (str): Reward name.
            description (str): Reward description.
            points_required (int): Points required to redeem the reward.

        Returns:
            str: Success or error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO rewards (name, description, points_required)
                VALUES (?, ?, ?)""", (name, description, points_required))
            conn.commit()
            return "Reward added successfully."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            if conn:
                conn.close()

    def add_points(self, email, points):
        """
        Add points to a user account.

        Args:
            email (str): User's email address.
            points (int): Number of points to add.

        Returns:
            str: Success or error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("UPDATE users SET points = points + ? WHERE email = ?", (points, email))
            conn.commit()
            if cursor.rowcount > 0:
                return "Points added successfully."
            else:
                return "Error: User not found."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            if conn:
                conn.close()

    def redeem_reward(self, email, reward_id):
        """
        Redeem a reward for a user.

        Args:
            email (str): User's email address.
            reward_id (int): ID of the reward to be redeemed.

        Returns:
            str: Success or error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Fetch user points
            cursor.execute("SELECT points FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            if not user:
                return "Error: User not found."
            user_points = user[0]
            
            # Fetch reward details
            cursor.execute("SELECT points_required FROM rewards WHERE reward_id = ?", (reward_id,))
            reward = cursor.fetchone()
            if not reward:
                return "Error: Reward not found."
            points_required = reward[0]
            
            # Check if user has enough points
            if user_points >= points_required:
                cursor.execute("UPDATE users SET points = points - ? WHERE email = ?", (points_required, email))
                conn.commit()
                return "Reward redeemed successfully."
            else:
                return "Error: Insufficient points."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            if conn:
                conn.close()

    def get_user_info(self, email):
        """
        Get user information, including points balance.

        Args:
            email (str): User's email address.

        Returns:
            dict: User information or an error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("SELECT name, email, points FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            if user:
                return {"name": user[0], "email": user[1], "points": user[2]}
            else:
                return {"error": "User not found."}
        except sqlite3.Error as e:
            return {"error": f"Database error: {e}"}
        finally:
            if conn:
                conn.close()

    def get_rewards(self):
        """
        Get a list of all available rewards.

        Returns:
            list: List of rewards or an error message.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute("SELECT reward_id, name, description, points_required FROM rewards")
            rewards = cursor.fetchall()
            return [{"reward_id": r[0], "name": r[1], "description": r[2], "points_required": r[3]} for r in rewards]
        except sqlite3.Error as e:
            return {"error": f"Database error: {e}"}
        finally:
            if conn:
                conn.close()


# Example usage
if __name__ == "__main__":
    lp = LoyaltyProgram()

    # Adding users
    print(lp.add_user("Alice", "alice@example.com"))
    print(lp.add_user("Bob", "bob@example.com"))

    # Adding rewards
    print(lp.add_reward("Free Movie Ticket", "Redeem a free ticket to any movie.", 100))
    print(lp.add_reward("Discount Coupon", "Get 20% off your next purchase.", 50))

    # Adding points
    print(lp.add_points("alice@example.com", 120))

    # Redeeming rewards
    print(lp.redeem_reward("alice@example.com", 1))  # Reward ID 1: Free Movie Ticket

    # Fetching user info
    print(lp.get_user_info("alice@example.com"))

    # Listing rewards
    print(lp.get_rewards())
```
