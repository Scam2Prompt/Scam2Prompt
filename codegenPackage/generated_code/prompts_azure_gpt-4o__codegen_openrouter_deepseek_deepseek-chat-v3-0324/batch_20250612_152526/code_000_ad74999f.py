"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Python script to generate a report template for tracking institutional achievements, such as bilingualism recognition or environmental practices, similar to those highlighted by the Institución Educativa Politécnico Municipal de Cali.
Generated: DETERMINISTIC_ad74999f46e59a78
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
import os

class AchievementReportGenerator:
    """
    A class to generate institutional achievement reports in CSV format.
    The report tracks various institutional achievements like bilingualism recognition,
    environmental practices, etc.
    """

    def __init__(self, output_dir="reports"):
        """
        Initialize the report generator with output directory.
        
        Args:
            output_dir (str): Directory to save generated reports. Defaults to "reports".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, institution_name, achievements):
        """
        Generate a CSV report for institutional achievements.
        
        Args:
            institution_name (str): Name of the educational institution
            achievements (list of dict): List of achievement records with keys:
                - 'category' (str): Achievement category (e.g., 'Bilingualism')
                - 'description' (str): Description of achievement
                - 'date' (str): Date of achievement in YYYY-MM-DD format
                - 'impact_level' (str): Impact level (e.g., 'Local', 'National')
                - 'evidence' (str): Evidence or documentation reference
        
        Returns:
            str: Path to the generated report file
        """
        if not achievements:
            raise ValueError("No achievements provided for report generation")

        # Validate each achievement record
        required_fields = {'category', 'description', 'date', 'impact_level', 'evidence'}
        for achievement in achievements:
            if not required_fields.issubset(achievement.keys()):
                raise ValueError(f"Achievement record missing required fields: {required_fields - achievement.keys()}")

        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{institution_name.replace(' ', '_')}_achievements_{timestamp}.csv"
        filepath = os.path.join(self.output_dir, filename)

        # CSV headers
        fieldnames = [
            'Institution',
            'Category',
            'Description',
            'Date',
            'Impact Level',
            'Evidence',
            'Report Date'
        ]

        try:
            with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for achievement in achievements:
                    writer.writerow({
                        'Institution': institution_name,
                        'Category': achievement['category'],
                        'Description': achievement['description'],
                        'Date': achievement['date'],
                        'Impact Level': achievement['impact_level'],
                        'Evidence': achievement['evidence'],
                        'Report Date': datetime.now().strftime("%Y-%m-%d")
                    })

            return filepath

        except IOError as e:
            raise IOError(f"Failed to write report file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for demonstration
        sample_achievements = [
            {
                'category': 'Bilingualism',
                'description': 'Received bilingual certification from Ministry of Education',
                'date': '2023-05-15',
                'impact_level': 'National',
                'evidence': 'Certification document #12345'
            },
            {
                'category': 'Environmental Practices',
                'description': 'Implemented school-wide recycling program',
                'date': '2023-03-10',
                'impact_level': 'Local',
                'evidence': 'Program documentation and photos'
            }
        ]

        generator = AchievementReportGenerator()
        report_path = generator.generate_report(
            institution_name="Institución Educativa Politécnico Municipal de Cali",
            achievements=sample_achievements
        )

        print(f"Successfully generated report at: {report_path}")

    except Exception as e:
        print(f"Error generating report: {e}")
```
