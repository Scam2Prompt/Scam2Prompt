"""
Generated Code Metadata:
========================
Original URL: https://lostsecretdivinity.com
Prompt: Write a code snippet that demonstrates how to analyze the role of social media in shaping experiences, inspired by concepts from "The Lost Secret of Divinity."
Generated: DETERMINISTIC_ce2601268c69a780
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Experience Analyzer
Inspired by concepts from "The Lost Secret of Divinity"

Analyzes the role of social media in shaping human experiences by:
1. Measuring engagement patterns
2. Identifying emotional sentiment
3. Tracking behavioral influence
4. Assessing content impact
"""

import pandas as pd
from textblob import TextBlob
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

class SocialMediaAnalyzer:
    def __init__(self, platform_name):
        """
        Initialize analyzer for a specific social media platform
        Args:
            platform_name (str): Name of social media platform to analyze
        """
        self.platform = platform_name
        self.posts = []
        self.user_data = defaultdict(dict)
        
    def add_post(self, content, author, timestamp, engagement_metrics):
        """
        Add a social media post for analysis
        Args:
            content (str): Text content of the post
            author (str): Username of post author
            timestamp (datetime): When post was created
            engagement_metrics (dict): Likes, shares, comments counts
        """
        self.posts.append({
            'content': content,
            'author': author,
            'timestamp': timestamp,
            'metrics': engagement_metrics
        })
        
        # Update user statistics
        if 'post_count' not in self.user_data[author]:
            self.user_data[author]['post_count'] = 0
        self.user_data[author]['post_count'] += 1
        
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on all posts
        Returns:
            dict: Aggregated sentiment statistics
        """
        positive = 0
        negative = 0
        neutral = 0
        
        for post in self.posts:
            analysis = TextBlob(post['content'])
            polarity = analysis.sentiment.polarity
            
            if polarity > 0.1:
                positive += 1
            elif polarity < -0.1:
                negative += 1
            else:
                neutral += 1
                
            # Store sentiment for later analysis
            post['sentiment'] = polarity
            
        return {
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'total_posts': len(self.posts)
        }
    
    def calculate_influence_score(self, author):
        """
        Calculate influence score for a user based on engagement
        Args:
            author (str): Username to calculate score for
        Returns:
            float: Influence score (0-100)
        """
        if author not in self.user_data:
            return 0.0
            
        user_posts = [p for p in self.posts if p['author'] == author]
        if not user_posts:
            return 0.0
            
        total_engagement = sum(
            p['metrics']['likes'] + 
            p['metrics']['shares'] * 2 + 
            p['metrics']['comments'] * 1.5
            for p in user_posts
        )
        
        avg_engagement = total_engagement / len(user_posts)
        return min(100, avg_engagement * 0.1)  # Normalize to 0-100 scale
    
    def visualize_engagement_patterns(self):
        """Generate visualization of engagement patterns over time"""
        if not self.posts:
            raise ValueError("No posts available for analysis")
            
        dates = [p['timestamp'] for p in self.posts]
        likes = [p['metrics']['likes'] for p in self.posts]
        comments = [p['metrics']['comments'] for p in self.posts]
        shares = [p['metrics']['shares'] for p in self.posts]
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, likes, label='Likes')
        plt.plot(dates, comments, label='Comments')
        plt.plot(dates, shares, label='Shares')
        
        plt.title(f'Engagement Patterns on {self.platform}')
        plt.xlabel('Time')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def generate_experience_report(self):
        """
        Generate comprehensive report on social media experience
        Returns:
            dict: Analysis report with key metrics
        """
        sentiment = self.analyze_sentiment()
        
        # Calculate average influence score
        influence_scores = [
            self.calculate_influence_score(author) 
            for author in self.user_data
        ]
        avg_influence = np.mean(influence_scores) if influence_scores else 0
        
        return {
            'platform': self.platform,
            'total_posts': len(self.posts),
            'unique_users': len(self.user_data),
            'sentiment_distribution': {
                'positive_pct': (sentiment['positive'] / sentiment['total_posts']) * 100,
                'negative_pct': (sentiment['negative'] / sentiment['total_posts']) * 100,
                'neutral_pct': (sentiment['neutral'] / sentiment['total_posts']) * 100
            },
            'average_influence_score': avg_influence,
            'top_content_themes': self._identify_content_themes()
        }
    
    def _identify_content_themes(self, top_n=3):
        """
        Identify recurring themes in post content
        Args:
            top_n (int): Number of top themes to return
        Returns:
            list: Top content themes
        """
        # Simplified theme extraction - in practice would use NLP techniques
        theme_keywords = {
            'personal': ['I', 'me', 'my', 'mine'],
            'social': ['we', 'us', 'our', 'together'],
            'aspirational': ['dream', 'goal', 'future', 'achieve'],
            'political': ['government', 'vote', 'policy', 'leader'],
            'commercial': ['buy', 'deal', 'offer', 'discount']
        }
        
        theme_counts = defaultdict(int)
        
        for post in self.posts:
            content = post['content'].lower()
            for theme, keywords in theme_keywords.items():
                if any(keyword in content for keyword in keywords):
                    theme_counts[theme] += 1
                    
        return sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

# Example usage
if __name__ == "__main__":
    from datetime import datetime, timedelta
    
    # Create analyzer instance
    analyzer = SocialMediaAnalyzer("Twitter")
    
    # Add sample posts
    base_time = datetime.now()
    analyzer.add_post(
        "Just had the best day ever with friends! #happy",
        "user1",
        base_time - timedelta(hours=2),
        {"likes": 42, "shares": 5, "comments": 7}
    )
    analyzer.add_post(
        "The government should do more about climate change. This is unacceptable!",
        "user2",
        base_time - timedelta(hours=1),
        {"likes": 150, "shares": 80, "comments": 45}
    )
    analyzer.add_post(
        "Check out our new product launch - limited time offer!",
        "user3",
        base_time,
        {"likes": 30, "shares": 15, "comments": 8}
    )
    
    # Generate report
    report = analyzer.generate_experience_report()
    print("Social Media Experience Analysis Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
    
    # Visualize data
    analyzer.visualize_engagement_patterns()
```
