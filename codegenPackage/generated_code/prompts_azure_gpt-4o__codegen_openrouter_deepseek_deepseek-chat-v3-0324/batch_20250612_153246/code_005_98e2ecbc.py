"""
Generated Code Metadata:
========================
Original URL: https://www.thedigilancer.com
Prompt: Create a Python program to analyze social media marketing (SMM) campaign effectiveness, referencing Ratul Kalra's focus on boosting visibility and driving engagement.
Generated: DETERMINISTIC_98e2ecbc13f40689
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Marketing (SMM) Campaign Effectiveness Analyzer

This program analyzes the effectiveness of SMM campaigns by evaluating key metrics
such as engagement rates, reach, conversions, and ROI. The analysis is inspired by
Ratul Kalra's focus on boosting visibility and driving engagement.

Key Features:
- Calculate engagement rate (likes, comments, shares per post)
- Measure reach and impressions
- Track conversions and ROI
- Generate visual reports
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class SMMAnalyzer:
    """
    A class to analyze social media marketing campaign effectiveness.
    """
    
    def __init__(self, campaign_data: Dict[str, List[Dict]]):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            campaign_data: Dictionary containing platform-specific campaign data.
                          Format: {'platform': [list of post metrics]}
        """
        self.campaign_data = campaign_data
        self.platforms = list(campaign_data.keys())
        self.analysis_results = {}
        
    def calculate_engagement_rate(self, likes: int, comments: int, shares: int, followers: int) -> float:
        """
        Calculate engagement rate for a post.
        
        Args:
            likes: Number of likes
            comments: Number of comments
            shares: Number of shares
            followers: Total followers count
            
        Returns:
            Engagement rate as percentage
        """
        try:
            engagement = likes + comments + shares
            return (engagement / followers) * 100 if followers > 0 else 0.0
        except Exception as e:
            print(f"Error calculating engagement rate: {e}")
            return 0.0
    
    def analyze_platform(self, platform: str) -> Dict:
        """
        Analyze metrics for a specific platform.
        
        Args:
            platform: Name of the platform to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        if platform not in self.campaign_data:
            raise ValueError(f"Platform {platform} not found in campaign data")
            
        posts = self.campaign_data[platform]
        if not posts:
            return {}
            
        df = pd.DataFrame(posts)
        
        # Basic metrics
        total_posts = len(df)
        total_reach = df['reach'].sum()
        total_impressions = df['impressions'].sum()
        total_engagement = df['likes'].sum() + df['comments'].sum() + df['shares'].sum()
        
        # Calculate engagement rates
        df['engagement_rate'] = df.apply(
            lambda row: self.calculate_engagement_rate(
                row['likes'], row['comments'], row['shares'], row['followers']
            ), axis=1
        )
        
        avg_engagement_rate = df['engagement_rate'].mean()
        
        # Conversion metrics (if available)
        conversions = df.get('conversions', pd.Series([0] * total_posts)).sum()
        conversion_rate = (conversions / total_reach * 100) if total_reach > 0 else 0
        
        # ROI calculation (if cost data available)
        cost = df.get('cost', pd.Series([0] * total_posts)).sum()
        revenue = df.get('revenue', pd.Series([0] * total_posts)).sum()
        roi = ((revenue - cost) / cost * 100) if cost > 0 else 0
        
        return {
            'platform': platform,
            'total_posts': total_posts,
            'total_reach': total_reach,
            'total_impressions': total_impressions,
            'total_engagement': total_engagement,
            'avg_engagement_rate': avg_engagement_rate,
            'conversions': conversions,
            'conversion_rate': conversion_rate,
            'cost': cost,
            'revenue': revenue,
            'roi': roi,
            'top_posts': self._get_top_posts(df)
        }
    
    def _get_top_posts(self, df: pd.DataFrame, n: int = 3) -> List[Dict]:
        """
        Identify top performing posts by engagement rate.
        
        Args:
            df: DataFrame containing post metrics
            n: Number of top posts to return
            
        Returns:
            List of top posts with their metrics
        """
        try:
            top_posts = df.nlargest(n, 'engagement_rate')
            return top_posts.to_dict('records')
        except Exception as e:
            print(f"Error identifying top posts: {e}")
            return []
    
    def analyze_all_platforms(self) -> Dict:
        """
        Analyze metrics across all platforms.
        
        Returns:
            Dictionary containing analysis results for all platforms
        """
        for platform in self.platforms:
            try:
                self.analysis_results[platform] = self.analyze_platform(platform)
            except Exception as e:
                print(f"Error analyzing platform {platform}: {e}")
                continue
                
        return self.analysis_results
    
    def generate_report(self, output_dir: str = "reports") -> None:
        """
        Generate visual report of campaign analysis.
        
        Args:
            output_dir: Directory to save report files
        """
        if not self.analysis_results:
            self.analyze_all_platforms()
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = os.path.join(output_dir, f"smm_report_{timestamp}.pdf")
        
        try:
            self._generate_visualizations(report_filename)
            self._save_analysis_json(output_dir, timestamp)
            print(f"Report generated successfully: {report_filename}")
        except Exception as e:
            print(f"Error generating report: {e}")
    
    def _generate_visualizations(self, filename: str) -> None:
        """
        Create visualizations for the report.
        
        Args:
            filename: Path to save the visualization
        """
        platforms = list(self.analysis_results.keys())
        metrics = ['avg_engagement_rate', 'conversion_rate', 'roi']
        
        fig, axes = plt.subplots(nrows=len(metrics), figsize=(10, 15))
        fig.suptitle('SMM Campaign Performance Analysis', fontsize=16)
        
        for i, metric in enumerate(metrics):
            values = [self.analysis_results[p][metric] for p in platforms]
            axes[i].bar(platforms, values, color=['#1DA1F2', '#4267B2', '#E1306C'])
            axes[i].set_title(metric.replace('_', ' ').title())
            axes[i].set_ylabel('Percentage (%)')
            
            # Add value labels
            for j, v in enumerate(values):
                axes[i].text(j, v + 0.5, f"{v:.2f}%", ha='center')
        
        plt.tight_layout()
        plt.savefig(filename, format='pdf')
        plt.close()
    
    def _save_analysis_json(self, output_dir: str, timestamp: str) -> None:
        """
        Save analysis results as JSON file.
        
        Args:
            output_dir: Directory to save the file
            timestamp: Timestamp for filename
        """
        filename = os.path.join(output_dir, f"analysis_results_{timestamp}.json")
        try:
            with open(filename, 'w') as f:
                json.dump(self.analysis_results, f, indent=4)
        except Exception as e:
            print(f"Error saving analysis results: {e}")

def load_campaign_data(filepath: str) -> Dict:
    """
    Load campaign data from JSON file.
    
    Args:
        filepath: Path to JSON file containing campaign data
        
    Returns:
        Dictionary containing campaign data
    """
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return {}
    except Exception as e:
        print(f"Error loading campaign data: {e}")
        return {}

def sample_campaign_data() -> Dict:
    """
    Generate sample campaign data for demonstration.
    
    Returns:
        Dictionary containing sample campaign data
    """
    return {
        "Instagram": [
            {
                "post_id": "IG1",
                "date": "2023-01-01",
                "likes": 1500,
                "comments": 120,
                "shares": 300,
                "reach": 5000,
                "impressions": 8000,
                "followers": 10000,
                "cost": 200,
                "revenue": 800,
                "conversions": 40
            },
            {
                "post_id": "IG2",
                "date": "2023-01-05",
                "likes": 2000,
                "comments": 150,
                "shares": 400,
                "reach": 6000,
                "impressions": 9500,
                "followers": 10000,
                "cost
