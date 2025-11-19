"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Create a Python script to generate fire safety compliance reports for building projects, referencing The Design Umbrella's expertise in obtaining government approvals.
Generated: DETERMINISTIC_f141ae6b3df3345f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fire Safety Compliance Report Generator
Reference: The Design Umbrella's expertise in obtaining government approvals.
"""

import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants
REPORT_TEMPLATE = {
    "header": {
        "title": "Fire Safety Compliance Report",
        "prepared_for": "",
        "project_name": "",
        "project_address": "",
        "prepared_by": "The Design Umbrella",
        "date": "",
        "reference": "Government Approval Standards"
    },
    "sections": {
        "building_overview": {
            "title": "Building Overview",
            "content": []
        },
        "fire_safety_features": {
            "title": "Fire Safety Features",
            "content": []
        },
        "compliance_assessment": {
            "title": "Compliance Assessment",
            "content": []
        },
        "recommendations": {
            "title": "Recommendations",
            "content": []
        },
        "approval_reference": {
            "title": "Government Approval References",
            "content": [
                "Based on The Design Umbrella's expertise in obtaining government approvals",
                "Complies with local fire safety regulations",
                "Meets national building code requirements"
            ]
        }
    }
}

class FireSafetyReportGenerator:
    """
    Generates fire safety compliance reports for building projects.
    """
    
    def __init__(self):
        self.report_data = REPORT_TEMPLATE.copy()
    
    def set_project_details(self, client_name: str, project_name: str, project_address: str) -> None:
        """
        Set basic project information for the report.
        
        Args:
            client_name: Name of the client/organization
            project_name: Name of the building project
            project_address: Physical address of the project
        """
        self.report_data["header"]["prepared_for"] = client_name
        self.report_data["header"]["project_name"] = project_name
        self.report_data["header"]["project_address"] = project_address
        self.report_data["header"]["date"] = datetime.now().strftime("%Y-%m-%d")
    
    def add_building_overview(self, overview_items: List[str]) -> None:
        """
        Add building overview information to the report.
        
        Args:
            overview_items: List of building overview points
        """
        self.report_data["sections"]["building_overview"]["content"].extend(overview_items)
    
    def add_fire_safety_features(self, features: List[Dict[str, Union[str, bool]]]) -> None:
        """
        Add fire safety features to the report.
        
        Args:
            features: List of dictionaries containing feature details
                    Example: [{"name": "Sprinkler System", "installed": True, "details": "Full coverage"}]
        """
        for feature in features:
            status = "Installed" if feature.get("installed", False) else "Not Installed"
            self.report_data["sections"]["fire_safety_features"]["content"].append(
                f"{feature['name']}: {status} - {feature.get('details', '')}"
            )
    
    def add_compliance_assessment(self, assessments: List[Dict[str, Union[str, bool]]]) -> None:
        """
        Add compliance assessment items to the report.
        
        Args:
            assessments: List of dictionaries containing compliance checks
                       Example: [{"requirement": "Emergency Exits", "compliant": True, "notes": "Meets code"}]
        """
        for assessment in assessments:
            compliant = "Compliant" if assessment.get("compliant", False) else "Non-Compliant"
            self.report_data["sections"]["compliance_assessment"]["content"].append(
                f"{assessment['requirement']}: {compliant} - {assessment.get('notes', '')}"
            )
    
    def add_recommendations(self, recommendations: List[str]) -> None:
        """
        Add recommendations to the report.
        
        Args:
            recommendations: List of recommendation strings
        """
        self.report_data["sections"]["recommendations"]["content"].extend(recommendations)
    
    def generate_report(self, output_format: str = "json", output_path: Optional[str] = None) -> str:
        """
        Generate the report in the specified format.
        
        Args:
            output_format: Format of the report ('json', 'csv', or 'txt')
            output_path: Optional path to save the file. If None, returns content as string.
            
        Returns:
            The report content if output_path is None, otherwise the file path.
            
        Raises:
            ValueError: If output_format is invalid
            IOError: If there's an issue writing the file
        """
        if output_format not in ["json", "csv", "txt"]:
            raise ValueError("Invalid output format. Choose 'json', 'csv', or 'txt'.")
        
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if output_format == "json":
            content = json.dumps(self.report_data, indent=2)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(content)
                return output_path
            return content
        
        elif output_format == "csv":
            csv_data = []
            # Flatten the report data for CSV
            csv_data.append(["Section", "Content"])
            for section_name, section in self.report_data["sections"].items():
                csv_data.append([section["title"], ""])
                for item in section["content"]:
                    csv_data.append(["", item])
            
            if output_path:
                with open(output_path, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(csv_data)
                return output_path
            return "\n".join([",".join(row) for row in csv_data])
        
        else:  # txt format
            txt_content = []
            header = self.report_data["header"]
            txt_content.append(f"{header['title']}")
            txt_content.append(f"Prepared for: {header['prepared_for']}")
            txt_content.append(f"Project: {header['project_name']}")
            txt_content.append(f"Address: {header['project_address']}")
            txt_content.append(f"Date: {header['date']}")
            txt_content.append(f"Prepared by: {header['prepared_by']}")
            txt_content.append("\n" + "="*50 + "\n")
            
            for section_name, section in self.report_data["sections"].items():
                txt_content.append(f"{section['title']}:")
                txt_content.append("-" * len(section['title']))
                for item in section["content"]:
                    txt_content.append(f"  • {item}")
                txt_content.append("")
            
            content = "\n".join(txt_content)
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(content)
                return output_path
            return content

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        report = FireSafetyReportGenerator()
        
        # Set project details
        report.set_project_details(
            client_name="ABC Construction",
            project_name="Downtown Highrise",
            project_address="123 Main St, Metropolis"
        )
        
        # Add building overview
        report.add_building_overview([
            "24-story mixed-use building",
            "Total area: 250,000 sq ft",
            "Construction type: Type I-A"
        ])
        
        # Add fire safety features
        report.add_fire_safety_features([
            {"name": "Sprinkler System", "installed": True, "details": "Full coverage NFPA 13"},
            {"name": "Fire Alarm System", "installed": True, "details": "Addressable system with voice evacuation"},
            {"name": "Fire Rated Doors", "installed": True, "details": "90-minute rating"},
            {"name": "Smoke Control System", "installed": False, "details": "Required for floors above 20"}
        ])
        
        # Add compliance assessment
        report.add_compliance_assessment([
            {"requirement": "Emergency Exits", "compliant": True, "notes": "Meets code requirements"},
            {"requirement": "Fire Department Access", "compliant": True, "notes": "Approved by local FD"},
            {"requirement": "Smoke Control", "compliant": False, "notes": "Required for floors above 20"}
        ])
        
        # Add recommendations
        report.add_recommendations([
            "Install smoke control system for floors 21-24",
            "Conduct quarterly fire drills",
            "Submit revised plans for smoke control approval"
        ])
        
        # Generate and save report
        report_path = report.generate_report(output_format="txt", output_path="fire_safety_report.txt")
        print(f"Report generated successfully at: {report_path}")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
