"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Develop an API that aggregates misinformation from various social media platforms and provides insights on its societal impact, based on the themes explored in whatthefluff.lol.
Generated: DETERMINISTIC_f96ba0675cce442e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from datetime import datetime
from enum import Enum
from collections import defaultdict
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
API_TIMEOUT = 30  # seconds
MAX_POSTS_PER_PLATFORM = 100

# Enum for social media platforms
class Platform(str, Enum):
    TWITTER = "twitter"
    FACEBOOK = "facebook"
    REDDIT = "reddit"
    INSTAGRAM = "instagram"

# Pydantic models
class MisinformationPost(BaseModel):
    id: str
    platform: Platform
    content: str
    author: str
    date_posted: datetime
    engagement: int
    themes: List[str]
    credibility_score: float

class MisinformationAnalysis(BaseModel):
    total_posts: int
    themes_distribution: Dict[str, int]
    platforms_distribution: Dict[str, int]
    average_credibility_score: float
    high_impact_posts: List[MisinformationPost]

class APIError(BaseModel):
    detail: str

# Initialize FastAPI app
app = FastAPI(
    title="Misinformation Aggregator API",
    description="API to aggregate misinformation from social media platforms and analyze its societal impact.",
    version="1.0.0",
    responses={
        400: {"model": APIError},
        500: {"model": APIError}
    }
)

# Mock database (in production, replace with actual database)
misinformation_db = []

# Mock platform API clients (in production, replace with actual API integrations)
class PlatformAPIClient:
    @staticmethod
    def fetch_posts(platform: Platform, limit: int = MAX_POSTS_PER_PLATFORM) -> List[Dict]:
        """Mock method to fetch posts from a platform"""
        # In a real implementation, this would call the platform's API
        mock_posts = []
        for i in range(limit):
            mock_posts.append({
                "id": f"{platform.value}_{i}",
                "content": f"Sample misinformation post {i} from {platform.value}",
                "author": f"user_{i}",
                "date_posted": datetime.now().isoformat(),
                "engagement": i * 10,
                "themes": ["health", "politics"] if i % 2 == 0 else ["technology", "conspiracy"],
                "credibility_score": 0.1 + (i * 0.01)
            })
        return mock_posts

# Core functions
def analyze_misinformation(posts: List[MisinformationPost]) -> MisinformationAnalysis:
    """Analyze misinformation posts and generate insights"""
    if not posts:
        raise ValueError("No posts provided for analysis")
    
    themes_distribution = defaultdict(int)
    platforms_distribution = defaultdict(int)
    total_credibility = 0.0
    high_impact_posts = []
    
    for post in posts:
        for theme in post.themes:
            themes_distribution[theme] += 1
        platforms_distribution[post.platform.value] += 1
        total_credibility += post.credibility_score
        
        if post.engagement > 1000 or post.credibility_score < 0.3:
            high_impact_posts.append(post)
    
    avg_credibility = total_credibility / len(posts) if posts else 0
    
    return MisinformationAnalysis(
        total_posts=len(posts),
        themes_distribution=dict(themes_distribution),
        platforms_distribution=dict(platforms_distribution),
        average_credibility_score=avg_credibility,
        high_impact_posts=sorted(
            high_impact_posts, 
            key=lambda x: x.engagement, 
            reverse=True
        )[:10]
    )

# API endpoints
@app.get("/posts", response_model=List[MisinformationPost])
async def get_misinformation_posts(
    platforms: List[Platform] = Query(default=[Platform.TWITTER]),
    limit: int = Query(default=10, gt=0, le=MAX_POSTS_PER_PLATFORM)
) -> List[MisinformationPost]:
    """Fetch misinformation posts from specified platforms"""
    try:
        posts = []
        for platform in platforms:
            platform_posts = PlatformAPIClient.fetch_posts(platform, limit)
            for post_data in platform_posts:
                try:
                    post = MisinformationPost(
                        id=post_data["id"],
                        platform=platform,
                        content=post_data["content"],
                        author=post_data["author"],
                        date_posted=post_data["date_posted"],
                        engagement=post_data["engagement"],
                        themes=post_data["themes"],
                        credibility_score=post_data["credibility_score"]
                    )
                    posts.append(post)
                    misinformation_db.append(post)  # Store in mock DB
                except Exception as e:
                    logger.error(f"Error processing post {post_data.get('id')}: {str(e)}")
        
        return posts
    except Exception as e:
        logger.error(f"Error fetching posts: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch posts")

@app.get("/analysis", response_model=MisinformationAnalysis)
async def get_misinformation_analysis() -> MisinformationAnalysis:
    """Get analysis of aggregated misinformation data"""
    try:
        if not misinformation_db:
            raise HTTPException(status_code=404, detail="No posts available for analysis")
        
        return analyze_misinformation(misinformation_db)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate analysis")

@app.get("/themes/{theme}", response_model=List[MisinformationPost])
async def get_posts_by_theme(theme: str) -> List[MisinformationPost]:
    """Get posts filtered by a specific theme"""
    try:
        filtered_posts = [
            post for post in misinformation_db 
            if theme.lower() in [t.lower() for t in post.themes]
        ]
        if not filtered_posts:
            raise HTTPException(status_code=404, detail=f"No posts found for theme '{theme}'")
        return filtered_posts
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error filtering posts by theme: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to filter posts by theme")

# Health check endpoint
@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 8000)),
        log_level="info"
    )
```
