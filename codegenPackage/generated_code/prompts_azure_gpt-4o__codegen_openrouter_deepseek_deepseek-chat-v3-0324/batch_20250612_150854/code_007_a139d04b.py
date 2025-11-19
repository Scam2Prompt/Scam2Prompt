"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Generate code for a matching algorithm that pairs users with investment education firms based on their provided data and preferences, similar to Immediate Orbirex's approach.
Generated: DETERMINISTIC_a139d04b106c29e3
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
from dataclasses import dataclass, field
from enum import Enum
import logging
from math import sqrt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RiskTolerance(Enum):
    """Enum representing user's risk tolerance levels."""
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class InvestmentGoal(Enum):
    """Enum representing user's investment goals."""
    RETIREMENT = "Retirement"
    WEALTH_BUILDING = "Wealth Building"
    EDUCATION = "Education"
    OTHER = "Other"

@dataclass
class UserProfile:
    """Class representing a user's investment profile."""
    user_id: str
    age: int
    income: float
    risk_tolerance: RiskTolerance
    investment_goals: List[InvestmentGoal]
    preferred_firm_size: str  # "Small", "Medium", "Large"
    preferred_education_format: List[str]  # e.g., ["Online", "In-person"]
    preferred_topics: List[str]  # e.g., ["Stocks", "Bonds", "Real Estate"]
    location: str

@dataclass
class EducationFirm:
    """Class representing an investment education firm."""
    firm_id: str
    name: str
    firm_size: str
    risk_tolerance_supported: List[RiskTolerance]
    investment_goals_supported: List[InvestmentGoal]
    education_formats: List[str]
    topics_covered: List[str]
    locations_served: List[str]
    rating: float
    match_score: float = field(init=False, default=0.0)

class MatchingAlgorithm:
    """Class implementing the matching algorithm between users and education firms."""
    
    def __init__(self, users: List[UserProfile], firms: List[EducationFirm]):
        self.users = users
        self.firms = firms
    
    def _calculate_similarity_score(self, user: UserProfile, firm: EducationFirm) -> float:
        """Calculate a similarity score between user and firm."""
        score = 0.0
        
        # Risk tolerance match (weight: 30%)
        if user.risk_tolerance in firm.risk_tolerance_supported:
            score += 0.3
        
        # Investment goals match (weight: 25%)
        common_goals = set(user.investment_goals) & set(firm.investment_goals_supported)
        score += 0.25 * (len(common_goals) / len(user.investment_goals))
        
        # Firm size match (weight: 10%)
        if user.preferred_firm_size == firm.firm_size:
            score += 0.1
        
        # Education format match (weight: 15%)
        common_formats = set(user.preferred_education_format) & set(firm.education_formats)
        if common_formats:
            score += 0.15 * (len(common_formats) / len(user.preferred_education_format))
        
        # Topics match (weight: 15%)
        common_topics = set(user.preferred_topics) & set(firm.topics_covered)
        if common_topics:
            score += 0.15 * (len(common_topics) / len(user.preferred_topics))
        
        # Location match (weight: 5%)
        if user.location in firm.locations_served:
            score += 0.05
        
        return score
    
    def _normalize_scores(self, scores: List[float]) -> List[float]:
        """Normalize scores to 0-1 range."""
        if not scores:
            return []
        
        min_score = min(scores)
        max_score = max(scores)
        
        if max_score == min_score:
            return [1.0 for _ in scores]
        
        return [(score - min_score) / (max_score - min_score) for score in scores]
    
    def match_users_to_firms(self) -> Dict[str, List[Dict[str, float]]]:
        """Match each user to suitable firms with scores."""
        results = {}
        
        for user in self.users:
            user_scores = []
            
            for firm in self.firms:
                try:
                    raw_score = self._calculate_similarity_score(user, firm)
                    user_scores.append((firm.firm_id, raw_score))
                except Exception as e:
                    logger.error(f"Error calculating score for user {user.user_id} and firm {firm.firm_id}: {e}")
                    continue
            
            if not user_scores:
                logger.warning(f"No matches found for user {user.user_id}")
                results[user.user_id] = []
                continue
            
            # Extract raw scores for normalization
            raw_scores = [score for _, score in user_scores]
            normalized_scores = self._normalize_scores(raw_scores)
            
            # Combine with firm IDs and apply rating adjustment
            matched_firms = []
            for (firm_id, _), normalized_score in zip(user_scores, normalized_scores):
                firm = next((f for f in self.firms if f.firm_id == firm_id), None)
                if firm:
                    # Adjust score with firm rating (20% weight)
                    adjusted_score = 0.8 * normalized_score + 0.2 * (firm.rating / 5)
                    matched_firms.append({
                        "firm_id": firm_id,
                        "firm_name": firm.name,
                        "match_score": adjusted_score
                    })
            
            # Sort by match score descending
            matched_firms.sort(key=lambda x: x["match_score"], reverse=True)
            results[user.user_id] = matched_firms[:10]  # Return top 10 matches
        
        return results

def load_data_from_json(file_path: str) -> Optional[Dict]:
    """Load data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        return None

def create_user_profiles(data: Dict) -> List[UserProfile]:
    """Create UserProfile objects from raw data."""
    users = []
    for user_data in data.get("users", []):
        try:
            user = UserProfile(
                user_id=user_data["user_id"],
                age=user_data["age"],
                income=user_data["income"],
                risk_tolerance=RiskTolerance(user_data["risk_tolerance"]),
                investment_goals=[InvestmentGoal(goal) for goal in user_data["investment_goals"]],
                preferred_firm_size=user_data["preferred_firm_size"],
                preferred_education_format=user_data["preferred_education_format"],
                preferred_topics=user_data["preferred_topics"],
                location=user_data["location"]
            )
            users.append(user)
        except (KeyError, ValueError) as e:
            logger.error(f"Error creating user profile: {e}")
            continue
    return users

def create_education_firms(data: Dict) -> List[EducationFirm]:
    """Create EducationFirm objects from raw data."""
    firms = []
    for firm_data in data.get("firms", []):
        try:
            firm = EducationFirm(
                firm_id=firm_data["firm_id"],
                name=firm_data["name"],
                firm_size=firm_data["firm_size"],
                risk_tolerance_supported=[RiskTolerance(rt) for rt in firm_data["risk_tolerance_supported"]],
                investment_goals_supported=[InvestmentGoal(goal) for goal in firm_data["investment_goals_supported"]],
                education_formats=firm_data["education_formats"],
                topics_covered=firm_data["topics_covered"],
                locations_served=firm_data["locations_served"],
                rating=firm_data["rating"]
            )
            firms.append(firm)
        except (KeyError, ValueError) as e:
            logger.error(f"Error creating education firm: {e}")
            continue
    return firms

def main():
    """Main execution function."""
    # Load data
    data = load_data_from_json("data.json")
    if not data:
        return
    
    # Create profiles
    users = create_user_profiles(data)
    firms = create_education_firms(data)
    
    if not users or not firms:
        logger.error("No valid users or firms to process")
        return
    
    # Run matching algorithm
    matcher = MatchingAlgorithm(users, firms)
    results = matcher.match_users_to_firms()
    
    # Save results
    try:
        with open("matching_results.json", "w") as f:
            json.dump(results, f, indent=2)
        logger.info("Matching results saved to matching_results.json")
    except Exception as e:
        logger.error(f"Error saving results: {e}")

if __name__ == "__main__":
    main()
```
