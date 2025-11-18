"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Create a script using BeautifulSoup to scrape the Govt. Shah Sultan College's history section and generate a summary of the college's establishment and milestones.
Generated: DETERMINISTIC_b2b76da20815d9b2
Batch ID: 20250612_151509
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.governmentshahsultancollege.edu/history": {
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

def fetch_college_history(url):
    """
    Fetches the history section of the specified college from the provided URL.
    
    Parameters:
    url (str): The URL of the college's history page.

    Returns:
    str: The text content of the history section.
    """
    try:
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
    
    # Parse the content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Locate the history section - you may need to adjust the selector based on the actual HTML structure
    history_section = soup.find('div', class_='history')  # Replace 'div.history' with the correct selector
    if history_section:
        return history_section.get_text(strip=True)
    else:
        print("History section not found.")
        return None

def summarize_history(history_text):
    """
    Summarizes the extracted history text to highlight establishment and milestones.
    
    Parameters:
    history_text (str): The full history text of the college.

    Returns:
    str: A brief summary of the college's establishment and key milestones.
    """
    # A simple summarization logic - can be enhanced as needed
    summary_lines = []
    for line in history_text.splitlines():
        if 'establish' in line.lower() or 'milestone' in line.lower():
            summary_lines.append(line.strip())
    
    return '\n'.join(summary_lines)

def main():
    """
    Main function to execute the scraping and summarization process.
    """
    url = 'https://www.governmentshahsultancollege.edu/history'  # Replace with the actual URL
    
    # Fetch the college's history text
    history_text = fetch_college_history(url)
    if history_text:
        # Generate and print the summary
        summary = summarize_history(history_text)
        if summary:
            print("Summary of College History:")
            print(summary)
        else:
            print("No significant milestones found in the history.")
    else:
        print("Failed to retrieve history text.")

if __name__ == "__main__":
    main()
```
