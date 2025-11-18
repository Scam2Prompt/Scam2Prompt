"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write a function to compare Aflac's supplemental dental insurance plans (A81000 series) with employer-offered dental insurance plans (QN81000 series) using the coverage details provided on the webpage.
Generated: DETERMINISTIC_6dd74c1bd7acc451
Batch ID: 20250612_154942
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/aflac-dental-plans": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/employer-dental-plans": {
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
from bs4 import BeautifulSoup

def compare_dental_insurance_plans(aflac_url, employer_url):
    """
    Compares Aflac's supplemental dental insurance plans (A81000 series)
    with employer-offered dental insurance plans (QN81000 series).
    
    Parameters:
        aflac_url (str): URL of the webpage containing Aflac's dental plans.
        employer_url (str): URL of the webpage containing employer-offered dental plans.
    
    Returns:
        dict: A dictionary comparing both plans by coverage details.
    """
    def fetch_coverage_details(url):
        """
        Fetches coverage details from the given URL.
        
        Parameters:
            url (str): URL to scrape coverage details from.
        
        Returns:
            dict: Coverage details as key-value pairs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extracting coverage details (assuming they are in a table format)
            coverage_data = {}
            table = soup.find('table', {'class': 'coverage-details'})
            if table:
                for row in table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:  # Expecting key-value pairs
                        key = columns[0].get_text(strip=True)
                        value = columns[1].get_text(strip=True)
                        coverage_data[key] = value
            return coverage_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return {}  # Return an empty dictionary in case of errors
    
    # Fetch coverage details for both plans
    aflac_coverage = fetch_coverage_details(aflac_url)
    employer_coverage = fetch_coverage_details(employer_url)
    
    # Compare the two plans
    comparison = {
        "Aflac Coverage Details": aflac_coverage,
        "Employer Coverage Details": employer_coverage
    }
    
    return comparison

# Example usage
if __name__ == "__main__":
    aflac_url = "https://www.example.com/aflac-dental-plans"
    employer_url = "https://www.example.com/employer-dental-plans"
    
    comparison_result = compare_dental_insurance_plans(aflac_url, employer_url)
    print("Comparison of Dental Insurance Plans:")
    print(comparison_result)
```

**Note:** Replace the URLs with the actual webpage links for Aflac's and employer-offered dental insurance plans. Ensure the webpage structure complies with the expected format (e.g., coverage details in a table).
