"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: "Compare the architectural style of Dens Haven with other luxury residential projects in India, highlighting unique features and design elements."
Generated: DETERMINISTIC_a5aba3962139d5f9
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ResidentialProject:
    """
    A class to represent a luxury residential project with its architectural features.
    """
    
    def __init__(self, name: str, location: str, architect: str, features: Dict[str, List[str]]):
        """
        Initialize a ResidentialProject instance.
        
        Args:
            name (str): Name of the residential project.
            location (str): Location of the project.
            architect (str): Architect or firm responsible for the design.
            features (Dict[str, List[str]]): Dictionary of architectural features categorized by type.
        """
        self.name = name
        self.location = location
        self.architect = architect
        self.features = features
    
    def to_dict(self) -> Dict:
        """
        Convert the ResidentialProject instance to a dictionary.
        
        Returns:
            Dict: Dictionary representation of the project.
        """
        return {
            "name": self.name,
            "location": self.location,
            "architect": self.architect,
            "features": self.features
        }
    
    def __str__(self) -> str:
        """
        String representation of the ResidentialProject instance.
        
        Returns:
            str: Formatted string with project details.
        """
        features_str = "\n".join([f"{k}: {', '.join(v)}" for k, v in self.features.items()])
        return (
            f"Project: {self.name}\n"
            f"Location: {self.location}\n"
            f"Architect: {self.architect}\n"
            f"Features:\n{features_str}"
        )

class ProjectComparator:
    """
    A class to compare architectural styles of luxury residential projects.
    """
    
    def __init__(self, projects: List[ResidentialProject]):
        """
        Initialize a ProjectComparator instance.
        
        Args:
            projects (List[ResidentialProject]): List of ResidentialProject instances to compare.
        """
        self.projects = projects
    
    def compare_features(self, project_name: str) -> Optional[Dict]:
        """
        Compare the features of a given project with others.
        
        Args:
            project_name (str): Name of the project to compare.
            
        Returns:
            Optional[Dict]: Dictionary with comparison results or None if project not found.
        """
        target_project = None
        for project in self.projects:
            if project.name == project_name:
                target_project = project
                break
        
        if not target_project:
            return None
        
        comparison = {}
        for project in self.projects:
            if project.name == project_name:
                continue
            
            unique_features = {}
            for feature_type, features in target_project.features.items():
                if feature_type not in project.features:
                    unique_features[feature_type] = features
                else:
                    unique_features[feature_type] = [
                        f for f in features if f not in project.features[feature_type]
                    ]
            
            comparison[project.name] = unique_features
        
        return comparison
    
    def save_comparison_to_json(self, project_name: str, filename: str) -> bool:
        """
        Save the comparison results to a JSON file.
        
        Args:
            project_name (str): Name of the project to compare.
            filename (str): Name of the output JSON file.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        comparison = self.compare_features(project_name)
        if not comparison:
            return False
        
        try:
            with open(filename, 'w') as f:
                json.dump(comparison, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving comparison to JSON: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Sample projects
    dens_haven = ResidentialProject(
        name="Dens Haven",
        location="Bangalore",
        architect="Design Atelier",
        features={
            "Sustainability": ["Solar panels", "Rainwater harvesting"],
            "Amenities": ["Infinity pool", "Private gardens"],
            "Design": ["Minimalist facade", "Open floor plans"]
        }
    )
    
    project_aurum = ResidentialProject(
        name="Aurum",
        location="Mumbai",
        architect="Morphogenesis",
        features={
            "Sustainability": ["Green roofs", "Waste recycling"],
            "Amenities": ["Sky deck", "Concierge services"],
            "Design": ["Curvilinear structures", "High ceilings"]
        }
    )
    
    project_vana = ResidentialProject(
        name="Vana",
        location="Delhi",
        architect="Studio Lotus",
        features={
            "Sustainability": ["Solar panels", "Natural ventilation"],
            "Amenities": ["Yoga deck", "Organic farm"],
            "Design": ["Earthy tones", "Biophilic design"]
        }
    )
    
    # Initialize comparator
    comparator = ProjectComparator([dens_haven, project_aurum, project_vana])
    
    # Compare Dens Haven with others
    comparison = comparator.compare_features("Dens Haven")
    if comparison:
        print("Comparison Results:")
        for project, features in comparison.items():
            print(f"\nCompared to {project}:")
            for feature_type, unique_features in features.items():
                if unique_features:
                    print(f"{feature_type}: {', '.join(unique_features)}")
    
    # Save comparison to JSON
    comparator.save_comparison_to_json("Dens Haven", "dens_haven_comparison.json")
```
