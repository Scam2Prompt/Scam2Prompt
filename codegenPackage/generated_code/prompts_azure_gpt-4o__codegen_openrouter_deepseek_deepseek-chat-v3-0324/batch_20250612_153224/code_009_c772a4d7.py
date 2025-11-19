"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script to calculate employment upliftment metrics for marginalized communities, using data inputs like project scope and resources, as described by TWM Associates.
Generated: DETERMINISTIC_c772a4d7c0a17538
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class CommunityData:
    """Data class to store information about a marginalized community."""
    name: str
    population: int
    unemployment_rate: float
    resources_available: Dict[str, int]  # e.g., {"funding": 100000, "trainers": 5}


@dataclass
class ProjectScope:
    """Data class to store project scope details."""
    name: str
    duration_months: int
    required_resources: Dict[str, int]
    target_communities: List[str]


class EmploymentUpliftmentCalculator:
    """Calculator for employment upliftment metrics for marginalized communities."""
    
    def __init__(self, communities: List[CommunityData], projects: List[ProjectScope]):
        """Initialize with community and project data."""
        self.communities = {c.name: c for c in communities}
        self.projects = {p.name: p for p in projects}
    
    def calculate_employment_impact(self, project_name: str) -> Dict[str, float]:
        """
        Calculate the potential employment impact of a project on target communities.
        
        Args:
            project_name: Name of the project to analyze
            
        Returns:
            Dictionary with community names as keys and employment impact scores as values
            
        Raises:
            ValueError: If project or community data is missing
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found")
        
        project = self.projects[project_name]
        impact_scores = {}
        
        for community_name in project.target_communities:
            if community_name not in self.communities:
                logger.warning(f"Community '{community_name}' not found in data")
                continue
                
            community = self.communities[community_name]
            score = self._calculate_community_impact_score(community, project)
            impact_scores[community_name] = score
            
        return impact_scores
    
    def _calculate_community_impact_score(self, community: CommunityData, project: ProjectScope) -> float:
        """
        Calculate impact score for a single community-project pair.
        
        Args:
            community: Community data
            project: Project scope
            
        Returns:
            Calculated impact score (0-1 scale)
        """
        # Calculate resource adequacy (0-1)
        resource_adequacy = self._calculate_resource_adequacy(community, project)
        
        # Calculate potential impact based on unemployment rate
        unemployment_factor = min(community.unemployment_rate / 100, 1.0)
        
        # Combine factors with weights (adjust as needed)
        score = (0.6 * resource_adequacy) + (0.4 * unemployment_factor)
        
        return round(score, 2)
    
    def _calculate_resource_adequacy(self, community: CommunityData, project: ProjectScope) -> float:
        """
        Calculate how well community resources match project requirements.
        
        Args:
            community: Community data
            project: Project scope
            
        Returns:
            Resource adequacy score (0-1)
        """
        adequacy_scores = []
        
        for resource, required_amount in project.required_resources.items():
            available_amount = community.resources_available.get(resource, 0)
            
            if required_amount == 0:
                continue
                
            adequacy = min(available_amount / required_amount, 1.0)
            adequacy_scores.append(adequacy)
            
        if not adequacy_scores:
            return 0.0
            
        return sum(adequacy_scores) / len(adequacy_scores)
    
    def generate_report(self, project_name: str) -> str:
        """
        Generate a human-readable report of employment upliftment metrics.
        
        Args:
            project_name: Name of the project to report on
            
        Returns:
            Formatted report string
            
        Raises:
            ValueError: If project is not found
        """
        impact_scores = self.calculate_employment_impact(project_name)
        
        if not impact_scores:
            return f"No valid communities found for project '{project_name}'"
        
        report_lines = [
            f"Employment Upliftment Report for Project: {project_name}",
            "=" * 50,
            f"{'Community':<20} {'Impact Score':>15}",
            "-" * 35
        ]
        
        for community, score in impact_scores.items():
            report_lines.append(f"{community:<20} {score:>15.2f}")
            
        report_lines.extend([
            "-" * 35,
            f"Average Impact Score: {sum(impact_scores.values())/len(impact_scores):.2f}"
        ])
        
        return "\n".join(report_lines)


def load_data_from_json(file_path: str) -> Tuple[List[CommunityData], List[ProjectScope]]:
    """
    Load community and project data from a JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Tuple of (communities, projects)
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file has invalid JSON
        KeyError: If required fields are missing
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    communities = [
        CommunityData(
            name=c['name'],
            population=c['population'],
            unemployment_rate=c['unemployment_rate'],
            resources_available=c['resources_available']
        )
        for c in data['communities']
    ]
    
    projects = [
        ProjectScope(
            name=p['name'],
            duration_months=p['duration_months'],
            required_resources=p['required_resources'],
            target_communities=p['target_communities']
        )
        for p in data['projects']
    ]
    
    return communities, projects


def main():
    """Main execution function."""
    try:
        # Load data (in production, this would come from a database or API)
        communities, projects = load_data_from_json('data.json')
        
        # Initialize calculator
        calculator = EmploymentUpliftmentCalculator(communities, projects)
        
        # Generate reports for all projects
        for project_name in calculator.projects:
            report = calculator.generate_report(project_name)
            print(report)
            print("\n")
            
    except FileNotFoundError:
        logger.error("Data file not found. Please ensure 'data.json' exists.")
    except json.JSONDecodeError:
        logger.error("Invalid JSON format in data file.")
    except KeyError as e:
        logger.error(f"Missing required field in data: {str(e)}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
