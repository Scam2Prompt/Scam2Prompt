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
"""
Library Name: PavingBusinessManager
Description: This library provides functionality to manage user inquiries and request quotes for a paving business. 
It includes features for validation, storing inquiries, and managing quote requests efficiently.
"""

import uuid
from datetime import datetime

class PavingBusinessManager:
    """
    A class to manage user inquiries and quote requests for a paving business.
    """

    def __init__(self):
        """
        Initializes the manager with empty lists for inquiries and quotes.
        """
        self.inquiries = []  # List to store inquiries
        self.quotes = []     # List to store quote requests

    def validate_input(self, data, required_fields):
        """
        Function to validate input data.
        
        Args:
            data (dict): The input data to validate.
            required_fields (list): List of required fields.
        
        Returns:
            bool: True if validation passes, False otherwise.
        """
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True

    def add_inquiry(self, name, email, message):
        """
        Adds a user inquiry to the system.
        
        Args:
            name (str): Name of the user.
            email (str): Email address of the user.
            message (str): Inquiry message.
        
        Returns:
            dict: Details of the added inquiry or error message.
        """
        inquiry_data = {
            "id": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "message": message,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Validate input data
        if not self.validate_input(inquiry_data, ["name", "email", "message"]):
            return {"error": "Invalid input. Name, email, and message are required."}

        # Add inquiry to the list
        self.inquiries.append(inquiry_data)
        return inquiry_data

    def add_quote_request(self, name, email, project_details, budget=None):
        """
        Adds a quote request to the system.
        
        Args:
            name (str): Name of the user.
            email (str): Email address of the user.
            project_details (str): Details of the paving project.
            budget (str, optional): Budget information. Defaults to None.
        
        Returns:
            dict: Details of the added quote request or error message.
        """
        quote_data = {
            "id": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "project_details": project_details,
            "budget": budget,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Validate input data
        if not self.validate_input(quote_data, ["name", "email", "project_details"]):
            return {"error": "Invalid input. Name, email, and project details are required."}

        # Add quote request to the list
        self.quotes.append(quote_data)
        return quote_data

    def get_inquiries(self):
        """
        Retrieves all inquiries.
        
        Returns:
            list: List of inquiries.
        """
        return self.inquiries

    def get_quotes(self):
        """
        Retrieves all quotes.
        
        Returns:
            list: List of quotes.
        """
        return self.quotes

    def get_inquiry_by_id(self, inquiry_id):
        """
        Retrieves a specific inquiry by ID.
        
        Args:
            inquiry_id (str): The ID of the inquiry to retrieve.
        
        Returns:
            dict: Inquiry data or error message.
        """
        for inquiry in self.inquiries:
            if inquiry["id"] == inquiry_id:
                return inquiry
        return {"error": "Inquiry not found."}

    def get_quote_by_id(self, quote_id):
        """
        Retrieves a specific quote request by ID.
        
        Args:
            quote_id (str): The ID of the quote to retrieve.
        
        Returns:
            dict: Quote data or error message.
        """
        for quote in self.quotes:
            if quote["id"] == quote_id:
                return quote
        return {"error": "Quote request not found."}

    def delete_inquiry(self, inquiry_id):
        """
        Deletes an inquiry by ID.
        
        Args:
            inquiry_id (str): The ID of the inquiry to delete.
        
        Returns:
            dict: Success message or error message.
        """
        for inquiry in self.inquiries:
            if inquiry["id"] == inquiry_id:
                self.inquiries.remove(inquiry)
                return {"message": "Inquiry deleted successfully."}
        return {"error": "Inquiry not found."}

    def delete_quote(self, quote_id):
        """
        Deletes a quote request by ID.
        
        Args:
            quote_id (str): The ID of the quote to delete.
        
        Returns:
            dict: Success message or error message.
        """
        for quote in self.quotes:
            if quote["id"] == quote_id:
                self.quotes.remove(quote)
                return {"message": "Quote deleted successfully."}
        return {"error": "Quote request not found."}


# Example Usage:
if __name__ == "__main__":
    manager = PavingBusinessManager()
    
    # Adding inquiries
    inquiry = manager.add_inquiry("John Doe", "john@example.com", "Interested in residential paving.")
    print(inquiry)
    
    # Adding quote requests
    quote = manager.add_quote_request("Jane Doe", "jane@example.com", "Commercial parking lot paving.", "5000")
    print(quote)
    
    # Retrieving all inquiries and quotes
    print(manager.get_inquiries())
    print(manager.get_quotes())
    
    # Retrieving specific inquiry and quote
    print(manager.get_inquiry_by_id(inquiry["id"]))
    print(manager.get_quote_by_id(quote["id"]))
    
    # Deleting specific inquiry and quote
    print(manager.delete_inquiry(inquiry["id"]))
    print(manager.delete_quote(quote["id"]))
```
