"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Illustrate how to implement a sales and marketing synchrony model in a web application, referencing the strategies provided by 3rd & Taylor for bridging sales and marketing gaps.
Generated: DETERMINISTIC_519db719e541352e
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Sales and Marketing Synchrony Model Implementation

```python
import json
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
import logging
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LeadStatus(Enum):
    """Enum representing different lead statuses in the funnel"""
    NEW = "new"
    MARKETING_QUALIFIED = "marketing_qualified"
    SALES_ACCEPTED = "sales_accepted"
    SALES_QUALIFIED = "sales_qualified"
    CONVERTED = "converted"
    UNQUALIFIED = "unqualified"

@dataclass
class Lead:
    """Data class representing a sales lead"""
    id: str
    name: str
    email: str
    company: str
    status: LeadStatus
    marketing_score: int
    sales_score: int
    last_contacted: Optional[datetime] = None
    notes: Optional[str] = None

@dataclass
class Campaign:
    """Data class representing a marketing campaign"""
    id: str
    name: str
    start_date: datetime
    end_date: datetime
    target_audience: str
    budget: float
    leads_generated: List[str] = None

class SalesMarketingSyncModel:
    """
    Implementation of the sales and marketing synchrony model based on 3rd & Taylor strategies.
    This class bridges the gap between sales and marketing teams by:
    - Shared lead scoring
    - Unified communication tracking
    - Aligned KPIs and reporting
    - Closed-loop feedback
    """
    
    def __init__(self):
        self.leads: Dict[str, Lead] = {}
        self.campaigns: Dict[str, Campaign] = {}
        self.shared_score_threshold = 50  # Threshold for MQL qualification
        
    def add_lead(self, lead: Lead) -> None:
        """Add a new lead to the system"""
        if lead.id in self.leads:
            raise ValueError(f"Lead with ID {lead.id} already exists")
        self.leads[lead.id] = lead
        logger.info(f"Added new lead: {lead.email}")
        
    def update_lead_status(self, lead_id: str, new_status: LeadStatus) -> None:
        """Update a lead's status with validation"""
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
        
        current_status = self.leads[lead_id].status
        valid_transitions = {
            LeadStatus.NEW: [LeadStatus.MARKETING_QUALIFIED, LeadStatus.UNQUALIFIED],
            LeadStatus.MARKETING_QUALIFIED: [LeadStatus.SALES_ACCEPTED, LeadStatus.UNQUALIFIED],
            LeadStatus.SALES_ACCEPTED: [LeadStatus.SALES_QUALIFIED, LeadStatus.UNQUALIFIED],
            LeadStatus.SALES_QUALIFIED: [LeadStatus.CONVERTED, LeadStatus.UNQUALIFIED],
        }
        
        if new_status not in valid_transitions.get(current_status, []):
            raise ValueError(
                f"Invalid status transition from {current_status} to {new_status}"
            )
            
        self.leads[lead_id].status = new_status
        logger.info(f"Updated lead {lead_id} status to {new_status}")
        
    def add_campaign(self, campaign: Campaign) -> None:
        """Add a new marketing campaign"""
        if campaign.id in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign.id} already exists")
        if campaign.leads_generated is None:
            campaign.leads_generated = []
        self.campaigns[campaign.id] = campaign
        logger.info(f"Added new campaign: {campaign.name}")
        
    def associate_lead_to_campaign(self, lead_id: str, campaign_id: str) -> None:
        """Associate a lead with a marketing campaign"""
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
            
        if lead_id not in self.campaigns[campaign_id].leads_generated:
            self.campaigns[campaign_id].leads_generated.append(lead_id)
            logger.info(f"Associated lead {lead_id} with campaign {campaign_id}")
            
    def calculate_combined_score(self, lead_id: str) -> int:
        """Calculate combined marketing and sales score for a lead"""
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
            
        lead = self.leads[lead_id]
        return lead.marketing_score + lead.sales_score
        
    def qualify_marketing_leads(self) -> List[str]:
        """
        Automatically qualify leads that meet the shared scoring threshold.
        Returns list of IDs for newly qualified leads.
        """
        newly_qualified = []
        
        for lead_id, lead in self.leads.items():
            if lead.status == LeadStatus.NEW:
                combined_score = self.calculate_combined_score(lead_id)
                if combined_score >= self.shared_score_threshold:
                    self.update_lead_status(lead_id, LeadStatus.MARKETING_QUALIFIED)
                    newly_qualified.append(lead_id)
                    
        logger.info(f"Qualified {len(newly_qualified)} new MQLs")
        return newly_qualified
        
    def get_campaign_performance(self, campaign_id: str) -> Dict:
        """
        Generate performance metrics for a campaign including:
        - Total leads generated
        - MQL conversion rate
        - SQL conversion rate
        - Customer conversion rate
        """
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
            
        campaign = self.campaigns[campaign_id]
        leads = [self.leads[lead_id] for lead_id in campaign.leads_generated]
        
        total_leads = len(leads)
        mql_count = sum(1 for lead in leads if lead.status.value >= LeadStatus.MARKETING_QUALIFIED.value)
        sql_count = sum(1 for lead in leads if lead.status.value >= LeadStatus.SALES_QUALIFIED.value)
        converted_count = sum(1 for lead in leads if lead.status == LeadStatus.CONVERTED)
        
        return {
            "campaign_id": campaign_id,
            "campaign_name": campaign.name,
            "total_leads": total_leads,
            "mql_conversion_rate": mql_count / total_leads if total_leads > 0 else 0,
            "sql_conversion_rate": sql_count / total_leads if total_leads > 0 else 0,
            "customer_conversion_rate": converted_count / total_leads if total_leads > 0 else 0,
            "roi": (converted_count * 1000 - campaign.budget) / campaign.budget  # Simplified ROI calculation
        }
        
    def get_sales_feedback(self, lead_id: str, feedback: str, score_adjustment: int) -> None:
        """
        Record sales feedback for a lead and adjust scores accordingly.
        Implements closed-loop feedback between sales and marketing.
        """
        if lead_id not in self.leads:
            raise ValueError(f"Lead with ID {lead_id} not found")
            
        lead = self.leads[lead_id]
        lead.notes = feedback
        lead.sales_score += score_adjustment
        
        # If negative feedback, potentially disqualify the lead
        if score_adjustment < -20 and lead.status != LeadStatus.UNQUALIFIED:
            self.update_lead_status(lead_id, LeadStatus.UNQUALIFIED)
            
        logger.info(f"Recorded sales feedback for lead {lead_id}")
        
    def export_lead_data(self, file_path: str) -> None:
        """Export all lead data to a JSON file"""
        data = {
            "leads": [asdict(lead) for lead in self.leads.values()],
            "campaigns": [asdict(campaign) for campaign in self.campaigns.values()],
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            logger.info(f"Successfully exported data to {file_path}")
        except IOError as e:
            logger.error(f"Failed to export data: {str(e)}")
            raise
            
    def import_lead_data(self, file_path: str) -> None:
        """Import lead data from a JSON file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            # Clear current data
            self.leads = {}
            self.campaigns = {}
            
            # Import leads
            for lead_data in data.get("leads", []):
