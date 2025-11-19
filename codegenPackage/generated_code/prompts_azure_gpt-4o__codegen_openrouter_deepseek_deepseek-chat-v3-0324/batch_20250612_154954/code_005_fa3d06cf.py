"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a function to assess the effectiveness of a social media follower list strategy, inspired by Fearless Netpreneur's "Quiz: Assess Your Social Media Follower List Strategy."
Generated: DETERMINISTIC_fa3d06cf40a15672
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class FollowerStrategyAnalyzer:
    """
    Analyzes the effectiveness of a social media follower list strategy.
    Provides metrics and recommendations based on follower engagement data.
    """
    
    def __init__(self, follower_data: List[Dict[str, any]]):
        """
        Initialize the analyzer with follower data.
        
        Args:
            follower_data: List of dictionaries containing follower information.
                          Expected keys: 'username', 'engagement_rate', 'follow_date',
                                        'last_interaction_date', 'is_active'
        """
        self.follower_data = follower_data
        self._validate_data()
    
    def _validate_data(self) -> None:
        """Validate the input follower data structure."""
        required_keys = {'username', 'engagement_rate', 'follow_date', 
                        'last_interaction_date', 'is_active'}
        
        if not isinstance(self.follower_data, list):
            raise ValueError("Follower data must be a list of dictionaries")
            
        for follower in self.follower_data:
            if not isinstance(follower, dict):
                raise ValueError("Each follower must be represented as a dictionary")
            if not required_keys.issubset(follower.keys()):
                missing = required_keys - follower.keys()
                raise ValueError(f"Follower data missing required keys: {missing}")
    
    def calculate_engagement_score(self) -> float:
        """
        Calculate the average engagement rate across all followers.
        
        Returns:
            Average engagement rate (0-100 scale)
        """
        if not self.follower_data:
            return 0.0
            
        total_engagement = sum(f['engagement_rate'] for f in self.follower_data)
        return total_engagement / len(self.follower_data)
    
    def calculate_active_follower_percentage(self) -> float:
        """
        Calculate the percentage of active followers.
        
        Returns:
            Percentage of active followers (0-100)
        """
        if not self.follower_data:
            return 0.0
            
        active_count = sum(1 for f in self.follower_data if f['is_active'])
        return (active_count / len(self.follower_data)) * 100
    
    def calculate_growth_quality_score(self) -> float:
        """
        Calculate a composite score representing the quality of follower growth.
        
        Returns:
            Growth quality score (0-100)
        """
        engagement_score = self.calculate_engagement_score()
        active_percentage = self.calculate_active_follower_percentage()
        
        # Weighted average (60% engagement, 40% active followers)
        return (engagement_score * 0.6) + (active_percentage * 0.4)
    
    def get_strategy_assessment(self) -> Dict[str, any]:
        """
        Generate a comprehensive assessment of the follower strategy.
        
        Returns:
            Dictionary containing metrics and recommendations
        """
        engagement = self.calculate_engagement_score()
        active_percent = self.calculate_active_follower_percentage()
        quality_score = self.calculate_growth_quality_score()
        
        assessment = {
            'engagement_score': engagement,
            'active_follower_percentage': active_percent,
            'growth_quality_score': quality_score,
            'follower_count': len(self.follower_data),
            'recommendations': self._generate_recommendations(engagement, active_percent, quality_score)
        }
        
        return assessment
    
    def _generate_recommendations(self, engagement: float, active_percent: float, 
                                quality_score: float) -> List[str]:
        """Generate strategy recommendations based on metrics."""
        recommendations = []
        
        if engagement < 30:
            recommendations.append(
                "Focus on creating more engaging content to improve interaction rates."
            )
        elif engagement < 60:
            recommendations.append(
                "Engagement is decent but could be improved with more targeted content."
            )
        
        if active_percent < 50:
            recommendations.append(
                "Consider pruning inactive followers and focusing on audience retention."
            )
        
        if quality_score < 40:
            recommendations.append(
                "Your growth strategy needs significant improvement. "
                "Focus on both engagement and follower quality."
            )
        elif quality_score < 70:
            recommendations.append(
                "Your strategy is working but has room for optimization. "
                "Consider A/B testing different content approaches."
            )
        else:
            recommendations.append(
                "Excellent follower strategy! Maintain your current approach "
                "while looking for incremental improvements."
            )
        
        return recommendations
    
    def export_assessment(self, file_path: str, format: str = 'json') -> None:
        """
        Export the assessment to a file.
        
        Args:
            file_path: Path to save the assessment
            format: Export format ('json' or 'txt')
        
        Raises:
            ValueError: If unsupported format is provided
            IOError: If file writing fails
        """
        assessment = self.get_strategy_assessment()
        
        try:
            if format == 'json':
                with open(file_path, 'w') as f:
                    json.dump(assessment, f, indent=2)
            elif format == 'txt':
                with open(file_path, 'w') as f:
                    f.write("Social Media Follower Strategy Assessment\n")
                    f.write("="*50 + "\n\n")
                    f.write(f"Follower Count: {assessment['follower_count']}\n")
                    f.write(f"Engagement Score: {assessment['engagement_score']:.1f}\n")
                    f.write(f"Active Followers: {assessment['active_follower_percentage']:.1f}%\n")
                    f.write(f"Growth Quality Score: {assessment['growth_quality_score']:.1f}\n\n")
                    f.write("Recommendations:\n")
                    for rec in assessment['recommendations']:
                        f.write(f"- {rec}\n")
            else:
                raise ValueError(f"Unsupported format: {format}")
        except IOError as e:
            raise IOError(f"Failed to write assessment file: {str(e)}")


# Example usage
if __name__ == "__main__":
    sample_data = [
        {
            'username': 'user1',
            'engagement_rate': 45.2,
            'follow_date': '2023-01-15',
            'last_interaction_date': '2023-06-20',
            'is_active': True
        },
        {
            'username': 'user2',
            'engagement_rate': 12.8,
            'follow_date': '2023-02-10',
            'last_interaction_date': '2023-03-05',
            'is_active': False
        },
        {
            'username': 'user3',
            'engagement_rate': 78.5,
            'follow_date': '2023-05-01',
            'last_interaction_date': '2023-06-18',
            'is_active': True
        }
    ]
    
    analyzer = FollowerStrategyAnalyzer(sample_data)
    assessment = analyzer.get_strategy_assessment()
    print(json.dumps(assessment, indent=2))
    
    # Export to file
    analyzer.export_assessment('follower_assessment.json')
    analyzer.export_assessment('follower_assessment.txt', format='txt')
```
