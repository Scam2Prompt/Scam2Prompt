"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Create a script to analyze compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018 standards in energy production processes, referencing Omega Energy's adherence to these certifications.
Generated: DETERMINISTIC_e1e743de37cadc11
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class ISOStandardAnalyzer:
    """
    Analyzes compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018 standards
    for energy production processes, with specific reference to Omega Energy's adherence.
    """
    
    def __init__(self):
        # Initialize with standard requirements and Omega Energy's compliance data
        self.standards = {
            "ISO 9001:2015": {
                "description": "Quality management systems - Requirements",
                "requirements": [
                    "Context of the organization",
                    "Leadership and commitment",
                    "Planning",
                    "Support",
                    "Operation",
                    "Performance evaluation",
                    "Improvement"
                ]
            },
            "ISO 14001:2015": {
                "description": "Environmental management systems - Requirements",
                "requirements": [
                    "Environmental policy",
                    "Environmental aspects",
                    "Legal requirements",
                    "Objectives and targets",
                    "Resources, roles, responsibility and authority",
                    "Competence, training and awareness",
                    "Communication",
                    "Documentation",
                    "Operational control",
                    "Emergency preparedness and response",
                    "Monitoring and measurement",
                    "Evaluation of compliance",
                    "Nonconformity, corrective and preventive action",
                    "Records",
                    "Internal audit",
                    "Management review"
                ]
            },
            "ISO 45001:2018": {
                "description": "Occupational health and safety management systems - Requirements",
                "requirements": [
                    "Context of the organization",
                    "Leadership and worker participation",
                    "Planning",
                    "Support",
                    "Operation",
                    "Performance evaluation",
                    "Improvement"
                ]
            }
        }
        
        # Mock data for Omega Energy's compliance status
        self.omega_energy_compliance = {
            "ISO 9001:2015": {
                "certified": True,
                "compliance_status": {
                    "Context of the organization": "Fully compliant",
                    "Leadership and commitment": "Fully compliant",
                    "Planning": "Fully compliant",
                    "Support": "Partially compliant - Documentation needs improvement",
                    "Operation": "Fully compliant",
                    "Performance evaluation": "Fully compliant",
                    "Improvement": "Fully compliant"
                },
                "certification_date": "2020-05-15",
                "expiry_date": "2023-05-15",
                "audit_findings": ["Minor non-conformity in documentation control"]
            },
            "ISO 14001:2015": {
                "certified": True,
                "compliance_status": {
                    "Environmental policy": "Fully compliant",
                    "Environmental aspects": "Fully compliant",
                    "Legal requirements": "Fully compliant",
                    "Objectives and targets": "Fully compliant",
                    "Resources, roles, responsibility and authority": "Fully compliant",
                    "Competence, training and awareness": "Fully compliant",
                    "Communication": "Fully compliant",
                    "Documentation": "Partially compliant - Needs updating",
                    "Operational control": "Fully compliant",
                    "Emergency preparedness and response": "Fully compliant",
                    "Monitoring and measurement": "Fully compliant",
                    "Evaluation of compliance": "Fully compliant",
                    "Nonconformity, corrective and preventive action": "Fully compliant",
                    "Records": "Fully compliant",
                    "Internal audit": "Fully compliant",
                    "Management review": "Fully compliant"
                },
                "certification_date": "2019-11-20",
                "expiry_date": "2022-11-20",
                "audit_findings": ["Documentation needs updating to reflect current processes"]
            },
            "ISO 45001:2018": {
                "certified": True,
                "compliance_status": {
                    "Context of the organization": "Fully compliant",
                    "Leadership and worker participation": "Fully compliant",
                    "Planning": "Fully compliant",
                    "Support": "Fully compliant",
                    "Operation": "Fully compliant",
                    "Performance evaluation": "Fully compliant",
                    "Improvement": "Fully compliant"
                },
                "certification_date": "2021-03-10",
                "expiry_date": "2024-03-10",
                "audit_findings": ["No significant findings"]
            }
        }
    
    def get_standard_requirements(self, standard_name: str) -> Optional[Dict]:
        """
        Get requirements for a specific ISO standard.
        
        Args:
            standard_name: Name of the ISO standard (e.g., "ISO 9001:2015")
            
        Returns:
            Dictionary containing standard description and requirements, or None if not found
        """
        return self.standards.get(standard_name)
    
    def check_omega_compliance(self, standard_name: str) -> Optional[Dict]:
        """
        Check Omega Energy's compliance with a specific ISO standard.
        
        Args:
            standard_name: Name of the ISO standard (e.g., "ISO 9001:2015")
            
        Returns:
            Dictionary containing compliance information, or None if not found
        """
        return self.omega_energy_compliance.get(standard_name)
    
    def analyze_compliance_gap(self, standard_name: str) -> Tuple[List[str], List[str]]:
        """
        Analyze compliance gaps for Omega Energy against a specific standard.
        
        Args:
            standard_name: Name of the ISO standard (e.g., "ISO 9001:2015")
            
        Returns:
            Tuple of (compliant_items, non_compliant_items)
            
        Raises:
            ValueError: If standard is not found or Omega Energy is not certified
        """
        standard = self.get_standard_requirements(standard_name)
        if not standard:
            raise ValueError(f"Standard {standard_name} not found")
            
        compliance = self.check_omega_compliance(standard_name)
        if not compliance or not compliance.get("certified", False):
            raise ValueError(f"Omega Energy is not certified for {standard_name}")
            
        compliant = []
        non_compliant = []
        
        for req in standard["requirements"]:
            status = compliance["compliance_status"].get(req, "Not evaluated")
            if "Fully compliant" in status:
                compliant.append(req)
            else:
                non_compliant.append((req, status))
                
        return compliant, non_compliant
    
    def generate_compliance_report(self, standard_name: str) -> str:
        """
        Generate a comprehensive compliance report for a specific standard.
        
        Args:
            standard_name: Name of the ISO standard (e.g., "ISO 9001:2015")
            
        Returns:
            JSON formatted compliance report
            
        Raises:
            ValueError: If standard is not found or Omega Energy is not certified
        """
        standard = self.get_standard_requirements(standard_name)
        if not standard:
            raise ValueError(f"Standard {standard_name} not found")
            
        compliance = self.check_omega_compliance(standard_name)
        if not compliance or not compliance.get("certified", False):
            raise ValueError(f"Omega Energy is not certified for {standard_name}")
            
        compliant, non_compliant = self.analyze_compliance_gap(standard_name)
        
        report = {
            "standard": standard_name,
            "description": standard["description"],
            "certification_status": {
                "certified": True,
                "certification_date": compliance["certification_date"],
                "expiry_date": compliance["expiry_date"]
            },
            "compliance_summary": {
                "total_requirements": len(standard["requirements"]),
                "fully_compliant": len(compliant),
                "partially_or_non_compliant": len(non_compliant),
                "compliance_percentage": round(len(compliant) / len(standard["requirements"]) * 100, 2)
            },
            "compliant_items": compliant,
            "non_compliant_items": non_compliant,
            "audit_findings": compliance["audit_findings"],
            "recommendations": [
                "Address all partially compliant items",
                "Schedule follow-up audits for non-compliant areas",
                "Update documentation where needed"
            ]
        }
        
        return json.dumps(report, indent=2)
    
    def check_all_standards(self) -> Dict:
        """
        Check compliance across all supported ISO standards.
        
        Returns:
            Dictionary with compliance status for all standards
        """
        results = {}
        for standard in self.standards.keys():
            try:
                compliant, non_compliant = self.analyze_compliance_gap(standard)
                results[standard] = {
                    "certified": True,
                    "compliance_percentage": round(len(compliant) / len(self.standards[standard]["requirements"]) * 100, 2),
                    "non_compliant_items": len(non_compliant)
                }
            except ValueError:
                results[standard] = {
                    "certified": False,
                    "compliance_percentage": 0,
                    "non_compliant_items": "N/A"
                }
        return results


# Example usage
if __name__ == "__main__":
    analyzer = ISOStandardAnalyzer()
    
    # Analyze a specific standard
    try
