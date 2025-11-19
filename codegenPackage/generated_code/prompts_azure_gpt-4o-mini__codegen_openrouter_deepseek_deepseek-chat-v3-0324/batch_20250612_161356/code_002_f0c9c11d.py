"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-qf-manager-bhrfz6odu-bootnode.vercel.app
Prompt: What are the key features of the Gitcoin Round Manager for managing grant funding?
Generated: DETERMINISTIC_f0c9c11dcf9060ce
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gitcoin Round Manager - Key Features Implementation

This module provides the core functionality for managing grant funding rounds in Gitcoin.
It includes features for round creation, application management, voting, and payout processing.
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import hashlib
import json

class RoundStatus(Enum):
    """Enum representing the status of a funding round."""
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class ApplicationStatus(Enum):
    """Enum representing the status of a grant application."""
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    FUNDED = "FUNDED"

class RoundManager:
    """Main class for managing Gitcoin funding rounds."""
    
    def __init__(self):
        self.rounds = {}  # round_id: round_data
        self.applications = {}  # application_id: application_data
        self.votes = {}  # vote_id: vote_data
        self.payouts = {}  # payout_id: payout_data
    
    def create_round(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        matching_pool: float,
        admin_address: str,
        metadata: Optional[Dict] = None
    ) -> str:
        """Create a new funding round.
        
        Args:
            name: Name of the round
            description: Description of the round
            start_date: When the round starts
            end_date: When the round ends
            matching_pool: Total matching funds available
            admin_address: Ethereum address of round admin
            metadata: Optional additional round data
            
        Returns:
            The ID of the created round
        """
        if start_date >= end_date:
            raise ValueError("End date must be after start date")
            
        if matching_pool <= 0:
            raise ValueError("Matching pool must be positive")
            
        round_id = hashlib.sha256(f"{name}{start_date}{end_date}".encode()).hexdigest()
        
        self.rounds[round_id] = {
            "id": round_id,
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "matching_pool": matching_pool,
            "admin_address": admin_address,
            "status": RoundStatus.DRAFT.value,
            "metadata": metadata or {},
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        return round_id
    
    def update_round_status(self, round_id: str, status: RoundStatus) -> bool:
        """Update the status of a funding round.
        
        Args:
            round_id: ID of the round to update
            status: New status for the round
            
        Returns:
            True if update was successful
        """
        if round_id not in self.rounds:
            raise ValueError("Round not found")
            
        current_status = self.rounds[round_id]["status"]
        
        # Validate status transitions
        valid_transitions = {
            RoundStatus.DRAFT: [RoundStatus.ACTIVE, RoundStatus.CANCELLED],
            RoundStatus.ACTIVE: [RoundStatus.COMPLETED, RoundStatus.CANCELLED],
        }
        
        if status.value not in [s.value for s in valid_transitions.get(RoundStatus(current_status), [])]:
            raise ValueError(f"Invalid status transition from {current_status} to {status.value}")
            
        self.rounds[round_id]["status"] = status.value
        self.rounds[round_id]["updated_at"] = datetime.now()
        return True
    
    def submit_application(
        self,
        round_id: str,
        project_name: str,
        project_description: str,
        funding_needed: float,
        applicant_address: str,
        metadata: Optional[Dict] = None
    ) -> str:
        """Submit a grant application to a funding round.
        
        Args:
            round_id: ID of the round to apply to
            project_name: Name of the project
            project_description: Description of the project
            funding_needed: Amount of funding requested
            applicant_address: Ethereum address of applicant
            metadata: Optional additional application data
            
        Returns:
            The ID of the created application
        """
        if round_id not in self.rounds:
            raise ValueError("Round not found")
            
        if self.rounds[round_id]["status"] != RoundStatus.ACTIVE.value:
            raise ValueError("Round is not active for applications")
            
        if funding_needed <= 0:
            raise ValueError("Funding needed must be positive")
            
        application_id = hashlib.sha256(f"{round_id}{project_name}{applicant_address}".encode()).hexdigest()
        
        self.applications[application_id] = {
            "id": application_id,
            "round_id": round_id,
            "project_name": project_name,
            "project_description": project_description,
            "funding_needed": funding_needed,
            "applicant_address": applicant_address,
            "status": ApplicationStatus.PENDING.value,
            "metadata": metadata or {},
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        return application_id
    
    def review_application(self, application_id: str, status: ApplicationStatus, reviewer_address: str) -> bool:
        """Review and approve/reject an application.
        
        Args:
            application_id: ID of the application to review
            status: New status (APPROVED/REJECTED)
            reviewer_address: Ethereum address of reviewer
            
        Returns:
            True if update was successful
        """
        if application_id not in self.applications:
            raise ValueError("Application not found")
            
        if status not in [ApplicationStatus.APPROVED, ApplicationStatus.REJECTED]:
            raise ValueError("Invalid status for review")
            
        self.applications[application_id]["status"] = status.value
        self.applications[application_id]["reviewer_address"] = reviewer_address
        self.applications[application_id]["updated_at"] = datetime.now()
        return True
    
    def submit_vote(
        self,
        round_id: str,
        application_id: str,
        voter_address: str,
        amount: float,
        token_address: str
    ) -> str:
        """Submit a vote for a grant application.
        
        Args:
            round_id: ID of the funding round
            application_id: ID of the application being voted on
            voter_address: Ethereum address of voter
            amount: Amount of tokens being contributed
            token_address: Address of the token being used
            
        Returns:
            The ID of the created vote
        """
        if round_id not in self.rounds:
            raise ValueError("Round not found")
            
        if application_id not in self.applications:
            raise ValueError("Application not found")
            
        if self.rounds[round_id]["status"] != RoundStatus.ACTIVE.value:
            raise ValueError("Round is not active for voting")
            
        if amount <= 0:
            raise ValueError("Vote amount must be positive")
            
        vote_id = hashlib.sha256(f"{round_id}{application_id}{voter_address}".encode()).hexdigest()
        
        self.votes[vote_id] = {
            "id": vote_id,
            "round_id": round_id,
            "application_id": application_id,
            "voter_address": voter_address,
            "amount": amount,
            "token_address": token_address,
            "created_at": datetime.now()
        }
        
        return vote_id
    
    def calculate_matching_funds(self, round_id: str) -> Dict[str, float]:
        """Calculate matching fund distribution for a round.
        
        Args:
            round_id: ID of the round to calculate
            
        Returns:
            Dictionary mapping application IDs to matching amounts
        """
        if round_id not in self.rounds:
            raise ValueError("Round not found")
            
        if self.rounds[round_id]["status"] != RoundStatus.COMPLETED.value:
            raise ValueError("Round must be completed to calculate matching")
            
        # Get all approved applications for this round
        applications = [
            app for app in self.applications.values() 
            if app["round_id"] == round_id and app["status"] == ApplicationStatus.APPROVED.value
        ]
        
        # Get all votes for this round
        votes = [vote for vote in self.votes.values() if vote["round_id"] == round_id]
        
        # Simple quadratic funding calculation
        # (This would be replaced with actual matching algorithm in production)
        vote_squares = {}
        for app in applications:
            app_votes = [v for v in votes if v["application_id"] == app["id"]]
            vote_squares[app["id"]] = sum((v["amount"] ** 0.5) for v in app_votes)
        
        total_squares = sum(vote_squares.values())
        if total_squares == 0:
            return {app["id"]: 0 for app in applications}
            
        matching_pool = self.rounds[round_id]["matching_pool"]
        return {
            app_id:
