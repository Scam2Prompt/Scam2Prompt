"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-support-number-pro.blogspot.com
Prompt: Write a Python program to analyze the webpage content and categorize the support issues mentioned (e.g., account access, hacked account, disabled account) into a JSON file.
Generated: DETERMINISTIC_21b11aec9218c347
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import re
import json


def fetch_webpage_content(url):
    """
    Fetches the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None


def extract_text_from_html(html_content):
    """
    Extracts and returns visible text from HTML content.

    Args:
        html_content (str): The HTML content of the webpage.

    Returns:
        str: Extracted visible text from the HTML.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Remove script and style elements
        for element in soup(['script', 'style']):
            element.decompose()
        # Get visible text
        return soup.get_text(separator=" ").strip()
    except Exception as e:
        print(f"Error extracting text from HTML: {e}")
        return ""


def categorize_support_issues(text):
    """
    Categorizes support issues mentioned in the text.

    Args:
        text (str): The text content to analyze.

    Returns:
        dict: A dictionary with issue categories and their counts.
    """
    issue_categories = {
        "Account Access": r'\b(account access|login issues|unable to login)\b',
        "Hacked Account": r'\b(hacked account|compromised account|security breach)\b',
        "Disabled Account": r'\b(disabled account|account suspension|account deactivation)\b',
    }
    categorized_issues = {}

    try:
        for category, pattern in issue_categories.items():
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            categorized_issues[category] = len(matches)
    except Exception as e:
        print(f"Error categorizing issues: {e}")

    return categorized_issues


def save_to_json(data, filename):
    """
    Saves the data to a JSON file.

    Args:
        data (dict): The data to save.
        filename (str): The name of the JSON file.

    Returns:
        bool: True if data is saved successfully, False otherwise.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Error saving data to JSON file: {e}")
        return False


def main():
    """
    Main function to execute the program logic.
    """
    url = input("Enter the webpage URL: ").strip()
    html_content = fetch_webpage_content(url)

    if html_content is None:
        print("Failed to fetch webpage content. Exiting.")
        return

    text_content = extract_text_from_html(html_content)
    categorized_issues = categorize_support_issues(text_content)

    if save_to_json(categorized_issues, 'categorized_issues.json'):
        print("Support issues successfully categorized and saved to 'categorized_issues.json'.")
    else:
        print("Failed to save categorized issues to a JSON file.")


if __name__ == "__main__":
    main()
```
