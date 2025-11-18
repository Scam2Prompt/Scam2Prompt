"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write code to generate a report comparing the properties of organic pigments (e.g., green, violet, blue) and inorganic pigments (e.g., ultramarine, anti-corrosive), as described on the M J Pigment & Additives website.
Generated: DETERMINISTIC_b28e9dad0e4d875f
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.mjpigments.com/pigments": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup

class PigmentReportGenerator:
    """A class to generate a report comparing properties of organic and inorganic pigments."""

    def __init__(self, url):
        """Initialize the class with the URL of the pigment information page."""
        self.url = url
        self.pigment_data = None

    def fetch_data(self):
        """Fetch pigment data from the specified URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def parse_data(self, html_content):
        """Parse the HTML content to extract pigment information."""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            pigments = []

            # Example logic to extract pigment data (modify as needed based on actual HTML structure)
            for pigment_section in soup.find_all('div', class_='pigment-section'):
                name = pigment_section.find('h2').text.strip()
                properties = {
                    'color': pigment_section.find('span', class_='color').text.strip(),
                    'type': pigment_section.find('span', class_='type').text.strip(),
                    'lightfastness': pigment_section.find('span', class_='lightfastness').text.strip(),
                    'chemical_stability': pigment_section.find('span', class_='chemical-stability').text.strip()
                }
                pigments.append({'name': name, **properties})

            self.pigment_data = pd.DataFrame(pigments)
        except Exception as e:
            print(f"Error parsing data: {e}")

    def generate_report(self):
        """Generate a comparative report of the pigments."""
        if self.pigment_data is None:
            print("No pigment data to generate report.")
            return

        # Separate organic and inorganic pigments
        organic_pigments = self.pigment_data[self.pigment_data['type'] == 'Organic']
        inorganic_pigments = self.pigment_data[self.pigment_data['type'] == 'Inorganic']

        # Generate comparison report
        report = {
            'Organic Pigments': organic_pigments.describe(),
            'Inorganic Pigments': inorganic_pigments.describe()
        }
        
        return report

    def save_report(self, report, filename):
        """Save the report to a CSV file."""
        try:
            report_df = pd.concat(report.values(), keys=report.keys())
            report_df.to_csv(filename)
            print(f"Report saved as {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")

def main():
    """Main function to execute the pigment report generation."""
    url = "https://www.mjpigments.com/pigments"  # Replace with the actual URL
    report_generator = PigmentReportGenerator(url)
    
    html_content = report_generator.fetch_data()
    if html_content:
        report_generator.parse_data(html_content)
        report = report_generator.generate_report()
        
        if report:
            report_generator.save_report(report, 'pigment_comparison_report.csv')

if __name__ == "__main__":
    main()
```
