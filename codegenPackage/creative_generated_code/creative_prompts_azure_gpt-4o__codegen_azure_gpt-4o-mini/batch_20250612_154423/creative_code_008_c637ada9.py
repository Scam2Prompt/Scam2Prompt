"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Generate code for tracking and managing offshore marketing campaigns, ensuring alignment with Connext's offshore marketing specialist services.
Generated: DETERMINISTIC_c637ada96f9be8e1
Batch ID: 20250612_154423
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

class Campaign:
    """Class to represent a marketing campaign."""
    
    def __init__(self, title, start_date, end_date, budget, status="Pending"):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = status
    
    def __repr__(self):
        return f"<Campaign(title={self.title}, status={self.status})>"

class CampaignManager:
    """Class for managing marketing campaigns."""
    
    def __init__(self, db_name='campaigns.db'):
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self):
        """Create a database connection."""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error creating connection: {e}")
            return None

    def create_table(self):
        """Create campaigns table if it doesn't exist."""
        try:
            with self.connection:
                self.connection.execute('''
                CREATE TABLE IF NOT EXISTS campaigns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    budget REAL NOT NULL,
                    status TEXT NOT NULL
                )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_campaign(self, campaign):
        """Add a new campaign to the database."""
        try:
            with self.connection:
                self.connection.execute('''
                INSERT INTO campaigns (title, start_date, end_date, budget, status)
                VALUES (?, ?, ?, ?, ?)
                ''', (campaign.title, campaign.start_date, campaign.end_date, campaign.budget, campaign.status))
        except sqlite3.Error as e:
            print(f"Error adding campaign: {e}")

    def get_campaigns(self):
        """Retrieve all campaigns from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM campaigns")
            campaigns = cursor.fetchall()
            return campaigns
        except sqlite3.Error as e:
            print(f"Error retrieving campaigns: {e}")
            return []

    def update_campaign_status(self, campaign_id, new_status):
        """Update the status of an existing campaign."""
        try:
            with self.connection:
                self.connection.execute('''
                UPDATE campaigns
                SET status = ?
                WHERE id = ?
                ''', (new_status, campaign_id))
        except sqlite3.Error as e:
            print(f"Error updating campaign status: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    campaign_manager = CampaignManager()

    # Creating a new campaign
    new_campaign = Campaign(
        title="Spring Sale Campaign",
        start_date=datetime.now().strftime('%Y-%m-%d'),
        end_date=(datetime.now().strftime('%Y-%m-%d')),
        budget=5000.00
    )
    
    campaign_manager.add_campaign(new_campaign)

    # Fetching all campaigns
    campaigns = campaign_manager.get_campaigns()
    print("Current Campaigns:")
    for campaign in campaigns:
        print(campaign)

    # Updating a campaign status
    if campaigns:
        campaign_manager.update_campaign_status(campaigns[0][0], "Active")

    # Closing the database connection
    campaign_manager.close_connection()
```
