"""
Generated Code Metadata:
========================
Original URL: https://cocfinance.com
Prompt: Generate a code snippet that interacts with an API to analyze trends in social media, specifically focusing on TikTok's impact on dietary culture as discussed in the article about "Skinnytok."
Generated: DETERMINISTIC_ae102ee19dbae846
Batch ID: 20250612_155859
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tiktok.com/v2/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TikTokTrendAnalyzer:
    """
    A class to analyze TikTok trends related to dietary culture using the TikTok API.
    Focuses on extracting and analyzing data about 'Skinnytok' and similar trends.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the TikTokTrendAnalyzer with an API key.
        
        Args:
            api_key (str): The API key for accessing the TikTok API.
        """
        self.api_key = api_key
        self.base_url = "https://api.tiktok.com/v2/"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a request to the TikTok API.
        
        Args:
            endpoint (str): The API endpoint to call.
            params (Optional[Dict]): Query parameters for the request.
            
        Returns:
            Dict: The JSON response from the API.
            
        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params or {}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
    
    def get_trending_hashtags(self, limit: int = 10) -> List[Dict]:
        """
        Get trending hashtags related to dietary culture.
        
        Args:
            limit (int): Maximum number of hashtags to retrieve.
            
        Returns:
            List[Dict]: List of trending hashtags with their metadata.
        """
        params = {
            "category": "diet",
            "limit": limit
        }
        return self._make_api_request("hashtags/trending", params).get("data", [])
    
    def get_videos_by_hashtag(self, hashtag: str, days: int = 7) -> List[Dict]:
        """
        Get videos for a specific hashtag within a time range.
        
        Args:
            hashtag (str): The hashtag to search for (e.g., 'Skinnytok').
            days (int): Number of days to look back for videos.
            
        Returns:
            List[Dict]: List of videos with their metadata.
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        params = {
            "hashtag": hashtag,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "limit": 100  # Max allowed by API
        }
        return self._make_api_request("videos/search", params).get("data", [])
    
    def analyze_diet_trends(self, hashtags: List[str] = None) -> pd.DataFrame:
        """
        Analyze dietary trends by aggregating video data for given hashtags.
        
        Args:
            hashtags (List[str]): List of hashtags to analyze. Defaults to ['Skinnytok'].
            
        Returns:
            pd.DataFrame: DataFrame with aggregated trend data.
        """
        if hashtags is None:
            hashtags = ["Skinnytok"]
        
        trend_data = []
        for hashtag in hashtags:
            videos = self.get_videos_by_hashtag(hashtag)
            if not videos:
                continue
            
            # Aggregate metrics
            total_likes = sum(video.get("like_count", 0) for video in videos)
            total_comments = sum(video.get("comment_count", 0) for video in videos)
            total_shares = sum(video.get("share_count", 0) for video in videos)
            
            trend_data.append({
                "hashtag": hashtag,
                "video_count": len(videos),
                "total_likes": total_likes,
                "total_comments": total_comments,
                "total_shares": total_shares,
                "avg_likes": total_likes / len(videos) if videos else 0,
                "avg_comments": total_comments / len(videos) if videos else 0,
                "avg_shares": total_shares / len(videos) if videos else 0
            })
        
        return pd.DataFrame(trend_data)

# Example usage
if __name__ == "__main__":
    api_key = "your_tiktok_api_key_here"  # Replace with actual API key
    analyzer = TikTokTrendAnalyzer(api_key)
    
    try:
        # Get trending dietary hashtags
        trending_hashtags = analyzer.get_trending_hashtags()
        print("Trending Dietary Hashtags:", trending_hashtags)
        
        # Analyze specific hashtags
        df = analyzer.analyze_diet_trends(["Skinnytok", "DietCulture"])
        print("\nDiet Trend Analysis:")
        print(df.to_string(index=False))
        
    except Exception as e:
        print(f"Error occurred: {e}")
```
