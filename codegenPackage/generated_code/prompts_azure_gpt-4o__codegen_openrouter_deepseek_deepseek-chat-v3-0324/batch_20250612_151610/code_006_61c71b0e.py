"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Provide a step-by-step guide to setting up a content creation pipeline for digital marketing campaigns, inspired by Cara Productions' expertise in boosting Kenya's digital footprint.
Generated: DETERMINISTIC_61c71b0e06565054
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Content Creation Pipeline for Digital Marketing Campaigns
Inspired by Cara Productions' expertise in boosting Kenya's digital footprint.

This script outlines a step-by-step pipeline for creating and managing digital marketing content.
"""

import os
import json
import datetime
from typing import List, Dict, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContentPipeline:
    """
    A class to manage the content creation pipeline for digital marketing campaigns.
    """
    
    def __init__(self, campaign_name: str, target_audience: str, platforms: List[str]):
        """
        Initialize the content pipeline with campaign details.
        
        Args:
            campaign_name: Name of the marketing campaign
            target_audience: Description of target audience
            platforms: List of platforms to publish content on
        """
        self.campaign_name = campaign_name
        self.target_audience = target_audience
        self.platforms = platforms
        self.content_calendar = {}
        self.assets = {}
        
        # Create campaign directory structure
        self.base_dir = Path(f"campaigns/{self.campaign_name}")
        self._setup_directory_structure()
        
    def _setup_directory_structure(self) -> None:
        """Create necessary directories for the campaign."""
        try:
            directories = [
                "briefs",
                "content",
                "assets",
                "approvals",
                "published",
                "analytics"
            ]
            
            for directory in directories:
                path = self.base_dir / directory
                path.mkdir(parents=True, exist_ok=True)
                
            logger.info(f"Directory structure created for campaign: {self.campaign_name}")
        except Exception as e:
            logger.error(f"Error setting up directory structure: {e}")
            raise
            
    def create_campaign_brief(self, objectives: str, key_messages: List[str], 
                            timeline: Dict[str, datetime.date]) -> None:
        """
        Create a campaign brief document.
        
        Args:
            objectives: Campaign objectives
            key_messages: List of key messages to convey
            timeline: Dictionary of key dates (start, end, milestones)
        """
        try:
            brief = {
                "campaign_name": self.campaign_name,
                "target_audience": self.target_audience,
                "platforms": self.platforms,
                "objectives": objectives,
                "key_messages": key_messages,
                "timeline": {k: v.isoformat() for k, v in timeline.items()},
                "created_at": datetime.datetime.now().isoformat()
            }
            
            brief_path = self.base_dir / "briefs" / "campaign_brief.json"
            with open(brief_path, 'w') as f:
                json.dump(brief, f, indent=4)
                
            logger.info(f"Campaign brief created at {brief_path}")
        except Exception as e:
            logger.error(f"Error creating campaign brief: {e}")
            raise
            
    def plan_content_calendar(self, content_plan: List[Dict[str, str]]) -> None:
        """
        Plan and save the content calendar.
        
        Args:
            content_plan: List of content items with details (date, platform, type, topic)
        """
        try:
            for item in content_plan:
                date_key = item['date']
                if date_key not in self.content_calendar:
                    self.content_calendar[date_key] = []
                self.content_calendar[date_key].append(item)
                
            calendar_path = self.base_dir / "content" / "content_calendar.json"
            with open(calendar_path, 'w') as f:
                json.dump(self.content_calendar, f, indent=4)
                
            logger.info(f"Content calendar created with {len(content_plan)} items")
        except Exception as e:
            logger.error(f"Error planning content calendar: {e}")
            raise
            
    def create_content(self, content_type: str, content_data: Dict[str, str], 
                      assets: Optional[List[str]] = None) -> str:
        """
        Create content for the campaign.
        
        Args:
            content_type: Type of content (post, video, infographic, etc.)
            content_data: Dictionary with content details (title, body, etc.)
            assets: List of asset filenames to associate with this content
            
        Returns:
            Path to the created content file
        """
        try:
            content_id = f"{content_type}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            content_path = self.base_dir / "content" / f"{content_id}.json"
            
            content = {
                "content_id": content_id,
                "type": content_type,
                "data": content_data,
                "assets": assets or [],
                "status": "draft",
                "created_at": datetime.datetime.now().isoformat()
            }
            
            with open(content_path, 'w') as f:
                json.dump(content, f, indent=4)
                
            logger.info(f"Content created: {content_id}")
            return str(content_path)
        except Exception as e:
            logger.error(f"Error creating content: {e}")
            raise
            
    def review_content(self, content_path: str, reviewer: str, 
                       feedback: Optional[str] = None) -> bool:
        """
        Review and approve/reject content.
        
        Args:
            content_path: Path to content file
            reviewer: Name of reviewer
            feedback: Optional feedback comments
            
        Returns:
            True if approved, False if rejected
        """
        try:
            with open(content_path, 'r') as f:
                content = json.load(f)
                
            # Simulate review process (in production, this would be more complex)
            approved = True  # In real implementation, this would come from reviewer input
            
            content['review'] = {
                "reviewer": reviewer,
                "feedback": feedback,
                "approved": approved,
                "reviewed_at": datetime.datetime.now().isoformat()
            }
            
            content['status'] = "approved" if approved else "rejected"
            
            with open(content_path, 'w') as f:
                json.dump(content, f, indent=4)
                
            # Move to approvals directory
            if approved:
                approval_path = self.base_dir / "approvals" / Path(content_path).name
                os.rename(content_path, approval_path)
                logger.info(f"Content approved and moved to approvals directory: {approval_path}")
            else:
                logger.info(f"Content rejected: {content_path}")
                
            return approved
        except Exception as e:
            logger.error(f"Error reviewing content: {e}")
            raise
            
    def publish_content(self, content_path: str, publish_date: datetime.datetime) -> None:
        """
        Publish content to specified platforms.
        
        Args:
            content_path: Path to approved content file
            publish_date: Date to publish the content
        """
        try:
            with open(content_path, 'r') as f:
                content = json.load(f)
                
            if content['status'] != "approved":
                raise ValueError("Only approved content can be published")
                
            # Simulate publishing to platforms (in production, would use platform APIs)
            for platform in self.platforms:
                logger.info(f"Publishing {content['content_id']} to {platform} on {publish_date}")
                
            # Update content status
            content['published'] = True
            content['publish_date'] = publish_date.isoformat()
            content['status'] = "published"
            
            with open(content_path, 'w') as f:
                json.dump(content, f, indent=4)
                
            # Move to published directory
            published_path = self.base_dir / "published" / Path(content_path).name
            os.rename(content_path, published_path)
            
            logger.info(f"Content published and moved to published directory: {published_path}")
        except Exception as e:
            logger.error(f"Error publishing content: {e}")
            raise
            
    def track_performance(self, content_id: str, metrics: Dict[str, int]) -> None:
        """
        Track performance metrics for published content.
        
        Args:
            content_id: ID of the content to track
            metrics: Dictionary of performance metrics (views, likes, shares, etc.)
        """
        try:
            analytics_path = self.base_dir / "analytics" / f"{content_id}_metrics.json"
            
            data = {
                "content_id": content_id,
                "metrics": metrics,
                "tracked_at": datetime.datetime.now().isoformat()
            }
            
            with open(analytics_path, 'w') as f:
                json.dump(data, f, indent=4)
                
            logger.info(f"Performance metrics saved for {content_id}")
        except Exception as e:
            logger.error(f"Error tracking performance: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize pipeline
        pipeline = ContentPipeline(
            campaign_name="Kenya_Tourism_2023",
            target_audience="International travelers aged
