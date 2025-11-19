"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Design a system to manage industrial academia linkages and provide a code snippet to automate the process of matching industry partners with research projects.
Generated: DETERMINISTIC_a8f29e9c345119c2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_academia_linkages.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class IndustryType(str, Enum):
    """Industry type enumeration"""
    TECHNOLOGY = "technology"
    HEALTHCARE = "healthcare"
    FINANCE = "finance"
    OTHER = "other"

@dataclass
class IndustryPartner:
    """Industry partner data class"""
    id: int
    name: str
    industry_type: IndustryType
    areas_of_interest: List[str]

@dataclass
class ResearchProject:
    """Research project data class"""
    id: int
    title: str
    description: str
    required_skills: List[str]

class LinkageManager:
    """Industrial academia linkage manager class"""

    def __init__(self):
        self.industry_partners: Dict[int, IndustryPartner] = {}
        self.research_projects: Dict[int, ResearchProject] = {}
        self.linkages: Dict[int, Dict[int, str]] = {}

    def add_industry_partner(self, partner: IndustryPartner):
        """Add an industry partner"""
        self.industry_partners[partner.id] = partner

    def add_research_project(self, project: ResearchProject):
        """Add a research project"""
        self.research_projects[project.id] = project

    def create_linkage(self, partner_id: int, project_id: int, match_reason: str):
        """Create a linkage between an industry partner and a research project"""
        if partner_id not in self.industry_partners:
            raise ValueError("Industry partner not found")
        if project_id not in self.research_projects:
            raise ValueError("Research project not found")

        if partner_id not in self.linkages:
            self.linkages[partner_id] = {}
        
        self.linkages[partner_id][project_id] = match_reason

    def get_linkages(self, partner_id: int = None, project_id: int = None):
        """Get linkages"""
        if partner_id:
            return self.linkages.get(partner_id, {})
        elif project_id:
            linkages = {}
            for partner_id, projects in self.linkages.items():
                if project_id in projects:
                    linkages[partner_id] = projects[project_id]
            return linkages
        else:
            return self.linkages

    def automate_matching(self):
        """Automate matching of industry partners with research projects"""
        matches = {}
        for partner in self.industry_partners.values():
            best_match = None
            best_match_score = 0
            for project in self.research_projects.values():
                match_score = self.calculate_match_score(partner, project)
                if match_score > best_match_score:
                    best_match = project
                    best_match_score = match_score
            if best_match:
                matches[partner.id] = (best_match.id, best_match_score)
        return matches

    @staticmethod
    def calculate_match_score(partner: IndustryPartner, project: ResearchProject):
        """Calculate match score between an industry partner and a research project"""
        score = 0
        for area in partner.areas_of_interest:
            if area in project.required_skills:
                score += 1
        return score

def main():
    # Example usage
    manager = LinkageManager()

    # Create industry partners
    partner1 = IndustryPartner(1, "Partner 1", IndustryType.TECHNOLOGY, ["AI", "ML", "Data Science"])
    partner2 = IndustryPartner(2, "Partner 2", IndustryType.HEALTHCARE, ["Medical Imaging", "Healthcare IT"])

    # Create research projects
    project1 = ResearchProject(1, "Project 1", "AI for Healthcare", ["AI", "ML", "Medical Imaging"])
    project2 = ResearchProject(2, "Project 2", "Data Science for Finance", ["Data Science", "Finance"])

    # Add industry partners and research projects
    manager.add_industry_partner(partner1)
    manager.add_industry_partner(partner2)
    manager.add_research_project(project1)
    manager.add_research_project(project2)

    # Automate matching
    matches = manager.automate_matching()
    print("Automated Matches:")
    for partner_id, (project_id, score) in matches.items():
        print(f"Partner {partner_id} -> Project {project_id} (Score: {score})")

    # Create linkages
    manager.create_linkage(partner1.id, project1.id, "Matched on AI and ML")
    manager.create_linkage(partner2.id, project2.id, "Matched on Data Science and Finance")

    # Get linkages
    print("\nLinkages:")
    for partner_id, projects in manager.get_linkages().items():
        print(f"Partner {partner_id}:")
        for project_id, reason in projects.items():
            print(f"  -> Project {project_id} ({reason})")

if __name__ == "__main__":
    main()
```
