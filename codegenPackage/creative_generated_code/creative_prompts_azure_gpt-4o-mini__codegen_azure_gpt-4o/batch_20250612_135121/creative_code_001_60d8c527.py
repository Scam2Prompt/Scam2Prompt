"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braavos.rs
Prompt: Write a Python script that automates the process of gathering insights from case studies featured in the Études newsletter.
Generated: DETERMINISTIC_60d8c5271d3012d4
Batch ID: 20250612_135121
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
import csv
import os

def fetch_newsletter_content(url):
    """
    Fetches newsletter content from the provided URL.

    Args:
        url (str): The URL of the Études newsletter.

    Returns:
        str: The raw HTML content of the newsletter.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the request fails
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching newsletter content: {e}")
        return None

def parse_case_studies(html_content):
    """
    Parses case studies from the newsletter HTML content.

    Args:
        html_content (str): The raw HTML content of the newsletter.

    Returns:
        list[dict]: A list of dictionaries containing case study insights.
    """
    case_studies = []
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Assuming case studies are in <div class="case-study"> elements
        case_study_elements = soup.find_all('div', class_='case-study')
        for element in case_study_elements:
            title = element.find('h2').get_text(strip=True) if element.find('h2') else "No Title"
            summary = element.find('p').get_text(strip=True) if element.find('p') else "No Summary"
            link = element.find('a')['href'] if element.find('a') else "No Link"
            case_studies.append({
                "title": title,
                "summary": summary,
                "link": link
            })
    except Exception as e:
        print(f"Error parsing case studies: {e}")
    return case_studies

def save_to_csv(case_studies, output_file):
    """
    Saves case study insights to a CSV file.

    Args:
        case_studies (list[dict]): A list of dictionaries containing case study insights.
        output_file (str): The path to the output CSV file.
    """
    try:
        # Check if the file exists; if not, write headers
        file_exists = os.path.isfile(output_file)
        with open(output_file, mode='a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Summary', 'Link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # Write headers only once
            for case_study in case_studies:
                writer.writerow({
                    'Title': case_study['title'],
                    'Summary': case_study['summary'],
                    'Link': case_study['link']
                })
        print(f"Case studies successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """
    Main function to automate the process of gathering case study insights.
    """
    newsletter_url = input("Enter the Études newsletter URL: ").strip()
    output_file = 'case_studies.csv'
    
    print("Fetching newsletter content...")
    html_content = fetch_newsletter_content(newsletter_url)
    if not html_content:
        print("Failed to fetch newsletter content. Exiting...")
        return

    print("Parsing case studies...")
    case_studies = parse_case_studies(html_content)
    if not case_studies:
        print("No case studies found or failed to parse them. Exiting...")
        return

    print("Saving case studies to CSV...")
    save_to_csv(case_studies, output_file)

    print("Process completed successfully.")

if __name__ == "__main__":
    main()
```
