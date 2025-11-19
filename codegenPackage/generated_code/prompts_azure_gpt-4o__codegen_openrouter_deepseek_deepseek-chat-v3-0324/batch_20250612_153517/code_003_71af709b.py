"""
Generated Code Metadata:
========================
Original URL: https://tidhholding.com
Prompt: Write a program that matches investors with foreign partners and projects, inspired by TIDH Holding's service of connecting investors for international business ventures.
Generated: DETERMINISTIC_71af709b66a1609d
Batch ID: 20250612_153517
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
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
from datetime import datetime

class ProjectCategory(Enum):
    REAL_ESTATE = "Real Estate"
    TECHNOLOGY = "Technology"
    MANUFACTURING = "Manufacturing"
    AGRICULTURE = "Agriculture"
    ENERGY = "Energy"
    INFRASTRUCTURE = "Infrastructure"
    OTHER = "Other"

class InvestorType(Enum):
    INDIVIDUAL = "Individual"
    VENTURE_CAPITAL = "Venture Capital"
    PRIVATE_EQUITY = "Private Equity"
    CORPORATE = "Corporate"
    GOVERNMENT = "Government"

@dataclass
class Investor:
    id: str
    name: str
    type: InvestorType
    preferred_categories: List[ProjectCategory]
    investment_range_min: float
    investment_range_max: float
    preferred_countries: List[str]
    contact_email: str
    date_registered: str

@dataclass
class Project:
    id: str
    name: str
    category: ProjectCategory
    description: str
    country: str
    funding_required: float
    contact_email: str
    date_posted: str

@dataclass
class MatchResult:
    investor: Investor
    project: Project
    match_score: float
    match_reasons: List[str]

class InvestorProjectMatcher:
    def __init__(self):
        self.investors: Dict[str, Investor] = {}
        self.projects: Dict[str, Project] = {}

    def register_investor(self, name: str, investor_type: InvestorType, 
                         preferred_categories: List[ProjectCategory],
                         investment_range_min: float, investment_range_max: float,
                         preferred_countries: List[str], contact_email: str) -> Investor:
        """Register a new investor in the system."""
        if investment_range_min > investment_range_max:
            raise ValueError("Minimum investment cannot be greater than maximum investment")
        
        investor_id = str(uuid.uuid4())
        investor = Investor(
            id=investor_id,
            name=name,
            type=investor_type,
            preferred_categories=preferred_categories,
            investment_range_min=investment_range_min,
            investment_range_max=investment_range_max,
            preferred_countries=preferred_countries,
            contact_email=contact_email,
            date_registered=datetime.now().isoformat()
        )
        self.investors[investor_id] = investor
        return investor

    def post_project(self, name: str, category: ProjectCategory, description: str,
                     country: str, funding_required: float, contact_email: str) -> Project:
        """Post a new project to the system."""
        if funding_required <= 0:
            raise ValueError("Funding required must be positive")
        
        project_id = str(uuid.uuid4())
        project = Project(
            id=project_id,
            name=name,
            category=category,
            description=description,
            country=country,
            funding_required=funding_required,
            contact_email=contact_email,
            date_posted=datetime.now().isoformat()
        )
        self.projects[project_id] = project
        return project

    def find_matches_for_investor(self, investor_id: str) -> List[MatchResult]:
        """Find matching projects for a specific investor."""
        if investor_id not in self.investors:
            raise ValueError("Investor not found")
        
        investor = self.investors[investor_id]
        matches = []
        
        for project in self.projects.values():
            match_score = 0.0
            match_reasons = []
            
            # Category match
            if project.category in investor.preferred_categories:
                match_score += 0.4
                match_reasons.append(f"Matching category: {project.category.value}")
            
            # Country match
            if project.country in investor.preferred_countries:
                match_score += 0.3
                match_reasons.append(f"Matching country: {project.country}")
            
            # Funding match
            if (investor.investment_range_min <= project.funding_required <= 
                investor.investment_range_max):
                match_score += 0.3
                match_reasons.append("Funding requirement within investor's range")
            
            if match_score > 0:
                matches.append(MatchResult(
                    investor=investor,
                    project=project,
                    match_score=match_score,
                    match_reasons=match_reasons
                ))
        
        # Sort by match score descending
        matches.sort(key=lambda x: x.match_score, reverse=True)
        return matches

    def find_matches_for_project(self, project_id: str) -> List[MatchResult]:
        """Find matching investors for a specific project."""
        if project_id not in self.projects:
            raise ValueError("Project not found")
        
        project = self.projects[project_id]
        matches = []
        
        for investor in self.investors.values():
            match_score = 0.0
            match_reasons = []
            
            # Category match
            if project.category in investor.preferred_categories:
                match_score += 0.4
                match_reasons.append(f"Matching category: {project.category.value}")
            
            # Country match
            if project.country in investor.preferred_countries:
                match_score += 0.3
                match_reasons.append(f"Matching country: {project.country}")
            
            # Funding match
            if (investor.investment_range_min <= project.funding_required <= 
                investor.investment_range_max):
                match_score += 0.3
                match_reasons.append("Funding requirement within investor's range")
            
            if match_score > 0:
                matches.append(MatchResult(
                    investor=investor,
                    project=project,
                    match_score=match_score,
                    match_reasons=match_reasons
                ))
        
        # Sort by match score descending
        matches.sort(key=lambda x: x.match_score, reverse=True)
        return matches

    def save_to_file(self, filename: str):
        """Save all investors and projects to a JSON file."""
        data = {
            "investors": [asdict(inv) for inv in self.investors.values()],
            "projects": [asdict(proj) for proj in self.projects.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str):
        """Load investors and projects from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.investors.clear()
        self.projects.clear()
        
        for inv_data in data["investors"]:
            inv_data["type"] = InvestorType(inv_data["type"])
            inv_data["preferred_categories"] = [ProjectCategory(cat) for cat in inv_data["preferred_categories"]]
            investor = Investor(**inv_data)
            self.investors[investor.id] = investor
        
        for proj_data in data["projects"]:
            proj_data["category"] = ProjectCategory(proj_data["category"])
            project = Project(**proj_data)
            self.projects[project.id] = project

