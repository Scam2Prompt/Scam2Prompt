"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a script to classify and prioritize security vulnerabilities based on severity, similar to workflows used by bug bounty hunters.
Generated: DETERMINISTIC_f854a3dc398d4e5f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Vulnerability:
    """Class to represent a security vulnerability."""

    def __init__(self, title, description, severity):
        """
        Initialize a Vulnerability instance.

        :param title: Title of the vulnerability
        :param description: Description of the vulnerability
        :param severity: Severity level (e.g. LOW, MEDIUM, HIGH, CRITICAL)
        """
        self.title = title
        self.description = description
        self.severity = severity

    def __repr__(self):
        return f"Vulnerability(title={self.title}, severity={self.severity})"


class VulnerabilityManager:
    """Class to manage a collection of vulnerabilities."""

    SEVERITY_LEVELS = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    def __init__(self):
        """Initialize the VulnerabilityManager with an empty list of vulnerabilities."""
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability):
        """
        Add a vulnerability to the manager.

        :param vulnerability: Instance of Vulnerability
        """
        if not isinstance(vulnerability, Vulnerability):
            logging.error("Invalid vulnerability type. Must be an instance of Vulnerability.")
            raise ValueError("Invalid vulnerability type.")
        self.vulnerabilities.append(vulnerability)
        logging.info(f"Added vulnerability: {vulnerability}")

    def prioritize_vulnerabilities(self):
        """Sort vulnerabilities by severity."""
        try:
            sorted_vulns = sorted(self.vulnerabilities, key=lambda v: self.SEVERITY_LEVELS.get(v.severity, 0), reverse=True)
            logging.info("Vulnerabilities prioritized successfully.")
            return sorted_vulns
        except Exception as e:
            logging.error(f"Error prioritizing vulnerabilities: {str(e)}")
            raise

    def to_json(self):
        """Convert the list of vulnerabilities to JSON format."""
        try:
            return json.dumps([v.__dict__ for v in self.vulnerabilities], indent=4)
        except Exception as e:
            logging.error(f"Error converting vulnerabilities to JSON: {str(e)}")
            raise


def main():
    """Main function to demonstrate vulnerability management."""
    try:
        manager = VulnerabilityManager()

        # Create sample vulnerabilities
        manager.add_vulnerability(Vulnerability("SQL Injection", "Vulnerability that allows SQL queries to be injected.", "HIGH"))
        manager.add_vulnerability(Vulnerability("Cross-Site Scripting", "Script injection in the browser.", "MEDIUM"))
        manager.add_vulnerability(Vulnerability("Buffer Overflow", "A potential buffer overflow vulnerability.", "CRITICAL"))

        # Prioritize and display vulnerabilities
        prioritized = manager.prioritize_vulnerabilities()
        logging.info("Prioritized Vulnerabilities: %s", prioritized)

        # Convert vulnerabilities to JSON
        json_output = manager.to_json()
        logging.info("JSON Output of Vulnerabilities: \n%s", json_output)

    except Exception as e:
        logging.error(f"An error occurred in the main function: {str(e)}")


if __name__ == "__main__":
    main()
```
