"""
Generated Code Metadata:
========================
Original URL: https://aipad.club
Prompt: Create a Python script to analyze and summarize AI-related discussions from a Slack community like AiPAD Club.
Generated: DETERMINISTIC_c8fcd2d89a4c6714
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import re
from collections import Counter
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class SlackAIAnalyzer:
    """
    A class to analyze and summarize AI-related discussions from a Slack community.
    """
    
    def __init__(self, slack_token: str, channel_id: str):
        """
        Initialize the Slack AI Analyzer with Slack token and channel ID.
        
        Args:
            slack_token (str): Slack API token
            channel_id (str): Channel ID to analyze
        """
        self.client = WebClient(token=slack_token)
        self.channel_id = channel_id
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.ai_keywords = {
            'ai', 'artificial intelligence', 'machine learning', 'ml', 'deep learning',
            'neural network', 'nlp', 'natural language processing', 'llm', 'gpt',
            'transformer', 'computer vision', 'cv', 'generative ai', 'chatbot',
            'autonomous', 'robotics', 'algorithm', 'data science', 'big data'
        }
        
    def _preprocess_text(self, text: str) -> List[str]:
        """
        Preprocess text by tokenizing, removing stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            List[str]: List of processed tokens
        """
        # Remove URLs and special characters
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\W', ' ', text)
        
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and len(token) > 2]
        return tokens
    
    def _is_ai_related(self, text: str) -> bool:
        """
        Check if text is AI-related based on keywords.
        
        Args:
            text (str): Text to check
            
        Returns:
            bool: True if AI-related, False otherwise
        """
        tokens = self._preprocess_text(text)
        return any(keyword in ' '.join(tokens) for keyword in self.ai_keywords)
    
    def fetch_messages(self, days: int = 30) -> List[Dict]:
        """
        Fetch messages from Slack channel within specified days.
        
        Args:
            days (int): Number of days to look back
            
        Returns:
            List[Dict]: List of message dictionaries
        """
        try:
            oldest = (datetime.now() - pd.Timedelta(days=days)).timestamp()
            result = self.client.conversations_history(
                channel=self.channel_id,
                oldest=oldest
            )
            return result['messages']
        except SlackApiError as e:
            print(f"Error fetching messages: {e.response['error']}")
            return []
    
    def analyze_messages(self, messages: List[Dict]) -> Dict:
        """
        Analyze messages and generate statistics.
        
        Args:
            messages (List[Dict]): List of message dictionaries
            
        Returns:
            Dict: Analysis results
        """
        ai_messages = []
        all_tokens = []
        user_counts = Counter()
        day_counts = Counter()
        
        for msg in messages:
            if 'text' not in msg or 'user' not in msg:
                continue
                
            text = msg['text']
            if not self._is_ai_related(text):
                continue
                
            ai_messages.append(msg)
            tokens = self._preprocess_text(text)
            all_tokens.extend(tokens)
            
            # Count user participation
            user_counts[msg['user']] += 1
            
            # Count by day
            timestamp = float(msg['ts'])
            day = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            day_counts[day] += 1
            
        # Get top terms
        term_counts = Counter(all_tokens)
        top_terms = term_counts.most_common(20)
        
        return {
            'total_messages': len(messages),
            'ai_messages': len(ai_messages),
            'top_users': user_counts.most_common(10),
            'top_terms': top_terms,
            'daily_counts': dict(day_counts),
            'sample_messages': ai_messages[:5]  # Sample of AI messages
        }
    
    def generate_wordcloud(self, terms: List[Tuple[str, int]], filename: str = 'wordcloud.png'):
        """
        Generate a word cloud from terms.
        
        Args:
            terms (List[Tuple[str, int]]): List of (term, count) tuples
            filename (str): Output filename
        """
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(terms))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
    
    def generate_report(self, analysis: Dict, output_dir: str = 'reports'):
        """
        Generate a comprehensive report from analysis.
        
        Args:
            analysis (Dict): Analysis results
            output_dir (str): Output directory for reports
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Save JSON report
        with open(f'{output_dir}/analysis_report.json', 'w') as f:
            json.dump(analysis, f, indent=2)
            
        # Generate word cloud
        self.generate_wordcloud(analysis['top_terms'], f'{output_dir}/wordcloud.png')
        
        # Generate CSV report
        df = pd.DataFrame({
            'Metric': ['Total Messages', 'AI-Related Messages', 'AI Percentage'],
            'Value': [
                analysis['total_messages'],
                analysis['ai_messages'],
                round(analysis['ai_messages'] / analysis['total_messages'] * 100, 2)
            ]
        })
        df.to_csv(f'{output_dir}/summary_stats.csv', index=False)
        
        # Generate daily activity CSV
        daily_df = pd.DataFrame(list(analysis['daily_counts'].items()), columns=['Date', 'AI Messages'])
        daily_df.to_csv(f'{output_dir}/daily_activity.csv', index=False)
        
        print(f"Report generated in {output_dir} directory")
    
    def run_analysis(self, days: int = 30, output_dir: str = 'reports'):
        """
        Run complete analysis pipeline.
        
        Args:
            days (int): Number of days to analyze
            output_dir (str): Output directory for reports
        """
        messages = self.fetch_messages(days)
        if not messages:
            print("No messages found or error occurred.")
            return
            
        analysis = self.analyze_messages(messages)
        self.generate_report(analysis, output_dir)

# Example usage
if __name__ == "__main__":
    # Replace with your Slack token and channel ID
    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    CHANNEL_ID = 'C12345678'  # Replace with your channel ID
    
    if not SLACK_TOKEN:
        raise ValueError("Please set SLACK_TOKEN environment variable")
    
    analyzer = SlackAIAnalyzer(SLACK_TOKEN, CHANNEL_ID)
    analyzer.run_analysis(days=30)
```
