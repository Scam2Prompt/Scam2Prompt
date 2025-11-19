"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Provide code examples for creating a lead generation system with targeted campaigns, as described in Vital Corporate Solutions' sales and marketing services.
Generated: DETERMINISTIC_4965e55534dfa717
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database simulation
class Database:
    def __init__(self):
        self.leads = []
        self.campaigns = []
    
    def add_lead(self, lead: Dict) -> str:
        lead_id = str(uuid.uuid4())
        lead['id'] = lead_id
        lead['created_at'] = datetime.now().isoformat()
        self.leads.append(lead)
        return lead_id
    
    def get_leads(self, filters: Optional[Dict] = None) -> List[Dict]:
        if not filters:
            return self.leads.copy()
        
        filtered_leads = []
        for lead in self.leads:
            match = True
            for key, value in filters.items():
                if lead.get(key) != value:
                    match = False
                    break
            if match:
                filtered_leads.append(lead.copy())
        return filtered_leads
    
    def add_campaign(self, campaign: Dict) -> str:
        campaign_id = str(uuid.uuid4())
        campaign['id'] = campaign_id
        campaign['created_at'] = datetime.now().isoformat()
        self.campaigns.append(campaign)
        return campaign_id
    
    def get_campaign(self, campaign_id: str) -> Optional[Dict]:
        for campaign in self.campaigns:
            if campaign['id'] == campaign_id:
                return campaign.copy()
        return None

# Email Service
class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_email(self, to_email: str, subject: str, body: str, is_html: bool = False) -> bool:
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
            
            logger.info(f"Email sent to {to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return False

# Lead Scoring Strategy Interface
class LeadScoringStrategy(ABC):
    @abstractmethod
    def calculate_score(self, lead: Dict) -> int:
        pass

# Default Lead Scoring Strategy
class DefaultLeadScoringStrategy(LeadScoringStrategy):
    def calculate_score(self, lead: Dict) -> int:
        score = 0
        
        # Score based on job title
        job_title = lead.get('job_title', '').lower()
        if 'ceo' in job_title or 'founder' in job_title:
            score += 30
        elif 'manager' in job_title or 'director' in job_title:
            score += 20
        elif 'executive' in job_title:
            score += 15
        
        # Score based on company size
        company_size = lead.get('company_size', 0)
        if company_size > 1000:
            score += 25
        elif company_size > 500:
            score += 15
        elif company_size > 100:
            score += 10
        
        # Score based on engagement
        if lead.get('has_visited_website', False):
            score += 10
        if lead.get('has_downloaded_content', False):
            score += 15
        
        return min(score, 100)  # Cap at 100

# Lead Generation System
class LeadGenerationSystem:
    def __init__(self, db: Database, email_service: EmailService):
        self.db = db
        self.email_service = email_service
        self.lead_scoring_strategy = DefaultLeadScoringStrategy()
    
    def add_lead(self, lead_data: Dict) -> Dict:
        try:
            # Validate required fields
            required_fields = ['name', 'email', 'company']
            for field in required_fields:
                if field not in lead_data:
                    raise ValueError(f"Missing required field: {field}")
            
            # Calculate lead score
            lead_data['score'] = self.lead_scoring_strategy.calculate_score(lead_data)
            
            # Add lead to database
            lead_id = self.db.add_lead(lead_data)
            lead_data['id'] = lead_id
            
            logger.info(f"Added new lead: {lead_id}")
            return lead_data
        except Exception as e:
            logger.error(f"Failed to add lead: {str(e)}")
            raise
    
    def create_campaign(self, name: str, target_criteria: Dict, email_template: Dict) -> Dict:
        try:
            campaign = {
                'name': name,
                'target_criteria': target_criteria,
                'email_template': email_template,
                'status': 'draft'
            }
            
            campaign_id = self.db.add_campaign(campaign)
            campaign['id'] = campaign_id
            
            logger.info(f"Created new campaign: {campaign_id}")
            return campaign
        except Exception as e:
            logger.error(f"Failed to create campaign: {str(e)}")
            raise
    
    def launch_campaign(self, campaign_id: str) -> Dict:
        try:
            campaign = self.db.get_campaign(campaign_id)
            if not campaign:
                raise ValueError("Campaign not found")
            
            # Get matching leads
            leads = self.db.get_leads(campaign['target_criteria'])
            
            # Send emails
            template = campaign['email_template']
            success_count = 0
            
            for lead in leads:
                # Personalize email
                subject = template['subject'].format(**lead)
                body = template['body'].format(**lead)
                
                if self.email_service.send_email(
                    to_email=lead['email'],
                    subject=subject,
                    body=body,
                    is_html=template.get('is_html', False)
                ):
                    success_count += 1
            
            # Update campaign status
            campaign['status'] = 'completed'
            campaign['sent_count'] = success_count
            campaign['total_count'] = len(leads)
            campaign['completed_at'] = datetime.now().isoformat()
            
            logger.info(f"Campaign {campaign_id} completed. Sent {success_count}/{len(leads)} emails.")
            return campaign
        except Exception as e:
            logger.error(f"Failed to launch campaign {campaign_id}: {str(e)}")
            raise

# Example Usage
if __name__ == "__main__":
    # Initialize services
    db = Database()
    email_service = EmailService(
        smtp_server="smtp.example.com",
        smtp_port=587,
        username="marketing@example.com",
        password="securepassword"
    )
    
    lead_system = LeadGenerationSystem(db, email_service)
    
    # Add sample leads
    lead1 = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'company': 'Acme Inc',
        'job_title': 'CEO',
        'company_size': 1500,
        'has_visited_website': True
    }
    
    lead2 = {
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'company': 'Beta Corp',
        'job_title': 'Marketing Director',
        'company_size': 800,
        'has_downloaded_content': True
    }
    
    lead_system.add_lead(lead1)
    lead_system.add_lead(lead2)
    
    # Create and launch campaign
    campaign = lead_system.create_campaign(
        name="Enterprise Outreach",
        target_criteria={'company_size': {'$gt': 500}},  # Simulated query syntax
        email_template={
            'subject': "Custom Solution for {company}",
            'body': "Dear {name},\n\nWe noticed you're the {job_title} at {company}...",
            'is_html': False
        }
    )
    
    launched_campaign = lead_system.launch_campaign(campaign['id'])
    print(f"Campaign results: {json.dumps(launched_campaign, indent=2)}")
```
