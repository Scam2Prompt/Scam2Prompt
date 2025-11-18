"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Provide code examples for creating a web scraping tool to extract cybersecurity course details, such as the "9 Online Cyber Security Courses for $49.99" mentioned on Blue Training Academy.
Generated: DETERMINISTIC_9470d4fa1a357269
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/cybersecurity-courses": {
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

class CyberSecurityCourseScraper:
    def __init__(self, url):
        """
        Initializes the scraper with the provided URL.

        :param url: str - The URL of the page to scrape.
        """
        self.url = url

    def fetch_page(self):
        """
        Fetches the content of the page.

        :return: str - The HTML content of the page.
        :raises Exception: If the request to the URL fails.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch page: {e}")

    def parse_courses(self, html):
        """
        Parses the HTML to extract course details.

        :param html: str - The HTML content of the page.
        :return: list - A list of course details.
        """
        soup = BeautifulSoup(html, 'html.parser')
        courses = []

        # Adjust the selector based on the actual HTML structure of the page
        course_elements = soup.select('.course-listing')  # Example selector
        for element in course_elements:
            title = element.select_one('.course-title').get_text(strip=True)
            price = element.select_one('.course-price').get_text(strip=True)
            courses.append({'title': title, 'price': price})

        return courses

    def scrape(self):
        """
        Scrapes the course details from the specified URL.

        :return: list - A list of dictionaries containing course details.
        :raises Exception: If any error occurs during scraping.
        """
        html = self.fetch_page()
        return self.parse_courses(html)

if __name__ == "__main__":
    # Example URL to be replaced with the actual page URL
    url = "https://example.com/cybersecurity-courses"
    
    scraper = CyberSecurityCourseScraper(url)
    try:
        courses = scraper.scrape()
        for course in courses:
            print(f"Course Title: {course['title']}, Price: {course['price']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note**: Replace the placeholder URL and CSS selectors with the actual ones from the page you are scraping.
