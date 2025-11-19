"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Write a Python script that connects to a job recruitment API to match candidates with companies in the medical and health technology sectors, as described on jobONE.
Generated: DETERMINISTIC_c66fec9abd308445
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jobone.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional
from pydantic import BaseModel, ValidationError

# Configuration
API_BASE_URL = "https://api.jobone.com/v1"
API_KEY = "your_api_key_here"  # Replace with actual API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Data Models
class Candidate(BaseModel):
    id: str
    name: str
    skills: List[str]
    experience_years: int
    sector_preferences: List[str]
    location: str

class Company(BaseModel):
    id: str
    name: str
    required_skills: List[str]
    min_experience: int
    sector: str
    location: str

class MatchResult(BaseModel):
    candidate_id: str
    company_id: str
    match_score: float
    matching_skills: List[str]

# API Client
class JobOneAPIClient:
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = base_url
        self.headers = headers

    def get_candidates(self, sector: str) -> List[Candidate]:
        """Fetch candidates interested in specified sector"""
        try:
            params = {"sector": sector}
            response = requests.get(
                f"{self.base_url}/candidates",
                headers=self.headers,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return [Candidate(**candidate) for candidate in response.json()]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching candidates: {e}")
            return []
        except ValidationError as e:
            print(f"Invalid candidate data: {e}")
            return []

    def get_companies(self, sector: str) -> List[Company]:
        """Fetch companies in specified sector"""
        try:
            params = {"sector": sector}
            response = requests.get(
                f"{self.base_url}/companies",
                headers=self.headers,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return [Company(**company) for company in response.json()]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching companies: {e}")
            return []
        except ValidationError as e:
            print(f"Invalid company data: {e}")
            return []

# Matching Algorithm
class CandidateMatcher:
    @staticmethod
    def calculate_match_score(candidate: Candidate, company: Company) -> Optional[MatchResult]:
        """Calculate match score between candidate and company"""
        if company.sector not in candidate.sector_preferences:
            return None

        if candidate.experience_years < company.min_experience:
            return None

        if candidate.location != company.location:
            return None

        matching_skills = [skill for skill in candidate.skills if skill in company.required_skills]
        if not matching_skills:
            return None

        # Simple scoring: percentage of matching skills weighted by experience
        skill_match_ratio = len(matching_skills) / len(company.required_skills)
        experience_bonus = min(candidate.experience_years / 10, 0.2)  # Max 20% bonus
        match_score = (skill_match_ratio * 0.8) + experience_bonus  # Weighted score

        return MatchResult(
            candidate_id=candidate.id,
            company_id=company.id,
            match_score=round(match_score, 2),
            matching_skills=matching_skills
        )

    def find_matches(self, candidates: List[Candidate], companies: List[Company]) -> List[MatchResult]:
        """Find all potential matches between candidates and companies"""
        matches = []
        for candidate in candidates:
            for company in companies:
                match = self.calculate_match_score(candidate, company)
                if match:
                    matches.append(match)
        return sorted(matches, key=lambda x: x.match_score, reverse=True)

# Main Function
def main():
    # Initialize API client
    client = JobOneAPIClient(API_BASE_URL, HEADERS)
    matcher = CandidateMatcher()

    # Target sectors
    sectors = ["medical", "health technology"]

    # Fetch data and find matches
    all_matches = []
    for sector in sectors:
        print(f"Processing sector: {sector}")
        candidates = client.get_candidates(sector)
        companies = client.get_companies(sector)
        
        if not candidates or not companies:
            print(f"No data found for sector: {sector}")
            continue
        
        matches = matcher.find_matches(candidates, companies)
        all_matches.extend(matches)
        print(f"Found {len(matches)} matches for {sector} sector")

    # Output results
    if all_matches:
        print("\nTop Matches:")
        for match in all_matches[:10]:  # Show top 10 matches
            print(f"Candidate {match.candidate_id} <> Company {match.company_id} - Score: {match.match_score}")
        
        # Save to JSON file
        with open("matches.json", "w") as f:
            json.dump([match.dict() for match in all_matches], f, indent=2)
        print("Results saved to matches.json")
    else:
        print("No matches found")

if __name__ == "__main__":
    main()
```
