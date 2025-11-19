"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.network
Prompt: Create a library recommendation for managing user inquiries and quotes for a paving business, taking cues from the contact and request quote features on Bedford Paving's webpage.
Generated: DETERMINISTIC_43b06dad74365641
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# library_recommender.py

from enum import Enum
from typing import Dict, List

class InquiryStatus(Enum):
    """Inquiry status types"""
    NEW = "new"
    PENDING = "pending"
    QUOTED = "quoted"
    COMPLETED = "completed"

class UserInquiry:
    """Represents a user inquiry"""
    def __init__(self, id: int, name: str, email: str, phone: str, description: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.description = description
        self.status = InquiryStatus.NEW
        self.quote = None

    def update_status(self, status: InquiryStatus):
        """Update the inquiry status"""
        self.status = status

    def add_quote(self, quote: str):
        """Add a quote to the inquiry"""
        self.quote = quote

class Quote:
    """Represents a quote"""
    def __init__(self, id: int, inquiry_id: int, price: float, description: str):
        self.id = id
        self.inquiry_id = inquiry_id
        self.price = price
        self.description = description

class PavingLibrary:
    """Manages user inquiries and quotes"""
    def __init__(self):
        self.inquiries: Dict[int, UserInquiry] = {}
        self.quotes: Dict[int, Quote] = {}
        self.inquiry_id_counter = 1
        self.quote_id_counter = 1

    def create_inquiry(self, name: str, email: str, phone: str, description: str) -> UserInquiry:
        """Create a new user inquiry"""
        inquiry = UserInquiry(self.inquiry_id_counter, name, email, phone, description)
        self.inquiries[self.inquiry_id_counter] = inquiry
        self.inquiry_id_counter += 1
        return inquiry

    def get_inquiry(self, id: int) -> UserInquiry:
        """Get an inquiry by ID"""
        return self.inquiries.get(id)

    def update_inquiry_status(self, id: int, status: InquiryStatus):
        """Update the status of an inquiry"""
        inquiry = self.get_inquiry(id)
        if inquiry:
            inquiry.update_status(status)
        else:
            raise ValueError("Inquiry not found")

    def add_quote_to_inquiry(self, inquiry_id: int, price: float, description: str) -> Quote:
        """Add a quote to an inquiry"""
        inquiry = self.get_inquiry(inquiry_id)
        if inquiry:
            quote = Quote(self.quote_id_counter, inquiry_id, price, description)
            self.quotes[self.quote_id_counter] = quote
            inquiry.add_quote(description)
            self.quote_id_counter += 1
            return quote
        else:
            raise ValueError("Inquiry not found")

    def get_quote(self, id: int) -> Quote:
        """Get a quote by ID"""
        return self.quotes.get(id)

def main():
    library = PavingLibrary()

    # Create a new inquiry
    inquiry = library.create_inquiry("John Doe", "john@example.com", "123-456-7890", "Paving for a driveway")

    # Update the inquiry status
    library.update_inquiry_status(inquiry.id, InquiryStatus.PENDING)

    # Add a quote to the inquiry
    quote = library.add_quote_to_inquiry(inquiry.id, 1000.0, "This is a quote for the paving job")

    # Print the inquiry and quote
    print(f"Inquiry {inquiry.id} - {inquiry.name}: {inquiry.description}")
    print(f"Status: {inquiry.status.value}")
    print(f"Quote: {quote.description} - ${quote.price}")

if __name__ == "__main__":
    main()
```
