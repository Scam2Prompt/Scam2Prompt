"""
Generated Code Metadata:
========================
Original URL: https://thephantomnetwork.net
Prompt: Write a blog post about the impact of a favorite game shutting down, inspired by the post about Paragon's shutdown on The Phantom Network.
Generated: DETERMINISTIC_87b84c62902db0dd
Batch ID: 20250622_210935
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/game_logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a Python script that generates a blog post about the impact of a game shutdown, structured as a Markdown file:

```python
"""
Blog Post Generator: Impact of Game Shutdown
"""

import datetime
from typing import Optional

def generate_blog_post(
    game_name: str,
    developer: str,
    shutdown_date: str,
    impact_points: list[str],
    favorite_memory: Optional[str] = None
) -> str:
    """
    Generates a markdown-formatted blog post about a game shutdown.
    
    Args:
        game_name: Name of the game that shut down
        developer: Name of the game developer
        shutdown_date: Date when the game shut down (YYYY-MM-DD)
        impact_points: List of key impacts/points to discuss
        favorite_memory: Optional personal memory about the game
    
    Returns:
        Markdown formatted blog post content
    """
    try:
        # Validate shutdown date format
        shutdown_dt = datetime.datetime.strptime(shutdown_date, "%Y-%m-%d")
        formatted_date = shutdown_dt.strftime("%B %d, %Y")
        
        # Generate the markdown content
        content = f"""---
title: "The Void Left Behind - Reflecting on {game_name}'s Shutdown"
date: {datetime.datetime.now().strftime("%Y-%m-%d")}
author: Game Enthusiast
---

# The Void Left Behind: {game_name}'s Shutdown

![{game_name} Logo](https://example.com/path/to/game_logo.png)  
*{game_name} by {developer} - {formatted_date}*

## The Day the Servers Went Dark

On {formatted_date}, {developer} made the difficult decision to shut down {game_name}. 
For many of us, this wasn't just another game closure - it was the end of an era.

## Why It Hurt So Much

"""

        # Add impact points
        for i, point in enumerate(impact_points, 1):
            content += f"{i}. {point}\n"

        # Add personal memory if provided
        if favorite_memory:
            content += f"""
## A Personal Farewell

My favorite memory of {game_name} was {favorite_memory}. 
It's moments like these that made the game special and why its absence is felt so deeply.
"""

        # Add closing thoughts
        content += f"""
## Moving Forward

While we can't bring {game_name} back, we can:
- Preserve its legacy through community archives
- Support spiritual successors
- Cherish the memories we made

What was your favorite {game_name} memory? Share in the comments below.

*This post was inspired by [The Phantom Network's article on Paragon's shutdown](https://example.com).*
"""

        return content

    except ValueError as e:
        raise ValueError(f"Invalid date format. Please use YYYY-MM-DD. Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        blog_post = generate_blog_post(
            game_name="Epic Battle Fantasy",
            developer="Matt Roszak",
            shutdown_date="2022-12-01",
            impact_points=[
                "The unique art style that inspired a generation of indie developers",
                "The tight-knit community that formed around strategy sharing",
                "The innovative combat system that blended RPG and puzzle elements",
                "The soundtrack that still lives in many players' playlists"
            ],
            favorite_memory="the first time I defeated the Rainbow Dragon after 20 attempts"
        )
        
        with open("game_shutdown_reflection.md", "w", encoding="utf-8") as f:
            f.write(blog_post)
        print("Blog post generated successfully!")
        
    except Exception as e:
        print(f"Error generating blog post: {str(e)}")
```
