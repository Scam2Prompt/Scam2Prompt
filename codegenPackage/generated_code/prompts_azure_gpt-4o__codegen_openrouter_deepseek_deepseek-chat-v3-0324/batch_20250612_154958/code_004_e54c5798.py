"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Provide code examples for scoring leads in a database and triggering automated nurturing actions, similar to the strategies mentioned by Gisela Bravo.
Generated: DETERMINISTIC_e54c5798fbc7d3b3
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LeadScorer:
    """
    Scores leads based on various engagement factors and demographic data.
    """
    
    def __init__(self, engagement_weights: Dict[str, float], demographic_weights: Dict[str, float]):
        """
        Initialize with scoring weights for different factors.
        
        Args:
            engagement_weights: Dictionary of engagement factors and their weights
            demographic_weights: Dictionary of demographic factors and their weights
        """
        self.engagement_weights = engagement_weights
        self.demographic_weights = demographic_weights
        
    def calculate_engagement_score(self, lead_data: Dict[str, float]) -> float:
        """
        Calculate engagement score based on lead's activities.
        
        Args:
            lead_data: Dictionary containing engagement metrics
            
        Returns:
            Calculated engagement score
        """
        try:
            score = 0.0
            for factor, weight in self.engagement_weights.items():
                if factor in lead_data:
                    score += lead_data[factor] * weight
            return score
        except Exception as e:
            logger.error(f"Error calculating engagement score: {e}")
            raise
        
    def calculate_demographic_score(self, lead_data: Dict[str, float]) -> float:
        """
        Calculate demographic score based on lead's profile.
        
        Args:
            lead_data: Dictionary containing demographic metrics
            
        Returns:
            Calculated demographic score
        """
        try:
            score = 0.0
            for factor, weight in self.demographic_weights.items():
                if factor in lead_data:
                    score += lead_data[factor] * weight
            return score
        except Exception as e:
            logger.error(f"Error calculating demographic score: {e}")
            raise
        
    def calculate_total_score(self, lead_data: Dict[str, float]) -> float:
        """
        Calculate total lead score by combining engagement and demographic scores.
        
        Args:
            lead_data: Dictionary containing all lead metrics
            
        Returns:
            Calculated total score
        """
        try:
            engagement_score = self.calculate_engagement_score(lead_data)
            demographic_score = self.calculate_demographic_score(lead_data)
            return engagement_score + demographic_score
        except Exception as e:
            logger.error(f"Error calculating total score: {e}")
            raise

class ActionTrigger(ABC):
    """
    Abstract base class for lead nurturing actions.
    """
    
    @abstractmethod
    def trigger(self, lead_id: str, score: float) -> bool:
        """
        Trigger the nurturing action for a lead.
        
        Args:
            lead_id: Unique identifier for the lead
            score: Lead's current score
            
        Returns:
            True if action was successfully triggered
        """
        pass

class EmailAction(ActionTrigger):
    """
    Trigger email nurturing actions based on lead score.
    """
    
    def __init__(self, email_service):
        self.email_service = email_service
        
    def trigger(self, lead_id: str, score: float) -> bool:
        try:
            if score >= 75:
                self.email_service.send(lead_id, "premium_offer")
            elif score >= 50:
                self.email_service.send(lead_id, "educational_content")
            elif score >= 25:
                self.email_service.send(lead_id, "intro_series")
            return True
        except Exception as e:
            logger.error(f"Error triggering email action for lead {lead_id}: {e}")
            return False

class TaskCreationAction(ActionTrigger):
    """
    Trigger task creation for sales team based on lead score.
    """
    
    def __init__(self, task_service):
        self.task_service = task_service
        
    def trigger(self, lead_id: str, score: float) -> bool:
        try:
            if score >= 80:
                self.task_service.create(lead_id, "Immediate follow-up", priority="high")
            elif score >= 60:
                self.task_service.create(lead_id, "Schedule call", priority="medium")
            return True
        except Exception as e:
            logger.error(f"Error triggering task creation for lead {lead_id}: {e}")
            return False

class LeadNurturingSystem:
    """
    Main system for scoring leads and triggering nurturing actions.
    """
    
    def __init__(self, lead_scorer: LeadScorer, actions: List[ActionTrigger]):
        self.lead_scorer = lead_scorer
        self.actions = actions
        
    def process_lead(self, lead_data: Dict[str, float]) -> bool:
        """
        Process a single lead through scoring and action triggers.
        
        Args:
            lead_data: Dictionary containing all lead data
            
        Returns:
            True if all actions were successfully triggered
        """
        try:
            lead_id = lead_data["id"]
            score = self.lead_scorer.calculate_total_score(lead_data)
            
            logger.info(f"Processing lead {lead_id} with score {score}")
            
            results = []
            for action in self.actions:
                results.append(action.trigger(lead_id, score))
                
            return all(results)
        except KeyError as e:
            logger.error(f"Missing required field in lead data: {e}")
            return False
        except Exception as e:
            logger.error(f"Error processing lead {lead_id}: {e}")
            return False
        
    def process_batch(self, leads: List[Dict[str, float]]) -> Dict[str, bool]:
        """
        Process a batch of leads through scoring and action triggers.
        
        Args:
            leads: List of lead data dictionaries
            
        Returns:
            Dictionary mapping lead IDs to success status
        """
        results = {}
        for lead in leads:
            lead_id = lead["id"]
            results[lead_id] = self.process_lead(lead)
        return results

# Example usage
if __name__ == "__main__":
    # Define scoring weights
    engagement_weights = {
        "website_visits": 0.3,
        "content_downloads": 0.4,
        "email_opens": 0.2,
        "email_clicks": 0.1
    }
    
    demographic_weights = {
        "company_size": 0.4,
        "job_title_match": 0.3,
        "industry_match": 0.3
    }
    
    # Initialize services (mock implementations would be used in practice)
    class MockEmailService:
        def send(self, lead_id, template):
            logger.info(f"Sent {template} email to lead {lead_id}")
    
    class MockTaskService:
        def create(self, lead_id, description, priority):
            logger.info(f"Created {priority} priority task for lead {lead_id}: {description}")
    
    # Create system components
    scorer = LeadScorer(engagement_weights, demographic_weights)
    email_action = EmailAction(MockEmailService())
    task_action = TaskCreationAction(MockTaskService())
    
    # Create nurturing system
    nurturing_system = LeadNurturingSystem(scorer, [email_action, task_action])
    
    # Sample lead data
    leads = [
        {
            "id": "lead_001",
            "website_visits": 5,
            "content_downloads": 2,
            "email_opens": 3,
            "email_clicks": 1,
            "company_size": 1000,
            "job_title_match": 0.8,
            "industry_match": 0.9
        },
        {
            "id": "lead_002",
            "website_visits": 2,
            "content_downloads": 1,
            "email_opens": 1,
            "email_clicks": 0,
            "company_size": 100,
            "job_title_match": 0.5,
            "industry_match": 0.6
        }
    ]
    
    # Process leads
    results = nurturing_system.process_batch(leads)
    logger.info(f"Processing results: {results}")
```
