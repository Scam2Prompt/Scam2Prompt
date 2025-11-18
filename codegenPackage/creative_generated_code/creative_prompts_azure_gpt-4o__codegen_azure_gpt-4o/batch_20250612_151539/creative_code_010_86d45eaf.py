"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Generate code to display a leaderboard of the highest-ranked casinos based on user ratings, similar to the ranking system on Santa Claus Casino.
Generated: DETERMINISTIC_86d45eaf5183f1e1
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database setup
DB_NAME = "casinos.db"

def setup_database():
    """Sets up the database with necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create casinos table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS casinos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 5)
        )
    """)
    conn.commit()
    conn.close()

def fetch_top_casinos(limit=10):
    """
    Fetches the top casinos based on user ratings.
    Args:
        limit (int): Number of top casinos to fetch.
    Returns:
        list: List of dictionaries containing casino details.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Fetch casinos ordered by rating in descending order
        cursor.execute("""
            SELECT name, rating
            FROM casinos
            ORDER BY rating DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        # Convert rows to a list of dictionaries
        return [{"name": row[0], "rating": row[1]} for row in rows]
    except sqlite3.Error as e:
        print(f"Error fetching data from database: {e}")
        return []

def display_leaderboard(casinos):
    """
    Displays the leaderboard of top casinos.
    Args:
        casinos (list): List of dictionaries containing casino details.
    """
    print("Leaderboard - Top Casinos")
    print("-" * 30)
    print(f"{'Rank':<6}{'Casino Name':<20}{'Rating':<6}")
    print("-" * 30)
    for rank, casino in enumerate(casinos, start=1):
        print(f"{rank:<6}{casino['name']:<20}{casino['rating']:<6.1f}")

def main():
    """Main function to display the leaderboard."""
    setup_database()  # Ensure the database is set up
    top_casinos = fetch_top_casinos(limit=10)  # Fetch top 10 casinos
    display_leaderboard(top_casinos)  # Display the leaderboard

if __name__ == "__main__":
    main()
```
