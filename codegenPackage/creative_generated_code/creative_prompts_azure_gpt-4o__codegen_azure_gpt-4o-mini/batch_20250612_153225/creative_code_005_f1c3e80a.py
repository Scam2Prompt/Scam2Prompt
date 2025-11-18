"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lojaoficial.cloud
Prompt: Write a function to fetch and display case studies and articles from the Études website, highlighting architectural insights and design innovations.
Generated: DETERMINISTIC_f1c3e80adf0e80b1
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://etudes.com/articles": {
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

def fetch_case_studies_and_articles(url):
    """
    Fetches case studies and articles from the specified URL of the Études website
    and returns a list of dictionaries containing title and summary.

    Parameters:
    url (str): The URL of the Études website to fetch data from.

    Returns:
    list: A list of dictionaries with 'title' and 'summary' of each item.
    """
    try:
        # Send a request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all case studies and articles sections
        articles = soup.find_all(class_='article-class')  # Replace with actual class name
        
        case_studies = []
        for article in articles:
            title = article.find(class_='title-class').get_text(strip=True)  # Replace with actual class name
            summary = article.find(class_='summary-class').get_text(strip=True)  # Replace with actual class name
            
            case_studies.append({
                'title': title,
                'summary': summary
            })

        return case_studies

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors
    return []  # Return an empty list if an error occurs

def display_case_studies(case_studies):
    """
    Displays the case studies in a readable format.

    Parameters:
    case_studies (list): A list of case study dictionaries to display.
    """
    if not case_studies:
        print("No case studies found.")
        return

    for idx, case_study in enumerate(case_studies, start=1):
        print(f"{idx}. {case_study['title']}")
        print(f"   Summary: {case_study['summary']}\n")

# Example usage
if __name__ == "__main__":
    url = "https://etudes.com/articles"  # Replace with the actual URL
    case_studies = fetch_case_studies_and_articles(url)
    display_case_studies(case_studies)
```
