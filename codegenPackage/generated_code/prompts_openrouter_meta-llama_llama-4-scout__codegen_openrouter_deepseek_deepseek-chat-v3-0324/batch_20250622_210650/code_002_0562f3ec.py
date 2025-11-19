"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Generate a code snippet to create a simple risk assessment tool for corporate investigations, incorporating factors like threat analysis and vulnerability assessment."
Generated: DETERMINISTIC_0562f3ec918c5dea
Batch ID: 20250622_210650
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

class RiskAssessmentTool:
    """
    A simple risk assessment tool for corporate investigations.
    Evaluates risks based on threat analysis and vulnerability assessment.
    """
    
    def __init__(self):
        self.threat_factors = {
            'internal': 0.7,
            'external': 0.5,
            'physical': 0.6,
            'cyber': 0.8
        }
        self.vulnerability_factors = {
            'access_control': 0.9,
            'data_protection': 0.7,
            'network_security': 0.8,
            'physical_security': 0.6
        }
        self.risk_thresholds = {
            'low': 0.3,
            'medium': 0.6,
            'high': 0.8
        }
    
    def assess_threat(self, threat_type: str, likelihood: float) -> float:
        """
        Calculate threat score based on type and likelihood.
        
        Args:
            threat_type: Type of threat (internal/external/physical/cyber)
            likelihood: Probability of threat occurring (0-1)
            
        Returns:
            Calculated threat score
            
        Raises:
            ValueError: If invalid threat type or likelihood out of range
        """
        if threat_type not in self.threat_factors:
            raise ValueError(f"Invalid threat type: {threat_type}")
        if not 0 <= likelihood <= 1:
            raise ValueError("Likelihood must be between 0 and 1")
            
        return self.threat_factors[threat_type] * likelihood
    
    def assess_vulnerability(self, vulnerability_type: str, exposure: float) -> float:
        """
        Calculate vulnerability score based on type and exposure.
        
        Args:
            vulnerability_type: Type of vulnerability
            exposure: Degree of exposure (0-1)
            
        Returns:
            Calculated vulnerability score
            
        Raises:
            ValueError: If invalid vulnerability type or exposure out of range
        """
        if vulnerability_type not in self.vulnerability_factors:
            raise ValueError(f"Invalid vulnerability type: {vulnerability_type}")
        if not 0 <= exposure <= 1:
            raise ValueError("Exposure must be between 0 and 1")
            
        return self.vulnerability_factors[vulnerability_type] * exposure
    
    def calculate_risk(self, threat_score: float, vulnerability_score: float) -> float:
        """
        Calculate overall risk score from threat and vulnerability scores.
        
        Args:
            threat_score: Calculated threat score
            vulnerability_score: Calculated vulnerability score
            
        Returns:
            Combined risk score (0-1)
        """
        return (threat_score + vulnerability_score) / 2
    
    def evaluate_risk_level(self, risk_score: float) -> str:
        """
        Determine risk level based on calculated score.
        
        Args:
            risk_score: Combined risk score (0-1)
            
        Returns:
            Risk level (low/medium/high)
            
        Raises:
            ValueError: If risk score is out of range
        """
        if not 0 <= risk_score <= 1:
            raise ValueError("Risk score must be between 0 and 1")
            
        if risk_score < self.risk_thresholds['low']:
            return 'low'
        elif risk_score < self.risk_thresholds['medium']:
            return 'medium'
        elif risk_score < self.risk_thresholds['high']:
            return 'high'
        else:
            return 'critical'
    
    def full_assessment(self, threat_type: str, threat_likelihood: float,
                       vulnerability_type: str, vulnerability_exposure: float) -> Dict:
        """
        Perform complete risk assessment with all steps.
        
        Args:
            threat_type: Type of threat
            threat_likelihood: Probability of threat
            vulnerability_type: Type of vulnerability
            vulnerability_exposure: Degree of exposure
            
        Returns:
            Dictionary containing all assessment results
        """
        try:
            threat_score = self.assess_threat(threat_type, threat_likelihood)
            vuln_score = self.assess_vulnerability(vulnerability_type, vulnerability_exposure)
            risk_score = self.calculate_risk(threat_score, vuln_score)
            risk_level = self.evaluate_risk_level(risk_score)
            
            return {
                'threat_score': round(threat_score, 2),
                'vulnerability_score': round(vuln_score, 2),
                'risk_score': round(risk_score, 2),
                'risk_level': risk_level,
                'assessment': 'complete'
            }
        except ValueError as e:
            return {
                'error': str(e),
                'assessment': 'failed'
            }
    
    def save_assessment(self, assessment_data: Dict, filename: str) -> bool:
        """
        Save assessment results to JSON file.
        
        Args:
            assessment_data: Dictionary containing assessment results
            filename: Output file name
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(assessment_data, f, indent=2)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving assessment: {e}")
            return False

# Example usage
if __name__ == "__main__":
    tool = RiskAssessmentTool()
    
    # Sample assessment
    results = tool.full_assessment(
        threat_type='cyber',
        threat_likelihood=0.7,
        vulnerability_type='data_protection',
        vulnerability_exposure=0.5
    )
    
    print("Risk Assessment Results:")
    print(json.dumps(results, indent=2))
    
    # Save results
    tool.save_assessment(results, 'risk_assessment.json')
```
