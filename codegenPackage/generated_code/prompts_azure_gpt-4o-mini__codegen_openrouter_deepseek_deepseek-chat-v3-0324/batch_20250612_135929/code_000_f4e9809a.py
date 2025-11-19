"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Generate a Python script that utilizes AI techniques to enhance YouTube channel performance, as discussed in the AI Mastery course review on Was Broke.
Generated: DETERMINISTIC_f4e9809a64167684
Batch ID: 20250612_135929
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
import time
from datetime import datetime
from typing import List, Dict, Optional
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import openai
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class YouTubeAIAnalyzer:
    """
    A class to analyze and enhance YouTube channel performance using AI techniques.
    """
    
    def __init__(self, api_key: str, openai_key: str, channel_id: str):
        """
        Initialize the YouTube analyzer with API keys and channel ID.
        
        Args:
            api_key (str): YouTube Data API v3 key
            openai_key (str): OpenAI API key
            channel_id (str): YouTube channel ID to analyze
        """
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.openai_key = openai_key
        self.channel_id = channel_id
        openai.api_key = openai_key
        
        # Initialize NLP components
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    def get_channel_stats(self) -> Dict:
        """
        Get basic statistics for the YouTube channel.
        
        Returns:
            Dict: Channel statistics including viewCount, subscriberCount, etc.
        """
        try:
            request = self.youtube.channels().list(
                part='statistics,snippet',
                id=self.channel_id
            )
            response = request.execute()
            
            if not response['items']:
                raise ValueError("Channel not found or no data available")
                
            return {
                'title': response['items'][0]['snippet']['title'],
                'subscribers': int(response['items'][0]['statistics']['subscriberCount']),
                'views': int(response['items'][0]['statistics']['viewCount']),
                'videos': int(response['items'][0]['statistics']['videoCount']),
                'description': response['items'][0]['snippet']['description']
            }
        except HttpError as e:
            raise Exception(f"YouTube API error: {e}")
        except Exception as e:
            raise Exception(f"Error getting channel stats: {e}")
    
    def get_video_data(self, max_results: int = 50) -> List[Dict]:
        """
        Get data for videos from the channel.
        
        Args:
            max_results (int): Maximum number of videos to retrieve
            
        Returns:
            List[Dict]: List of video data dictionaries
        """
        try:
            videos = []
            next_page_token = None
            
            while len(videos) < max_results:
                request = self.youtube.search().list(
                    part='id,snippet',
                    channelId=self.channel_id,
                    maxResults=min(50, max_results - len(videos)),
                    order='date',
                    type='video',
                    pageToken=next_page_token
                )
                response = request.execute()
                
                video_ids = [item['id']['videoId'] for item in response['items']]
                
                # Get video statistics
                stats_request = self.youtube.videos().list(
                    part='statistics,snippet',
                    id=','.join(video_ids)
                )
                stats_response = stats_request.execute()
                
                for item in stats_response['items']:
                    videos.append({
                        'video_id': item['id'],
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'published_at': item['snippet']['publishedAt'],
                        'views': int(item['statistics'].get('viewCount', 0)),
                        'likes': int(item['statistics'].get('likeCount', 0)),
                        'comments': int(item['statistics'].get('commentCount', 0)),
                        'duration': item['contentDetails'].get('duration', '') if 'contentDetails' in item else '',
                        'tags': item['snippet'].get('tags', [])
                    })
                
                next_page_token = response.get('nextPageToken')
                if not next_page_token:
                    break
            
            return videos
        except HttpError as e:
            raise Exception(f"YouTube API error: {e}")
        except Exception as e:
            raise Exception(f"Error getting video data: {e}")
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text for NLP analysis.
        
        Args:
            text (str): Text to preprocess
            
        Returns:
            str: Preprocessed text
        """
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token.isalpha() and token not in self.stop_words]
        return ' '.join(tokens)
    
    def analyze_video_content(self, videos: List[Dict]) -> Dict:
        """
        Analyze video content using NLP and clustering.
        
        Args:
            videos (List[Dict]): List of video data dictionaries
            
        Returns:
            Dict: Analysis results including clusters and keywords
        """
        try:
            # Prepare text data
            video_texts = [f"{video['title']} {video['description']}" for video in videos]
            preprocessed_texts = [self.preprocess_text(text) for text in video_texts]
            
            # Vectorize text
            vectorizer = TfidfVectorizer(max_features=1000)
            X = vectorizer.fit_transform(preprocessed_texts)
            
            # Cluster videos
            kmeans = KMeans(n_clusters=5, random_state=42)
            clusters = kmeans.fit_predict(X)
            
            # Get top keywords per cluster
            feature_names = vectorizer.get_feature_names_out()
            top_keywords = {}
            
            for i in range(kmeans.n_clusters):
                cluster_center = kmeans.cluster_centers_[i]
                top_indices = cluster_center.argsort()[-10:][::-1]
                top_keywords[f'cluster_{i}'] = [feature_names[idx] for idx in top_indices]
            
            return {
                'clusters': clusters.tolist(),
                'keywords': top_keywords,
                'vectorizer': vectorizer,
                'model': kmeans
            }
        except Exception as e:
            raise Exception(f"Error analyzing video content: {e}")
    
    def generate_ai_content_suggestions(self, analysis_results: Dict) -> List[str]:
        """
        Generate content suggestions using OpenAI.
        
        Args:
            analysis_results (Dict): Results from video content analysis
            
        Returns:
            List[str]: List of content suggestions
        """
        try:
            prompt = f"""
            Based on the following YouTube video content analysis, suggest 5 new video ideas 
            that would perform well for this channel. The analysis shows the following 
            content clusters and their top keywords:
            
            {json.dumps(analysis_results['keywords'], indent=2)}
            
            Please suggest creative, engaging video ideas that align with these content themes.
            Return the suggestions as a numbered list.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a YouTube content strategy expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            suggestions = response.choices[0].message.content.split('\n')
            return [s.strip() for s in suggestions if s.strip()]
        except Exception as e:
            raise Exception(f"Error generating AI suggestions: {e}")
    
    def analyze_performance_trends(self, videos: List[Dict]) -> Dict:
        """
        Analyze performance trends across videos.
        
        Args:
            videos (List[Dict]): List of video data dictionaries
            
        Returns:
            Dict: Performance analysis results
        """
        try:
            df = pd.DataFrame(videos)
            df['published_at'] = pd.to_datetime(df['published_at'])
            df['engagement_rate'] = (df['likes'] + df['comments']) / df['views']
            
            # Calculate moving averages
            df = df.sort_values('published_at')
            df['views_ma'] = df['views'].rolling(window=5, min_periods=1).mean()
            df['engagement_ma'] = df['engagement_rate'].rolling(window=5, min_periods=1).mean()
            
            # Find best performing videos
            top_videos = df.nlargest(5, 'views')
            
            return {
                'performance_df': df,
                'top_videos': top_videos.to_dict('records'),
                'avg_engagement': df['engagement_rate'].mean(),
                'avg_views': df['views'].
