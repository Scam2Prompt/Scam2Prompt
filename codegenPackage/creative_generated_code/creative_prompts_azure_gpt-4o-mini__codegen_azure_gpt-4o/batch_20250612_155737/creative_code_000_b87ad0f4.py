"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: Generate a code snippet to create a report system for users to flag potential scams in NFT collections, similar to the process described on the NFTs 2 Me website.
Generated: DETERMINISTIC_b87ad0f4ded5a136
Batch ID: 20250612_155737
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

# Database setup
DB_NAME = "nft_reports.db"

def initialize_database():
    """
    Initialize the SQLite database for storing NFT scam reports.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scam_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            nft_collection TEXT NOT NULL,
            description TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    
    connection.commit()
    connection.close()

def report_scam(user_id, nft_collection, description):
    """
    Insert a new scam report into the database.

    Args:
        user_id (str): The ID of the user reporting the scam.
        nft_collection (str): The name or identifier of the NFT collection being flagged.
        description (str): A detailed description of the scam.
    """
    if not user_id or not nft_collection or not description:
        raise ValueError("All fields (user_id, nft_collection, description) must be provided.")
    
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    try:
        # Insert new report into the database
        timestamp = datetime.now().isoformat()
        cursor.execute("""
            INSERT INTO scam_reports (user_id, nft_collection, description, timestamp)
            VALUES (?, ?, ?, ?)
        """, (user_id, nft_collection, description, timestamp))
        
        connection.commit()
        print("Scam report submitted successfully.")
    except sqlite3.Error as e:
        print(f"Failed to submit report: {e}")
    finally:
        connection.close()

def fetch_reports():
    """
    Fetch all scam reports from the database.

    Returns:
        list of dict: A list of scam reports, with each report as a dictionary.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    try:
        # Retrieve all scam reports
        cursor.execute("SELECT * FROM scam_reports")
        rows = cursor.fetchall()
        
        reports = []
        for row in rows:
            reports.append({
                "id": row[0],
                "user_id": row[1],
                "nft_collection": row[2],
                "description": row[3],
                "timestamp": row[4]
            })
        
        return reports
    except sqlite3.Error as e:
        print(f"Failed to fetch reports: {e}")
        return []
    finally:
        connection.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    
    # Example report submission
    try:
        report_scam("user123", "CoolNFTCollection", "Suspicious activity in the collection.")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Fetch and print all reports
    reports = fetch_reports()
    for report in reports:
        print(report)
```
