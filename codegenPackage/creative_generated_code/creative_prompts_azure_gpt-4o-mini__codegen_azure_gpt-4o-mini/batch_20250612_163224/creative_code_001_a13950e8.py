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
  "https://example.com/api": {
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
    A class to manage customer testimonials using an external API.
    """

    def __init__(self, api_url):
        """
        Initializes the TestimonialManager with the API URL.

        Args:
            api_url (str): The base URL of the testimonials API.
        """
        self.api_url = api_url

    def get_testimonials(self):
        """
        Fetches all testimonials from the API.

        Returns:
            list: A list of testimonials.

        Raises:
            Exception: If the API request fails.
        """
        try:
            response = requests.get(f"{self.api_url}/testimonials")
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Returns the JSON response as a list
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch testimonials: {e}")

    def add_testimonial(self, customer_name, testimonial_text):
        """
        Adds a new testimonial to the API.

        Args:
            customer_name (str): The name of the customer giving the testimonial.
            testimonial_text (str): The testimonial text.

        Returns:
            dict: The created testimonial response.

        Raises:
            Exception: If the API request fails.
        """
        payload = {
            "customer_name": customer_name,
            "testimonial_text": testimonial_text
        }

        try:
            response = requests.post(f"{self.api_url}/testimonials", json=payload)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Returns the created testimonial
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to add testimonial: {e}")

    def update_testimonial(self, testimonial_id, updated_text):
        """
        Updates an existing testimonial.

        Args:
            testimonial_id (int): The ID of the testimonial to update.
            updated_text (str): The new testimonial text.

        Returns:
            dict: The updated testimonial response.

        Raises:
            Exception: If the API request fails.
        """
        payload = {
            "testimonial_text": updated_text
        }

        try:
            response = requests.put(f"{self.api_url}/testimonials/{testimonial_id}", json=payload)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Returns the updated testimonial
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to update testimonial: {e}")

    def delete_testimonial(self, testimonial_id):
        """
        Deletes a testimonial by its ID.

        Args:
            testimonial_id (int): The ID of the testimonial to delete.

        Raises:
            Exception: If the API request fails.
        """
        try:
            response = requests.delete(f"{self.api_url}/testimonials/{testimonial_id}")
            response.raise_for_status()  # Raises an error for bad responses
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to delete testimonial: {e}")

if __name__ == "__main__":
    # Example usage
    API_URL = "https://example.com/api"  # Replace with the actual API URL
    manager = TestimonialManager(API_URL)

    try:
        # Fetch and print testimonials
        testimonials = manager.get_testimonials()
        print("Current Testimonials:", json.dumps(testimonials, indent=4))

        # Add a new testimonial
        new_testimonial = manager.add_testimonial("John Doe", "Amazing paving service!")
        print("Added Testimonial:", json.dumps(new_testimonial, indent=4))

        # Update a testimonial
        updated_testimonial = manager.update_testimonial(new_testimonial['id'], "Fantastic paving service!")
        print("Updated Testimonial:", json.dumps(updated_testimonial, indent=4))

        # Delete a testimonial
        manager.delete_testimonial(new_testimonial['id'])
        print("Deleted Testimonial with ID:", new_testimonial['id'])

    except Exception as e:
        print("Error:", e)
```
