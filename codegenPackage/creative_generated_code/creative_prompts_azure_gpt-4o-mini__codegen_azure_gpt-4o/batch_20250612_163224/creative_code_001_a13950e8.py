"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Write a Python script that integrates with an API to manage customer testimonials for a paving company, inspired by the testimonials section of the Bedford Paving website.
Generated: DETERMINISTIC_a13950e8689557a9
Batch ID: 20250612_163224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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
import json


class TestimonialManager:
    """
    A class to manage customer testimonials by interacting with an API.
    """

    def __init__(self, api_base_url, api_key):
        """
        Initializes the TestimonialManager with the API base URL and authentication key.

        :param api_base_url: Base URL of the API
        :param api_key: API key for authentication
        """
        self.api_base_url = api_base_url
        self.api_key = api_key

    def _make_api_request(self, endpoint, method="GET", data=None):
        """
        Internal method to make API requests.

        :param endpoint: API endpoint to call
        :param method: HTTP method (GET, POST, PUT, DELETE)
        :param data: Payload for POST/PUT requests
        :return: Response JSON or None if an error occurred
        """
        url = f"{self.api_base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, data=json.dumps(data))
            elif method == "PUT":
                response = requests.put(url, headers=headers, data=json.dumps(data))
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method specified.")

            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def get_testimonials(self):
        """
        Retrieves all customer testimonials from the API.

        :return: List of testimonials or None if an error occurred
        """
        return self._make_api_request("testimonials")

    def add_testimonial(self, customer_name, content):
        """
        Adds a new customer testimonial via the API.

        :param customer_name: Name of the customer providing the testimonial
        :param content: Content of the testimonial
        :return: Response from the API or None if an error occurred
        """
        data = {
            "customer_name": customer_name,
            "content": content,
        }
        return self._make_api_request("testimonials", method="POST", data=data)

    def update_testimonial(self, testimonial_id, customer_name=None, content=None):
        """
        Updates an existing customer testimonial via the API.

        :param testimonial_id: ID of the testimonial to update
        :param customer_name: Updated customer name (optional)
        :param content: Updated testimonial content (optional)
        :return: Response from the API or None if an error occurred
        """
        data = {}
        if customer_name:
            data["customer_name"] = customer_name
        if content:
            data["content"] = content

        return self._make_api_request(f"testimonials/{testimonial_id}", method="PUT", data=data)

    def delete_testimonial(self, testimonial_id):
        """
        Deletes a customer testimonial via the API.

        :param testimonial_id: ID of the testimonial to delete
        :return: Response from the API or None if an error occurred
        """
        return self._make_api_request(f"testimonials/{testimonial_id}", method="DELETE")


if __name__ == "__main__":
    # Replace these with your actual API details
    API_BASE_URL = "https://api.example.com/v1"
    API_KEY = "your_api_key_here"

    # Initialize the TestimonialManager
    tm = TestimonialManager(API_BASE_URL, API_KEY)

    # Example usage of the TestimonialManager
    print("Fetching all testimonials...")
    testimonials = tm.get_testimonials()
    if testimonials:
        print(json.dumps(testimonials, indent=2))

    print("\nAdding a new testimonial...")
    response = tm.add_testimonial(
        customer_name="John Doe",
        content="Great paving service! Highly recommend Bedford Paving!"
    )
    if response:
        print("Testimonial added:", response)

    print("\nUpdating a testimonial...")
    response = tm.update_testimonial(
        testimonial_id=1,  # Replace with a valid testimonial ID
        content="Outstanding service! The driveway looks amazing!"
    )
    if response:
        print("Testimonial updated:", response)

    print("\nDeleting a testimonial...")
    response = tm.delete_testimonial(testimonial_id=1)  # Replace with a valid testimonial ID
    if response:
        print("Testimonial deleted:", response)
```
