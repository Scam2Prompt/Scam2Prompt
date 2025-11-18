"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Write code to generate a report summarizing the benefits of Cummins engines for automotive and industrial use, referencing the reliability and support network described by Indusur.
Generated: DETERMINISTIC_ba5a767a16f9b9f1
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CumminsEngineReport:
    """
    A class to generate a comprehensive report summarizing the benefits of Cummins engines 
    for automotive and industrial use.
    """

    def __init__(self):
        """
        Initializes the report generator with predefined benefits data.
        """
        self.report_title = "Cummins Engines: Summary of Benefits"
        self.benefits = {
            "Automotive Use": [
                "High reliability ensures consistent performance.",
                "Exceptional fuel efficiency reduces operating costs.",
                "Wide range of engine options for various vehicle types."
            ],
            "Industrial Use": [
                "Robust design suited for heavy-duty applications.",
                "Proven durability under extreme conditions.",
                "Comprehensive product support from the Indusur network."
            ]
        }
        self.support_network = "Indusur Network"
        self.date_generated = datetime.datetime.now()

    def generate_report(self):
        """
        Generates the report summarizing the benefits of Cummins engines.
        
        Returns:
            str: A formatted report highlighting the benefits for automotive and industrial use.
        """
        try:
            # Prepare report content
            report = []
            report.append("=" * 50)
            report.append(f"{self.report_title}")
            report.append(f"Date Generated: {self.date_generated.strftime('%Y-%m-%d %H:%M:%S')}")
            report.append("=" * 50)
            report.append("\nBenefits of Cummins Engines:")
            
            for category, category_benefits in self.benefits.items():
                report.append(f"\n{category}:")
                for benefit in category_benefits:
                    report.append(f"- {benefit}")
            
            report.append("\n\nSupport Network:")
            report.append(f"The benefits are supported by the {self.support_network}, ensuring reliable product availability and expert assistance worldwide.")
            report.append("=" * 50)
            
            return "\n".join(report)
        
        except Exception as e:
            # Handle unexpected errors during report generation
            return f"An error occurred while generating the report: {str(e)}"

    def save_report_to_file(self, file_path):
        """
        Saves the generated report to a text file.
        
        Args:
            file_path (str): The path where the report file should be saved.
        """
        try:
            report_content = self.generate_report()
            with open(file_path, 'w') as file:
                file.write(report_content)
            print(f"Report successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the report to file: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the CumminsEngineReport class
    report_generator = CumminsEngineReport()
    
    # Generate the report and display it
    print(report_generator.generate_report())
    
    # Save the report to a file
    report_generator.save_report_to_file("Cummins_Engine_Report.txt")
```
