"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Create a Python script that retrieves and displays client testimonials for a photography service, focusing on user experiences similar to those found on the Perth Real Estate Photography site.
Generated: DETERMINISTIC_5318ae1f4cc6ebd2
Batch ID: 20250612_161353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.perthrealestatephotography.com/testimonials": {
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
from requests.exceptions import HTTPError

class TestimonialRetriever:
    """
    A class to retrieve and display client testimonials for a photography service.
    """

    def __init__(self, api_url):
        """
        Initializes the TestimonialRetriever with the API URL.
        
        Parameters:
            api_url (str): The URL of the API endpoint to fetch testimonials.
        """
        self.api_url = api_url

    def fetch_testimonials(self):
        """
        Fetches testimonials from the API.

        Returns:
            list: A list of testimonials if the request is successful, otherwise an empty list.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Assumes the response is in JSON format
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
        return []  # Return an empty list if an error occurs

    def display_testimonials(self, testimonials):
        """
        Displays the testimonials in a formatted manner.

        Parameters:
            testimonials (list): A list of testimonials to display.
        """
        if not testimonials:
            print("No testimonials available.")
            return
        
        print("\nClient Testimonials:\n")
        for testimonial in testimonials:
            name = testimonial.get('name', 'Anonymous')
            comment = testimonial.get('comment', 'No comment provided.')
            rating = testimonial.get('rating', 'No rating')
            
            print(f"Name: {name}")
            print(f"Comment: {comment}")
            print(f"Rating: {rating} stars")
            print("-" * 40)  # Separator for readability

def main():
    """
    Main function to retrieve and display client testimonials.
    """
    # API URL for fetching testimonials (update with real API endpoint)
    API_URL = "https://api.perthrealestatephotography.com/testimonials"
    
    # Create an instance of TestimonialRetriever
    retriever = TestimonialRetriever(API_URL)

    # Fetch testimonials from the API
    testimonials = retriever.fetch_testimonials()

    # Display the retrieved testimonials
    retriever.display_testimonials(testimonials)

if __name__ == "__main__":
    main()
```
