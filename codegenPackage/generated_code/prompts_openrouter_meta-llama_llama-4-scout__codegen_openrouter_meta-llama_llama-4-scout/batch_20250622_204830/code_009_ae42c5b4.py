"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-claim.pages.dev
Prompt: "Analyze the security audit reports from SolidProof and InterFi for Kangamoon's smart contract, highlighting key findings and recommendations."
Generated: DETERMINISTIC_ae42c5b4f06b49ee
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class SecurityAuditReportAnalyzer:
    def __init__(self, solidproof_report, interfi_report):
        """
        Initialize the analyzer with security audit reports from SolidProof and InterFi.

        Args:
            solidproof_report (str): Path to SolidProof report JSON file.
            interfi_report (str): Path to InterFi report JSON file.
        """
        self.solidproof_report = self.load_report(solidproof_report)
        self.interfi_report = self.load_report(interfi_report)

    def load_report(self, report_path):
        """
        Load a security audit report from a JSON file.

        Args:
            report_path (str): Path to the report JSON file.

        Returns:
            dict: Loaded report data.

        Raises:
            FileNotFoundError: If the report file does not exist.
            json.JSONDecodeError: If the report file is not valid JSON.
        """
        try:
            with open(report_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Report file '{report_path}' not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse report file '{report_path}': {e}")
            return {}

    def analyze_solidproof_report(self):
        """
        Analyze the SolidProof security audit report.

        Returns:
            dict: Key findings and recommendations.
        """
        findings = self.solidproof_report.get('findings', [])
        recommendations = []

        for finding in findings:
            severity = finding.get('severity')
            description = finding.get('description')
            recommendation = finding.get('recommendation')

            if severity == 'high':
                recommendations.append({
                    'severity': severity,
                    'description': description,
                    'recommendation': recommendation
                })

        return {
            'key_findings': len(findings),
            'recommendations': recommendations
        }

    def analyze_interfi_report(self):
        """
        Analyze the InterFi security audit report.

        Returns:
            dict: Key findings and recommendations.
        """
        findings = self.interfi_report.get('findings', [])
        recommendations = []

        for finding in findings:
            severity = finding.get('severity')
            description = finding.get('description')
            recommendation = finding.get('recommendation')

            if severity == 'high':
                recommendations.append({
                    'severity': severity,
                    'description': description,
                    'recommendation': recommendation
                })

        return {
            'key_findings': len(findings),
            'recommendations': recommendations
        }

    def compare_reports(self):
        """
        Compare the security audit reports from SolidProof and InterFi.

        Returns:
            dict: Comparison of key findings and recommendations.
        """
        solidproof_analysis = self.analyze_solidproof_report()
        interfi_analysis = self.analyze_interfi_report()

        return {
            'solidproof': solidproof_analysis,
            'interfi': interfi_analysis
        }

def main():
    solidproof_report_path = 'solidproof_report.json'
    interfi_report_path = 'interfi_report.json'

    analyzer = SecurityAuditReportAnalyzer(solidproof_report_path, interfi_report_path)
    comparison = analyzer.compare_reports()

    print(json.dumps(comparison, indent=4))

if __name__ == '__main__':
    main()
```
