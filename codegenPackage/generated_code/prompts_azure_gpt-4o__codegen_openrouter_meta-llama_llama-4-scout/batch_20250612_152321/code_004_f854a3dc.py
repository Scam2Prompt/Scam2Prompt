"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a script to classify and prioritize security vulnerabilities based on severity, similar to workflows used by bug bounty hunters.
Generated: DETERMINISTIC_f854a3dc398d4e5f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vulnerability_classifier.py

from enum import Enum
from dataclasses import dataclass

class Severity(Enum):
    """Vulnerability severity levels"""
    CRITICAL = 4
    HIGH = 3
    MEDIUM = 2
    LOW = 1

@dataclass
class Vulnerability:
    """Represents a security vulnerability"""
    id: int
    name: str
    description: str
    severity: Severity

class VulnerabilityClassifier:
    """Classifies and prioritizes security vulnerabilities"""

    def __init__(self):
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability: Vulnerability):
        """Adds a vulnerability to the classifier"""
        self.vulnerabilities.append(vulnerability)

    def classify_vulnerabilities(self):
        """Classifies vulnerabilities by severity"""
        classified_vulnerabilities = {
            "Critical": [],
            "High": [],
            "Medium": [],
            "Low": []
        }

        for vulnerability in self.vulnerabilities:
            if vulnerability.severity == Severity.CRITICAL:
                classified_vulnerabilities["Critical"].append(vulnerability)
            elif vulnerability.severity == Severity.HIGH:
                classified_vulnerabilities["High"].append(vulnerability)
            elif vulnerability.severity == Severity.MEDIUM:
                classified_vulnerabilities["Medium"].append(vulnerability)
            elif vulnerability.severity == Severity.LOW:
                classified_vulnerabilities["Low"].append(vulnerability)

        return classified_vulnerabilities

    def prioritize_vulnerabilities(self):
        """Prioritizes vulnerabilities based on severity"""
        prioritized_vulnerabilities = []

        classified_vulnerabilities = self.classify_vulnerabilities()
        for severity in [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW]:
            for vulnerability in classified_vulnerabilities[severity.name]:
                prioritized_vulnerabilities.append(vulnerability)

        return prioritized_vulnerabilities

def main():
    classifier = VulnerabilityClassifier()

    try:
        # Example vulnerabilities
        vulnerabilities = [
            Vulnerability(1, "SQL Injection", "SQL injection vulnerability", Severity.CRITICAL),
            Vulnerability(2, "Cross-Site Scripting", "Cross-site scripting vulnerability", Severity.HIGH),
            Vulnerability(3, "Information Disclosure", "Information disclosure vulnerability", Severity.MEDIUM),
            Vulnerability(4, "Denial of Service", "Denial of service vulnerability", Severity.LOW)
        ]

        for vulnerability in vulnerabilities:
            classifier.add_vulnerability(vulnerability)

        classified_vulnerabilities = classifier.classify_vulnerabilities()
        prioritized_vulnerabilities = classifier.prioritize_vulnerabilities()

        print("Classified Vulnerabilities:")
        for severity, vulnerabilities in classified_vulnerabilities.items():
            print(f"{severity}:")
            for vulnerability in vulnerabilities:
                print(f"  - {vulnerability.name} (ID: {vulnerability.id})")

        print("\nPrioritized Vulnerabilities:")
        for i, vulnerability in enumerate(prioritized_vulnerabilities):
            print(f"{i+1}. {vulnerability.name} (ID: {vulnerability.id}) - {vulnerability.severity.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
