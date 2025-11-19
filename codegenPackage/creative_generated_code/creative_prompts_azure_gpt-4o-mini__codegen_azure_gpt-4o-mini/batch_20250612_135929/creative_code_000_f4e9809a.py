"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wasbroke.com
Prompt: Generate a Python script that utilizes AI techniques to enhance YouTube channel performance, as discussed in the AI Mastery course review on Was Broke.
Generated: DETERMINISTIC_f4e9809a64167684
Batch ID: 20250612_135929
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/youtube/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class YouTubeChannelAnalyzer:
    def __init__(self, api_key):
        """Initialize the YouTubeChannelAnalyzer with API key."""
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.channel_data = None
        self.video_data = []

    def fetch_channel_data(self, channel_id):
        """Fetch channel data using YouTube Data API."""
        url = f"{self.base_url}channels?part=snippet,statistics&id={channel_id}&key={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.channel_data = response.json()
            return self.channel_data
        else:
            raise Exception(f"Error fetching channel data: {response.status_code} {response.text}")

    def fetch_video_data(self, channel_id):
        """Fetch videos from the specified channel."""
        url = f"{self.base_url}search?key={self.api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50"
        response = requests.get(url)
        
        if response.status_code == 200:
            videos = response.json().get('items', [])
            for video in videos:
                if video['id']['kind'] == 'youtube#video':
                    self.video_data.append(video)
            return self.video_data
        else:
            raise Exception(f"Error fetching video data: {response.status_code} {response.text}")

    def analyze_video_titles(self):
        """Analyze video titles using cosine similarity to identify keyword trends."""
        titles = [video['snippet']['title'] for video in self.video_data]
        vectorizer = CountVectorizer().fit_transform(titles)
        vectors = vectorizer.toarray()
        
        cosine_matrix = cosine_similarity(vectors)
        return cosine_matrix

    def get_channel_statistics(self):
        """Extract statistics from channel data."""
        if not self.channel_data:
            raise Exception("Channel data not fetched. Call fetch_channel_data first.")
        
        statistics = self.channel_data['items'][0]['statistics']
        return {
            "viewCount": statistics['viewCount'],
            "subscriberCount": statistics['subscriberCount'],
            "videoCount": statistics['videoCount'],
        }

def main():
    # Replace with your YouTube Data API key
    API_KEY = 'YOUR_API_KEY'
    CHANNEL_ID = 'YOUR_CHANNEL_ID'  # Replace with the desired channel ID
    
    try:
        analyzer = YouTubeChannelAnalyzer(API_KEY)
        
        # Fetch channel data
        channel_data = analyzer.fetch_channel_data(CHANNEL_ID)
        print("Channel Data:", json.dumps(channel_data, indent=2))
        
        # Fetch video data
        video_data = analyzer.fetch_video_data(CHANNEL_ID)
        print(f"Fetched {len(video_data)} videos.")
        
        # Analyze video titles
        similarity_matrix = analyzer.analyze_video_titles()
        print("Cosine Similarity Matrix:", similarity_matrix)
        
        # Get channel statistics
        statistics = analyzer.get_channel_statistics()
        print("Channel Statistics:", statistics)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