# Example usage
if __name__ == "__main__":
    matcher = InvestorProjectMatcher()
    
    # Register some investors
    investor1 = matcher.register_investor(
        name="Global Ventures",
        investor_type=InvestorType.VENTURE_CAPITAL,
        preferred_categories=[ProjectCategory.TECHNOLOGY, ProjectCategory.ENERGY],
        investment_range_min=1000000,
        investment_range_max=5000000,
        preferred_countries=["USA", "Germany", "Japan"],
        contact_email="contact@globalventures.com"
    )
    
    investor2 = matcher.register_investor(
        name="Emerging Markets Fund",
        investor_type=InvestorType.PRIVATE_EQUITY,
        preferred_categories=[ProjectCategory.INFRASTRUCTURE, ProjectCategory.MANUFACTURING],
        investment_range_min=5000000,
        investment_range_max=20000000,
        preferred_countries=["India", "Brazil", "South Africa"],
        contact_email="info@emfund.com"
    )
    
    # Post some projects
    project1 = matcher.post_project(
        name="Solar Farm in Germany",
        category=ProjectCategory.ENERGY,
        description="Large-scale solar energy farm in northern Germany",
        country="Germany",
        funding_required=3000000,
        contact_email="solar@germany.com"
    )
    
    project2 = matcher.post_project(
        name="Smart City Infrastructure in India",
        category=ProjectCategory.INFRASTRUCTURE,
        description="Developing smart city infrastructure in Bangalore",
        country="India",
        funding_required=10000000,
        contact_email="smartcity@india.com"
    )
    
    # Find matches
    print("Matches for Global Ventures:")
    matches = matcher.find_matches_for_investor(investor1.id)
    for match in matches:
        print(f"Project: {match.project.name}, Score: {match.match_score:.2f}")
        print
