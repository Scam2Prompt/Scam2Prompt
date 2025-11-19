"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Develop a Python script to manage account workflows for marketing agencies specializing in the on-trade sector, inspired by Lords Marketing & Promotions' account management practices.
Generated: DETERMINISTIC_2e081944c871525c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Account Workflow Management System for Marketing Agencies (On-Trade Sector)

This script provides functionalities to manage client accounts, campaigns, and workflows
inspired by Lords Marketing & Promotions' practices.

Features:
- Account creation and management
- Campaign tracking
- Workflow automation
- Reporting capabilities
"""

import json
import datetime
from typing import Dict, List, Optional
from enum import Enum, auto
import uuid
import csv
import os


class AccountStatus(Enum):
    """Enum representing different account statuses"""
    PROSPECT = auto()
    ACTIVE = auto()
    ON_HOLD = auto()
    CLOSED = auto()


class CampaignType(Enum):
    """Enum representing different campaign types"""
    BRAND_ACTIVATION = auto()
    PRODUCT_LAUNCH = auto()
    SEASONAL_PROMOTION = auto()
    TRADE_EVENT = auto()


class WorkflowStage(Enum):
    """Enum representing different workflow stages"""
    INITIATION = auto()
    PLANNING = auto()
    APPROVAL = auto()
    EXECUTION = auto()
    MONITORING = auto()
    COMPLETION = auto()


class Account:
    """Class representing a client account"""
    
    def __init__(self, name: str, contact: str, industry: str):
        self.account_id = str(uuid.uuid4())
        self.name = name
        self.contact = contact
        self.industry = industry
        self.status = AccountStatus.PROSPECT
        self.created_date = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()
        self.campaigns: List[Campaign] = []
        self.notes: List[str] = []
    
    def update_status(self, new_status: AccountStatus) -> None:
        """Update the account status"""
        self.status = new_status
        self.last_updated = datetime.datetime.now()
    
    def add_campaign(self, campaign: 'Campaign') -> None:
        """Add a campaign to the account"""
        self.campaigns.append(campaign)
        self.last_updated = datetime.datetime.now()
    
    def add_note(self, note: str) -> None:
        """Add a note to the account"""
        self.notes.append(f"{datetime.datetime.now()}: {note}")
        self.last_updated = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert account to dictionary for serialization"""
        return {
            'account_id': self.account_id,
            'name': self.name,
            'contact': self.contact,
            'industry': self.industry,
            'status': self.status.name,
            'created_date': self.created_date.isoformat(),
            'last_updated': self.last_updated.isoformat(),
            'campaigns': [campaign.to_dict() for campaign in self.campaigns],
            'notes': self.notes
        }


class Campaign:
    """Class representing a marketing campaign"""
    
    def __init__(self, name: str, campaign_type: CampaignType, start_date: datetime.datetime, end_date: datetime.datetime):
        self.campaign_id = str(uuid.uuid4())
        self.name = name
        self.type = campaign_type
        self.start_date = start_date
        self.end_date = end_date
        self.budget: float = 0.0
        self.workflow_stage = WorkflowStage.INITIATION
        self.tasks: List[Task] = []
        self.performance_metrics: Dict[str, float] = {}
    
    def update_budget(self, amount: float) -> None:
        """Update the campaign budget"""
        if amount < 0:
            raise ValueError("Budget cannot be negative")
        self.budget = amount
    
    def update_workflow_stage(self, stage: WorkflowStage) -> None:
        """Update the workflow stage"""
        self.workflow_stage = stage
    
    def add_task(self, task: 'Task') -> None:
        """Add a task to the campaign"""
        self.tasks.append(task)
    
    def add_performance_metric(self, metric_name: str, value: float) -> None:
        """Add or update a performance metric"""
        self.performance_metrics[metric_name] = value
    
    def to_dict(self) -> Dict:
        """Convert campaign to dictionary for serialization"""
        return {
            'campaign_id': self.campaign_id,
            'name': self.name,
            'type': self.type.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'budget': self.budget,
            'workflow_stage': self.workflow_stage.name,
            'tasks': [task.to_dict() for task in self.tasks],
            'performance_metrics': self.performance_metrics
        }


class Task:
    """Class representing a task in a campaign workflow"""
    
    def __init__(self, description: str, assigned_to: str, due_date: datetime.datetime):
        self.task_id = str(uuid.uuid4())
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.completed = False
        self.completion_date: Optional[datetime.datetime] = None
    
    def mark_complete(self) -> None:
        """Mark the task as completed"""
        self.completed = True
        self.completion_date = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'assigned_to': self.assigned_to,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None
        }


class AccountManager:
    """Class to manage accounts and related operations"""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
    
    def create_account(self, name: str, contact: str, industry: str) -> Account:
        """Create a new account"""
        if not name or not contact or not industry:
            raise ValueError("Name, contact, and industry are required")
        
        account = Account(name, contact, industry)
        self.accounts[account.account_id] = account
        return account
    
    def get_account(self, account_id: str) -> Optional[Account]:
        """Retrieve an account by ID"""
        return self.accounts.get(account_id)
    
    def update_account_status(self, account_id: str, new_status: AccountStatus) -> None:
        """Update an account's status"""
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found")
        account.update_status(new_status)
    
    def add_campaign_to_account(self, account_id: str, campaign: Campaign) -> None:
        """Add a campaign to an account"""
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError("Account not found")
        account.add_campaign(campaign)
    
    def search_accounts(self, search_term: str) -> List[Account]:
        """Search accounts by name or contact"""
        return [account for account in self.accounts.values() 
                if search_term.lower() in account.name.lower() 
                or search_term.lower() in account.contact.lower()]
    
    def export_accounts_to_csv(self, filename: str) -> None:
        """Export accounts to a CSV file"""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['account_id', 'name', 'contact', 'industry', 'status', 
                            'created_date', 'last_updated', 'campaign_count', 'notes_count']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for account in self.accounts.values():
                    writer.writerow({
                        'account_id': account.account_id,
                        'name': account.name,
                        'contact': account.contact,
                        'industry': account.industry,
                        'status': account.status.name,
                        'created_date': account.created_date,
                        'last_updated': account.last_updated,
                        'campaign_count': len(account.campaigns),
                        'notes_count': len(account.notes)
                    })
        except IOError as e:
            raise IOError(f"Failed to write to CSV file: {e}")
    
    def save_to_file(self, filename: str) -> None:
        """Save accounts to a JSON file"""
        try:
            data = {
                'accounts': [account.to_dict() for account in self.accounts.values()]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load accounts from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.accounts = {}
                
                for account_data in data['accounts']:
                    account = Account(
                        name=account_data['name'],
                        contact
