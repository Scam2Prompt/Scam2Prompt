"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: Create a Python script to extract and organize data about the "Másteres Online Oficiales UCH-CEU" offered by Unimel Educación, including course names and certification details.
Generated: DETERMINISTIC_23e0cb2214ddaf4c
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.unimel.edu/masters-online-oficiales-uch-ceu": {
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
import pandas as pd

# URL of the webpage to scrape
URL = "https://www.unimel.edu/masters-online-oficiales-uch-ceu"  # Placeholder URL

def fetch_course_data(url):
    """
    Fetches course data from the specified URL.

    Parameters:
    url (str): The URL to scrape.

    Returns:
    list: A list of dictionaries containing course names and certification details.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the course data (HTML structure is assumed)
        courses = soup.find_all('div', class_='course')  # Adjust selector as needed

        course_data = []
        
        # Iterate through each course and extract details
        for course in courses:
            name = course.find('h2', class_='course-name').get_text(strip=True)
            certification = course.find('p', class_='certification-details').get_text(strip=True)

            # Append the extracted data to the list
            course_data.append({
                'Course Name': name,
                'Certification Details': certification
            })

        return course_data

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def save_to_csv(data, filename='courses.csv'):
    """
    Saves the extracted course data to a CSV file.

    Parameters:
    data (list): The course data to save.
    filename (str): The name of the CSV file.
    """
    try:
        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Fetch course data
    course_data = fetch_course_data(URL)

    # Check if any data was retrieved
    if course_data:
        # Save the data to a CSV file
        save_to_csv(course_data)
    else:
        print("No course data to save.")

if __name__ == "__main__":
    main()
```

This script fetches and organizes data about the "Másteres Online Oficiales UCH-CEU" from a specified URL, extracting course names and certification details, and saves the data to a CSV file. Adjust the URL and HTML selectors according to the actual webpage structure.
