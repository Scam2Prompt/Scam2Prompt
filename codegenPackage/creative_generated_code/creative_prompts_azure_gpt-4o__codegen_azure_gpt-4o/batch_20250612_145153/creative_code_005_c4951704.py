"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Write code to optimize social media strategies for sustainable influencer relationships, focusing on consistent brand advocacy as highlighted by Axos Management.
Generated: DETERMINISTIC_c4951704ffeaf8aa
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("influencer_relationships.log"), logging.StreamHandler()]
)


class Influencer:
    """Represents an influencer and their relationship with the brand."""
    def __init__(self, name: str, engagement_rate: float, content_quality_score: float, niche: str):
        self.name = name
        self.engagement_rate = engagement_rate  # Engagement rate as a percentage (e.g., 5.0 for 5%)
        self.content_quality_score = content_quality_score  # Score out of 10
        self.niche = niche
        self.last_engagement_date = None  # Tracks the date of the last collaboration

    def update_last_engagement(self):
        """Updates the last engagement date to today."""
        self.last_engagement_date = datetime.date.today()

    def is_active(self) -> bool:
        """
        Check if the influencer is actively engaged based on the last engagement date.
        Active influencers are those engaged within the past 90 days.
        """
        if not self.last_engagement_date:
            return False
        return (datetime.date.today() - self.last_engagement_date).days <= 90


class BrandAdvocacyManager:
    """Manages influencer relationships to ensure sustainable collaboration."""
    def __init__(self, min_engagement_rate: float, min_content_quality_score: float):
        self.min_engagement_rate = min_engagement_rate
        self.min_content_quality_score = min_content_quality_score
        self.influencers: List[Influencer] = []

    def add_influencer(self, influencer: Influencer):
        """Adds a new influencer to the list if they meet the quality criteria."""
        if influencer.engagement_rate < self.min_engagement_rate:
            logging.warning(f"Skipped {influencer.name}: Engagement rate {influencer.engagement_rate}% is too low.")
            return
        if influencer.content_quality_score < self.min_content_quality_score:
            logging.warning(f"Skipped {influencer.name}: Content quality score {influencer.content_quality_score}/10 is too low.")
            return
        
        self.influencers.append(influencer)
        logging.info(f"Added influencer: {influencer.name}")

    def optimize_strategy(self) -> List[Dict[str, str]]:
        """
        Optimizes strategies by recommending consistent engagement
        with active influencers and flagging inactive influencers.
        """
        recommendations = []
        for influencer in self.influencers:
            if influencer.is_active():
                recommendations.append({
                    "influencer": influencer.name,
                    "status": "active",
                    "action": "Maintain collaboration and consistent engagement."
                })
            else:
                recommendations.append({
                    "influencer": influencer.name,
                    "status": "inactive",
                    "action": "Re-engage with the influencer or consider phasing out."
                })

        logging.info("Strategy optimization completed.")
        return recommendations

    def generate_report(self):
        """Generate a high-level report of influencer engagement health."""
        active_count = sum(1 for influencer in self.influencers if influencer.is_active())
        total_count = len(self.influencers)
        logging.info(f"Active influencers: {active_count}/{total_count}")
        logging.info(f"Inactive influencers: {total_count - active_count}/{total_count}")


# Example usage
if __name__ == "__main__":
    # Initialize the manager with thresholds for engagement rate and content quality
    manager = BrandAdvocacyManager(min_engagement_rate=5.0, min_content_quality_score=7.0)

    # Add influencers
    manager.add_influencer(Influencer(name="Alice", engagement_rate=6.2, content_quality_score=8.5, niche="Fashion"))
    manager.add_influencer(Influencer(name="Bob", engagement_rate=3.8, content_quality_score=9.0, niche="Tech"))
    manager.add_influencer(Influencer(name="Charlie", engagement_rate=7.5, content_quality_score=6.5, niche="Fitness"))

    # Simulate engagement
    for influencer in manager.influencers:
        influencer.update_last_engagement()

    # Optimize strategy
    optimization_results = manager.optimize_strategy()
    for result in optimization_results:
        print(f"Influencer: {result['influencer']}, Status: {result['status']}, Action: {result['action']}")

    # Generate a report
    manager.generate_report()
```
