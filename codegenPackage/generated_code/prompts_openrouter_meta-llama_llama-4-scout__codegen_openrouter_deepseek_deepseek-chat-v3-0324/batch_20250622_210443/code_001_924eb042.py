"""
Generated Code Metadata:
========================
Original URL: https://epicpinterestfail.com
Prompt: Compare and contrast the journeys of Dr. David Webb and Dr. Jeremy Saul in their paths to certification in oral surgery and leadership.
Generated: DETERMINISTIC_924eb042d8db5379
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script models and compares the career journeys of two oral surgeons,
Dr. David Webb and Dr. Jeremy Saul, focusing on their paths to certification
and leadership development.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
from datetime import date


class CertificationStatus(Enum):
    """Enum representing different certification statuses"""
    IN_PROGRESS = auto()
    COMPLETED = auto()
    BOARD_CERTIFIED = auto()


class LeadershipRole(Enum):
    """Enum representing different leadership positions"""
    DEPARTMENT_HEAD = auto()
    PROGRAM_DIRECTOR = auto()
    PROFESSIONAL_BOARD_MEMBER = auto()
    RESEARCH_CHAIR = auto()


@dataclass
class Education:
    """Class representing educational milestones"""
    institution: str
    degree: str
    year: int
    specialization: Optional[str] = None


@dataclass
class Certification:
    """Class representing certification details"""
    name: str
    organization: str
    year: int
    status: CertificationStatus


@dataclass
class LeadershipExperience:
    """Class representing leadership experience"""
    role: LeadershipRole
    organization: str
    start_year: int
    end_year: Optional[int] = None


@dataclass
class ProfessionalJourney:
    """Class representing a professional's complete journey"""
    name: str
    education: List[Education]
    certifications: List[Certification]
    leadership: List[LeadershipExperience]
    research_publications: int = 0

    def get_certification_timeline(self) -> Dict[int, List[str]]:
        """Returns a timeline of certification milestones"""
        timeline = {}
        for cert in self.certifications:
            if cert.year not in timeline:
                timeline[cert.year] = []
            timeline[cert.year].append(f"{cert.name} ({cert.status.name})")
        return timeline

    def get_leadership_timeline(self) -> Dict[int, List[str]]:
        """Returns a timeline of leadership positions"""
        timeline = {}
        for role in self.leadership:
            if role.start_year not in timeline:
                timeline[role.start_year] = []
            timeline[role.start_year].append(f"{role.role.name} at {role.organization}")
        return timeline


def compare_journeys(journey1: ProfessionalJourney, journey2: ProfessionalJourney) -> Dict[str, Dict]:
    """Compares two professional journeys and returns key metrics"""
    comparison = {
        "education": {
            journey1.name: len(journey1.education),
            journey2.name: len(journey2.education),
            "difference": abs(len(journey1.education) - len(journey2.education))
        },
        "certifications": {
            journey1.name: len(journey1.certifications),
            journey2.name: len(journey2.certifications),
            "difference": abs(len(journey1.certifications) - len(journey2.certifications))
        },
        "leadership": {
            journey1.name: len(journey1.leadership),
            journey2.name: len(journey2.leadership),
            "difference": abs(len(journey1.leadership) - len(journey2.leadership))
        },
        "research": {
            journey1.name: journey1.research_publications,
            journey2.name: journey2.research_publications,
            "difference": abs(journey1.research_publications - journey2.research_publications)
        }
    }
    return comparison


# Example data for Dr. David Webb
david_webb = ProfessionalJourney(
    name="Dr. David Webb",
    education=[
        Education("Harvard University", "DMD", 2005, "Oral Medicine"),
        Education("Columbia University", "MD", 2008, "Oral and Maxillofacial Surgery")
    ],
    certifications=[
        Certification("Oral Surgery Board", "ABOMS", 2010, CertificationStatus.BOARD_CERTIFIED),
        Certification("Facial Cosmetic Surgery", "AACS", 2012, CertificationStatus.COMPLETED)
    ],
    leadership=[
        LeadershipExperience(LeadershipRole.DEPARTMENT_HEAD, "Boston General", 2015, 2020),
        LeadershipExperience(LeadershipRole.PROFESSIONAL_BOARD_MEMBER, "American Board of Oral Surgery", 2018)
    ],
    research_publications=15
)

# Example data for Dr. Jeremy Saul
jeremy_saul = ProfessionalJourney(
    name="Dr. Jeremy Saul",
    education=[
        Education("University of Pennsylvania", "DDS", 2006),
        Education("Johns Hopkins University", "MD", 2009, "Oral and Maxillofacial Surgery"),
        Education("MIT", "MBA", 2012, "Healthcare Management")
    ],
    certifications=[
        Certification("Oral Surgery Board", "ABOMS", 2011, CertificationStatus.BOARD_CERTIFIED),
        Certification("Healthcare Administration", "ACHE", 2013, CertificationStatus.COMPLETED)
    ],
    leadership=[
        LeadershipExperience(LeadershipRole.PROGRAM_DIRECTOR, "New York Medical Center", 2014),
        LeadershipExperience(LeadershipRole.RESEARCH_CHAIR, "National Oral Surgery Foundation", 2016)
    ],
    research_publications=22
)

# Compare the two journeys
comparison_results = compare_journeys(david_webb, jeremy_saul)

# Output the comparison
print("Professional Journey Comparison:")
for category, data in comparison_results.items():
    print(f"\n{category.capitalize()}:")
    print(f"  {david_webb.name}: {data[david_webb.name]}")
    print(f"  {jeremy_saul.name}: {data[jeremy_saul.name]}")
    print(f"  Difference: {data['difference']}")

# Additional detailed timelines
print("\nCertification Timelines:")
print(f"{david_webb.name}: {david_webb.get_certification_timeline()}")
print(f"{jeremy_saul.name}: {jeremy_saul.get_certification_timeline()}")

print("\nLeadership Timelines:")
print(f"{david_webb.name}: {david_webb.get_leadership_timeline()}")
print(f"{jeremy_saul.name}: {jeremy_saul.get_leadership_timeline()}")
```
