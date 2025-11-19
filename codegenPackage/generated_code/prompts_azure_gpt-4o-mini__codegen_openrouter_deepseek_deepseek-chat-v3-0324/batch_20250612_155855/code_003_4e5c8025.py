"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Develop a code snippet that tracks donations for sustainability projects, ensuring transparency and community involvement in environmental health initiatives.
Generated: DETERMINISTIC_4e5c8025f8763f7d
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class DonationTracker:
    """
    A class to track donations for sustainability projects with transparency features.
    """
    
    def __init__(self, db_path: str = "donations.db"):
        """
        Initialize the donation tracker with a SQLite database.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self) -> None:
        """Initialize the database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Projects table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    target_amount REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Donations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    donor_name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_anonymous BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (project_id) REFERENCES projects (id)
                )
            """)
            
            # Community votes table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    voter_id TEXT NOT NULL,
                    vote_value INTEGER NOT NULL,  # 1 for upvote, -1 for downvote
                    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (project_id) REFERENCES projects (id),
                    UNIQUE(project_id, voter_id)
                )
            """)
            
            conn.commit()
    
    def add_project(self, name: str, description: str, target_amount: float) -> int:
        """
        Add a new sustainability project to track.
        
        Args:
            name: Name of the project
            description: Description of the project
            target_amount: Funding target amount
            
        Returns:
            The ID of the newly created project
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if not name or not description:
            raise ValueError("Project name and description cannot be empty")
        if target_amount <= 0:
            raise ValueError("Target amount must be positive")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO projects (name, description, target_amount) VALUES (?, ?, ?)",
                (name, description, target_amount)
            )
            conn.commit()
            return cursor.lastrowid
    
    def record_donation(self, project_id: int, donor_name: str, amount: float, is_anonymous: bool = False) -> int:
        """
        Record a donation to a project.
        
        Args:
            project_id: ID of the project receiving the donation
            donor_name: Name of the donor
            amount: Donation amount
            is_anonymous: Whether the donation should be anonymous
            
        Returns:
            The ID of the donation record
            
        Raises:
            ValueError: If parameters are invalid or project doesn't exist
        """
        if not donor_name and not is_anonymous:
            raise ValueError("Donor name must be provided unless donation is anonymous")
        if amount <= 0:
            raise ValueError("Donation amount must be positive")
            
        if not self._project_exists(project_id):
            raise ValueError("Project does not exist")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO donations (project_id, donor_name, amount, is_anonymous) VALUES (?, ?, ?, ?)",
                (project_id, donor_name if not is_anonymous else "Anonymous", amount, is_anonymous)
            )
            conn.commit()
            return cursor.lastrowid
    
    def _project_exists(self, project_id: int) -> bool:
        """Check if a project exists."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM projects WHERE id = ?", (project_id,))
            return cursor.fetchone() is not None
    
    def get_project_donations(self, project_id: int) -> List[Dict]:
        """
        Get all donations for a specific project.
        
        Args:
            project_id: ID of the project
            
        Returns:
            List of donation records as dictionaries
            
        Raises:
            ValueError: If project doesn't exist
        """
        if not self._project_exists(project_id):
            raise ValueError("Project does not exist")
            
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, donor_name, amount, donation_date, is_anonymous FROM donations WHERE project_id = ?",
                (project_id,)
            )
            return [dict(row) for row in cursor.fetchall()]
    
    def get_project_summary(self, project_id: int) -> Dict:
        """
        Get a summary of a project including donation totals and community votes.
        
        Args:
            project_id: ID of the project
            
        Returns:
            Dictionary containing project summary
            
        Raises:
            ValueError: If project doesn't exist
        """
        if not self._project_exists(project_id):
            raise ValueError("Project does not exist")
            
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Get project details
            cursor.execute("SELECT name, description, target_amount FROM projects WHERE id = ?", (project_id,))
            project = dict(cursor.fetchone())
            
            # Get donation total
            cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM donations WHERE project_id = ?", (project_id,))
            total_donated = cursor.fetchone()[0]
            
            # Get vote count
            cursor.execute("SELECT COALESCE(SUM(vote_value), 0) FROM votes WHERE project_id = ?", (project_id,))
            vote_score = cursor.fetchone()[0]
            
            return {
                "project_id": project_id,
                "name": project["name"],
                "description": project["description"],
                "target_amount": project["target_amount"],
                "total_donated": total_donated,
                "percent_funded": (total_donated / project["target_amount"]) * 100 if project["target_amount"] > 0 else 0,
                "community_vote_score": vote_score
            }
    
    def record_vote(self, project_id: int, voter_id: str, vote_value: int) -> None:
        """
        Record a community vote for a project.
        
        Args:
            project_id: ID of the project being voted on
            voter_id: Unique identifier for the voter
            vote_value: 1 for upvote, -1 for downvote
            
        Raises:
            ValueError: If parameters are invalid or project doesn't exist
        """
        if vote_value not in (1, -1):
            raise ValueError("Vote value must be 1 (upvote) or -1 (downvote)")
        if not voter_id:
            raise ValueError("Voter ID cannot be empty")
            
        if not self._project_exists(project_id):
            raise ValueError("Project does not exist")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Use INSERT OR REPLACE to handle vote updates
            cursor.execute(
                """INSERT OR REPLACE INTO votes (project_id, voter_id, vote_value)
                   VALUES (?, ?, ?)""",
                (project_id, voter_id, vote_value)
            )
            conn.commit()
    
    def get_all_projects(self) -> List[Dict]:
        """
        Get a list of all projects with their summary information.
        
        Returns:
            List of project summaries
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM projects")
            project_ids = [row[0] for row in cursor.fetchall()]
            
            return [self.get_project_summary(pid) for pid in project_ids]
    
    def export_transparency_report(self, project_id: int) -> str:
        """
        Generate a transparency report for a project in CSV format.
        
        Args:
            project_id: ID of the project
            
        Returns:
            CSV formatted string with donation details
            
        Raises:
            ValueError: If project doesn't exist
        """
        if not self._project_exists(project_id):
            raise ValueError("Project does not exist")
            
        donations = self.get_project_donations(project_id)
        summary = self.get_project_summary(project_id)
        
        report_lines = [
            f"Transparency Report for Project: {summary['name']} (ID: {project_id})",
            f"Description: {summary['description']}",
            f"Target Amount: {summary['target_amount']:.2f}",
            f"Total
