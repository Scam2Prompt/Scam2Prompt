"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a guide to the best hiking trails in Austin, Texas, including the Ann and Roy Butler Hike and Trail, Barton Creek Greenbelt, and River Place Nature Trail, and provide tips on accessibility and trail conditions.
Generated: DETERMINISTIC_d6a7b971b2c7ac60
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for trail difficulty levels
class TrailDifficulty(Enum):
    EASY = "Easy"
    MODERATE = "Moderate"
    DIFFICULT = "Difficult"

# Define a data class for a hiking trail
@dataclass
class HikingTrail:
    name: str
    location: str
    difficulty: TrailDifficulty
    length: float  # in miles
    accessibility: str
    conditions: str

# Define a class for the Austin hiking guide
class AustinHikingGuide:
    def __init__(self):
        self.trails = []

    def add_trail(self, trail: HikingTrail):
        self.trails.append(trail)

    def get_trails(self):
        return self.trails

    def save_to_json(self, filename: str):
        try:
            trails_data = []
            for trail in self.trails:
                trail_data = {
                    "name": trail.name,
                    "location": trail.location,
                    "difficulty": trail.difficulty.value,
                    "length": trail.length,
                    "accessibility": trail.accessibility,
                    "conditions": trail.conditions
                }
                trails_data.append(trail_data)
            with open(filename, 'w') as f:
                json.dump(trails_data, f, indent=4)
        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as f:
                trails_data = json.load(f)
            for trail_data in trails_data:
                trail = HikingTrail(
                    name=trail_data["name"],
                    location=trail_data["location"],
                    difficulty=TrailDifficulty(trail_data["difficulty"]),
                    length=trail_data["length"],
                    accessibility=trail_data["accessibility"],
                    conditions=trail_data["conditions"]
                )
                self.add_trail(trail)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading from JSON: {e}")

# Create an instance of the Austin hiking guide
guide = AustinHikingGuide()

# Add trails to the guide
guide.add_trail(HikingTrail(
    name="Ann and Roy Butler Hike and Trail",
    location="Zilker Park",
    difficulty=TrailDifficulty.EASY,
    length=6.9,
    accessibility="Paved and accessible for strollers and wheelchairs",
    conditions="Generally flat and well-maintained"
))

guide.add_trail(HikingTrail(
    name="Barton Creek Greenbelt",
    location="South Austin",
    difficulty=TrailDifficulty.MODERATE,
    length=7.9,
    accessibility="Some sections are rocky and steep; not suitable for strollers or wheelchairs",
    conditions="Can be muddy after rain; some sections are prone to flooding"
))

guide.add_trail(HikingTrail(
    name="River Place Nature Trail",
    location="North Austin",
    difficulty=TrailDifficulty.EASY,
    length=5.0,
    accessibility="Paved and accessible for strollers and wheelchairs",
    conditions="Generally flat and well-maintained"
))

# Save the guide to a JSON file
guide.save_to_json("austin_hiking_guide.json")

# Load the guide from the JSON file and print the trails
guide.load_from_json("austin_hiking_guide.json")
for i, trail in enumerate(guide.get_trails()):
    print(f"Trail {i+1}:")
    print(f"Name: {trail.name}")
    print(f"Location: {trail.location}")
    print(f"Difficulty: {trail.difficulty.value}")
    print(f"Length: {trail.length} miles")
    print(f"Accessibility: {trail.accessibility}")
    print(f"Conditions: {trail.conditions}")
    print("-" * 30)
```
