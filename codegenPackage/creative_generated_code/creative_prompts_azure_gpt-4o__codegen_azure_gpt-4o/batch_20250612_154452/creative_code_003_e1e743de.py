"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Create a script to analyze compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018 standards in energy production processes, referencing Omega Energy's adherence to these certifications.
Generated: DETERMINISTIC_e1e743de37cadc11
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to analyze compliance with ISO standards
class ISOComplianceAnalyzer:
    """
    A class to analyze compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018 standards
    in energy production processes.
    """

    def __init__(self, company_name):
        """
        Initializes the compliance analyzer for the specified company.

        Args:
            company_name (str): The name of the company being analyzed.
        """
        self.company_name = company_name
        self.standards = {
            "ISO 9001:2015": {
                "description": "Quality Management Systems",
                "requirements": ["Process efficiency", "Customer satisfaction", "Risk-based thinking"]
            },
            "ISO 14001:2015": {
                "description": "Environmental Management Systems",
                "requirements": ["Pollution prevention", "Sustainable resource use", "Compliance obligations"]
            },
            "ISO 45001:2018": {
                "description": "Occupational Health and Safety Management Systems",
                "requirements": ["Hazard identification", "Worker participation", "Continuous improvement"]
            }
        }
        self.compliance_data = {}

    def load_compliance_data(self, file_path):
        """
        Loads compliance data from a JSON file.

        Args:
            file_path (str): Path to the compliance data file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.compliance_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in compliance data file.")

    def analyze_compliance(self):
        """
        Analyzes compliance with ISO standards based on loaded compliance data.

        Returns:
            dict: A dictionary containing compliance results for each standard.
        """
        if not self.compliance_data:
            raise ValueError("Compliance data is not loaded. Please load data before analyzing.")

        results = {}
        for standard, details in self.standards.items():
            standard_requirements = details["requirements"]
            compliance_score = 0
            for requirement in standard_requirements:
                # Check if the company meets the requirement
                if requirement in self.compliance_data.get("adherence", {}).get(standard, []):
                    compliance_score += 1
            compliance_percentage = (compliance_score / len(standard_requirements)) * 100
            results[standard] = {
                "description": details["description"],
                "compliance_percentage": round(compliance_percentage, 2),
                "requirements_met": compliance_score,
                "total_requirements": len(standard_requirements)
            }
        return results

    def generate_report(self, output_path):
        """
        Generates a compliance report and saves it to a file.

        Args:
            output_path (str): Path to save the compliance report.

        Raises:
            IOError: If the report cannot be written to the specified path.
        """
        try:
            results = self.analyze_compliance()
            report = {
                "company_name": self.company_name,
                "compliance_report": results
            }
            with open(output_path, 'w') as file:
                json.dump(report, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write report to '{output_path}': {e}")

# Example Usage
if __name__ == "__main__":
    analyzer = ISOComplianceAnalyzer(company_name="Omega Energy")
    
    try:
        # Load compliance data from a JSON file
        analyzer.load_compliance_data("compliance_data.json")
        
        # Analyze compliance and generate a report
        analyzer.generate_report("compliance_report.json")
        print("Compliance report generated successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
