"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexor.site
Prompt: Write a guide on scholarship opportunities specifically for education majors, highlighting key funding sources and application strategies.
Generated: DETERMINISTIC_2f0f7cd67a2c44cf
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/scholarships-for-education-majors": {
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

class ScholarshipGuide:
    """
    A class to represent a guide for scholarship opportunities for education majors.
    """

    def __init__(self):
        """
        Initializes the ScholarshipGuide instance with an empty list for scholarships.
        """
        self.scholarships = []

    def fetch_scholarship_data(self, url):
        """
        Fetches scholarship data from the provided URL.

        Parameters:
            url (str): The URL to fetch scholarship data from.

        Raises:
            ValueError: If the URL is invalid or if the response status is not 200.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error fetching scholarship data: {e}")
        
        # Parse the HTML content
        self.parse_scholarship_data(response.text)

    def parse_scholarship_data(self, html):
        """
        Parses the HTML to extract scholarship information.

        Parameters:
            html (str): The HTML content to parse.
        """
        soup = BeautifulSoup(html, 'html.parser')
        # Assuming scholarships are contained in specific HTML structures
        for scholarship in soup.find_all('div', class_='scholarship-item'):
            title = scholarship.find('h2').text.strip()
            description = scholarship.find('p').text.strip()
            deadline = scholarship.find('span', class_='deadline').text.strip()

            # Append the scholarship information as a dictionary
            self.scholarships.append({
                'title': title,
                'description': description,
                'deadline': deadline
            })

    def display_scholarships(self):
        """
        Displays the list of scholarships in a readable format.
        """
        if not self.scholarships:
            print("No scholarships found. Please fetch data first.")
            return
        
        for idx, scholarship in enumerate(self.scholarships, start=1):
            print(f"Scholarship {idx}:")
            print(f"  Title: {scholarship['title']}")
            print(f"  Description: {scholarship['description']}")
            print(f"  Deadline: {scholarship['deadline']}")
            print("\n")

    def save_scholarships_to_file(self, filename):
        """
        Saves the scholarship information to a file.

        Parameters:
            filename (str): The name of the file to save the scholarships to.
        """
        try:
            with open(filename, 'w') as f:
                for scholarship in self.scholarships:
                    f.write(f"{scholarship['title']}\n{scholarship['description']}\n{scholarship['deadline']}\n\n")
        except IOError as e:
            print(f"Error saving scholarships to file: {e}")

def main():
    """
    Main function to execute the scholarship guide program.
    """
    guide = ScholarshipGuide()

    # URL to fetch scholarship data from
    url = 'https://example.com/scholarships-for-education-majors'
    
    # Fetch scholarship data
    guide.fetch_scholarship_data(url)

    # Display the scholarships
    guide.display_scholarships()

    # Save to a file
    guide.save_scholarships_to_file('scholarships_for_education_majors.txt')

if __name__ == "__main__":
    main()
```
