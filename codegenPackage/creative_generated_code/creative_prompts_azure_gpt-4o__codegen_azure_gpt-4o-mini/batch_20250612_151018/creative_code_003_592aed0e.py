"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Create a shareable link generator for a COVID-19 data visualization tool, ensuring the link includes parameters like selected region, scale, and data type as described on the webpage.
Generated: DETERMINISTIC_592aed0e50e0439d
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://covid19dataviztool.com": {
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
from urllib.parse import urlencode, urljoin

class ShareableLinkGenerator:
    """
    A class to generate shareable links for a COVID-19 data visualization tool.
    """

    BASE_URL = "https://covid19dataviztool.com"  # Base URL for the data visualization tool

    def __init__(self, region: str, scale: str, data_type: str):
        """
        Initialize the link generator with the required parameters.

        :param region: The selected region for data visualization (e.g., country or state).
        :param scale: The scale for the visualization (e.g., daily, cumulative).
        :param data_type: The type of data to visualize (e.g., cases, deaths, vaccinations).
        """
        self.region = region
        self.scale = scale
        self.data_type = data_type

    def validate_parameters(self):
        """
        Validate the parameters before generating the link.
        
        :raises ValueError: If any of the parameters are invalid.
        """
        if not self.region:
            raise ValueError("Region must be provided.")
        if self.scale not in ['daily', 'cumulative']:
            raise ValueError("Scale must be either 'daily' or 'cumulative'.")
        if self.data_type not in ['cases', 'deaths', 'vaccinations']:
            raise ValueError("Data type must be one of 'cases', 'deaths', or 'vaccinations'.")

    def generate_link(self) -> str:
        """
        Generate a shareable link with the specified parameters.

        :return: A string containing the complete shareable link.
        """
        # Validate parameters before generating the link
        self.validate_parameters()

        # Create a dictionary of query parameters
        params = {
            'region': self.region,
            'scale': self.scale,
            'data_type': self.data_type
        }

        # Build the complete URL with query parameters
        shareable_link = urljoin(self.BASE_URL, 'visualization') + '?' + urlencode(params)
        return shareable_link


# Example usage of the ShareableLinkGenerator
if __name__ == "__main__":
    try:
        # Instantiate the link generator with example parameters
        generator = ShareableLinkGenerator(region='USA', scale='daily', data_type='cases')
        
        # Generate the shareable link
        link = generator.generate_link()
        
        print("Shareable Link:", link)
    
    except ValueError as e:
        print("Error:", e)
```
