"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Create a program to track and visualize public participation in environmental campaigns, inspired by the collaborative approach of "Čuvari Šare."
Generated: DETERMINISTIC_86af4a47514cf038
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple

class EnvironmentalCampaignTracker:
    """
    A class to track and visualize public participation in environmental campaigns.
    """
    
    def __init__(self, db_name: str = "campaigns.db"):
        """
        Initialize the tracker with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary database tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            start_date TEXT NOT NULL,
            end_date TEXT,
            target_participants INTEGER,
            location TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            participation_date TEXT NOT NULL,
            hours_contributed REAL DEFAULT 0,
            FOREIGN KEY (campaign_id) REFERENCES campaigns (id)
        )
        """)
        
        self.conn.commit()
    
    def add_campaign(self, name: str, start_date: str, description: str = None,
                    end_date: str = None, target_participants: int = None,
                    location: str = None) -> int:
        """
        Add a new environmental campaign to the tracker.
        
        Args:
            name: Name of the campaign
            start_date: Start date in YYYY-MM-DD format
            description: Description of the campaign
            end_date: End date in YYYY-MM-DD format (optional)
            target_participants: Target number of participants (optional)
            location: Location of the campaign (optional)
            
        Returns:
            ID of the newly created campaign
            
        Raises:
            ValueError: If start_date is not in correct format
        """
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO campaigns (name, description, start_date, end_date, target_participants, location)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, description, start_date, end_date, target_participants, location))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def add_participant(self, campaign_id: int, name: str, participation_date: str,
                       email: str = None, hours_contributed: float = 0) -> int:
        """
        Add a participant to a campaign.
        
        Args:
            campaign_id: ID of the campaign
            name: Name of the participant
            participation_date: Date of participation in YYYY-MM-DD format
            email: Email of the participant (optional)
            hours_contributed: Hours contributed by the participant (optional)
            
        Returns:
            ID of the newly created participant record
            
        Raises:
            ValueError: If participation_date is not in correct format or campaign doesn't exist
        """
        try:
            datetime.strptime(participation_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
            
        # Verify campaign exists
        if not self.get_campaign(campaign_id):
            raise ValueError(f"Campaign with ID {campaign_id} does not exist")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO participants (campaign_id, name, email, participation_date, hours_contributed)
        VALUES (?, ?, ?, ?, ?)
        """, (campaign_id, name, email, participation_date, hours_contributed))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def get_campaign(self, campaign_id: int) -> Optional[Dict]:
        """
        Get campaign details by ID.
        
        Args:
            campaign_id: ID of the campaign
            
        Returns:
            Dictionary with campaign details or None if not found
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM campaigns WHERE id = ?", (campaign_id,))
        row = cursor.fetchone()
        
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None
    
    def get_participants(self, campaign_id: int) -> List[Dict]:
        """
        Get all participants for a campaign.
        
        Args:
            campaign_id: ID of the campaign
            
        Returns:
            List of dictionaries with participant details
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM participants WHERE campaign_id = ?", (campaign_id,))
        rows = cursor.fetchall()
        
        if rows:
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        return []
    
    def get_campaign_stats(self, campaign_id: int) -> Dict:
        """
        Get statistics for a campaign.
        
        Args:
            campaign_id: ID of the campaign
            
        Returns:
            Dictionary with campaign statistics
        """
        campaign = self.get_campaign(campaign_id)
        if not campaign:
            return {}
            
        cursor = self.conn.cursor()
        
        # Get participant count
        cursor.execute("SELECT COUNT(*) FROM participants WHERE campaign_id = ?", (campaign_id,))
        participant_count = cursor.fetchone()[0]
        
        # Get total hours contributed
        cursor.execute("SELECT SUM(hours_contributed) FROM participants WHERE campaign_id = ?", (campaign_id,))
        total_hours = cursor.fetchone()[0] or 0
        
        return {
            "campaign_id": campaign_id,
            "name": campaign["name"],
            "participant_count": participant_count,
            "total_hours": total_hours,
            "target_participants": campaign["target_participants"],
            "participation_rate": participant_count / campaign["target_participants"] * 100 
                if campaign["target_participants"] else None
        }
    
    def visualize_participation(self, campaign_id: int, save_path: str = None) -> None:
        """
        Generate a visualization of campaign participation.
        
        Args:
            campaign_id: ID of the campaign
            save_path: Path to save the visualization (optional)
        """
        stats = self.get_campaign_stats(campaign_id)
        if not stats:
            print(f"No campaign found with ID {campaign_id}")
            return
            
        participants = self.get_participants(campaign_id)
        
        # Prepare data for visualization
        dates = [p["participation_date"] for p in participants]
        date_counts = {}
        for date in dates:
            date_counts[date] = date_counts.get(date, 0) + 1
            
        sorted_dates = sorted(date_counts.items(), key=lambda x: x[0])
        dates = [date for date, count in sorted_dates]
        counts = [count for date, count in sorted_dates]
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.bar(dates, counts, color='green')
        plt.title(f"Participation in {stats['name']}")
        plt.xlabel("Date")
        plt.ylabel("Number of Participants")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            print(f"Visualization saved to {save_path}")
        else:
            plt.show()
    
    def export_campaign_data(self, campaign_id: int, file_path: str) -> None:
        """
        Export campaign data to a JSON file.
        
        Args:
            campaign_id: ID of the campaign
            file_path: Path to save the JSON file
            
        Raises:
            ValueError: If campaign doesn't exist
        """
        campaign = self.get_campaign(campaign_id)
        if not campaign:
            raise ValueError(f"Campaign with ID {campaign_id} does not exist")
            
        participants = self.get_participants(campaign_id)
        stats = self.get_campaign_stats(campaign_id)
        
        data = {
            "campaign": campaign,
            "participants": participants,
            "statistics": stats
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for
