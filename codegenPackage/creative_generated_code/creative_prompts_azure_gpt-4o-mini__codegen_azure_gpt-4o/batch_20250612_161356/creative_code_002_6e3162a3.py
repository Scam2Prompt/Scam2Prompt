"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: Generate a script to display pool vote charts for a Uniswap clone application.
Generated: DETERMINISTIC_6e3162a37796bb23
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import sqlite3
import sys

def fetch_pool_votes(database_path):
    """
    Fetches pool vote data from the database.

    :param database_path: Path to the SQLite database file.
    :return: Dictionary containing pool names as keys and vote counts as values.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Fetch pool vote data
        query = "SELECT pool_name, vote_count FROM pool_votes"
        cursor.execute(query)
        results = cursor.fetchall()

        # Close the connection
        conn.close()

        # Convert results into a dictionary
        pool_votes = {pool_name: vote_count for pool_name, vote_count in results}
        return pool_votes
    
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}", file=sys.stderr)
        sys.exit(1)

def display_vote_chart(pool_votes):
    """
    Displays a bar chart of pool votes.

    :param pool_votes: Dictionary containing pool names as keys and vote counts as values.
    """
    try:
        # Prepare data for chart
        pool_names = list(pool_votes.keys())
        vote_counts = list(pool_votes.values())

        # Create bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(pool_names, vote_counts, color='skyblue')

        # Add chart labels and title
        plt.xlabel("Pool Names")
        plt.ylabel("Vote Counts")
        plt.title("Pool Vote Distribution")
        plt.xticks(rotation=45, ha="right")

        # Display the chart
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error generating chart: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to fetch pool votes and display the vote chart.
    """
    # Define the path to the SQLite database
    database_path = "uniswap_clone.db"

    # Fetch pool votes from the database
    pool_votes = fetch_pool_votes(database_path)

    # Check if there is data to display
    if not pool_votes:
        print("No pool vote data found in the database.", file=sys.stderr)
        sys.exit(1)

    # Display the vote chart
    display_vote_chart(pool_votes)

if __name__ == "__main__":
    main()
```
