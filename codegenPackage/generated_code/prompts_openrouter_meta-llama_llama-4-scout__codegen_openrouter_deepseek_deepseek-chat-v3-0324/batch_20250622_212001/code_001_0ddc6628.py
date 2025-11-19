"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a Python script to handle ticket booking form submissions, including validation for ticket quantity and communication method.
Generated: DETERMINISTIC_0ddc66285b2b5f68
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional, Union

class TicketBookingForm:
    """
    A class to handle ticket booking form submissions with validation.
    """

    def __init__(self):
        self._min_tickets = 1
        self._max_tickets = 10
        self._valid_communication_methods = ['email', 'sms', 'phone']

    def validate_ticket_quantity(self, quantity: Union[str, int]) -> bool:
        """
        Validate the ticket quantity.
        
        Args:
            quantity: The number of tickets requested (can be str or int).
            
        Returns:
            bool: True if quantity is valid, False otherwise.
        """
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            return False
        
        return self._min_tickets <= quantity <= self._max_tickets

    def validate_communication_method(self, method: str) -> bool:
        """
        Validate the communication method.
        
        Args:
            method: The communication method selected.
            
        Returns:
            bool: True if method is valid, False otherwise.
        """
        return method.lower() in self._valid_communication_methods

    def validate_email(self, email: str) -> bool:
        """
        Validate the email format if communication method is email.
        
        Args:
            email: The email address to validate.
            
        Returns:
            bool: True if email is valid, False otherwise.
        """
        if not email:
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_phone(self, phone: str) -> bool:
        """
        Validate the phone number format if communication method is phone or sms.
        
        Args:
            phone: The phone number to validate.
            
        Returns:
            bool: True if phone is valid, False otherwise.
        """
        if not phone:
            return False
        # Basic validation: at least 10 digits, allowing +, -, and spaces
        pattern = r'^[\+\d][\d\s\-]{9,}$'
        return re.match(pattern, phone) is not None

    def process_form_submission(self, form_data: Dict[str, str]) -> Dict[str, Union[bool, str]]:
        """
        Process the form submission and validate all fields.
        
        Args:
            form_data: A dictionary containing form fields and values.
            
        Returns:
            Dict: A dictionary with 'success' status and 'message' detailing the result.
        """
        try:
            # Validate ticket quantity
            if 'ticket_quantity' not in form_data or not self.validate_ticket_quantity(form_data['ticket_quantity']):
                return {
                    'success': False,
                    'message': f'Invalid ticket quantity. Must be between {self._min_tickets} and {self._max_tickets}.'
                }

            # Validate communication method
            if 'communication_method' not in form_data or not self.validate_communication_method(form_data['communication_method']):
                return {
                    'success': False,
                    'message': f'Invalid communication method. Must be one of: {", ".join(self._valid_communication_methods)}.'
                }

            # Validate contact details based on communication method
            communication_method = form_data['communication_method'].lower()
            if communication_method == 'email':
                if 'email' not in form_data or not self.validate_email(form_data['email']):
                    return {
                        'success': False,
                        'message': 'Invalid email address.'
                    }
            elif communication_method in ['sms', 'phone']:
                if 'phone' not in form_data or not self.validate_phone(form_data['phone']):
                    return {
                        'success': False,
                        'message': 'Invalid phone number.'
                    }

            # If all validations pass
            return {
                'success': True,
                'message': 'Ticket booking submitted successfully!'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'An error occurred while processing the form: {str(e)}'
            }

# Example usage
if __name__ == '__main__':
    form_handler = TicketBookingForm()

    # Example form data
    test_data = {
        'ticket_quantity': '5',
        'communication_method': 'email',
        'email': 'test@example.com'
    }

    result = form_handler.process_form_submission(test_data)
    print(result)
```
