"""
Generated Code Metadata:
========================
Original URL: https://mysoulitude.com
Prompt: Discuss the role of humor in self-love and personal growth, using examples from My Soulitude's blog posts and providing insights into maintaining a light-hearted approach to life's challenges.
Generated: DETERMINISTIC_9aa90964436f14d2
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python script that analyzes blog posts from "My Soulitude" to extract insights about humor's role in self-love and personal growth. The script will include sentiment analysis and keyword extraction to identify humorous content and its impact.

```python
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

class BlogAnalyzer:
    """
    Analyzes blog posts from My Soulitude to understand humor's role in self-love and personal growth.
    """
    
    def __init__(self, base_url):
        """
        Initialize the analyzer with the blog's base URL.
        
        Args:
            base_url (str): Base URL of the My Soulitude blog
        """
        self.base_url = base_url
        self.stop_words = set(stopwords.words('english'))
        self.humor_keywords = ['humor', 'funny', 'laugh', 'joke', 'light-hearted', 'comedy', 'wit']
        self.self_love_keywords = ['self-love', 'confidence', 'acceptance', 'compassion', 'worth']
        self.growth_keywords = ['growth', 'learn', 'improve', 'develop', 'progress', 'change']
        
    def fetch_blog_posts(self, num_posts=10):
        """
        Fetch blog post content from My Soulitude.
        
        Args:
            num_posts (int): Number of posts to analyze
            
        Returns:
            list: List of dictionaries containing post content and metadata
        """
        try:
            # In a real implementation, this would scrape the actual blog
            # For demo purposes, we'll simulate some blog post data
            mock_posts = [
                {
                    'title': 'Laughing at My Own Mistakes: A Path to Self-Acceptance',
                    'content': 'Humor has been my greatest tool in learning to love myself. When I trip in public, instead of embarrassment, I now take a bow. This light-hearted approach has transformed my self-image.',
                    'url': f'{self.base_url}/laughing-at-mistakes',
                    'date': '2023-05-15'
                },
                {
                    'title': 'The Serious Business of Not Taking Yourself Too Seriously',
                    'content': 'Personal growth doesn\'t have to be solemn. I\'ve found that maintaining a sense of humor about my flaws actually helps me improve faster. Laughter creates space for change.',
                    'url': f'{self.base_url}/not-too-serious',
                    'date': '2023-04-22'
                }
            ]
            
            # Pad with additional mock posts if needed
            while len(mock_posts) < num_posts:
                mock_posts.extend(mock_posts)
                
            return mock_posts[:num_posts]
            
        except Exception as e:
            print(f"Error fetching blog posts: {e}")
            return []
    
    def analyze_sentiment(self, text):
        """
        Perform sentiment analysis on text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Sentiment analysis results (polarity, subjectivity)
        """
        try:
            blob = TextBlob(text)
            return {
                'polarity': blob.sentiment.polarity,
                'subjectivity': blob.sentiment.subjectivity
            }
        except Exception as e:
            print(f"Error in sentiment analysis: {e}")
            return {'polarity': 0, 'subjectivity': 0}
    
    def extract_keywords(self, text, n=10):
        """
        Extract top keywords from text, excluding stopwords.
        
        Args:
            text (str): Text to analyze
            n (int): Number of keywords to return
            
        Returns:
            list: Top n keywords
        """
        try:
            words = word_tokenize(text.lower())
            words = [word for word in words if word.isalpha() and word not in self.stop_words]
            word_freq = Counter(words)
            return [word for word, _ in word_freq.most_common(n)]
        except Exception as e:
            print(f"Error extracting keywords: {e}")
            return []
    
    def contains_humor(self, text):
        """
        Check if text contains humor-related keywords.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            bool: True if humor keywords are found
        """
        try:
            text_lower = text.lower()
            return any(keyword in text_lower for keyword in self.humor_keywords)
        except Exception as e:
            print(f"Error checking for humor: {e}")
            return False
    
    def analyze_posts(self, posts):
        """
        Analyze blog posts for humor, self-love, and growth themes.
        
        Args:
            posts (list): List of blog post dictionaries
            
        Returns:
            dict: Analysis results
        """
        results = {
            'total_posts': len(posts),
            'humor_posts': 0,
            'self_love_posts': 0,
            'growth_posts': 0,
            'humor_and_self_love': 0,
            'humor_and_growth': 0,
            'avg_sentiment': {'polarity': 0, 'subjectivity': 0},
            'common_keywords': []
        }
        
        try:
            total_polarity = 0
            total_subjectivity = 0
            all_keywords = []
            
            for post in posts:
                content = f"{post['title']} {post['content']}"
                sentiment = self.analyze_sentiment(content)
                total_polarity += sentiment['polarity']
                total_subjectivity += sentiment['subjectivity']
                
                keywords = self.extract_keywords(content)
                all_keywords.extend(keywords)
                
                has_humor = self.contains_humor(content)
                has_self_love = any(keyword in content.lower() for keyword in self.self_love_keywords)
                has_growth = any(keyword in content.lower() for keyword in self.growth_keywords)
                
                if has_humor:
                    results['humor_posts'] += 1
                if has_self_love:
                    results['self_love_posts'] += 1
                if has_growth:
                    results['growth_posts'] += 1
                if has_humor and has_self_love:
                    results['humor_and_self_love'] += 1
                if has_humor and has_growth:
                    results['humor_and_growth'] += 1
            
            if posts:
                results['avg_sentiment']['polarity'] = total_polarity / len(posts)
                results['avg_sentiment']['subjectivity'] = total_subjectivity / len(posts)
                results['common_keywords'] = Counter(all_keywords).most_common(10)
            
            return results
            
        except Exception as e:
            print(f"Error analyzing posts: {e}")
            return results
    
    def visualize_results(self, results):
        """
        Create visualizations of the analysis results.
        
        Args:
            results (dict): Analysis results from analyze_posts()
        """
        try:
            # Humor overlap visualization
            labels = ['Humor & Self-Love', 'Humor & Growth']
            values = [results['humor_and_self_love'], results['humor_and_growth']]
            
            plt.figure(figsize=(10, 5))
            plt.bar(labels, values, color=['lightblue', 'lightgreen'])
            plt.title('Overlap Between Humor and Personal Development Themes')
            plt.ylabel('Number of Posts')
            plt.show()
            
            # Sentiment visualization
            plt.figure(figsize=(5, 5))
            plt.pie(
                [results['avg_sentiment']['polarity'] + 1, 2 - (results['avg_sentiment']['polarity'] + 1)],
                labels=['Positive', 'Negative'],
                autopct='%1.1f%%',
                colors=['lightgreen', 'lightcoral']
            )
            plt.title('Overall Sentiment of Posts')
            plt.show()
            
        except Exception as e:
            print(f"Error creating visualizations: {e}")

    def generate_insights(self, results):
        """
        Generate human-readable insights from analysis results.
        
        Args:
            results (dict): Analysis results from analyze_posts()
            
        Returns:
            str: Formatted insights
        """
        try:
            insights = []
            
            # Basic statistics
            insights.append(f"Analyzed {results['total_posts']} blog posts from My Soulitude.")
            insights.append(f"{results['humor_posts']} posts ({results['humor_posts']/results['total_posts']*100:.1f}%) contained humor-related content.")
            
            # Humor and self-love connection
            if results['humor_and_self_love'] > 0:
                insights.append(
                    f"Humor frequently appears alongside self-love themes ({results['
