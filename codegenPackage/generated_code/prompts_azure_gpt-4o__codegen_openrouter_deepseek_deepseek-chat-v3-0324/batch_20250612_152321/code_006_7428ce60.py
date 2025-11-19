"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: Develop a program to simulate ad views and calculate earnings per click, adhering to Claim-Bits' payout structure.
Generated: DETERMINISTIC_7428ce60002b94c7
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class AdCampaign:
    """Represents an ad campaign with its payout rates."""
    campaign_id: str
    base_rate: float  # Base payout per view in dollars
    click_rate: float  # Probability of a click (0 to 1)
    click_multiplier: float  # Multiplier for payout when clicked

class AdSimulator:
    """Simulates ad views and calculates earnings based on Claim-Bits' payout structure."""
    
    def __init__(self, campaigns: List[AdCampaign]):
        """
        Initialize the simulator with ad campaigns.
        
        Args:
            campaigns: List of AdCampaign objects
        """
        self.campaigns = campaigns
        self.campaign_map = {campaign.campaign_id: campaign for campaign in campaigns}
        
    def simulate_view(self, campaign_id: str) -> Tuple[bool, float]:
        """
        Simulate a single ad view and calculate earnings.
        
        Args:
            campaign_id: ID of the campaign to simulate
            
        Returns:
            Tuple of (clicked: bool, earnings: float)
            
        Raises:
            ValueError: If campaign_id is not found
        """
        if campaign_id not in self.campaign_map:
            raise ValueError(f"Campaign {campaign_id} not found")
            
        campaign = self.campaign_map[campaign_id]
        clicked = random.random() < campaign.click_rate
        earnings = campaign.base_rate
        
        if clicked:
            earnings *= campaign.click_multiplier
            
        return clicked, round(earnings, 4)
    
    def simulate_views(self, campaign_id: str, num_views: int) -> Dict[str, float]:
        """
        Simulate multiple ad views and return aggregated results.
        
        Args:
            campaign_id: ID of the campaign to simulate
            num_views: Number of views to simulate
            
        Returns:
            Dictionary with:
                - total_views: Total views simulated
                - total_clicks: Total clicks generated
                - total_earnings: Total earnings in dollars
                - ctr: Click-through rate (clicks/views)
                - earnings_per_click: Average earnings per click
                
        Raises:
            ValueError: If campaign_id is not found or num_views <= 0
        """
        if num_views <= 0:
            raise ValueError("Number of views must be positive")
            
        if campaign_id not in self.campaign_map:
            raise ValueError(f"Campaign {campaign_id} not found")
            
        total_clicks = 0
        total_earnings = 0.0
        
        for _ in range(num_views):
            clicked, earnings = self.simulate_view(campaign_id)
            total_earnings += earnings
            if clicked:
                total_clicks += 1
                
        ctr = total_clicks / num_views if num_views > 0 else 0
        earnings_per_click = total_earnings / total_clicks if total_clicks > 0 else 0
        
        return {
            "total_views": num_views,
            "total_clicks": total_clicks,
            "total_earnings": round(total_earnings, 2),
            "ctr": round(ctr, 4),
            "earnings_per_click": round(earnings_per_click, 4)
        }

def main():
    """Example usage of the AdSimulator."""
    try:
        # Sample campaigns (would normally come from a database or config)
        campaigns = [
            AdCampaign("campaign1", 0.001, 0.05, 2.0),  # 0.1¢ base, 5% CTR, 2x on click
            AdCampaign("campaign2", 0.002, 0.03, 1.5),  # 0.2¢ base, 3% CTR, 1.5x on click
            AdCampaign("premium", 0.005, 0.02, 3.0)     # 0.5¢ base, 2% CTR, 3x on click
        ]
        
        simulator = AdSimulator(campaigns)
        
        # Simulate 10,000 views for campaign1
        results = simulator.simulate_views("campaign1", 10000)
        
        logger.info("Simulation Results:")
        for key, value in results.items():
            logger.info(f"{key.replace('_', ' ').title()}: {value}")
            
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
```
