"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Generate an API request for a legal service that allows users to submit inquiries about family law, business law, and immigration law, as described on the Juridisk Klinik website.
Generated: DETERMINISTIC_95128ed776980859
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.juridiskklinik.com/inquiries": {
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

class LegalServiceAPI:
    """
    A client to interact with the Juridisk Klinik's legal service API.
    Allows users to submit inquiries related to family law, business law, and immigration law.
    """

    BASE_URL = "https://api.juridiskklinik.com/inquiries"

    def __init__(self):
        """Initializes the LegalServiceAPI client."""
        pass

    def submit_inquiry(self, name, email, phone, inquiry_type, message):
        """
        Submits an inquiry to the legal service API.

        :param name: str - The name of the user submitting the inquiry.
        :param email: str - The email address of the user.
        :param phone: str - The phone number of the user.
        :param inquiry_type: str - The type of law related to the inquiry (family, business, immigration).
        :param message: str - The detailed message or inquiry content.
        :raises ValueError: If any required field is empty or if the inquiry_type is invalid.
        :returns: dict - The response from the API, if the submission is successful.
        """
        # Validate input
        if not all([name, email, phone, inquiry_type, message]):
            raise ValueError("All fields must be filled out.")

        valid_types = ['family', 'business', 'immigration']
        if inquiry_type not in valid_types:
            raise ValueError(f"inquiry_type must be one of {valid_types}")

        # Prepare the payload
        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "inquiry_type": inquiry_type,
            "message": message
        }

        try:
            # Make the API request
            response = requests.post(self.BASE_URL, json=payload)

            # Check for HTTP errors
            response.raise_for_status()

            # Return the response if successful
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error

        return None  # Return None if submission fails


# Example usage
if __name__ == "__main__":
    legal_service = LegalServiceAPI()
    try:
        response = legal_service.submit_inquiry(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            inquiry_type="family",
            message="I need help with child custody issues."
        )
        if response:
            print("Inquiry submitted successfully:", response)
        else:
            print("Failed to submit inquiry.")
    except ValueError as ve:
        print("Input error:", ve)
```
