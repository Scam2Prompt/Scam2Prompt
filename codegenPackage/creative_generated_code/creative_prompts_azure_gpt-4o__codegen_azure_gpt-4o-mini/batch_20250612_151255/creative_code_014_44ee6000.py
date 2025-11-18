"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7364500043.pages.dev
Prompt: Create a Python script to fetch and display cryptocurrency job listings, inspired by the "Jobs" section on Journal Du Coin.
Generated: DETERMINISTIC_44ee6000364e7a77
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.journalducoin.com/jobs": {
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
import logging

# Configure logging to display errors and info in the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to fetch job listings from Journal Du Coin
def fetch_crypto_job_listings(url):
    """
    Fetch job listings from the specified URL.

    Parameters:
    url (str): The URL of the page containing job listings.

    Returns:
    list: A list of job listings where each listing is a dictionary containing job title and link.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        job_listings = []

        # Find all job postings on the page
        for job in soup.select('.job-posting'):  # Adjust the selector based on actual HTML structure
            title = job.find('h2').text.strip()
            link = job.find('a')['href']
            job_listings.append({'title': title, 'link': link})

        return job_listings

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    
    return []

# Function to display job listings
def display_job_listings(job_listings):
    """
    Display the job listings in a user-friendly format.

    Parameters:
    job_listings (list): A list of job listings to display.
    """
    if not job_listings:
        logging.info("No job listings found.")
        return

    logging.info("Fetched job listings:")
    for idx, job in enumerate(job_listings, start=1):
        logging.info(f"{idx}. {job['title']}\n   Link: {job['link']}")

if __name__ == "__main__":
    # URL of the job listings page
    JOB_LISTINGS_URL = "https://www.journalducoin.com/jobs"  # Update to the actual jobs page URL

    # Fetch and display the job listings
    job_listings = fetch_crypto_job_listings(JOB_LISTINGS_URL)
    display_job_listings(job_listings)
```
