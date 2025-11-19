"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a script to organize innovation competitions and idea submissions, inspired by ORIC's innovation/idea competition initiatives.
Generated: DETERMINISTIC_04bb3fa9a7ca8013
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import uuid
from datetime import datetime
from typing import List, Dict, Optional

# Database file path
DB_FILE = "innovations_db.json"

class InnovationCompetition:
    """
    A class to manage innovation competitions and idea submissions.
    """
    
    def __init__(self):
        """Initialize the competition database."""
        self.db = self._load_database()
    
    def _load_database(self) -> Dict:
        """Load the database from file or create a new one if it doesn't exist."""
        try:
            if os.path.exists(DB_FILE):
                with open(DB_FILE, 'r') as f:
                    return json.load(f)
            return {
                "competitions": {},
                "submissions": {},
                "next_competition_id": 1,
                "next_submission_id": 1
            }
        except Exception as e:
            print(f"Error loading database: {e}")
            return {
                "competitions": {},
                "submissions": {},
                "next_competition_id": 1,
                "next_submission_id": 1
            }
    
    def _save_database(self) -> bool:
        """Save the database to file."""
        try:
            with open(DB_FILE, 'w') as f:
                json.dump(self.db, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving database: {e}")
            return False
    
    def create_competition(
        self,
        title: str,
        description: str,
        start_date: str,
        end_date: str,
        rules: Optional[str] = None,
        prizes: Optional[str] = None
    ) -> Optional[int]:
        """
        Create a new innovation competition.
        
        Args:
            title: Competition title
            description: Detailed description
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            rules: Competition rules (optional)
            prizes: Prize details (optional)
            
        Returns:
            Competition ID if successful, None otherwise
        """
        try:
            # Validate dates
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
            
            competition_id = self.db["next_competition_id"]
            self.db["competitions"][competition_id] = {
                "id": competition_id,
                "title": title,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "rules": rules,
                "prizes": prizes,
                "created_at": datetime.now().isoformat(),
                "status": "upcoming"
            }
            
            self.db["next_competition_id"] += 1
            self._save_database()
            return competition_id
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return None
        except Exception as e:
            print(f"Error creating competition: {e}")
            return None
    
    def get_competition(self, competition_id: int) -> Optional[Dict]:
        """Get competition details by ID."""
        return self.db["competitions"].get(competition_id)
    
    def list_competitions(self, status: Optional[str] = None) -> List[Dict]:
        """List all competitions, optionally filtered by status."""
        competitions = list(self.db["competitions"].values())
        if status:
            return [c for c in competitions if c["status"].lower() == status.lower()]
        return competitions
    
    def update_competition_status(self, competition_id: int, status: str) -> bool:
        """Update competition status (upcoming, active, completed, canceled)."""
        if competition_id not in self.db["competitions"]:
            print("Competition not found")
            return False
        
        valid_statuses = ["upcoming", "active", "completed", "canceled"]
        if status.lower() not in valid_statuses:
            print(f"Invalid status. Must be one of: {valid_statuses}")
            return False
        
        self.db["competitions"][competition_id]["status"] = status.lower()
        self._save_database()
        return True
    
    def submit_idea(
        self,
        competition_id: int,
        title: str,
        description: str,
        submitter_name: str,
        submitter_email: str,
        attachments: Optional[List[str]] = None,
        additional_info: Optional[Dict] = None
    ) -> Optional[int]:
        """
        Submit an idea to a competition.
        
        Args:
            competition_id: ID of the competition
            title: Idea title
            description: Detailed description
            submitter_name: Name of submitter
            submitter_email: Email of submitter
            attachments: List of file paths (optional)
            additional_info: Additional metadata (optional)
            
        Returns:
            Submission ID if successful, None otherwise
        """
        try:
            if competition_id not in self.db["competitions"]:
                print("Competition not found")
                return None
            
            submission_id = self.db["next_submission_id"]
            self.db["submissions"][submission_id] = {
                "id": submission_id,
                "competition_id": competition_id,
                "title": title,
                "description": description,
                "submitter_name": submitter_name,
                "submitter_email": submitter_email,
                "attachments": attachments or [],
                "additional_info": additional_info or {},
                "submitted_at": datetime.now().isoformat(),
                "status": "submitted",
                "unique_id": str(uuid.uuid4())
            }
            
            self.db["next_submission_id"] += 1
            self._save_database()
            return submission_id
        except Exception as e:
            print(f"Error submitting idea: {e}")
            return None
    
    def get_submission(self, submission_id: int) -> Optional[Dict]:
        """Get submission details by ID."""
        return self.db["submissions"].get(submission_id)
    
    def list_submissions(self, competition_id: Optional[int] = None) -> List[Dict]:
        """List all submissions, optionally filtered by competition ID."""
        submissions = list(self.db["submissions"].values())
        if competition_id:
            return [s for s in submissions if s["competition_id"] == competition_id]
        return submissions
    
    def update_submission_status(self, submission_id: int, status: str) -> bool:
        """Update submission status (submitted, under_review, approved, rejected)."""
        if submission_id not in self.db["submissions"]:
            print("Submission not found")
            return False
        
        valid_statuses = ["submitted", "under_review", "approved", "rejected"]
        if status.lower() not in valid_statuses:
            print(f"Invalid status. Must be one of: {valid_statuses}")
            return False
        
        self.db["submissions"][submission_id]["status"] = status.lower()
        self._save_database()
        return True
    
    def add_submission_comment(self, submission_id: int, comment: str, reviewer: str) -> bool:
        """Add a comment/review to a submission."""
        if submission_id not in self.db["submissions"]:
            print("Submission not found")
            return False
        
        if "comments" not in self.db["submissions"][submission_id]:
            self.db["submissions"][submission_id]["comments"] = []
            
        self.db["submissions"][submission_id]["comments"].append({
            "comment": comment,
            "reviewer": reviewer,
            "timestamp": datetime.now().isoformat()
        })
        
        self._save_database()
        return True
    
    def get_competition_submissions_stats(self, competition_id: int) -> Optional[Dict]:
        """Get statistics for submissions in a competition."""
        if competition_id not in self.db["competitions"]:
            print("Competition not found")
            return None
        
        submissions = self.list_submissions(competition_id)
        if not submissions:
            return None
            
        status_counts = {}
        for submission in submissions:
            status = submission["status"]
            status_counts[status] = status_counts.get(status, 0) + 1
            
        return {
            "total_submissions": len(submissions),
            "status_counts": status_counts,
            "first_submission": min(s["submitted_at"] for s in submissions),
            "last_submission": max(s["submitted_at"] for s in submissions)
        }


# Example usage
if __name__ == "__main__":
    competition = InnovationCompetition()
    
    # Create a competition
    comp_id = competition.create_competition(
        title="Green Energy Solutions",
        description="Submit your innovative ideas for sustainable energy",
        start_date="2023-11-01",
        end_date="2023-12-31",
        prizes="1st: $10,000, 2nd: $5,000, 3rd: $2,500"
    )
    
    if comp_id:
        print(f"Created competition with ID: {comp_id}")
        
        # Submit an idea
        submission_id = competition.submit_idea(
            competition_id=comp_id,
            title="Solar-Powered Water Purification",
