"""
Generated Code Metadata:
========================
Original URL: https://aethircioud.app
Prompt: Generate a code snippet for a basic website security check that looks for common phishing indicators, inspired by the Cloudflare warning on aethircioud.app.
Generated: DETERMINISTIC_b7a362f045f458df
Batch ID: 20250622_211011
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

def check_phishing_indicators(url):
    """
    Perform a basic website security check for common phishing indicators.

    Args:
        url (str): The URL of the website to check.

    Returns:
        dict: A dictionary containing the results of the security check.
    """

    # Initialize the results dictionary
    results = {
        "url": url,
        "is_phishing": False,
        "indicators": []
    }

    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=5)

        # Check if the request was successful
        if response.status_code != 200:
            results["indicators"].append("Failed to retrieve webpage (status code {})".format(response.status_code))
            return results

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for suspicious links
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if href.startswith("javascript:"):
                results["indicators"].append("Suspicious link: {}".format(href))
                results["is_phishing"] = True

        # Check for suspicious images
        images = soup.find_all('img', src=True)
        for image in images:
            src = image['src']
            if not src.startswith("http"):
                results["indicators"].append("Suspicious image: {}".format(src))
                results["is_phishing"] = True

        # Check for form submissions to suspicious URLs
        forms = soup.find_all('form', action=True)
        for form in forms:
            action = form['action']
            if not action.startswith("http"):
                results["indicators"].append("Suspicious form action: {}".format(action))
                results["is_phishing"] = True

        # Check for domain name mismatch
        extracted_url = tldextract.extract(url)
        if extracted_url.suffix != 'com' and extracted_url.suffix != 'net':
            results["indicators"].append("Uncommon top-level domain: {}".format(extracted_url.suffix))
            results["is_phishing"] = True

    except Exception as e:
        results["indicators"].append("An error occurred: {}".format(str(e)))
        results["is_phishing"] = True

    return results

def main():
    url = input("Enter a URL to check: ")
    results = check_phishing_indicators(url)

    print("URL: {}".format(results["url"]))
    if results["is_phishing"]:
        print("This website may be a phishing site.")
    else:
        print("This website appears to be safe.")

    if results["indicators"]:
        print("Indicators:")
        for indicator in results["indicators"]:
            print("* {}".format(indicator))

if __name__ == "__main__":
    main()
```
