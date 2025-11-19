"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Write a Python script that retrieves and displays information about the "Técnico Superior Universitario en Higienista Dental" program from the INESO website, focusing on duration and job opportunities.
Generated: DETERMINISTIC_1c634a02e0ecdfad
Batch ID: 20250612_162502
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
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

def fetch_program_info(url, program_name):
    """
    Fetches information about a specific educational program from a website.

    Args:
        url (str): The URL of the website to scrape.
        program_name (str): The name of the program to search for.

    Returns:
        dict: A dictionary containing program information, including its duration and job opportunities.
    """
    try:
        # Send a GET request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the response code is not 200
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

    try:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the section containing the program information
        program_section = soup.find('section', string=lambda text: text and program_name in text)
        if not program_section:
            print(f"Program '{program_name}' not found on the website.")
            return None

        # Extract the duration and job opportunities
        duration = program_section.find('p', class_='duration').text.strip()
        job_opportunities = program_section.find('p', class_='job-opportunities').text.strip()

        # Return the extracted information as a dictionary
        return {
            "Program Name": program_name,
            "Duration": duration,
            "Job Opportunities": job_opportunities
        }

    except Exception as e:
        print(f"Error processing the website content: {e}")
        return None


def main():
    """
    Main function to retrieve and display program information.
    """
    # URL of the INESO website
    ineso_url = 'https://www.example.com'  # Replace with the actual URL

    # Name of the program to search for
    program_name = "Técnico Superior Universitario en Higienista Dental"

    # Fetch program information
    program_info = fetch_program_info(ineso_url, program_name)

    # Display the result
    if program_info:
        print("Program Information:")
        for key, value in program_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve program information.")


# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:** Replace `'https://www.example.com'` with the actual URL of the INESO website. Also, ensure the HTML structure and class names (e.g., `'duration'`, `'job-opportunities'`) are accurate based on the website's source code. Adjust the selectors as needed.
