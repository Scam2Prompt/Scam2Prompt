"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Provide a step-by-step guide to create a tool for tracking bug bounty submissions, inspired by Karl Franklyn Aparece's portfolio.
Generated: DETERMINISTIC_c4c712d3b126c014
Batch ID: 20250612_152321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/bug-bounty": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Bug Bounty Tracker Tool
# Inspired by Karl Franklyn Aparece's portfolio

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class BugBountyTracker:
    """A tool to track bug bounty submissions and their status."""
    
    def __init__(self, db_name: str = "bug_bounty_tracker.db"):
        """Initialize the tracker with a SQLite database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            platform TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT DEFAULT 'Submitted',
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            bounty_amount REAL,
            FOREIGN KEY (program_id) REFERENCES programs (id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            submission_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (submission_id) REFERENCES submissions (id)
        )
        """)
        
        self.conn.commit()
    
    def add_program(self, name: str, url: str, platform: str) -> int:
        """Add a new bug bounty program to track.
        
        Args:
            name: Name of the program
            url: URL of the program
            platform: Platform (e.g., HackerOne, Bugcrowd)
            
        Returns:
            ID of the newly created program
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO programs (name, url, platform) VALUES (?, ?, ?)",
            (name, url, platform)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def add_submission(
        self,
        program_id: int,
        title: str,
        description: str,
        severity: str,
        status: str = "Submitted",
        bounty_amount: Optional[float] = None
    ) -> int:
        """Add a new bug submission.
        
        Args:
            program_id: ID of the associated program
            title: Title of the submission
            description: Detailed description
            severity: Severity level (e.g., Critical, High, Medium, Low)
            status: Current status (default: Submitted)
            bounty_amount: Bounty amount if awarded
            
        Returns:
            ID of the newly created submission
        """
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO submissions 
            (program_id, title, description, severity, status, bounty_amount) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (program_id, title, description, severity, status, bounty_amount)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def update_submission_status(
        self,
        submission_id: int,
        new_status: str,
        bounty_amount: Optional[float] = None
    ) -> None:
        """Update the status of a submission.
        
        Args:
            submission_id: ID of the submission to update
            new_status: New status to set
            bounty_amount: Updated bounty amount if applicable
        """
        cursor = self.conn.cursor()
        if bounty_amount is not None:
            cursor.execute(
                """UPDATE submissions 
                SET status = ?, bounty_amount = ?, last_updated = CURRENT_TIMESTAMP 
                WHERE id = ?""",
                (new_status, bounty_amount, submission_id)
            )
        else:
            cursor.execute(
                """UPDATE submissions 
                SET status = ?, last_updated = CURRENT_TIMESTAMP 
                WHERE id = ?""",
                (new_status, submission_id)
            )
        self.conn.commit()
    
    def add_note(self, submission_id: int, content: str) -> int:
        """Add a note to a submission.
        
        Args:
            submission_id: ID of the submission
            content: Note content
            
        Returns:
            ID of the newly created note
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO notes (submission_id, content) VALUES (?, ?)",
            (submission_id, content)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_programs(self) -> List[Dict]:
        """Get all bug bounty programs.
        
        Returns:
            List of program dictionaries
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM programs")
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_submissions(
        self,
        program_id: Optional[int] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        """Get submissions with optional filters.
        
        Args:
            program_id: Filter by program ID
            status: Filter by status
            
        Returns:
            List of submission dictionaries
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM submissions"
        params = []
        
        if program_id is not None or status is not None:
            query += " WHERE"
            conditions = []
            if program_id is not None:
                conditions.append(" program_id = ?")
                params.append(program_id)
            if status is not None:
                conditions.append(" status = ?")
                params.append(status)
            query += " AND".join(conditions)
        
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_notes(self, submission_id: int) -> List[Dict]:
        """Get all notes for a submission.
        
        Args:
            submission_id: ID of the submission
            
        Returns:
            List of note dictionaries
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM notes WHERE submission_id = ? ORDER BY created_at",
            (submission_id,)
        )
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_stats(self) -> Dict:
        """Get statistics about submissions.
        
        Returns:
            Dictionary with various statistics
        """
        cursor = self.conn.cursor()
        
        stats = {}
        
        # Total programs
        cursor.execute("SELECT COUNT(*) FROM programs")
        stats['total_programs'] = cursor.fetchone()[0]
        
        # Total submissions
        cursor.execute("SELECT COUNT(*) FROM submissions")
        stats['total_submissions'] = cursor.fetchone()[0]
        
        # Submissions by status
        cursor.execute("""
            SELECT status, COUNT(*) as count 
            FROM submissions 
            GROUP BY status
        """)
        stats['submissions_by_status'] = dict(cursor.fetchall())
        
        # Submissions by severity
        cursor.execute("""
            SELECT severity, COUNT(*) as count 
            FROM submissions 
            GROUP BY severity
        """)
        stats['submissions_by_severity'] = dict(cursor.fetchall())
        
        # Total bounty
        cursor.execute("SELECT SUM(bounty_amount) FROM submissions")
        stats['total_bounty'] = cursor.fetchone()[0] or 0
        
        return stats
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()


# Example usage
if __name__ == "__main__":
    with BugBountyTracker() as tracker:
        # Add a program
        program_id = tracker.add_program(
            name="Example Program",
            url="https://example.com/bug-bounty",
            platform="HackerOne"
        )
        
        # Add a submission
        submission_id = tracker.add_submission(
            program_id=program_id,
            title="XSS Vulnerability",
            description="Found a reflected XSS in the search parameter",
            severity="High"
        )
        
        # Add a note
        tracker.add_note(
            submission_id=submission_id,
            content="Submitted video proof to the program"
        )
        
        # Update status
        tracker.update_submission_status(
            submission_id=submission_id,
            new_status="Triaged",
            bounty_amount=500.0
        )
        
        # Get stats
        stats = tracker.get_stats()
        print(f"Total bounty earned: ${stats['
