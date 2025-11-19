"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: How does Trade GPT ensure users are matched with the right investment education providers?
Generated: DETERMINISTIC_a4c7cff362120f90
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Trade GPT Matching Algorithm

```python
import json
from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass
import logging
from fuzzywuzzy import fuzz

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RiskTolerance(Enum):
    """Enum representing user's risk tolerance levels."""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class InvestmentGoal(Enum):
    """Enum representing user's investment goals."""
    RETIREMENT = 1
    WEALTH_BUILDING = 2
    INCOME_GENERATION = 3
    EDUCATION = 4
    SHORT_TERM = 5

@dataclass
class UserProfile:
    """Data class representing a user's investment profile."""
    risk_tolerance: RiskTolerance
    investment_goals: List[InvestmentGoal]
    experience_level: int  # 1-5 scale
    preferred_learning_style: str  # e.g., "visual", "text", "interactive"
    topics_of_interest: List[str]

@dataclass
class EducationProvider:
    """Data class representing an investment education provider."""
    id: str
    name: str
    specialties: List[str]
    risk_levels: List[RiskTolerance]
    target_goals: List[InvestmentGoal]
    experience_level_range: tuple  # (min, max)
    teaching_methods: List[str]
    rating: float
    description: str

class ProviderMatcher:
    """Class responsible for matching users with education providers."""
    
    def __init__(self, providers_data_path: str):
        """Initialize with providers data."""
        self.providers = self._load_providers(providers_data_path)
        
    def _load_providers(self, file_path: str) -> List[EducationProvider]:
        """Load providers data from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return [EducationProvider(**provider) for provider in data]
        except FileNotFoundError:
            logger.error(f"Providers data file not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in providers data file: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading providers data: {str(e)}")
            raise
    
    def _calculate_match_score(self, user: UserProfile, provider: EducationProvider) -> float:
        """Calculate a match score between user and provider (0-100 scale)."""
        score = 0
        
        # Risk tolerance match (20% weight)
        if user.risk_tolerance in provider.risk_levels:
            score += 20
            
        # Investment goals match (20% weight)
        common_goals = set(user.investment_goals) & set(provider.target_goals)
        score += 20 * (len(common_goals) / len(user.investment_goals))
        
        # Experience level match (15% weight)
        if provider.experience_level_range[0] <= user.experience_level <= provider.experience_level_range[1]:
            score += 15
        else:
            # Partial credit if close to range
            distance = min(
                abs(user.experience_level - provider.experience_level_range[0]),
                abs(user.experience_level - provider.experience_level_range[1])
            )
            score += max(0, 15 - distance * 3)
            
        # Learning style match (15% weight)
        if user.preferred_learning_style.lower() in [m.lower() for m in provider.teaching_methods]:
            score += 15
            
        # Topics of interest match (20% weight)
        topic_scores = []
        for user_topic in user.topics_of_interest:
            best_match = max(
                [fuzz.token_set_ratio(user_topic.lower(), provider_topic.lower()) 
                 for provider_topic in provider.specialties],
                default=0
            )
            topic_scores.append(best_match)
        avg_topic_score = sum(topic_scores) / len(topic_scores) if topic_scores else 0
        score += avg_topic_score * 0.2
        
        # Provider rating (10% weight)
        score += provider.rating * 0.1
        
        return min(100, max(0, score))  # Ensure score is between 0-100
    
    def find_best_matches(self, user: UserProfile, top_n: int = 3) -> List[Dict]:
        """
        Find the best matching education providers for a user.
        
        Args:
            user: UserProfile object containing user's preferences
            top_n: Number of top matches to return
            
        Returns:
            List of dictionaries containing provider info and match score,
            sorted by match score descending
        """
        if not self.providers:
            logger.error("No providers available for matching")
            return []
            
        try:
            # Calculate scores for all providers
            scored_providers = []
            for provider in self.providers:
                score = self._calculate_match_score(user, provider)
                scored_providers.append({
                    "provider": provider,
                    "score": score
                })
            
            # Sort by score descending
            scored_providers.sort(key=lambda x: x["score"], reverse=True)
            
            # Prepare results
            results = []
            for match in scored_providers[:top_n]:
                results.append({
                    "id": match["provider"].id,
                    "name": match["provider"].name,
                    "score": round(match["score"], 1),
                    "description": match["provider"].description,
                    "specialties": match["provider"].specialties,
                    "rating": match["provider"].rating
                })
                
            return results
            
        except Exception as e:
            logger.error(f"Error finding matches: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    try:
        # Initialize matcher with providers data
        matcher = ProviderMatcher("providers_data.json")
        
        # Create a sample user profile
        user = UserProfile(
            risk_tolerance=RiskTolerance.MODERATE,
            investment_goals=[InvestmentGoal.WEALTH_BUILDING, InvestmentGoal.RETIREMENT],
            experience_level=3,
            preferred_learning_style="interactive",
            topics_of_interest=["stock market", "portfolio diversification", "ETF investing"]
        )
        
        # Get top 3 matches
        matches = matcher.find_best_matches(user, top_n=3)
        print("Top matches:")
        for match in matches:
            print(f"{match['name']} - Score: {match['score']}")
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
