"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Develop a case study on the benefits of using Dexodoor's UPVC window and door systems for a residential project, focusing on eco-friendliness and energy efficiency."
Generated: DETERMINISTIC_fb4e06540bae3159
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Benefits of Dexodoor's UPVC Window and Door Systems for Residential Projects

This script generates a case study report highlighting the eco-friendliness and energy efficiency
benefits of Dexodoor's UPVC products for residential applications.
"""

import json
from datetime import datetime
from typing import Dict, List

class CaseStudyGenerator:
    """
    Generates a case study report for Dexodoor's UPVC window and door systems.
    """
    
    def __init__(self, project_name: str, location: str, year: int):
        """
        Initialize the case study generator with project details.
        
        Args:
            project_name: Name of the residential project
            location: Geographic location of the project
            year: Year of project completion
        """
        self.project_name = project_name
        self.location = location
        self.year = year
        self.report_data = {
            'title': f"Case Study: {project_name}",
            'subtitle': "Benefits of Dexodoor UPVC Window and Door Systems",
            'date': datetime.now().strftime("%Y-%m-%d"),
            'sections': []
        }
    
    def add_section(self, title: str, content: str) -> None:
        """
        Add a section to the case study report.
        
        Args:
            title: Section title
            content: Section content
        """
        self.report_data['sections'].append({
            'title': title,
            'content': content
        })
    
    def _generate_eco_friendliness_section(self) -> Dict[str, str]:
        """Generate the eco-friendliness benefits section."""
        return {
            'title': "Eco-Friendly Benefits",
            'content': (
                f"Dexodoor's UPVC systems in {self.project_name} demonstrate significant "
                "environmental advantages:\n\n"
                "- Made from recyclable materials with low environmental impact\n"
                "- Long lifespan reduces replacement frequency and waste\n"
                "- Manufacturing process consumes less energy compared to alternatives\n"
                "- Free from toxic materials like lead and cadmium\n"
                "- Contributes to LEED certification points for sustainable buildings"
            )
        }
    
    def _generate_energy_efficiency_section(self) -> Dict[str, str]:
        """Generate the energy efficiency benefits section."""
        return {
            'title': "Energy Efficiency Performance",
            'content': (
                f"The UPVC systems installed at {self.project_name} provide exceptional "
                "thermal performance:\n\n"
                "- Multi-chamber profiles reduce heat transfer by up to 40%\n"
                "- Superior insulation maintains consistent indoor temperatures\n"
                "- Energy savings of 15-20% compared to traditional materials\n"
                "- Reduced HVAC load lowers carbon footprint\n"
                "- Excellent weather sealing prevents air leakage"
            )
        }
    
    def _generate_project_overview(self) -> Dict[str, str]:
        """Generate the project overview section."""
        return {
            'title': "Project Overview",
            'content': (
                f"Project: {self.project_name}\n"
                f"Location: {self.location}\n"
                f"Year: {self.year}\n\n"
                "This residential project selected Dexodoor's premium UPVC window "
                "and door systems for their combination of sustainability and performance."
            )
        }
    
    def generate_report(self) -> str:
        """
        Generate the complete case study report in JSON format.
        
        Returns:
            JSON string containing the formatted case study
        """
        try:
            # Add standard sections
            self.add_section(**self._generate_project_overview())
            self.add_section(**self._generate_eco_friendliness_section())
            self.add_section(**self._generate_energy_efficiency_section())
            
            # Convert to JSON with pretty printing
            return json.dumps(self.report_data, indent=2)
        except Exception as e:
            raise RuntimeError(f"Failed to generate case study: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        case_study = CaseStudyGenerator(
            project_name="Green Heights Residence",
            location="London, UK",
            year=2023
        )
        
        report = case_study.generate_report()
        print(report)
        
        # Optionally save to file
        with open("dexodoor_case_study.json", "w") as f:
            f.write(report)
            
    except Exception as e:
        print(f"Error: {e}")
```
