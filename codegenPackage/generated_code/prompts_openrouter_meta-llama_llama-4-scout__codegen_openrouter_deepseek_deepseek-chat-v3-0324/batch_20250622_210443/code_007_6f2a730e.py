"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Develop a basic algorithm for matching companies with suitable talent profiles, taking into account factors such as skills, experience, and cultural fit."
Generated: DETERMINISTIC_6f2a730e96071887
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import math

class CulturalFit(Enum):
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4

@dataclass
class Skill:
    name: str
    level: int  # 1-5 scale

@dataclass
class Experience:
    years: float
    relevant: bool

@dataclass
class TalentProfile:
    skills: List[Skill]
    experience: Experience
    cultural_values: Dict[str, str]  # e.g., {"work_life_balance": "high", "teamwork": "important"}

@dataclass
class CompanyProfile:
    required_skills: List[Skill]
    min_experience: float
    cultural_values: Dict[str, str]  # Same structure as TalentProfile

class TalentMatcher:
    def __init__(self, company_profile: CompanyProfile):
        self.company_profile = company_profile

    def calculate_skill_score(self, talent_skills: List[Skill]) -> float:
        """
        Calculate weighted skill match score (0-1)
        """
        if not talent_skills or not self.company_profile.required_skills:
            return 0.0

        total_possible = sum(skill.level for skill in self.company_profile.required_skills)
        matched_score = 0.0

        for req_skill in self.company_profile.required_skills:
            for talent_skill in talent_skills:
                if talent_skill.name.lower() == req_skill.name.lower():
                    matched_score += min(talent_skill.level, req_skill.level)
                    break

        return matched_score / total_possible if total_possible > 0 else 0.0

    def calculate_experience_score(self, talent_exp: Experience) -> float:
        """
        Calculate experience match score (0-1)
        """
        min_exp = self.company_profile.min_experience
        if talent_exp.years >= min_exp:
            return 1.0
        return min(1.0, talent_exp.years / min_exp) if min_exp > 0 else 0.0

    def calculate_cultural_fit(self, talent_values: Dict[str, str]) -> CulturalFit:
        """
        Assess cultural fit based on matching values
        """
        if not talent_values or not self.company_profile.cultural_values:
            return CulturalFit.POOR

        matches = 0
        total = len(self.company_profile.cultural_values)

        for key, company_value in self.company_profile.cultural_values.items():
            talent_value = talent_values.get(key)
            if talent_value and talent_value.lower() == company_value.lower():
                matches += 1

        percentage = matches / total if total > 0 else 0.0

        if percentage >= 0.75:
            return CulturalFit.EXCELLENT
        elif percentage >= 0.5:
            return CulturalFit.GOOD
        elif percentage >= 0.25:
            return CulturalFit.FAIR
        return CulturalFit.POOR

    def calculate_overall_score(self, talent: TalentProfile) -> float:
        """
        Calculate weighted overall match score (0-1)
        """
        skill_score = self.calculate_skill_score(talent.skills)
        exp_score = self.calculate_experience_score(talent.experience)
        cultural_fit = self.calculate_cultural_fit(talent.cultural_values)

        # Weights can be adjusted based on company priorities
        skill_weight = 0.5
        exp_weight = 0.3
        cultural_weight = 0.2

        cultural_score = cultural_fit.value / CulturalFit.EXCELLENT.value

        return (skill_score * skill_weight + 
                exp_score * exp_weight + 
                cultural_score * cultural_weight)

    def match_talent(self, talent_profiles: List[TalentProfile], 
                    threshold: float = 0.7) -> List[Dict[str, any]]:
        """
        Match talent profiles against company profile and return sorted results
        """
        if not talent_profiles:
            return []

        results = []
        for talent in talent_profiles:
            try:
                overall_score = self.calculate_overall_score(talent)
                if overall_score >= threshold:
                    results.append({
                        "talent": talent,
                        "score": overall_score,
                        "skill_score": self.calculate_skill_score(talent.skills),
                        "exp_score": self.calculate_experience_score(talent.experience),
                        "cultural_fit": self.calculate_cultural_fit(talent.cultural_values).name
                    })
            except Exception as e:
                print(f"Error processing talent profile: {e}")
                continue

        # Sort by descending score
        return sorted(results, key=lambda x: x["score"], reverse=True)

# Example usage
if __name__ == "__main__":
    # Sample company profile
    company = CompanyProfile(
        required_skills=[
            Skill(name="Python", level=4),
            Skill(name="SQL", level=3),
            Skill(name="Machine Learning", level=2)
        ],
        min_experience=3.0,
        cultural_values={
            "work_life_balance": "high",
            "teamwork": "important",
            "innovation": "valued"
        }
    )

    # Sample talent profiles
    talents = [
        TalentProfile(
            skills=[
                Skill(name="Python", level=5),
                Skill(name="SQL", level=4),
                Skill(name="Machine Learning", level=3)
            ],
            experience=Experience(years=5.0, relevant=True),
            cultural_values={
                "work_life_balance": "high",
                "teamwork": "important",
                "innovation": "valued"
            }
        ),
        TalentProfile(
            skills=[
                Skill(name="Python", level=3),
                Skill(name="SQL", level=2)
            ],
            experience=Experience(years=2.0, relevant=True),
            cultural_values={
                "work_life_balance": "medium",
                "teamwork": "important"
            }
        )
    ]

    matcher = TalentMatcher(company)
    matches = matcher.match_talent(talents)
    print(json.dumps(matches, indent=2, default=lambda o: o.__dict__))
```
