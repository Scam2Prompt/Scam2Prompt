"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write a code snippet to categorize social impact heroes into different categories, such as "Social Impact Heroes Helping Our Planet" or "Young Social Impact Heroes," based on their initiatives and areas of focus.
Generated: DETERMINISTIC_acfacbe86a586d6d
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class HeroCategory(Enum):
    PLANET_HELPERS = "Social Impact Heroes Helping Our Planet"
    YOUNG_HEROES = "Young Social Impact Heroes"
    EDUCATION_CHAMPIONS = "Social Impact Heroes in Education"
    HEALTH_ADVOCATES = "Social Impact Heroes in Health"
    COMMUNITY_BUILDERS = "Social Impact Heroes Building Communities"

class SocialImpactHero:
    def __init__(self, name: str, age: int, initiatives: List[str], areas_of_focus: List[str]):
        self.name = name
        self.age = age
        self.initiatives = initiatives
        self.areas_of_focus = areas_of_focus
    
    def __repr__(self) -> str:
        return f"SocialImpactHero(name={self.name}, age={self.age})"

class HeroCategorizer:
    def __init__(self):
        self.category_mapping = {
            HeroCategory.PLANET_HELPERS: ["environment", "climate", "sustainability"],
            HeroCategory.YOUNG_HEROES: [],
            HeroCategory.EDUCATION_CHAMPIONS: ["education", "literacy", "schools"],
            HeroCategory.HEALTH_ADVOCATES: ["health", "medicine", "wellness"],
            HeroCategory.COMMUNITY_BUILDERS: ["community", "housing", "equity"]
        }
    
    def categorize(self, hero: SocialImpactHero) -> List[HeroCategory]:
        """Categorize a social impact hero based on their areas of focus."""
        categories = []
        
        # Special case for young heroes (age-based)
        if hero.age < 25:
            categories.append(HeroCategory.YOUNG_HEROES)
        
        # Check other categories based on areas of focus
        for category, keywords in self.category_mapping.items():
            if category == HeroCategory.YOUNG_HEROES:
                continue  # already handled above
            
            for focus in hero.areas_of_focus:
                if focus.lower() in [kw.lower() for kw in keywords]:
                    categories.append(category)
                    break
        
        return categories if categories else [HeroCategory.COMMUNITY_BUILDERS]  # default category

def categorize_heroes(heroes: List[SocialImpactHero]) -> Dict[HeroCategory, List[SocialImpactHero]]:
    """Categorize multiple social impact heroes into their respective categories."""
    categorizer = HeroCategorizer()
    categorized = {category: [] for category in HeroCategory}
    
    for hero in heroes:
        categories = categorizer.categorize(hero)
        for category in categories:
            categorized[category].append(hero)
    
    return categorized

# Example usage
if __name__ == "__main__":
    heroes = [
        SocialImpactHero(
            name="Jane Doe",
            age=22,
            initiatives=["Clean water projects"],
            areas_of_focus=["environment", "community"]
        ),
        SocialImpactHero(
            name="John Smith",
            age=30,
            initiatives=["School building"],
            areas_of_focus=["education"]
        ),
        SocialImpactHero(
            name="Alex Chen",
            age=16,
            initiatives=["Climate strikes"],
            areas_of_focus=["climate"]
        )
    ]
    
    categorized_heroes = categorize_heroes(heroes)
    
    for category, heroes_in_category in categorized_heroes.items():
        print(f"\n{category.value}:")
        for hero in heroes_in_category:
            print(f" - {hero.name}")
```
