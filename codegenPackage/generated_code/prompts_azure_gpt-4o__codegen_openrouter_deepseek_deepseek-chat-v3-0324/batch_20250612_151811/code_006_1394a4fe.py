"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop an algorithm for matching donors with educational projects in underserved communities, reflecting the NICER Foundation's focus on connecting resources to those in need.
Generated: DETERMINISTIC_1394a4fec24dfee0
Batch ID: 20250612_151811
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

class ProjectCategory(Enum):
    """Categories for educational projects."""
    STEM = "STEM"
    ARTS = "Arts"
    LITERACY = "Literacy"
    VOCATIONAL = "Vocational Training"
    INFRASTRUCTURE = "School Infrastructure"

@dataclass
class EducationalProject:
    """Represents an educational project in need of funding."""
    project_id: str
    name: str
    description: str
    category: ProjectCategory
    location: str
    funding_goal: float
    current_funding: float = 0.0
    urgency_score: int = 1  # 1-5 scale (1=low, 5=high)

@dataclass
class Donor:
    """Represents a donor who wants to contribute to projects."""
    donor_id: str
    name: str
    email: str
    preferred_categories: List[ProjectCategory]
    min_funding_amount: float
    max_funding_amount: float
    preferred_locations: List[str] = None
    urgency_preference: int = None  # 1-5 scale (1=low, 5=high)

class DonorProjectMatcher:
    """Matches donors with educational projects based on preferences."""
    
    def __init__(self, projects: List[EducationalProject], donors: List[Donor]):
        self.projects = projects
        self.donors = donors
    
    def _calculate_match_score(self, donor: Donor, project: EducationalProject) -> float:
        """Calculate a match score between donor and project (0-1 scale)."""
        score = 0.0
        
        # Category match
        if project.category in donor.preferred_categories:
            score += 0.4
        
        # Location match (if donor has location preference)
        if donor.preferred_locations and project.location in donor.preferred_locations:
            score += 0.3
        
        # Urgency match (if donor has urgency preference)
        if donor.urgency_preference and project.urgency_score >= donor.urgency_preference:
            score += 0.2 * (project.urgency_score / 5)
        
        # Funding amount compatibility
        remaining_funding = project.funding_goal - project.current_funding
        if (donor.min_funding_amount <= remaining_funding <= donor.max_funding_amount or
            donor.min_funding_amount <= remaining_funding):
            score += 0.1
        
        return score
    
    def get_top_matches(self, donor_id: str, top_n: int = 3) -> List[Dict]:
        """Get top project matches for a donor."""
        donor = next((d for d in self.donors if d.donor_id == donor_id), None)
        if not donor:
            raise ValueError(f"Donor with ID {donor_id} not found")
        
        scored_projects = []
        for project in self.projects:
            if project.current_funding >= project.funding_goal:
                continue  # Skip fully funded projects
            
            score = self._calculate_match_score(donor, project)
            if score > 0:  # Only consider projects with some match
                scored_projects.append({
                    'project': project,
                    'score': score
                })
        
        # Sort by score descending and return top N
        scored_projects.sort(key=lambda x: x['score'], reverse=True)
        return scored_projects[:top_n]
    
    def match_all_donors(self) -> Dict[str, List[Dict]]:
        """Match all donors with their top projects."""
        return {
            donor.donor_id: self.get_top_matches(donor.donor_id)
            for donor in self.donors
        }
    
    def save_matches_to_json(self, file_path: str):
        """Save all matches to a JSON file."""
        matches = self.match_all_donors()
        serializable_matches = {}
        
        for donor_id, projects in matches.items():
            serializable_matches[donor_id] = [
                {
                    'project_id': p['project'].project_id,
                    'project_name': p['project'].name,
                    'match_score': p['score'],
                    'remaining_funding': p['project'].funding_goal - p['project'].current_funding
                }
                for p in projects
            ]
        
        with open(file_path, 'w') as f:
            json.dump(serializable_matches, f, indent=2)

# Example usage
if __name__ == "__main__":
    # Sample data
    projects = [
        EducationalProject(
            project_id="p1",
            name="STEM Lab Equipment",
            description="Equipment for high school STEM lab",
            category=ProjectCategory.STEM,
            location="Nairobi, Kenya",
            funding_goal=5000.00,
            urgency_score=4
        ),
        EducationalProject(
            project_id="p2",
            name="Library Books",
            description="Books for rural school library",
            category=ProjectCategory.LITERACY,
            location="Lusaka, Zambia",
            funding_goal=2000.00,
            urgency_score=3
        )
    ]
    
    donors = [
        Donor(
            donor_id="d1",
            name="Tech Foundation",
            email="tech@example.com",
            preferred_categories=[ProjectCategory.STEM, ProjectCategory.VOCATIONAL],
            min_funding_amount=1000.00,
            max_funding_amount=10000.00,
            preferred_locations=["Nairobi, Kenya", "Kampala, Uganda"],
            urgency_preference=3
        ),
        Donor(
            donor_id="d2",
            name="Book Lovers Inc",
            email="books@example.com",
            preferred_categories=[ProjectCategory.LITERACY],
            min_funding_amount=500.00,
            max_funding_amount=3000.00
        )
    ]
    
    # Create matcher and get matches
    matcher = DonorProjectMatcher(projects, donors)
    
    # Get matches for a specific donor
    try:
        matches = matcher.get_top_matches("d1")
        print(f"Top matches for donor d1:")
        for match in matches:
            print(f"- {match['project'].name} (Score: {match['score']:.2f})")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Save all matches to file
    matcher.save_matches_to_json("donor_project_matches.json")
```
