"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.network
Prompt: Create a library recommendation for managing user inquiries and quotes for a paving business, taking cues from the contact and request quote features on Bedford Paving's webpage.
Generated: DETERMINISTIC_43b06dad74365641
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# library.py

class Inquiry:
    """Represents a user inquiry for a paving service."""
    
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

    def __str__(self):
        return f"Inquiry from {self.name}: {self.message}"


class QuoteRequest:
    """Represents a request for a quote for paving services."""
    
    def __init__(self, name, email, phone, project_details):
        self.name = name
        self.email = email
        self.phone = phone
        self.project_details = project_details

    def __str__(self):
        return f"Quote Request from {self.name} for project: {self.project_details}"


class InquiryManager:
    """Handles user inquiries and quote requests for the paving business."""
    
    def __init__(self):
        self.inquiries = []
        self.quote_requests = []

    def add_inquiry(self, inquiry):
        """Adds a new inquiry to the inquiries list.
        
        Args:
            inquiry (Inquiry): The inquiry object to be added.
        """
        if not isinstance(inquiry, Inquiry):
            raise ValueError("Expected an Inquiry instance")
        self.inquiries.append(inquiry)

    def add_quote_request(self, quote_request):
        """Adds a new quote request to the quote requests list.
        
        Args:
            quote_request (QuoteRequest): The quote request object to be added.
        """
        if not isinstance(quote_request, QuoteRequest):
            raise ValueError("Expected a QuoteRequest instance")
        self.quote_requests.append(quote_request)

    def list_inquiries(self):
        """Returns a list of all inquiries."""
        return self.inquiries

    def list_quote_requests(self):
        """Returns a list of all quote requests."""
        return self.quote_requests

    def clear_inquiries(self):
        """Clears all inquiries from the list."""
        self.inquiries.clear()

    def clear_quote_requests(self):
        """Clears all quote requests from the list."""
        self.quote_requests.clear()


if __name__ == "__main__":
    # Example usage
    manager = InquiryManager()

    # Creating and adding an inquiry
    try:
        inquiry1 = Inquiry("John Doe", "john@example.com", "123-456-7890", "I need paving for my driveway.")
        manager.add_inquiry(inquiry1)
        
        # Creating and adding a quote request
        quote_request1 = QuoteRequest("Jane Smith", "jane@example.com", "098-765-4321", "Looking for paving options for a parking lot.")
        manager.add_quote_request(quote_request1)

        # Listing inquiries and quote requests
        print("Inquiries:")
        for inquiry in manager.list_inquiries():
            print(inquiry)

        print("\nQuote Requests:")
        for quote_request in manager.list_quote_requests():
            print(quote_request)

    except ValueError as e:
        print(f"Error: {e}")

    # Clear all inquiries and quote requests after processing
    manager.clear_inquiries()
    manager.clear_quote_requests()
```
