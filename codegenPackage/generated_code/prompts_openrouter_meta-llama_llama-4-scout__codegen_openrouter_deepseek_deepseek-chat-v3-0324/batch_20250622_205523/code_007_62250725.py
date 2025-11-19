"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Recommend a set of metrics for evaluating the success of community development projects, using data and insights from the Starke Orte Netzwerk's Wissensplattform."
Generated: DETERMINISTIC_622507250d03eaa0
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

class CommunityProjectMetrics:
    """
    A class to calculate and recommend metrics for evaluating community development projects.
    Based on insights from Starke Orte Netzwerk's Wissensplattform.
    """
    
    def __init__(self, project_data: pd.DataFrame):
        """
        Initialize with project data.
        
        Args:
            project_data: DataFrame containing project information with relevant columns
        """
        self.project_data = project_data
        
    def validate_data(self) -> bool:
        """
        Validate that required columns exist in the input data.
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        required_columns = {
            'participants_count',
            'events_organized',
            'local_partners',
            'funding_amount',
            'duration_months',
            'social_media_engagement',
            'volunteer_hours'
        }
        return required_columns.issubset(self.project_data.columns)
    
    def calculate_basic_metrics(self) -> Dict[str, float]:
        """
        Calculate basic quantitative metrics.
        
        Returns:
            Dictionary of basic metrics
        """
        if not self.validate_data():
            raise ValueError("Input data is missing required columns")
            
        return {
            'total_participants': self.project_data['participants_count'].sum(),
            'average_events_per_month': (
                self.project_data['events_organized'].sum() / 
                self.project_data['duration_months'].sum()
            ),
            'participation_rate_per_event': (
                self.project_data['participants_count'].sum() / 
                self.project_data['events_organized'].sum()
            ),
            'funding_efficiency': (
                self.project_data['participants_count'].sum() / 
                self.project_data['funding_amount'].sum()
            ),
            'volunteer_engagement': (
                self.project_data['volunteer_hours'].sum() / 
                self.project_data['participants_count'].sum()
            )
        }
    
    def calculate_network_metrics(self) -> Dict[str, float]:
        """
        Calculate network and partnership metrics.
        
        Returns:
            Dictionary of network metrics
        """
        if not self.validate_data():
            raise ValueError("Input data is missing required columns")
            
        return {
            'average_partners_per_project': self.project_data['local_partners'].mean(),
            'social_media_reach_per_participant': (
                self.project_data['social_media_engagement'].sum() / 
                self.project_data['participants_count'].sum()
            ),
            'partner_diversity_index': self._calculate_diversity_index()
        }
    
    def _calculate_diversity_index(self) -> float:
        """
        Helper method to calculate partner diversity index.
        
        Returns:
            float: Diversity index score
        """
        # Placeholder for actual diversity calculation
        # In practice, this would analyze partner types/sectors
        return 0.75  # Example value
    
    def calculate_qualitative_metrics(self) -> Dict[str, Optional[float]]:
        """
        Calculate qualitative metrics (placeholders for actual survey data).
        
        Returns:
            Dictionary of qualitative metrics
        """
        return {
            'participant_satisfaction': None,  # Would come from surveys
            'community_impact_score': None,    # Would come from expert assessments
            'sustainability_index': None       # Would evaluate long-term effects
        }
    
    def get_recommended_metrics(self) -> Dict[str, Dict[str, float]]:
        """
        Get all recommended metrics for project evaluation.
        
        Returns:
            Dictionary containing all metric categories
        """
        try:
            return {
                'quantitative_metrics': self.calculate_basic_metrics(),
                'network_metrics': self.calculate_network_metrics(),
                'qualitative_metrics': self.calculate_qualitative_metrics()
            }
        except Exception as e:
            raise RuntimeError(f"Error calculating metrics: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data - in practice would come from database/API
    sample_data = pd.DataFrame({
        'participants_count': [150, 200, 180],
        'events_organized': [5, 8, 6],
        'local_partners': [3, 5, 4],
        'funding_amount': [10000, 15000, 12000],
        'duration_months': [6, 8, 7],
        'social_media_engagement': [500, 800, 600],
        'volunteer_hours': [300, 400, 350]
    })
    
    try:
        evaluator = CommunityProjectMetrics(sample_data)
        metrics = evaluator.get_recommended_metrics()
        print("Recommended Community Project Metrics:")
        for category, values in metrics.items():
            print(f"\n{category.replace('_', ' ').title()}:")
            for metric, value in values.items():
                print(f"  {metric.replace('_', ' ').title()}: {value:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
