"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write Python code to simulate a patent filing process for an invention, incorporating the guidelines provided by ORIC at Kinnaird College.
Generated: DETERMINISTIC_cf5689678d428076
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
from datetime import datetime
from uuid import uuid4
from typing import Dict, List, Optional, Tuple

class PatentFilingSystem:
    """
    A system to simulate the patent filing process following ORIC guidelines at Kinnaird College.
    Handles invention submissions, validations, reviews, and approvals.
    """
    
    def __init__(self):
        self.patents_db = {}  # Stores all patent records
        self.inventors_db = {}  # Stores inventor information
        self.reviewers_db = {}  # Stores reviewer information
        self.statuses = ["DRAFT", "SUBMITTED", "UNDER_REVIEW", "APPROVED", "REJECTED"]
    
    def register_inventor(self, name: str, email: str, department: str) -> str:
        """
        Register a new inventor in the system.
        
        Args:
            name: Full name of the inventor
            email: Email address
            department: Department/affiliation
            
        Returns:
            inventor_id: Unique identifier for the inventor
        """
        if not all([name, email, department]):
            raise ValueError("All inventor details must be provided")
            
        inventor_id = f"INV-{uuid4().hex[:8]}"
        self.inventors_db[inventor_id] = {
            "name": name,
            "email": email,
            "department": department,
            "registration_date": datetime.now().isoformat()
        }
        return inventor_id
    
    def register_reviewer(self, name: str, email: str, expertise: List[str]) -> str:
        """
        Register a new patent reviewer in the system.
        
        Args:
            name: Full name of the reviewer
            email: Email address
            expertise: List of technical expertise areas
            
        Returns:
            reviewer_id: Unique identifier for the reviewer
        """
        if not all([name, email, expertise]):
            raise ValueError("All reviewer details must be provided")
            
        reviewer_id = f"REV-{uuid4().hex[:8]}"
        self.reviewers_db[reviewer_id] = {
            "name": name,
            "email": email,
            "expertise": expertise,
            "registration_date": datetime.now().isoformat()
        }
        return reviewer_id
    
    def submit_invention(self, 
                        title: str, 
                        description: str, 
                        inventors: List[str], 
                        category: str,
                        attachments: Optional[List[Dict]] = None) -> str:
        """
        Submit a new invention for patent consideration.
        
        Args:
            title: Title of the invention
            description: Detailed description
            inventors: List of inventor IDs
            category: Invention category (e.g., "Software", "Hardware")
            attachments: Optional list of supporting documents
            
        Returns:
            patent_id: Unique identifier for the patent application
        """
        if not all([title, description, inventors, category]):
            raise ValueError("All required fields must be provided")
            
        for inventor_id in inventors:
            if inventor_id not in self.inventors_db:
                raise ValueError(f"Inventor {inventor_id} not registered")
                
        patent_id = f"PAT-{uuid4().hex[:8]}"
        
        self.patents_db[patent_id] = {
            "title": title,
            "description": description,
            "inventors": inventors,
            "category": category,
            "status": "DRAFT",
            "submission_date": None,
            "reviewers": [],
            "attachments": attachments or [],
            "reviews": [],
            "decision": None,
            "decision_date": None,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        return patent_id
    
    def submit_patent_application(self, patent_id: str) -> bool:
        """
        Submit a draft patent application for official review.
        
        Args:
            patent_id: ID of the patent to submit
            
        Returns:
            bool: True if submission was successful
        """
        if patent_id not in self.patents_db:
            raise ValueError("Patent not found")
            
        if self.patents_db[patent_id]["status"] != "DRAFT":
            raise ValueError("Only draft patents can be submitted")
            
        self.patents_db[patent_id]["status"] = "SUBMITTED"
        self.patents_db[patent_id]["submission_date"] = datetime.now().isoformat()
        self.patents_db[patent_id]["updated_at"] = datetime.now().isoformat()
        
        return True
    
    def assign_reviewers(self, patent_id: str, reviewer_ids: List[str]) -> bool:
        """
        Assign reviewers to a submitted patent application.
        
        Args:
            patent_id: ID of the patent to review
            reviewer_ids: List of reviewer IDs to assign
            
        Returns:
            bool: True if assignment was successful
        """
        if patent_id not in self.patents_db:
            raise ValueError("Patent not found")
            
        if self.patents_db[patent_id]["status"] != "SUBMITTED":
            raise ValueError("Only submitted patents can be assigned reviewers")
            
        for reviewer_id in reviewer_ids:
            if reviewer_id not in self.reviewers_db:
                raise ValueError(f"Reviewer {reviewer_id} not registered")
                
        self.patents_db[patent_id]["reviewers"] = reviewer_ids
        self.patents_db[patent_id]["status"] = "UNDER_REVIEW"
        self.patents_db[patent_id]["updated_at"] = datetime.now().isoformat()
        
        return True
    
    def submit_review(self, 
                     patent_id: str, 
                     reviewer_id: str, 
                     comments: str, 
                     recommendation: str) -> bool:
        """
        Submit a review for a patent application.
        
        Args:
            patent_id: ID of the patent being reviewed
            reviewer_id: ID of the reviewer
            comments: Detailed review comments
            recommendation: "APPROVE" or "REJECT"
            
        Returns:
            bool: True if review submission was successful
        """
        if patent_id not in self.patents_db:
            raise ValueError("Patent not found")
            
        if reviewer_id not in self.reviewers_db:
            raise ValueError("Reviewer not registered")
            
        if self.patents_db[patent_id]["status"] != "UNDER_REVIEW":
            raise ValueError("Patent is not under review")
            
        if reviewer_id not in self.patents_db[patent_id]["reviewers"]:
            raise ValueError("Reviewer not assigned to this patent")
            
        if recommendation not in ["APPROVE", "REJECT"]:
            raise ValueError("Recommendation must be either APPROVE or REJECT")
            
        review = {
            "reviewer_id": reviewer_id,
            "comments": comments,
            "recommendation": recommendation,
            "review_date": datetime.now().isoformat()
        }
        
        self.patents_db[patent_id]["reviews"].append(review)
        self.patents_db[patent_id]["updated_at"] = datetime.now().isoformat()
        
        return True
    
    def make_decision(self, patent_id: str) -> bool:
        """
        Make a final decision on a patent application based on reviews.
        
        Args:
            patent_id: ID of the patent to decide on
            
        Returns:
            bool: True if decision was made successfully
        """
        if patent_id not in self.patents_db:
            raise ValueError("Patent not found")
            
        if self.patents_db[patent_id]["status"] != "UNDER_REVIEW":
            raise ValueError("Patent is not under review")
            
        reviews = self.patents_db[patent_id]["reviews"]
        if not reviews:
            raise ValueError("No reviews submitted for this patent")
            
        # Simple decision logic: majority approval
        approvals = sum(1 for r in reviews if r["recommendation"] == "APPROVE")
        rejections = len(reviews) - approvals
        
        if approvals > rejections:
            decision = "APPROVED"
        else:
            decision = "REJECTED"
            
        self.patents_db[patent_id]["status"] = decision
        self.patents_db[patent_id]["decision"] = decision
        self.patents_db[patent_id]["decision_date"] = datetime.now().isoformat()
        self.patents_db[patent_id]["updated_at"] = datetime.now().isoformat()
        
        return True
    
    def get_patent_status(self, patent_id: str) -> Dict:
        """
        Retrieve the current status of a patent application.
        
        Args:
            patent_id: ID of the patent to check
            
        Returns:
            dict: Patent status information
        """
        if patent_id not in self.patents_db:
            raise ValueError("Patent not found")
            
        return {
            "patent_id": patent_id,
            "title": self.patents_db[patent_id]["title"],
            "status": self.patents_db[patent_id]["status"],
            "decision": self.patents_db[patent_id]["decision"],
            "last_updated": self.patents_db[patent_id]["
