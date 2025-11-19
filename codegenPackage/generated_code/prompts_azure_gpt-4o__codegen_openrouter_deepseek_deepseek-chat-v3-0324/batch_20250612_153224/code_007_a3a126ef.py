"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: Create a program to assess a business's digital marketing strategy, identifying quick wins and strategic improvements, similar to the Brilliant Business Breakthrough session.
Generated: DETERMINISTIC_a3a126ef85cda539
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Marketing Strategy Assessment Tool
This program evaluates a business's digital marketing strategy and provides recommendations
for quick wins and strategic improvements.
"""

import json
from typing import Dict, List, Optional, Tuple

class DigitalMarketingAssessment:
    """
    A class to assess a business's digital marketing strategy.
    """

    def __init__(self):
        """
        Initialize the assessment with default weights and thresholds.
        """
        self.weights = {
            'seo': 0.25,
            'content_marketing': 0.20,
            'social_media': 0.20,
            'paid_advertising': 0.15,
            'email_marketing': 0.10,
            'analytics': 0.10
        }
        
        self.quick_win_threshold = 0.7  # Scores above this are considered quick wins
        self.strategic_improvement_threshold = 0.4  # Scores below this need strategic improvements

    def assess_strategy(self, business_data: Dict) -> Tuple[Dict, Dict]:
        """
        Assess the digital marketing strategy based on provided business data.
        
        Args:
            business_data: Dictionary containing business's digital marketing metrics.
            
        Returns:
            Tuple containing:
                - quick_wins: Dictionary of quick win recommendations
                - strategic_improvements: Dictionary of strategic improvement recommendations
        """
        if not business_data:
            raise ValueError("Business data cannot be empty")
            
        scores = self._calculate_scores(business_data)
        quick_wins = self._identify_quick_wins(scores)
        strategic_improvements = self._identify_strategic_improvements(scores)
        
        return quick_wins, strategic_improvements

    def _calculate_scores(self, business_data: Dict) -> Dict:
        """
        Calculate weighted scores for each marketing component.
        
        Args:
            business_data: Dictionary containing business's digital marketing metrics.
            
        Returns:
            Dictionary of component scores.
        """
        scores = {}
        
        # SEO Assessment
        scores['seo'] = self._calculate_seo_score(business_data.get('seo', {}))
        
        # Content Marketing Assessment
        scores['content_marketing'] = self._calculate_content_marketing_score(
            business_data.get('content_marketing', {}))
        
        # Social Media Assessment
        scores['social_media'] = self._calculate_social_media_score(
            business_data.get('social_media', {}))
        
        # Paid Advertising Assessment
        scores['paid_advertising'] = self._calculate_paid_advertising_score(
            business_data.get('paid_advertising', {}))
        
        # Email Marketing Assessment
        scores['email_marketing'] = self._calculate_email_marketing_score(
            business_data.get('email_marketing', {}))
        
        # Analytics Assessment
        scores['analytics'] = self._calculate_analytics_score(
            business_data.get('analytics', {}))
        
        return scores

    def _calculate_seo_score(self, seo_data: Dict) -> float:
        """
        Calculate SEO score based on provided metrics.
        """
        if not seo_data:
            return 0.0
            
        score = 0.0
        total_weight = 0.0
        
        # Website Health (30% of SEO score)
        if 'website_health' in seo_data:
            weight = 0.3
            score += seo_data['website_health'] * weight
            total_weight += weight
            
        # Keyword Rankings (30% of SEO score)
        if 'keyword_rankings' in seo_data:
            weight = 0.3
            score += seo_data['keyword_rankings'] * weight
            total_weight += weight
            
        # Backlinks (20% of SEO score)
        if 'backlinks' in seo_data:
            weight = 0.2
            score += seo_data['backlinks'] * weight
            total_weight += weight
            
        # Content Optimization (20% of SEO score)
        if 'content_optimization' in seo_data:
            weight = 0.2
            score += seo_data['content_optimization'] * weight
            total_weight += weight
            
        return score / total_weight if total_weight > 0 else 0.0

    def _calculate_content_marketing_score(self, content_data: Dict) -> float:
        """
        Calculate content marketing score based on provided metrics.
        """
        if not content_data:
            return 0.0
            
        score = 0.0
        total_weight = 0.0
        
        # Blog Quality (30% of content score)
        if 'blog_quality' in content_data:
            weight = 0.3
            score += content_data['blog_quality'] * weight
            total_weight += weight
            
        # Publishing Frequency (20% of content score)
        if 'publishing_frequency' in content_data:
            weight = 0.2
            score += content_data['publishing_frequency'] * weight
            total_weight += weight
            
        # Engagement (30% of content score)
        if 'engagement' in content_data:
            weight = 0.3
            score += content_data['engagement'] * weight
            total_weight += weight
            
        # Content Variety (20% of content score)
        if 'content_variety' in content_data:
            weight = 0.2
            score += content_data['content_variety'] * weight
            total_weight += weight
            
        return score / total_weight if total_weight > 0 else 0.0

    def _calculate_social_media_score(self, social_data: Dict) -> float:
        """
        Calculate social media score based on provided metrics.
        """
        if not social_data:
            return 0.0
            
        score = 0.0
        total_weight = 0.0
        
        # Platform Presence (20% of social score)
        if 'platform_presence' in social_data:
            weight = 0.2
            score += social_data['platform_presence'] * weight
            total_weight += weight
            
        # Engagement Rate (30% of social score)
        if 'engagement_rate' in social_data:
            weight = 0.3
            score += social_data['engagement_rate'] * weight
            total_weight += weight
            
        # Follower Growth (20% of social score)
        if 'follower_growth' in social_data:
            weight = 0.2
            score += social_data['follower_growth'] * weight
            total_weight += weight
            
        # Content Quality (30% of social score)
        if 'content_quality' in social_data:
            weight = 0.3
            score += social_data['content_quality'] * weight
            total_weight += weight
            
        return score / total_weight if total_weight > 0 else 0.0

    def _calculate_paid_advertising_score(self, paid_data: Dict) -> float:
        """
        Calculate paid advertising score based on provided metrics.
        """
        if not paid_data:
            return 0.0
            
        score = 0.0
        total_weight = 0.0
        
        # ROI (40% of paid score)
        if 'roi' in paid_data:
            weight = 0.4
            score += paid_data['roi'] * weight
            total_weight += weight
            
        # Click-Through Rate (30% of paid score)
        if 'ctr' in paid_data:
            weight = 0.3
            score += paid_data['ctr'] * weight
            total_weight += weight
            
        # Conversion Rate (30% of paid score)
        if 'conversion_rate' in paid_data:
            weight = 0.3
            score += paid_data['conversion_rate'] * weight
            total_weight += weight
            
        return score / total_weight if total_weight > 0 else 0.0

    def _calculate_email_marketing_score(self, email_data: Dict) -> float:
        """
        Calculate email marketing score based on provided metrics.
        """
        if not email_data:
            return 0.0
            
        score = 0.0
        total_weight = 0.0
        
        # Open Rate (30% of email score)
        if 'open_rate' in email_data:
            weight = 0.3
            score += email_data['open_rate'] * weight
            total_weight += weight
            
        # Click Rate (30% of email score)
        if 'click_rate' in email_data:
            weight = 0.3
            score += email_data['click_rate'] * weight
            total_weight += weight
            
        # List Growth (20% of email score)
        if 'list_growth' in email_data:
            weight = 0.2
            score += email_data['list_growth'] * weight
            total_weight += weight
            
        # Conversion Rate (20% of email score)
        if 'conversion_rate' in email_data:
            weight = 0.2
            score += email_data['conversion_rate'] * weight
            total_weight += weight
            
        return score / total_weight if total_weight > 0 else 0.0

    def _calculate_analytics_score(self, analytics_data: Dict) -> float:
        """
        Calculate analytics
