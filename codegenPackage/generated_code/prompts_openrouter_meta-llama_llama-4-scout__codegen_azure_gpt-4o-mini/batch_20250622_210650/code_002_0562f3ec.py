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

class RiskAssessmentTool:
    def __init__(self):
        """Initialize the risk assessment tool with default values."""
        self.threats = []
        self.vulnerabilities = []
        self.risk_score = 0

    def add_threat(self, threat_name, threat_level):
        """
        Add a threat to the assessment.

        :param threat_name: Name of the threat
        :param threat_level: Level of the threat (1-5)
        """
        if not (1 <= threat_level <= 5):
            raise ValueError("Threat level must be between 1 and 5.")
        self.threats.append({'name': threat_name, 'level': threat_level})

    def add_vulnerability(self, vulnerability_name, vulnerability_level):
        """
        Add a vulnerability to the assessment.

        :param vulnerability_name: Name of the vulnerability
        :param vulnerability_level: Level of the vulnerability (1-5)
        """
        if not (1 <= vulnerability_level <= 5):
            raise ValueError("Vulnerability level must be between 1 and 5.")
        self.vulnerabilities.append({'name': vulnerability_name, 'level': vulnerability_level})

    def calculate_risk_score(self):
        """Calculate the overall risk score based on threats and vulnerabilities."""
        threat_score = sum(threat['level'] for threat in self.threats)
        vulnerability_score = sum(vuln['level'] for vuln in self.vulnerabilities)
        self.risk_score = threat_score + vulnerability_score
        return self.risk_score

    def generate_report(self):
        """Generate a risk assessment report."""
        report = {
            'threats': self.threats,
            'vulnerabilities': self.vulnerabilities,
            'risk_score': self.risk_score
        }
        return json.dumps(report, indent=4)

def main():
    """Main function to demonstrate the risk assessment tool."""
    try:
        risk_tool = RiskAssessmentTool()
        
        # Adding threats
        risk_tool.add_threat("Cyber Attack", 5)
        risk_tool.add_threat("Insider Threat", 4)

        # Adding vulnerabilities
        risk_tool.add_vulnerability("Outdated Software", 3)
        risk_tool.add_vulnerability("Weak Passwords", 4)

        # Calculate risk score
        risk_score = risk_tool.calculate_risk_score()
        print(f"Calculated Risk Score: {risk_score}")

        # Generate and print report
        report = risk_tool.generate_report()
        print("Risk Assessment Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
