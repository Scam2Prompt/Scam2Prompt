"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pledge-moso.app
Prompt: Write a Python script that detects phishing attempts by analyzing URLs and checking them against a list of known phishing sites.
Generated: DETERMINISTIC_52b0bf1b1736a4b1
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import requests

def is_valid_url(url):
    """
    Validates the format of a URL using regex.
    :param url: URL string to validate
    :return: True if valid, False otherwise
    """
    url_pattern = re.compile(
        r'^(https?:\/\/)?'  # Optional http or https
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # Domain name
        r'(\/[a-zA-Z0-9-.]*)*$'  # Optional path
    )
    return re.match(url_pattern, url) is not None


def check_phishing(url, phishing_sites):
    """
    Checks whether the given URL is a known phishing site.
    :param url: URL string to check
    :param phishing_sites: Set of known phishing site URLs
    :return: True if the URL is a phishing site, False otherwise
    """
    return url in phishing_sites


def load_phishing_sites(file_path):
    """
    Loads the list of phishing sites from a file.
    :param file_path: Path to the file containing phishing URLs
    :return: Set of phishing site URLs
    """
    try:
        with open(file_path, 'r') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()
    except Exception as e:
        print(f"Error occurred while loading phishing sites: {e}")
        return set()


def main():
    """
    Main function to detect phishing URLs.
    """
    # Path to the file containing known phishing sites
    phishing_sites_file = "phishing_sites.txt"

    # Load phishing sites
    phishing_sites = load_phishing_sites(phishing_sites_file)
    if not phishing_sites:
        print("No phishing sites loaded. Exiting.")
        return

    # Prompt user for a URL to check
    url = input("Enter a URL to check: ").strip()

    # Validate URL format
    if not is_valid_url(url):
        print("Error: The entered URL is not valid.")
        return

    # Check if the URL is a phishing site
    if check_phishing(url, phishing_sites):
        print("Warning: The URL is a known phishing site!")
    else:
        print("The URL does not match any known phishing sites.")


if __name__ == "__main__":
    main()
```

- Save the phishing sites list in a file named `phishing_sites.txt`, one URL per line, for the script to check against.
- Execute the script, and it will validate and check URLs against the list.
