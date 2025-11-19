"""
Generated Code Metadata:
========================
Original URL: https://networkitcnetworkmo.com
Prompt: Generate code to parse email headers and identify accidental deliveries in emails sent through VertiStream.
Generated: DETERMINISTIC_07ffd0ce561a38bf
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from email import message_from_string
from typing import Dict, List, Optional, Tuple

class EmailHeaderParser:
    """
    A class to parse email headers and identify accidental deliveries.
    """
    
    def __init__(self, email_content: str):
        """
        Initialize the parser with the raw email content.
        
        Args:
            email_content: Raw email content as a string.
        """
        self.email_content = email_content
        self.message = message_from_string(email_content)
        self.vertistream_headers = [
            'X-VertiStream-MessageID',
            'X-VertiStream-Sender',
            'X-VertiStream-Recipient'
        ]
    
    def get_headers(self) -> Dict[str, str]:
        """
        Extract all headers from the email.
        
        Returns:
            Dictionary of header names and values.
        """
        headers = {}
        for key, value in self.message.items():
            headers[key] = value
        return headers
    
    def is_vertistream_email(self) -> bool:
        """
        Check if the email was sent through VertiStream.
        
        Returns:
            True if VertiStream headers are present, False otherwise.
        """
        headers = self.get_headers()
        return any(header in headers for header in self.vertistream_headers)
    
    def get_vertistream_recipients(self) -> List[str]:
        """
        Extract recipients from VertiStream headers.
        
        Returns:
            List of recipient email addresses.
        """
        if not self.is_vertistream_email():
            return []
        
        headers = self.get_headers()
        recipient_header = headers.get('X-VertiStream-Recipient', '')
        return [addr.strip() for addr in recipient_header.split(',') if addr.strip()]
    
    def get_to_recipients(self) -> List[str]:
        """
        Extract recipients from standard 'To' header.
        
        Returns:
            List of recipient email addresses.
        """
        to_header = self.message.get('To', '')
        return self._parse_email_addresses(to_header)
    
    def get_cc_recipients(self) -> List[str]:
        """
        Extract recipients from standard 'Cc' header.
        
        Returns:
            List of recipient email addresses.
        """
        cc_header = self.message.get('Cc', '')
        return self._parse_email_addresses(cc_header)
    
    def _parse_email_addresses(self, header_value: str) -> List[str]:
        """
        Parse email addresses from a header value.
        
        Args:
            header_value: Raw header value containing email addresses.
            
        Returns:
            List of parsed email addresses.
        """
        if not header_value:
            return []
        
        # Simple regex to extract email addresses
        pattern = r'[\w\.-]+@[\w\.-]+'
        return re.findall(pattern, header_value)
    
    def find_accidental_deliveries(self) -> Tuple[List[str], List[str]]:
        """
        Identify accidental deliveries by comparing VertiStream recipients with To/Cc.
        
        Returns:
            Tuple of (unintended_recipients, missing_recipients)
        """
        if not self.is_vertistream_email():
            return [], []
        
        vertistream_recipients = set(self.get_vertistream_recipients())
        to_recipients = set(self.get_to_recipients())
        cc_recipients = set(self.get_cc_recipients())
        
        all_visible_recipients = to_recipients.union(cc_recipients)
        
        # Recipients in VertiStream but not in To/Cc
        unintended = list(vertistream_recipients - all_visible_recipients)
        
        # Recipients in To/Cc but not in VertiStream
        missing = list(all_visible_recipients - vertistream_recipients)
        
        return unintended, missing
    
    @staticmethod
    def analyze_email(email_content: str) -> Dict[str, List[str]]:
        """
        Static method to analyze an email and return accidental delivery information.
        
        Args:
            email_content: Raw email content as a string.
            
        Returns:
            Dictionary with analysis results.
        """
        parser = EmailHeaderParser(email_content)
        unintended, missing = parser.find_accidental_deliveries()
        
        return {
            'is_vertistream_email': parser.is_vertistream_email(),
            'unintended_recipients': unintended,
            'missing_recipients': missing,
            'vertistream_recipients': parser.get_vertistream_recipients(),
            'to_recipients': parser.get_to_recipients(),
            'cc_recipients': parser.get_cc_recipients()
        }
```
