"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Generate a Python script to scrape course data from an online platform like Teachable, assuming the Sui Foundation adds products in the future.
Generated: DETERMINISTIC_19d846912566dec9
Batch ID: 20250612_154133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.teachable.com/courses": {
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
import json
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class CourseScraper:
    """
    A class to scrape course data from an online platform.
    """

    def __init__(self, base_url):
        """
        Initialize the scraper.

        Args:
            base_url (str): The base URL of the platform to scrape.
        """
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def fetch_page(self, url):
        """
        Fetch the HTML content of a webpage.

        Args:
            url (str): The URL of the page to fetch.

        Returns:
            str: HTML content of the page or None if an error occurred.
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch URL {url}: {e}")
            return None

    def extract_courses(self, html_content):
        """
        Extract course information from the HTML content.

        Args:
            html_content (str): HTML content of the page.

        Returns:
            list[dict]: List of course data dictionaries.
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            courses = []

            # Example structure. Adjust selectors based on platform HTML structure.
            course_elements = soup.find_all('div', class_='course-card')  # Replace 'course-card' with actual class name
            for course in course_elements:
                title = course.find('h3', class_='course-title').text.strip()  # Replace 'course-title' with actual class name
                description = course.find('p', class_='course-description').text.strip()  # Replace 'course-description' with actual class name
                price = course.find('span', class_='course-price').text.strip()  # Replace 'course-price' with actual class name

                courses.append({
                    'title': title,
                    'description': description,
                    'price': price
                })

            return courses
        except Exception as e:
            logging.error(f"Failed to extract course data: {e}")
            return []

    def scrape_courses(self):
        """
        Scrapes course data from the platform.

        Returns:
            list[dict]: List of course data dictionaries.
        """
        logging.info("Starting course scraping...")
        html_content = self.fetch_page(self.base_url)
        if not html_content:
            logging.error("Failed to fetch the base page.")
            return []

        courses = self.extract_courses(html_content)
        logging.info(f"Extracted {len(courses)} courses.")
        return courses

    def save_courses_to_file(self, courses, filename="courses.json"):
        """
        Save course data to a JSON file.

        Args:
            courses (list[dict]): List of course data dictionaries.
            filename (str): File name to save the courses.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(courses, file, indent=4)
            logging.info(f"Saved courses to {filename}")
        except Exception as e:
            logging.error(f"Failed to save courses to file: {e}")

if __name__ == "__main__":
    # Replace the base URL below with the platform's URL to be scraped.
    BASE_URL = "https://example.teachable.com/courses"  # Replace with actual URL

    scraper = CourseScraper(BASE_URL)
    course_data = scraper.scrape_courses()

    if course_data:
        scraper.save_courses_to_file(course_data)
```

Replace the CSS selectors and `BASE_URL` with actual values based on the Teachable platform's HTML structure when products are added in the future. This code provides a framework for scraping, error handling, and saving the data.
