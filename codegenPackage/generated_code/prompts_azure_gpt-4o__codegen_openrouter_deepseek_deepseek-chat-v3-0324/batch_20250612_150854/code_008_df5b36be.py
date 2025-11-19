"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Generate an algorithm to rank investment education firms based on user preferences, budget constraints, and multilingual support, similar to Juros Xyro's matching system.
Generated: DETERMINISTIC_df5b36bee4411928
Batch ID: 20250612_150854
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
from enum import Enum

class Language(Enum):
    """Supported languages for education firms."""
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    PORTUGUESE = "pt"
    CHINESE = "zh"
    JAPANESE = "ja"

class EducationFirm:
    """Represents an investment education firm with relevant attributes."""
    
    def __init__(
        self,
        name: str,
        languages: List[Language],
        min_budget: float,
        max_budget: float,
        rating: float,
        specialties: List[str],
        user_reviews: List[Dict[str, float]]
    ):
        self.name = name
        self.languages = languages
        self.min_budget = min_budget
        self.max_budget = max_budget
        self.rating = rating
        self.specialties = specialties
        self.user_reviews = user_reviews

class UserPreferences:
    """Represents user preferences for matching with education firms."""
    
    def __init__(
        self,
        preferred_languages: List[Language],
        budget: float,
        desired_specialties: List[str],
        min_rating: float = 3.0,
        review_threshold: int = 10
    ):
        self.preferred_languages = preferred_languages
        self.budget = budget
        self.desired_specialties = desired_specialties
        self.min_rating = min_rating
        self.review_threshold = review_threshold

class FirmRanker:
    """Ranks education firms based on user preferences."""
    
    def __init__(self, firms: List[EducationFirm]):
        self.firms = firms
    
    def _filter_by_budget(self, user_prefs: UserPreferences) -> List[EducationFirm]:
        """Filter firms based on user's budget constraints."""
        return [
            firm for firm in self.firms
            if firm.min_budget <= user_prefs.budget <= firm.max_budget
        ]
    
    def _filter_by_language(self, firms: List[EducationFirm], user_prefs: UserPreferences) -> List[EducationFirm]:
        """Filter firms based on user's preferred languages."""
        return [
            firm for firm in firms
            if any(lang in firm.languages for lang in user_prefs.preferred_languages)
        ]
    
    def _filter_by_rating(self, firms: List[EducationFirm], user_prefs: UserPreferences) -> List[EducationFirm]:
        """Filter firms based on minimum rating."""
        return [firm for firm in firms if firm.rating >= user_prefs.min_rating]
    
    def _filter_by_reviews(self, firms: List[EducationFirm], user_prefs: UserPreferences) -> List[EducationFirm]:
        """Filter firms based on minimum number of reviews."""
        return [
            firm for firm in firms
            if len(firm.user_reviews) >= user_prefs.review_threshold
        ]
    
    def _filter_by_specialties(self, firms: List[EducationFirm], user_prefs: UserPreferences) -> List[EducationFirm]:
        """Filter firms based on desired specialties."""
        if not user_prefs.desired_specialties:
            return firms
        return [
            firm for firm in firms
            if any(specialty in firm.specialties for specialty in user_prefs.desired_specialties)
        ]
    
    def _calculate_match_score(self, firm: EducationFirm, user_prefs: UserPreferences) -> float:
        """Calculate a match score for a firm based on user preferences."""
        # Base score is the firm's rating (normalized to 0-1)
        score = firm.rating / 5.0
        
        # Bonus for matching languages
        matched_languages = len(set(firm.languages) & set(user_prefs.preferred_languages))
        score += 0.1 * matched_languages
        
        # Bonus for matching specialties
        if user_prefs.desired_specialties:
            matched_specialties = len(set(firm.specialties) & set(user_prefs.desired_specialties))
            score += 0.15 * matched_specialties
        
        # Penalty for budget deviation (closer to user's budget is better)
        budget_midpoint = (firm.min_budget + firm.max_budget) / 2
        budget_deviation = abs(budget_midpoint - user_prefs.budget) / user_prefs.budget
        score -= 0.1 * budget_deviation
        
        # Ensure score is within bounds
        return max(0.0, min(1.0, score))
    
    def rank_firms(self, user_prefs: UserPreferences) -> List[Dict[str, Optional[float]]]:
        """Rank firms based on user preferences."""
        # Apply all filters
        filtered_firms = self._filter_by_budget(user_prefs)
        filtered_firms = self._filter_by_language(filtered_firms, user_prefs)
        filtered_firms = self._filter_by_rating(filtered_firms, user_prefs)
        filtered_firms = self._filter_by_reviews(filtered_firms, user_prefs)
        filtered_firms = self._filter_by_specialties(filtered_firms, user_prefs)
        
        # Calculate scores and sort
        scored_firms = [
            {
                "firm": firm,
                "score": self._calculate_match_score(firm, user_prefs)
            }
            for firm in filtered_firms
        ]
        
        # Sort by score descending
        scored_firms.sort(key=lambda x: x["score"], reverse=True)
        
        return scored_firms

def load_firms_from_json(file_path: str) -> List[EducationFirm]:
    """Load education firms from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            firms = []
            for item in data:
                languages = [Language(lang) for lang in item["languages"]]
                firms.append(EducationFirm(
                    name=item["name"],
                    languages=languages,
                    min_budget=item["min_budget"],
                    max_budget=item["max_budget"],
                    rating=item["rating"],
                    specialties=item["specialties"],
                    user_reviews=item["user_reviews"]
                ))
            return firms
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in file: {file_path}")
    except KeyError as e:
        raise ValueError(f"Missing required field in JSON: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Load firms from JSON (in a real app, this would be from a database)
        firms = load_firms_from_json("education_firms.json")
        
        # Create ranker
        ranker = FirmRanker(firms)
        
        # Define user preferences
        user_prefs = UserPreferences(
            preferred_languages=[Language.ENGLISH, Language.SPANISH],
            budget=5000.0,
            desired_specialties=["Stocks", "ETFs"],
            min_rating=4.0,
            review_threshold=5
        )
        
        # Get ranked firms
        ranked_firms = ranker.rank_firms(user_prefs)
        
        # Display results
        print("Ranked Education Firms:")
        for idx, firm_data in enumerate(ranked_firms, 1):
            print(f"{idx}. {firm_data['firm'].name} - Score: {firm_data['score']:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
