"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Generate code for tracking and managing offshore marketing campaigns, ensuring alignment with Connext's offshore marketing specialist services.
Generated: DETERMINISTIC_c637ada96f9be8e1
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CampaignStatus(Enum):
    """Enum for campaign status options"""
    DRAFT = "Draft"
    ACTIVE = "Active"
    PAUSED = "Paused"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class CampaignChannel(Enum):
    """Enum for marketing channels"""
    SEO = "SEO"
    PPC = "PPC"
    SOCIAL_MEDIA = "Social Media"
    EMAIL = "Email"
    CONTENT_MARKETING = "Content Marketing"
    AFFILIATE = "Affiliate"

class CampaignTargetRegion(Enum):
    """Enum for target regions"""
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    ASIA = "Asia"
    LATIN_AMERICA = "Latin America"
    MIDDLE_EAST = "Middle East"
    AFRICA = "Africa"

class CampaignBudget(BaseModel):
    """Model for campaign budget details"""
    total_budget: float
    spent: float = 0.0
    currency: str = "USD"

    @validator('total_budget')
    def validate_budget(cls, v):
        if v <= 0:
            raise ValueError("Budget must be positive")
        return v

class CampaignPerformanceMetrics(BaseModel):
    """Model for tracking campaign performance"""
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    ctr: float = 0.0  # Click-through rate
    conversion_rate: float = 0.0
    roas: float = 0.0  # Return on ad spend

class OffshoreMarketingCampaign(BaseModel):
    """Main model for offshore marketing campaign"""
    campaign_id: str
    name: str
    description: Optional[str] = None
    start_date: datetime.date
    end_date: datetime.date
    status: CampaignStatus = CampaignStatus.DRAFT
    channels: List[CampaignChannel]
    target_regions: List[CampaignTargetRegion]
    budget: CampaignBudget
    performance: CampaignPerformanceMetrics = CampaignPerformanceMetrics()
    created_at: datetime.datetime = datetime.datetime.now()
    last_updated: datetime.datetime = datetime.datetime.now()

    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class CampaignManager:
    """Class for managing offshore marketing campaigns"""
    
    def __init__(self):
        self.campaigns: Dict[str, OffshoreMarketingCampaign] = {}
    
    def create_campaign(self, campaign: OffshoreMarketingCampaign) -> OffshoreMarketingCampaign:
        """Create a new campaign"""
        if campaign.campaign_id in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign.campaign_id} already exists")
        
        self.campaigns[campaign.campaign_id] = campaign
        logger.info(f"Created new campaign: {campaign.name} (ID: {campaign.campaign_id})")
        return campaign
    
    def get_campaign(self, campaign_id: str) -> Optional[OffshoreMarketingCampaign]:
        """Retrieve a campaign by ID"""
        return self.campaigns.get(campaign_id)
    
    def update_campaign(self, campaign_id: str, update_data: dict) -> OffshoreMarketingCampaign:
        """Update an existing campaign"""
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        updated_campaign = campaign.copy(update=update_data)
        updated_campaign.last_updated = datetime.datetime.now()
        
        self.campaigns[campaign_id] = updated_campaign
        logger.info(f"Updated campaign: {campaign_id}")
        return updated_campaign
    
    def update_campaign_status(self, campaign_id: str, new_status: CampaignStatus) -> OffshoreMarketingCampaign:
        """Update campaign status"""
        return self.update_campaign(campaign_id, {"status": new_status})
    
    def record_campaign_performance(self, campaign_id: str, metrics: dict) -> OffshoreMarketingCampaign:
        """Record performance metrics for a campaign"""
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        
        # Calculate derived metrics
        if 'impressions' in metrics and 'clicks' in metrics:
            metrics['ctr'] = (metrics['clicks'] / metrics['impressions']) * 100 if metrics['impressions'] > 0 else 0
        
        if 'clicks' in metrics and 'conversions' in metrics:
            metrics['conversion_rate'] = (metrics['conversions'] / metrics['clicks']) * 100 if metrics['clicks'] > 0 else 0
        
        if 'conversions' in metrics and campaign.budget.spent > 0:
            # Assuming average conversion value is 1 for ROAS calculation
            metrics['roas'] = (metrics['conversions'] / campaign.budget.spent) * 100
        
        return self.update_campaign(campaign_id, {"performance": metrics})
    
    def list_campaigns(self, status: Optional[CampaignStatus] = None) -> List[OffshoreMarketingCampaign]:
        """List all campaigns, optionally filtered by status"""
        if status:
            return [campaign for campaign in self.campaigns.values() if campaign.status == status]
        return list(self.campaigns.values())
    
    def delete_campaign(self, campaign_id: str) -> None:
        """Delete a campaign"""
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
        
        del self.campaigns[campaign_id]
        logger.info(f"Deleted campaign: {campaign_id}")

# Example usage
if __name__ == "__main__":
    manager = CampaignManager()
    
    # Create a new campaign
    new_campaign = OffshoreMarketingCampaign(
        campaign_id="campaign-001",
        name="Global Expansion Q3",
        description="SEO and PPC campaign for European and Asian markets",
        start_date=datetime.date(2023, 7, 1),
        end_date=datetime.date(2023, 9, 30),
        channels=[CampaignChannel.SEO, CampaignChannel.PPC],
        target_regions=[CampaignTargetRegion.EUROPE, CampaignTargetRegion.ASIA],
        budget=CampaignBudget(total_budget=50000.0)
    )
    
    created_campaign = manager.create_campaign(new_campaign)
    
    # Update campaign status
    active_campaign = manager.update_campaign_status("campaign-001", CampaignStatus.ACTIVE)
    
    # Record performance
    performance_update = {
        "impressions": 100000,
        "clicks": 5000,
        "conversions": 250,
        "spent": 12500.0
    }
    updated_campaign = manager.record_campaign_performance("campaign-001", performance_update)
    
    # List active campaigns
    active_campaigns = manager.list_campaigns(CampaignStatus.ACTIVE)
    print(f"Active campaigns: {[camp.name for camp in active_campaigns]}")
```
