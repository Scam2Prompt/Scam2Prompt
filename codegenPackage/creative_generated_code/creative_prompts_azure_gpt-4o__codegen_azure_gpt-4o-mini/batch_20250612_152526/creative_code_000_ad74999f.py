"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Python script to generate a report template for tracking institutional achievements, such as bilingualism recognition or environmental practices, similar to those highlighted by the Institución Educativa Politécnico Municipal de Cali.
Generated: DETERMINISTIC_ad74999f46e59a78
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

class AchievementReport:
    """
    A class to generate a report template for tracking institutional achievements.
    """

    def __init__(self, institution_name):
        """
        Initializes the AchievementReport with the institution name.

        :param institution_name: Name of the institution for the report
        """
        self.institution_name = institution_name
        self.report_data = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_achievement(self, date, achievement_type, description):
        """
        Adds an achievement entry to the report data.

        :param date: Date of the achievement
        :param achievement_type: Type of achievement (e.g., bilingualism, environmental practice)
        :param description: Description of the achievement
        """
        if not isinstance(date, str) or not isinstance(achievement_type, str) or not isinstance(description, str):
            raise ValueError("All parameters must be of type 'str'.")

        self.report_data.append({
            "Date": date,
            "Achievement Type": achievement_type,
            "Description": description
        })

    def generate_report(self):
        """
        Generates a report in the form of a pandas DataFrame.

        :return: DataFrame containing the report data
        """
        if not self.report_data:
            raise ValueError("No achievements have been added to the report.")
        
        report_df = pd.DataFrame(self.report_data)
        report_df.index += 1  # Start index at 1 for readability

        # Add institution name and timestamp as metadata
        report_summary = {
            "Institution Name": self.institution_name,
            "Generated On": self.timestamp
        }

        return report_summary, report_df

    def save_report(self, filename):
        """
        Saves the report to a CSV file.

        :param filename: Filename for the report CSV
        """
        try:
            report_summary, report_df = self.generate_report()
            summary_df = pd.DataFrame([report_summary])
            # Save both summary and report data to CSV
            with pd.ExcelWriter(filename) as writer:
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
                report_df.to_excel(writer, sheet_name='Achievements', index=True)
            print(f"Report saved successfully to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the report for the institution
        report = AchievementReport("Institución Educativa Politécnico Municipal de Cali")
        
        # Adding achievements
        report.add_achievement("2023-01-15", "Bilingualism Recognition", "Received recognition for bilingual education program.")
        report.add_achievement("2023-03-10", "Sustainability Initiative", "Launched a new recycling program in the campus.")
        
        # Generate and save the report
        report.save_report("achievement_report.xlsx")
    except Exception as e:
        print(f"An error occurred: {e}")
```
