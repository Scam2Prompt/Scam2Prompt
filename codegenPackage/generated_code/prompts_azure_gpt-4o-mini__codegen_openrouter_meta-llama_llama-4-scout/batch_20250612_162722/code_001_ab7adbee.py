"""
Generated Code Metadata:
========================
Original URL: https://appeal-polyhedra.app
Prompt: Write a Python script that checks URLs for phishing indicators, referencing the warning system used by Cloudflare for sites like appeal-polyhedra.app.
Generated: DETERMINISTIC_ab7adbeeb0006b26
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import tldextract
import re

def check_phishing_indicators(url):
    """
    Checks a URL for phishing indicators based on Cloudflare's warning system.

    Args:
        url (str): The URL to check.

    Returns:
        dict: A dictionary containing the results of the phishing check.
    """

    # Initialize the results dictionary
    results = {
        'phishing': False,
        'reasons': []
    }

    try:
        # Extract the domain from the URL
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"

        # Check for unusual or suspicious TLDs
        suspicious_tlds = ['ru', 'cn', 'biz', 'info']
        if extracted.suffix in suspicious_tlds:
            results['phishing'] = True
            results['reasons'].append(f"Suspicious TLD: {extracted.suffix}")

        # Check for numbers in the domain
        if re.search(r'\d', domain):
            results['phishing'] = True
            results['reasons'].append(f"Domain contains numbers: {domain}")

        # Check for hyphens in the domain
        if '-' in domain:
            results['phishing'] = True
            results['reasons'].append(f"Domain contains hyphens: {domain}")

        # Check for unusual or suspicious keywords in the URL
        suspicious_keywords = ['free', 'urgent', 'verify', 'update']
        for keyword in suspicious_keywords:
            if keyword in url.lower():
                results['phishing'] = True
                results['reasons'].append(f"Suspicious keyword: {keyword}")

        # Fetch the page content using requests
        response = requests.get(url, timeout=5)

        # If the request was successful, parse the HTML content
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Check for common phishing patterns in the HTML content
            for tag in soup.find_all(['title', 'h1', 'h2', 'p']):
                if 'login' in tag.text.lower() or 'password' in tag.text.lower():
                    results['phishing'] = True
                    results['reasons'].append(f"Potential login form: {tag.text.strip()}")

        else:
            results['reasons'].append(f"Failed to retrieve page: {response.status_code}")

    except requests.RequestException as e:
        results['reasons'].append(f"Request error: {e}")

    return results

def main():
    url = input("Enter a URL to check: ")
    results = check_phishing_indicators(url)

    if results['phishing']:
        print(f"URL {url} may be a phishing site:")
        for reason in results['reasons']:
            print(f"- {reason}")
    else:
        print(f"URL {url} appears to be safe.")

if __name__ == "__main__":
    main()
```
