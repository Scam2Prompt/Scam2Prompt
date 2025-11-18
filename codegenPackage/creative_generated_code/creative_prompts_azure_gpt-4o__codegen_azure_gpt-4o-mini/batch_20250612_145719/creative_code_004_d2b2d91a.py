"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Write code to analyze geographic metadata (e.g., `city`, `region`, `postalCode`) in a network security report, using the structure provided by netsecurity.pages.dev.
Generated: DETERMINISTIC_d2b2d91a934bf9cb
Batch ID: 20250612_145719
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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeoMetadataAnalyzer:
    """
    A class to analyze geographic metadata from network security reports.
    """

    def __init__(self, report_data: str):
        """
        Initializes the GeoMetadataAnalyzer with raw report data.

        :param report_data: JSON string containing network security report.
        """
        self.report_data = report_data
        self.metadata: List[Dict[str, Any]] = []

    def parse_report(self) -> None:
        """
        Parses the network security report and extracts geographic metadata.
        """
        try:
            # Load the JSON data
            data = json.loads(self.report_data)
            logging.info("Report data loaded successfully.")

            # Extract geographic metadata
            for entry in data.get('networkSecurityReports', []):
                geo_info = {
                    "city": entry.get("city"),
                    "region": entry.get("region"),
                    "postalCode": entry.get("postalCode")
                }
                self.metadata.append(geo_info)

            logging.info("Geographic metadata extracted: %s", self.metadata)

        except json.JSONDecodeError as e:
            logging.error("Failed to decode JSON data: %s", e)
            raise ValueError("Invalid report data format.") from e

    def analyze_metadata(self) -> Dict[str, int]:
        """
        Analyzes the collected geographic metadata and returns statistics.

        :return: A dictionary with counts of occurrences for each city.
        """
        city_count = {}
        
        for entry in self.metadata:
            city = entry.get("city")
            if city:
                city_count[city] = city_count.get(city, 0) + 1
        
        logging.info("City analysis complete: %s", city_count)
        return city_count

    def get_report(self) -> Dict[str, int]:
        """
        Generates a report of the geographic analysis.

        :return: A dictionary containing analysis results.
        """
        self.parse_report()  # Ensure the report is parsed before analysis
        return self.analyze_metadata()


# Example usage
if __name__ == "__main__":
    # Sample JSON report data as a string
    sample_report_data = '''
    {
        "networkSecurityReports": [
            {"city": "New York", "region": "NY", "postalCode": "10001"},
            {"city": "Los Angeles", "region": "CA", "postalCode": "90001"},
            {"city": "New York", "region": "NY", "postalCode": "10002"}
        ]
    }
    '''

    # Create an instance of GeoMetadataAnalyzer
    analyzer = GeoMetadataAnalyzer(sample_report_data)
    
    try:
        # Get and print the analysis report
        report = analyzer.get_report()
        print("Geographic Analysis Report:", report)
    except ValueError as e:
        logging.error("An error occurred during analysis: %s", e)
```
