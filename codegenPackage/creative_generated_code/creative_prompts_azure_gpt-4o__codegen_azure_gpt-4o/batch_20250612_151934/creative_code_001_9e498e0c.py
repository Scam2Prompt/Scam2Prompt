"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Generate code to create a web scraper that extracts course details, such as "DAE Textile Weaving" and "BS Textile," from the SMA Rizvi Textile Institute webpage.
Generated: DETERMINISTIC_9e498e0c14d64ddc
Batch ID: 20250612_151934
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.smarizvi.com": {
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

def scrape_courses(url):
    """
    Scrapes course details from the SMA Rizvi Textile Institute webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of course names extracted from the webpage.
    """
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract course details based on HTML structure
        # Change the CSS selector below based on the actual webpage structure
        course_elements = soup.select('.course-title')  # Example selector: Adjust based on the webpage
        
        # Extract and clean course names
        courses = [course.text.strip() for course in course_elements]

        return courses

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred while fetching the webpage: {e}")
        return []
    except Exception as e:
        # Handle parsing or other errors
        print(f"An error occurred while processing the webpage content: {e}")
        return []

if __name__ == "__main__":
    # URL of the SMA Rizvi Textile Institute webpage
    url = "https://www.smarizvi.com"  # Replace with the actual URL

    # Scrape the courses from the webpage
    course_list = scrape_courses(url)

    if course_list:
        print("Courses offered:")
        for course in course_list:
            print(f"- {course}")
    else:
        print("No courses found or an error occurred.")
```

### Notes:
- Replace the URL `"https://www.smarizvi.com"` with the actual URL of the SMA Rizvi Textile Institute webpage.
- Update the CSS selector `'.course-title'` in the `soup.select()` method to match the actual structure of the webpage. Use browser developer tools (e.g., Inspect Element) to identify the appropriate HTML tags and classes.
