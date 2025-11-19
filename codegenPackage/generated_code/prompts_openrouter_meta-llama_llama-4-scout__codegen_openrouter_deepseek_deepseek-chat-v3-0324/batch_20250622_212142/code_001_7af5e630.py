"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Write a Python script to manage a grants program, including tools for measuring program success and maximizing engagement."
Generated: DETERMINISTIC_7af5e630e98ec5cf
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import statistics
import matplotlib.pyplot as plt
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class GrantProgram:
    """
    A class to manage a grants program, including applicant tracking,
    grant distribution, and performance metrics.
    """
    
    def __init__(self, name: str, data_dir: str = "data"):
        """
        Initialize the GrantProgram with a name and data directory.
        
        Args:
            name: Name of the grant program
            data_dir: Directory to store program data (default: "data")
        """
        self.name = name
        self.data_dir = data_dir
        self.applicants_file = os.path.join(data_dir, "applicants.csv")
        self.grants_file = os.path.join(data_dir, "grants.csv")
        self.metrics_file = os.path.join(data_dir, "metrics.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self) -> None:
        """Initialize data files with headers if they don't exist."""
        if not os.path.exists(self.applicants_file):
            with open(self.applicants_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'id', 'name', 'email', 'organization', 
                    'project_title', 'project_description',
                    'requested_amount', 'submission_date', 
                    'status', 'reviewer_notes'
                ])
        
        if not os.path.exists(self.grants_file):
            with open(self.grants_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'grant_id', 'applicant_id', 'amount_awarded',
                    'award_date', 'project_duration', 
                    'success_metrics', 'completion_status'
                ])
        
        if not os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'w') as f:
                json.dump({
                    "total_applicants": 0,
                    "total_grants_awarded": 0,
                    "total_funds_distributed": 0,
                    "success_rate": 0,
                    "engagement_metrics": {}
                }, f)
    
    def add_applicant(
        self,
        name: str,
        email: str,
        organization: str,
        project_title: str,
        project_description: str,
        requested_amount: float
    ) -> str:
        """
        Add a new applicant to the program.
        
        Args:
            name: Applicant name
            email: Contact email
            organization: Organization name
            project_title: Title of proposed project
            project_description: Description of project
            requested_amount: Amount requested
            
        Returns:
            Applicant ID
        """
        applicant_id = f"APP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        submission_date = datetime.now().strftime('%Y-%m-%d')
        
        with open(self.applicants_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                applicant_id, name, email, organization,
                project_title, project_description,
                requested_amount, submission_date,
                'pending', ''
            ])
        
        self._update_metrics()
        return applicant_id
    
    def review_application(
        self,
        applicant_id: str,
        status: str,
        reviewer_notes: str,
        amount_awarded: Optional[float] = None
    ) -> bool:
        """
        Review an application and optionally award a grant.
        
        Args:
            applicant_id: ID of applicant to review
            status: New status ('approved', 'rejected', 'pending')
            reviewer_notes: Notes from reviewer
            amount_awarded: Amount to award if approved (optional)
            
        Returns:
            True if operation succeeded, False otherwise
        """
        applicants = []
        updated = False
        
        with open(self.applicants_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] == applicant_id:
                    row['status'] = status
                    row['reviewer_notes'] = reviewer_notes
                    updated = True
                applicants.append(row)
        
        if not updated:
            return False
        
        with open(self.applicants_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=applicants[0].keys())
            writer.writeheader()
            writer.writerows(applicants)
        
        if status == 'approved' and amount_awarded:
            self.award_grant(applicant_id, amount_awarded)
        
        self._update_metrics()
        return True
    
    def award_grant(
        self,
        applicant_id: str,
        amount_awarded: float,
        project_duration: str = "12 months"
    ) -> str:
        """
        Award a grant to an approved applicant.
        
        Args:
            applicant_id: ID of approved applicant
            amount_awarded: Amount being awarded
            project_duration: Duration of project (default: "12 months")
            
        Returns:
            Grant ID
        """
        grant_id = f"GRANT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        award_date = datetime.now().strftime('%Y-%m-%d')
        
        with open(self.grants_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                grant_id, applicant_id, amount_awarded,
                award_date, project_duration, '', 'in_progress'
            ])
        
        self._update_metrics()
        return grant_id
    
    def update_grant_status(
        self,
        grant_id: str,
        completion_status: str,
        success_metrics: Dict[str, float]
    ) -> bool:
        """
        Update the status and metrics of a granted project.
        
        Args:
            grant_id: ID of grant to update
            completion_status: New status ('completed', 'in_progress', 'terminated')
            success_metrics: Dictionary of success metrics
            
        Returns:
            True if operation succeeded, False otherwise
        """
        grants = []
        updated = False
        
        with open(self.grants_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['grant_id'] == grant_id:
                    row['completion_status'] = completion_status
                    row['success_metrics'] = json.dumps(success_metrics)
                    updated = True
                grants.append(row)
        
        if not updated:
            return False
        
        with open(self.grants_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=grants[0].keys())
            writer.writeheader()
            writer.writerows(grants)
        
        self._update_metrics()
        return True
    
    def _update_metrics(self) -> None:
        """Update program metrics based on current data."""
        # Calculate basic metrics
        with open(self.applicants_file, 'r') as f:
            reader = csv.DictReader(f)
            applicants = list(reader)
        
        with open(self.grants_file, 'r') as f:
            reader = csv.DictReader(f)
            grants = list(reader)
        
        total_applicants = len(applicants)
        total_grants_awarded = len(grants)
        total_funds_distributed = sum(float(g['amount_awarded']) for g in grants)
        
        success_rate = 0
        if total_applicants > 0:
            success_rate = total_grants_awarded / total_applicants
        
        # Calculate engagement metrics
        engagement_metrics = {
            "application_response_rate": self._calculate_response_rate(),
            "average_review_time": self._calculate_average_review_time(),
            "grantee_satisfaction": self._calculate_grantee_satisfaction()
        }
        
        # Save metrics
        metrics = {
            "total_applicants": total_applicants,
            "total_grants_awarded": total_grants_awarded,
            "total_funds_distributed": total_funds_distributed,
            "success_rate": success_rate,
            "engagement_metrics": engagement_metrics
        }
        
        with open(self.metrics_file, 'w') as f:
            json.dump(metrics, f, indent=2)
    
    def _calculate_response_rate(self) -> float:
        """Calculate the response rate to applicant communications."""
        # This is a simplified version - in production you might track actual communications
        with open(self.applicants_file, 'r') as f:
            reader = csv.DictReader(f)
            applicants = list(reader)
        
        responded = sum(1 for a in applicants
