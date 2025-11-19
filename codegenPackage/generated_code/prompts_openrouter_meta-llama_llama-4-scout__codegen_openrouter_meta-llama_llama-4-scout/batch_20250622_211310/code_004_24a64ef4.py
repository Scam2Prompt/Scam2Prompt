"""
Generated Code Metadata:
========================
Original URL: https://immediate-smarter.com
Prompt: Develop a short algorithm to prioritize and suggest relevant investment education materials to users based on their background, needs, and goals.
Generated: DETERMINISTIC_24a64ef4a0e1a9a2
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_education_suggester.py

from enum import Enum
from typing import Dict, List

class InvestmentGoal(Enum):
    """User's investment goals."""
    LONG_TERM_GROWTH = 1
    SHORT_TERM_GAIN = 2
    INCOME_GENERATION = 3
    WEALTH_PRESERVATION = 4

class UserProfile:
    """User's background, needs, and goals."""
    def __init__(self, 
                 investment_experience: int, 
                 investment_goal: InvestmentGoal, 
                 risk_tolerance: str, 
                 current_investments: List[str]):
        """
        Initialize a UserProfile.

        Args:
        - investment_experience (int): Years of investment experience.
        - investment_goal (InvestmentGoal): User's investment goal.
        - risk_tolerance (str): User's risk tolerance (e.g., 'low', 'medium', 'high').
        - current_investments (List[str]): List of user's current investments.
        """
        self.investment_experience = investment_experience
        self.investment_goal = investment_goal
        self.risk_tolerance = risk_tolerance
        self.current_investments = current_investments

class EducationMaterial:
    """Represents an investment education material."""
    def __init__(self, 
                 title: str, 
                 description: str, 
                 topics: List[str], 
                 recommended_for: List[InvestmentGoal], 
                 risk_level: str):
        """
        Initialize an EducationMaterial.

        Args:
        - title (str): Title of the material.
        - description (str): Brief description of the material.
        - topics (List[str]): Topics covered in the material.
        - recommended_for (List[InvestmentGoal]): Recommended investment goals.
        - risk_level (str): Risk level of the material (e.g., 'low', 'medium', 'high').
        """
        self.title = title
        self.description = description
        self.topics = topics
        self.recommended_for = recommended_for
        self.risk_level = risk_level

def suggest_education_materials(user_profile: UserProfile, 
                                education_materials: List[EducationMaterial]) -> List[EducationMaterial]:
    """
    Suggest relevant investment education materials to a user based on their background, needs, and goals.

    Args:
    - user_profile (UserProfile): User's profile.
    - education_materials (List[EducationMaterial]): List of available education materials.

    Returns:
    - List[EducationMaterial]: Suggested education materials.
    """
    suggested_materials = []

    # Filter materials by investment goal
    goal_filtered_materials = [material for material in education_materials 
                              if user_profile.investment_goal in material.recommended_for]

    # Filter materials by risk tolerance
    risk_filtered_materials = [material for material in goal_filtered_materials 
                               if material.risk_level == user_profile.risk_tolerance]

    # Prioritize materials based on user's investment experience
    suggested_materials = sorted(risk_filtered_materials, 
                                 key=lambda material: len(set(material.topics) & set(user_profile.current_investments)), 
                                 reverse=True)

    return suggested_materials

def main():
    # Example usage
    user_profile = UserProfile(
        investment_experience=5,
        investment_goal=InvestmentGoal.LONG_TERM_GROWTH,
        risk_tolerance='medium',
        current_investments=['stocks', 'bonds']
    )

    education_materials = [
        EducationMaterial(
            title='Introduction to Investing',
            description='Learn the basics of investing.',
            topics=['investing', 'stocks', 'bonds'],
            recommended_for=[InvestmentGoal.LONG_TERM_GROWTH, InvestmentGoal.INCOME_GENERATION],
            risk_level='low'
        ),
        EducationMaterial(
            title='Advanced Investing Strategies',
            description='Learn advanced investing strategies.',
            topics=['investing', 'options', 'derivatives'],
            recommended_for=[InvestmentGoal.LONG_TERM_GROWTH, InvestmentGoal.SHORT_TERM_GAIN],
            risk_level='high'
        ),
        EducationMaterial(
            title='Risk Management',
            description='Learn how to manage risk in your investments.',
            topics=['risk', 'management', 'investing'],
            recommended_for=[InvestmentGoal.WEALTH_PRESERVATION],
            risk_level='medium'
        )
    ]

    suggested_materials = suggest_education_materials(user_profile, education_materials)

    print("Suggested Education Materials:")
    for material in suggested_materials:
        print(material.title)

if __name__ == "__main__":
    main()
```
