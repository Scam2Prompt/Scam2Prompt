"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: "Generate a design proposal for a residential project that integrates architectural elements, material textures, and environmental consideration, with a focus on creating rich experiences and a happy and healthy life."
Generated: DETERMINISTIC_1583cb174602e9ab
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Residential Project Design Proposal Generator

This script generates a design proposal for a residential project focusing on:
- Architectural elements
- Material textures
- Environmental considerations
- Rich experiences
- Healthy living

The output is formatted as a structured document with sections covering all key aspects.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class DesignProposal:
    """
    A class to generate and manage residential design proposals.
    """
    
    def __init__(self, project_name: str, client_name: str, location: str):
        """
        Initialize the design proposal with basic project information.
        
        Args:
            project_name: Name of the residential project
            client_name: Name of the client
            location: Project site location
        """
        self.project_name = project_name
        self.client_name = client_name
        self.location = location
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.sections = {
            "Introduction": "",
            "Architectural Elements": [],
            "Material Selection": {},
            "Environmental Considerations": [],
            "Experience Design": [],
            "Health and Wellness": []
        }
    
    def add_architectural_element(self, element: str, description: str, benefits: List[str]):
        """
        Add an architectural element to the proposal.
        
        Args:
            element: Name of the architectural element
            description: Description of the element
            benefits: List of benefits this element provides
        """
        self.sections["Architectural Elements"].append({
            "element": element,
            "description": description,
            "benefits": benefits
        })
    
    def add_material(self, area: str, material: str, texture: str, sustainability: str):
        """
        Add material selection for a specific area.
        
        Args:
            area: Area of application (e.g., flooring, walls)
            material: Material name
            texture: Texture description
            sustainability: Sustainability features
        """
        if area not in self.sections["Material Selection"]:
            self.sections["Material Selection"][area] = []
        self.sections["Material Selection"][area].append({
            "material": material,
            "texture": texture,
            "sustainability": sustainability
        })
    
    def add_environmental_consideration(self, feature: str, description: str, impact: str):
        """
        Add an environmental consideration to the proposal.
        
        Args:
            feature: Environmental feature name
            description: Description of the feature
            impact: Positive environmental impact
        """
        self.sections["Environmental Considerations"].append({
            "feature": feature,
            "description": description,
            "impact": impact
        })
    
    def add_experience_element(self, element: str, description: str, emotional_impact: str):
        """
        Add an experience design element to the proposal.
        
        Args:
            element: Experience element name
            description: Description of the element
            emotional_impact: How it enhances resident experience
        """
        self.sections["Experience Design"].append({
            "element": element,
            "description": description,
            "emotional_impact": emotional_impact
        })
    
    def add_health_feature(self, feature: str, description: str, health_benefits: List[str]):
        """
        Add a health and wellness feature to the proposal.
        
        Args:
            feature: Health feature name
            description: Description of the feature
            health_benefits: List of health benefits
        """
        self.sections["Health and Wellness"].append({
            "feature": feature,
            "description": description,
            "health_benefits": health_benefits
        })
    
    def generate_proposal(self, output_format: str = "markdown") -> str:
        """
        Generate the final proposal document in the specified format.
        
        Args:
            output_format: Output format ("markdown" or "json")
            
        Returns:
            The generated proposal document
            
        Raises:
            ValueError: If unsupported output format is requested
        """
        if output_format == "markdown":
            return self._generate_markdown()
        elif output_format == "json":
            return self._generate_json()
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def _generate_markdown(self) -> str:
        """Generate markdown formatted proposal."""
        markdown = [
            f"# Residential Design Proposal: {self.project_name}",
            f"**Client:** {self.client_name}",
            f"**Location:** {self.location}",
            f"**Date:** {self.date}",
            "\n## Introduction\n",
            self.sections["Introduction"],
            "\n## Architectural Elements\n"
        ]
        
        for element in self.sections["Architectural Elements"]:
            markdown.append(f"### {element['element']}")
            markdown.append(element['description'])
            markdown.append("**Benefits:**")
            markdown.extend([f"- {benefit}" for benefit in element['benefits']])
            markdown.append("")
        
        markdown.append("\n## Material Selection\n")
        for area, materials in self.sections["Material Selection"].items():
            markdown.append(f"### {area.capitalize()}")
            for material in materials:
                markdown.append(f"- **Material:** {material['material']}")
                markdown.append(f"  - Texture: {material['texture']}")
                markdown.append(f"  - Sustainability: {material['sustainability']}")
            markdown.append("")
        
        markdown.append("\n## Environmental Considerations\n")
        for consideration in self.sections["Environmental Considerations"]:
            markdown.append(f"### {consideration['feature']}")
            markdown.append(consideration['description'])
            markdown.append(f"**Impact:** {consideration['impact']}")
            markdown.append("")
        
        markdown.append("\n## Experience Design\n")
        for experience in self.sections["Experience Design"]:
            markdown.append(f"### {experience['element']}")
            markdown.append(experience['description'])
            markdown.append(f"**Emotional Impact:** {experience['emotional_impact']}")
            markdown.append("")
        
        markdown.append("\n## Health and Wellness\n")
        for feature in self.sections["Health and Wellness"]:
            markdown.append(f"### {feature['feature']}")
            markdown.append(feature['description'])
            markdown.append("**Health Benefits:**")
            markdown.extend([f"- {benefit}" for benefit in feature['health_benefits']])
            markdown.append("")
        
        return "\n".join(markdown)
    
    def _generate_json(self) -> str:
        """Generate JSON formatted proposal."""
        proposal_data = {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "location": self.location,
            "date": self.date,
            "sections": self.sections
        }
        return json.dumps(proposal_data, indent=2)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize proposal
        proposal = DesignProposal(
            project_name="Harmony Residence",
            client_name="Smith Family",
            location="Portland, OR"
        )
        
        # Set introduction
        proposal.sections["Introduction"] = (
            "This proposal outlines a residential design focused on creating "
            "a harmonious living environment that promotes wellbeing through "
            "thoughtful architecture, sustainable materials, and spaces that "
            "enhance daily experiences."
        )
        
        # Add architectural elements
        proposal.add_architectural_element(
            "Open Floor Plan",
            "Fluid living spaces that connect common areas",
            ["Enhanced social interaction", "Improved natural light flow", "Flexible use of space"]
        )
        
        proposal.add_architectural_element(
            "Biophilic Design",
            "Integration of natural elements throughout the home",
            ["Reduced stress", "Improved air quality", "Connection to nature"]
        )
        
        # Add materials
        proposal.add_material(
            "flooring",
            "Bamboo",
            "Smooth, warm texture",
            "Rapidly renewable resource"
        )
        
        proposal.add_material(
            "walls",
            "Clay plaster",
            "Soft, organic texture",
            "Natural humidity regulation"
        )
        
        # Add environmental considerations
        proposal.add_environmental_consideration(
            "Solar Orientation",
            "Optimal placement for passive heating and cooling",
            "Reduced energy consumption by 30%"
        )
        
        proposal.add_environmental_consideration(
            "Rainwater Harvesting",
            "Integrated system for landscape irrigation",
            "Reduces municipal water usage by 40%"
        )
        
        # Add experience elements
        proposal.add_experience_element(
            "Meditation Garden",
            "Private outdoor space for reflection",
            "Promotes mindfulness and relaxation"
        )
        
        proposal.add_experience_element(
            "Chef's Kitchen",
            "Designed for culinary creativity",
            "Encourages family bonding through cooking"
        )
        
        # Add health features
        proposal.add_health_feature(
            "Air Purification System",
            "Advanced filtration for indoor air quality",
            ["Reduced allergens", "Improved respiratory health"]
        )
        
        proposal.add_health_fe
