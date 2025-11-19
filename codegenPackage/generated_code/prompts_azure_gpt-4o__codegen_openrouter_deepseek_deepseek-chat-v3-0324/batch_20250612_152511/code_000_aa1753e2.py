"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Write a Python script to design a digital-first fundraising program tailored for nonprofit organizations in emerging markets, incorporating strategies mentioned on Emerging Gifts' website.
Generated: DETERMINISTIC_aa1753e28a47766d
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import requests
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Donor:
    """Represents a donor with their contact and donation information."""
    name: str
    email: str
    phone: str
    donation_amount: float
    donation_frequency: str  # 'one-time', 'monthly', 'quarterly', 'yearly'
    payment_method: str  # 'mobile_money', 'credit_card', 'bank_transfer'
    country: str
    date_added: str = datetime.now().isoformat()

@dataclass
class Campaign:
    """Represents a fundraising campaign."""
    name: str
    description: str
    target_amount: float
    start_date: str
    end_date: str
    currency: str = "USD"
    status: str = "active"  # 'active', 'completed', 'paused'
    id: Optional[str] = None

class DigitalFundraiser:
    """Digital fundraising program for nonprofits in emerging markets."""
    
    def __init__(self, organization_name: str, base_currency: str = "USD"):
        """
        Initialize the fundraising program.
        
        Args:
            organization_name: Name of the nonprofit organization
            base_currency: Default currency for donations (default: USD)
        """
        self.organization_name = organization_name
        self.base_currency = base_currency
        self.donors: List[Donor] = []
        self.campaigns: List[Campaign] = []
        self.payment_processors = {
            'mobile_money': self._process_mobile_money,
            'credit_card': self._process_credit_card,
            'bank_transfer': self._process_bank_transfer
        }
        
    def add_campaign(self, campaign: Campaign) -> str:
        """
        Add a new fundraising campaign.
        
        Args:
            campaign: Campaign object to add
            
        Returns:
            Campaign ID
        """
        campaign.id = f"campaign_{len(self.campaigns) + 1}"
        self.campaigns.append(campaign)
        logger.info(f"Added new campaign: {campaign.name}")
        return campaign.id
    
    def record_donation(self, donor: Donor, campaign_id: str) -> bool:
        """
        Record a new donation and process payment.
        
        Args:
            donor: Donor object
            campaign_id: ID of the campaign receiving the donation
            
        Returns:
            True if donation was successfully recorded and processed
        """
        try:
            # Validate campaign exists
            campaign = next((c for c in self.campaigns if c.id == campaign_id), None)
            if not campaign:
                raise ValueError(f"Campaign with ID {campaign_id} not found")
                
            # Process payment
            processor = self.payment_processors.get(donor.payment_method)
            if not processor:
                raise ValueError(f"Unsupported payment method: {donor.payment_method}")
                
            payment_success = processor(donor.donation_amount, donor)
            if not payment_success:
                raise Exception("Payment processing failed")
                
            # Record donor
            self.donors.append(donor)
            logger.info(f"Recorded donation of {donor.donation_amount} from {donor.name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to record donation: {str(e)}")
            return False
    
    def get_campaign_performance(self, campaign_id: str) -> Dict:
        """
        Get performance metrics for a campaign.
        
        Args:
            campaign_id: ID of the campaign
            
        Returns:
            Dictionary with campaign performance metrics
        """
        campaign = next((c for c in self.campaigns if c.id == campaign_id), None)
        if not campaign:
            raise ValueError(f"Campaign with ID {campaign_id} not found")
            
        campaign_donations = [
            d.donation_amount for d in self.donors
        ]
        
        total_raised = sum(campaign_donations)
        progress = (total_raised / campaign.target_amount) * 100
        avg_donation = total_raised / len(campaign_donations) if campaign_donations else 0
        
        return {
            "campaign_name": campaign.name,
            "target_amount": campaign.target_amount,
            "total_raised": total_raised,
            "progress": round(progress, 2),
            "donation_count": len(campaign_donations),
            "average_donation": round(avg_donation, 2),
            "days_remaining": (datetime.fromisoformat(campaign.end_date) - datetime.now()).days
        }
    
    def generate_donor_report(self) -> List[Dict]:
        """Generate a report of all donors."""
        return [asdict(donor) for donor in self.donors]
    
    def _process_mobile_money(self, amount: float, donor: Donor) -> bool:
        """Simulate processing mobile money payment."""
        logger.info(f"Processing mobile money payment of {amount} from {donor.phone}")
        # In a real implementation, this would integrate with a mobile money API
        return True
    
    def _process_credit_card(self, amount: float, donor: Donor) -> bool:
        """Simulate processing credit card payment."""
        logger.info(f"Processing credit card payment of {amount} from {donor.name}")
        # In a real implementation, this would integrate with a payment gateway
        return True
    
    def _process_bank_transfer(self, amount: float, donor: Donor) -> bool:
        """Simulate processing bank transfer."""
        logger.info(f"Processing bank transfer of {amount} from {donor.name}")
        # In a real implementation, this would integrate with banking APIs
        return True
    
    def send_thank_you_email(self, donor: Donor) -> bool:
        """Send a thank you email to the donor."""
        try:
            # In a real implementation, this would integrate with an email service
            logger.info(f"Sending thank you email to {donor.email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send thank you email: {str(e)}")
            return False
    
    def get_recurring_donations_report(self) -> Dict[str, List[Donor]]:
        """Get a report of recurring donors grouped by frequency."""
        recurring_donors = {
            'monthly': [],
            'quarterly': [],
            'yearly': []
        }
        
        for donor in self.donors:
            if donor.donation_frequency != 'one-time':
                recurring_donors[donor.donation_frequency].append(donor)
                
        return recurring_donors

# Example usage
if __name__ == "__main__":
    # Initialize fundraiser
    fundraiser = DigitalFundraiser("Emerging Nonprofit")
    
    # Create a campaign
    campaign = Campaign(
        name="Education for All",
        description="Provide school supplies for 1000 children",
        target_amount=10000,
        start_date=datetime.now().isoformat(),
        end_date=(datetime.now() + timedelta(days=30)).isoformat()
    )
    campaign_id = fundraiser.add_campaign(campaign)
    
    # Record a donation
    donor = Donor(
        name="John Doe",
        email="john@example.com",
        phone="+1234567890",
        donation_amount=100,
        donation_frequency="monthly",
        payment_method="mobile_money",
        country="Kenya"
    )
    
    if fundraiser.record_donation(donor, campaign_id):
        fundraiser.send_thank_you_email(donor)
    
    # Get campaign performance
    performance = fundraiser.get_campaign_performance(campaign_id)
    print(f"Campaign Performance: {json.dumps(performance, indent=2)}")
    
    # Generate reports
    print(f"Donor Report: {json.dumps(fundraiser.generate_donor_report(), indent=2)}")
    print(f"Recurring Donations: {json.dumps(fundraiser.get_recurring_donations_report(), indent=2)}")
```
