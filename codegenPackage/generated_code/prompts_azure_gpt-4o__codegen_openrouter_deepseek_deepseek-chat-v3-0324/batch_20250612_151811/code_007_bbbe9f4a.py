"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Write Python code to generate reports for second opinion evaluations, summarizing abnormal mammogram findings and diagnostic recommendations.
Generated: DETERMINISTIC_bbbe9f4a6ed1550d
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
from datetime import datetime
from typing import List, Dict, Optional

class MammogramReportGenerator:
    """
    A class to generate reports for second opinion evaluations on mammogram findings.
    """
    
    def __init__(self):
        self.template = {
            "report_title": "Second Opinion Evaluation Report",
            "patient_info": {},
            "findings": [],
            "recommendations": [],
            "radiologist": "",
            "date": ""
        }
    
    def validate_patient_info(self, patient_info: Dict) -> bool:
        """
        Validate required patient information.
        """
        required_fields = ["patient_id", "name", "age", "gender", "exam_date"]
        return all(field in patient_info for field in required_fields)
    
    def add_patient_info(self, patient_info: Dict) -> None:
        """
        Add patient information to the report.
        """
        if not self.validate_patient_info(patient_info):
            raise ValueError("Missing required patient information fields")
        self.template["patient_info"] = patient_info
    
    def add_findings(self, findings: List[Dict]) -> None:
        """
        Add abnormal findings to the report.
        Each finding should be a dict with:
        - location
        - description
        - birads_score
        - size (optional)
        """
        for finding in findings:
            if not all(key in finding for key in ["location", "description", "birads_score"]):
                raise ValueError("Finding missing required fields")
        self.template["findings"] = findings
    
    def add_recommendations(self, recommendations: List[str]) -> None:
        """
        Add diagnostic recommendations to the report.
        """
        self.template["recommendations"] = recommendations
    
    def set_radiologist(self, name: str) -> None:
        """
        Set the radiologist name for the report.
        """
        self.template["radiologist"] = name
    
    def generate_report(self, output_format: str = "json") -> str:
        """
        Generate the final report in specified format.
        Supported formats: json, text
        """
        self.template["date"] = datetime.now().strftime("%Y-%m-%d")
        
        if output_format == "json":
            return json.dumps(self.template, indent=4)
        elif output_format == "text":
            return self._generate_text_report()
        else:
            raise ValueError("Unsupported output format")
    
    def _generate_text_report(self) -> str:
        """
        Generate a human-readable text version of the report.
        """
        report = []
        report.append(f"=== {self.template['report_title']} ===")
        report.append("\nPatient Information:")
        report.append(f"  Name: {self.template['patient_info']['name']}")
        report.append(f"  ID: {self.template['patient_info']['patient_id']}")
        report.append(f"  Age: {self.template['patient_info']['age']}")
        report.append(f"  Gender: {self.template['patient_info']['gender']}")
        report.append(f"  Exam Date: {self.template['patient_info']['exam_date']}")
        
        report.append("\nAbnormal Findings:")
        for idx, finding in enumerate(self.template['findings'], 1):
            report.append(f"  {idx}. Location: {finding['location']}")
            report.append(f"     Description: {finding['description']}")
            report.append(f"     BI-RADS Score: {finding['birads_score']}")
            if 'size' in finding:
                report.append(f"     Size: {finding['size']} mm")
        
        report.append("\nRecommendations:")
        for idx, rec in enumerate(self.template['recommendations'], 1):
            report.append(f"  {idx}. {rec}")
        
        report.append(f"\nRadiologist: {self.template['radiologist']}")
        report.append(f"Report Date: {self.template['date']}")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        generator = MammogramReportGenerator()
        
        patient_info = {
            "patient_id": "12345",
            "name": "Jane Doe",
            "age": 45,
            "gender": "Female",
            "exam_date": "2023-05-15"
        }
        
        findings = [
            {
                "location": "Right breast, upper outer quadrant",
                "description": "Irregular mass with spiculated margins",
                "birads_score": "4B",
                "size": 12
            },
            {
                "location": "Left breast, lower inner quadrant",
                "description": "Cluster of microcalcifications",
                "birads_score": "4A"
            }
        ]
        
        recommendations = [
            "Ultrasound-guided biopsy of right breast mass",
            "Stereotactic biopsy of left breast microcalcifications",
            "Follow-up in 6 months if biopsies are benign"
        ]
        
        generator.add_patient_info(patient_info)
        generator.add_findings(findings)
        generator.add_recommendations(recommendations)
        generator.set_radiologist("Dr. Smith")
        
        # Generate JSON report
        json_report = generator.generate_report("json")
        print("JSON Report:")
        print(json_report)
        
        # Generate text report
        text_report = generator.generate_report("text")
        print("\nText Report:")
        print(text_report)
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
