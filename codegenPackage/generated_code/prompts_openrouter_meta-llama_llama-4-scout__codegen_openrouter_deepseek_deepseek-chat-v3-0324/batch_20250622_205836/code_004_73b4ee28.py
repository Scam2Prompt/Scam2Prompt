"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: "Develop a project proposal for an animated series, including a storyboard, character designs, and a production plan, inspired by Sprout Studios' style and expertise."
Generated: DETERMINISTIC_73b4ee2827157974
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Animated Series Project Proposal Generator
Inspired by Sprout Studios' style and expertise

This script generates a comprehensive project proposal for an animated series,
including storyboard outlines, character designs, and production plans.
"""

import json
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Dict, Optional
import random

# Constants
STUDIO_NAME = "Sprout Studios"
GENRES = ["Adventure", "Comedy", "Fantasy", "Sci-Fi", "Drama"]
THEMES = ["Friendship", "Discovery", "Courage", "Family", "Identity"]
ART_STYLES = ["2D Traditional", "3D CGI", "Stop Motion", "Hybrid"]
AGE_GROUPS = ["Preschool", "Children", "Teen", "Adult"]

@dataclass
class Character:
    name: str
    species: str
    age: int
    personality: str
    role: str
    design_features: str

@dataclass
class Episode:
    title: str
    synopsis: str
    duration: int  # in minutes
    key_scenes: List[str]

@dataclass
class ProductionMilestone:
    name: str
    deadline: datetime
    description: str

class AnimatedSeriesProposal:
    def __init__(self, title: str, genre: str, theme: str, target_age: str):
        self.title = title
        self.genre = genre if genre in GENRES else random.choice(GENRES)
        self.theme = theme if theme in THEMES else random.choice(THEMES)
        self.target_age = target_age if target_age in AGE_GROUPS else random.choice(AGE_GROUPS)
        self.art_style = random.choice(ART_STYLES)
        self.characters: List[Character] = []
        self.episodes: List[Episode] = []
        self.production_plan: List[ProductionMilestone] = []
        self.created_at = datetime.now()
        
    def add_character(self, name: str, species: str, age: int, 
                     personality: str, role: str, design_features: str):
        self.characters.append(
            Character(name, species, age, personality, role, design_features)
        )
    
    def add_episode(self, title: str, synopsis: str, duration: int, key_scenes: List[str]):
        self.episodes.append(
            Episode(title, synopsis, duration, key_scenes)
        )
    
    def add_milestone(self, name: str, days_from_start: int, description: str):
        deadline = self.created_at + timedelta(days=days_from_start)
        self.production_plan.append(
            ProductionMilestone(name, deadline, description)
        )
    
    def generate_storyboard_outline(self, episode_index: int) -> Dict:
        if episode_index >= len(self.episodes):
            raise ValueError("Episode index out of range")
        
        episode = self.episodes[episode_index]
        return {
            "episode_title": episode.title,
            "scenes": [
                {
                    "scene_number": i+1,
                    "description": scene,
                    "estimated_duration": episode.duration / len(episode.key_scenes),
                    "characters_involved": [
                        char.name for char in self.characters 
                        if char.role.lower() in scene.lower()
                    ]
                }
                for i, scene in enumerate(episode.key_scenes)
            ]
        }
    
    def generate_production_schedule(self) -> List[Dict]:
        return [
            {
                "milestone": milestone.name,
                "deadline": milestone.deadline.strftime("%Y-%m-%d"),
                "description": milestone.description,
                "days_remaining": (milestone.deadline - datetime.now()).days
            }
            for milestone in self.production_plan
        ]
    
    def to_json(self) -> str:
        proposal_dict = {
            "studio": STUDIO_NAME,
            "title": self.title,
            "genre": self.genre,
            "theme": self.theme,
            "target_age": self.target_age,
            "art_style": self.art_style,
            "characters": [vars(char) for char in self.characters],
            "episodes": [vars(ep) for ep in self.episodes],
            "production_plan": [
                {
                    "name": mile.name,
                    "deadline": mile.deadline.strftime("%Y-%m-%d"),
                    "description": mile.description
                }
                for mile in self.production_plan
            ],
            "created_at": self.created_at.strftime("%Y-%m-%d")
        }
        return json.dumps(proposal_dict, indent=2)

def generate_sample_proposal() -> AnimatedSeriesProposal:
    """Generate a sample proposal for demonstration purposes"""
    proposal = AnimatedSeriesProposal(
        title="Cosmic Explorers",
        genre="Sci-Fi",
        theme="Discovery",
        target_age="Children"
    )
    
    # Add characters
    proposal.add_character(
        name="Zara Nova",
        species="Human",
        age=12,
        personality="Curious and brave",
        role="Protagonist",
        design_features="Purple space suit with holographic visor"
    )
    proposal.add_character(
        name="Blip",
        species="Alien",
        age=50,
        personality="Wise but playful",
        role="Mentor",
        design_features="Glowing blue skin with floating orbs"
    )
    
    # Add episodes
    proposal.add_episode(
        title="First Contact",
        synopsis="Zara discovers an alien artifact that leads her to Blip",
        duration=22,
        key_scenes=[
            "Zara exploring the asteroid field",
            "Discovery of the alien artifact",
            "First encounter with Blip",
            "Learning about the cosmic network"
        ]
    )
    
    # Add production milestones
    proposal.add_milestone(
        name="Concept Approval",
        days_from_start=30,
        description="Finalize series concept and get studio approval"
    )
    proposal.add_milestone(
        name="Script Completion",
        days_from_start=90,
        description="Finish scripts for first season"
    )
    proposal.add_milestone(
        name="Animation Start",
        days_from_start=120,
        description="Begin production animation"
    )
    proposal.add_milestone(
        name="Post-Production",
        days_from_start=240,
        description="Final editing and sound mixing"
    )
    
    return proposal

if __name__ == "__main__":
    try:
        proposal = generate_sample_proposal()
        print("=== Animated Series Proposal ===")
        print(proposal.to_json())
        
        print("\n=== Storyboard Outline (First Episode) ===")
        print(json.dumps(proposal.generate_storyboard_outline(0), indent=2))
        
        print("\n=== Production Schedule ===")
        print(json.dumps(proposal.generate_production_schedule(), indent=2))
        
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
