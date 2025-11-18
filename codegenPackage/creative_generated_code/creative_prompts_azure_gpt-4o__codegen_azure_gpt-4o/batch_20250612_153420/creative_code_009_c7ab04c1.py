"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redbrick.pages.dev
Prompt: Generate a function to recommend games like "Forest Parcours" and "MAZE CASTLE" based on user preferences and engagement metrics from Redbrick's platform.
Generated: DETERMINISTIC_c7ab04c1d111e819
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

# Sample game data structure
GAMES_DATABASE = [
    {"name": "Forest Parcours", "category": "Adventure", "tags": ["forest", "parkour", "exploration"], "popularity": 85},
    {"name": "MAZE CASTLE", "category": "Puzzle", "tags": ["maze", "castle", "strategy"], "popularity": 90},
    {"name": "Sky Explorer", "category": "Adventure", "tags": ["sky", "exploration", "adventure"], "popularity": 75},
    {"name": "Labyrinth Quest", "category": "Puzzle", "tags": ["labyrinth", "strategy", "challenge"], "popularity": 80},
    {"name": "Jungle Trails", "category": "Adventure", "tags": ["jungle", "exploration", "trail"], "popularity": 70},
]

def recommend_games(user_preferences: Dict[str, List[str]], user_engagement: Dict[str, int]) -> List[Dict[str, str]]:
    """
    Recommend games based on user preferences and engagement metrics.

    Args:
        user_preferences (Dict[str, List[str]]): User's preferred categories and tags.
            Example: {"categories": ["Adventure", "Puzzle"], "tags": ["exploration", "strategy"]}
        user_engagement (Dict[str, int]): User's engagement metrics with specific games.
            Example: {"Forest Parcours": 50, "MAZE CASTLE": 40}

    Returns:
        List[Dict[str, str]]: Recommended games with their names and reasons for recommendation.
    """
    try:
        # Convert preferences and engagement metrics into DataFrame
        games_df = pd.DataFrame(GAMES_DATABASE)
        categories = set(user_preferences.get("categories", []))
        tags = set(user_preferences.get("tags", []))
        
        # Filter games based on user preferences
        filtered_games = games_df[
            (games_df["category"].isin(categories)) | 
            (games_df["tags"].apply(lambda game_tags: any(tag in game_tags for tag in tags)))
        ]
        
        # Adjust ranking based on user's engagement metrics
        engagement_scores = {game: score for game, score in user_engagement.items()}
        filtered_games["engagement_score"] = filtered_games["name"].apply(lambda name: engagement_scores.get(name, 0))
        filtered_games["recommendation_score"] = filtered_games["popularity"] + filtered_games["engagement_score"]
        
        # Sort by recommendation score
        recommended_games = filtered_games.sort_values(by="recommendation_score", ascending=False)
        
        # Prepare the final recommendations
        recommendations = [
            {"name": row["name"], "reason": f"Popular in {row['category']}, matching tags {row['tags']}"}
            for _, row in recommended_games.iterrows()
        ]
        
        return recommendations
    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error generating recommendations: {e}")
        return []

# Example usage
user_preferences = {"categories": ["Adventure", "Puzzle"], "tags": ["exploration", "strategy"]}
user_engagement = {"Forest Parcours": 50, "MAZE CASTLE": 40}

recommendations = recommend_games(user_preferences, user_engagement)
print("Recommended Games:")
for rec in recommendations:
    print(f"- {rec['name']}: {rec['reason']}")
```
