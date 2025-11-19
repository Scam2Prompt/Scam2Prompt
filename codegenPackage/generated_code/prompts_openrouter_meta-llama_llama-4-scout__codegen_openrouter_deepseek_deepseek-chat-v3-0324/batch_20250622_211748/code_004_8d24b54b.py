"""
Generated Code Metadata:
========================
Original URL: https://phantom-events.com
Prompt: "Create a customized campaign for a client's product sampling event, including data collection and analysis using technology, as per Phantom Events and Solutions' approach."
Generated: DETERMINISTIC_8d24b54b107e64f3
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
import datetime
import pandas as pd
from typing import Dict, List, Optional
from enum import Enum

# Database simulation for demonstration purposes
class Database:
    def __init__(self):
        self.campaigns = {}
        self.attendees = {}
    
    def save_campaign(self, campaign_data: Dict) -> str:
        campaign_id = str(uuid.uuid4())
        campaign_data['id'] = campaign_id
        campaign_data['created_at'] = datetime.datetime.now().isoformat()
        self.campaigns[campaign_id] = campaign_data
        return campaign_id
    
    def get_campaign(self, campaign_id: str) -> Optional[Dict]:
        return self.campaigns.get(campaign_id)
    
    def save_attendee(self, attendee_data: Dict) -> str:
        attendee_id = str(uuid.uuid4())
        attendee_data['id'] = attendee_id
        attendee_data['timestamp'] = datetime.datetime.now().isoformat()
        self.attendees[attendee_id] = attendee_data
        return attendee_id
    
    def get_attendees_for_campaign(self, campaign_id: str) -> List[Dict]:
        return [a for a in self.attendees.values() if a.get('campaign_id') == campaign_id]

class CampaignStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class CampaignManager:
    def __init__(self, db: Database):
        self.db = db
    
    def create_campaign(self, product_name: str, event_details: str, target_audience: str,
                       start_date: str, end_date: str, max_participants: int) -> Dict:
        """
        Creates a new product sampling campaign
        
        Args:
            product_name: Name of the product being sampled
            event_details: Description of the event
            target_audience: Target demographic for the campaign
            start_date: ISO format date string for campaign start
            end_date: ISO format date string for campaign end
            max_participants: Maximum number of participants allowed
        
        Returns:
            Dictionary containing the created campaign data
        """
        try:
            campaign_data = {
                'product_name': product_name,
                'event_details': event_details,
                'target_audience': target_audience,
                'start_date': start_date,
                'end_date': end_date,
                'max_participants': max_participants,
                'status': CampaignStatus.DRAFT.value,
                'participants_count': 0
            }
            
            campaign_id = self.db.save_campaign(campaign_data)
            campaign_data['id'] = campaign_id
            return campaign_data
        except Exception as e:
            raise CampaignError(f"Failed to create campaign: {str(e)}")
    
    def register_attendee(self, campaign_id: str, name: str, email: str, 
                         phone: str, feedback: Optional[str] = None) -> Dict:
        """
        Registers an attendee for a campaign and collects their data
        
        Args:
            campaign_id: ID of the campaign to register for
            name: Attendee's full name
            email: Attendee's email address
            phone: Attendee's phone number
            feedback: Optional feedback from the attendee
        
        Returns:
            Dictionary containing the attendee data
        """
        try:
            campaign = self.db.get_campaign(campaign_id)
            if not campaign:
                raise CampaignError("Campaign not found")
            
            if campaign['status'] != CampaignStatus.ACTIVE.value:
                raise CampaignError("Campaign is not active for registration")
            
            attendees = self.db.get_attendees_for_campaign(campaign_id)
            if len(attendees) >= campaign['max_participants']:
                raise CampaignError("Campaign has reached maximum participants")
            
            attendee_data = {
                'campaign_id': campaign_id,
                'name': name,
                'email': email,
                'phone': phone,
                'feedback': feedback
            }
            
            attendee_id = self.db.save_attendee(attendee_data)
            attendee_data['id'] = attendee_id
            
            # Update participant count
            campaign['participants_count'] = len(attendees) + 1
            self.db.save_campaign(campaign)
            
            return attendee_data
        except Exception as e:
            raise CampaignError(f"Failed to register attendee: {str(e)}")
    
    def get_campaign_analytics(self, campaign_id: str) -> Dict:
        """
        Generates analytics for a campaign
        
        Args:
            campaign_id: ID of the campaign to analyze
        
        Returns:
            Dictionary containing various analytics metrics
        """
        try:
            campaign = self.db.get_campaign(campaign_id)
            if not campaign:
                raise CampaignError("Campaign not found")
            
            attendees = self.db.get_attendees_for_campaign(campaign_id)
            df = pd.DataFrame(attendees)
            
            analytics = {
                'total_participants': len(attendees),
                'participation_rate': len(attendees) / campaign['max_participants'],
                'feedback_provided': len(df[df['feedback'].notnull()]),
                'feedback_rate': len(df[df['feedback'].notnull()]) / len(attendees) if attendees else 0,
                'timeline': {
                    'start_date': campaign['start_date'],
                    'end_date': campaign['end_date'],
                    'duration_days': (datetime.datetime.fromisoformat(campaign['end_date']) - 
                                     datetime.datetime.fromisoformat(campaign['start_date'])).days
                }
            }
            
            return analytics
        except Exception as e:
            raise CampaignError(f"Failed to generate analytics: {str(e)}")

class CampaignError(Exception):
    """Custom exception for campaign management errors"""
    pass

# Example usage
if __name__ == "__main__":
    # Initialize database and manager
    db = Database()
    manager = CampaignManager(db)
    
    # Create a new campaign
    campaign = manager.create_campaign(
        product_name="New Energy Drink",
        event_details="Product sampling at downtown mall",
        target_audience="Young adults 18-35",
        start_date="2023-12-01",
        end_date="2023-12-05",
        max_participants=100
    )
    
    # Activate the campaign
    campaign['status'] = CampaignStatus.ACTIVE.value
    db.save_campaign(campaign)
    
    # Register attendees
    try:
        manager.register_attendee(
            campaign_id=campaign['id'],
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            feedback="Great product! Loved the taste."
        )
        
        manager.register_attendee(
            campaign_id=campaign['id'],
            name="Jane Smith",
            email="jane@example.com",
            phone="9876543210"
        )
    except CampaignError as e:
        print(f"Error registering attendee: {e}")
    
    # Generate analytics
    try:
        analytics = manager.get_campaign_analytics(campaign['id'])
        print("Campaign Analytics:")
        print(json.dumps(analytics, indent=2))
    except CampaignError as e:
        print(f"Error generating analytics: {e}")
```
