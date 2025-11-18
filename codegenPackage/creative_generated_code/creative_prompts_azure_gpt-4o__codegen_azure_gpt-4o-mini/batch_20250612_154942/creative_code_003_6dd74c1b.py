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
  "https://example.com/aflac-dental-plans": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/employer-dental-plans": {
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

def fetch_insurance_data(url):
    """
    Fetches insurance plan data from the provided URL.

    Parameters:
    url (str): The URL of the webpage to scrape.

    Returns:
    dict: A dictionary containing insurance plan details.

    Raises:
    requests.exceptions.RequestException: If there is an error in the HTTP request.
    ValueError: If the expected data is not found on the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch data from {url}: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming coverage details are in a specific table format
    plans = {}
    table = soup.find('table', {'id': 'insurance-plans'})
    
    if not table:
        raise ValueError("Unable to find the insurance plans table on the webpage.")

    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) < 3:  # Adjust based on expected number of columns
            continue
        plan_type = columns[0].text.strip()
        coverage_details = columns[1].text.strip()
        plans[plan_type] = coverage_details

    return plans

def compare_plans(aflac_url, employer_url):
    """
    Compares Aflac's supplemental dental insurance plans with employer-offered plans.

    Parameters:
    aflac_url (str): The URL to fetch Aflac's insurance plans.
    employer_url (str): The URL to fetch employer-offered insurance plans.

    Returns:
    dict: A dictionary containing the comparison results.
    """
    aflac_plans = fetch_insurance_data(aflac_url)
    employer_plans = fetch_insurance_data(employer_url)

    comparison_results = {}

    for plan, details in aflac_plans.items():
        comparison_results[plan] = {
            'Aflac Coverage': details,
            'Employer Coverage': employer_plans.get(plan, 'Not Offered')
        }

    return comparison_results

if __name__ == '__main__':
    aflac_url = 'https://example.com/aflac-dental-plans'
    employer_url = 'https://example.com/employer-dental-plans'

    try:
        result = compare_plans(aflac_url, employer_url)
        for plan, details in result.items():
            print(f"Plan: {plan}")
            print(f"Aflac Coverage: {details['Aflac Coverage']}")
            print(f"Employer Coverage: {details['Employer Coverage']}\n")
    except Exception as e:
        print(f"Error during comparison: {e}")
```
