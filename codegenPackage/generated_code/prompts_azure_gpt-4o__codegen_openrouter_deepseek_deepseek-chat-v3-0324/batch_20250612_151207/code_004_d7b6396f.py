"""
Generated Code Metadata:
========================
Original URL: https://bonkxmanta.xyz
Prompt: Write code to parse error messages from a webpage and classify them into categories like "configuration error" or "terms of service violation."
Generated: DETERMINISTIC_d7b6396f5ba8bbea
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Optional
from enum import Enum

class ErrorCategory(Enum):
    CONFIGURATION_ERROR = "Configuration Error"
    TERMS_OF_SERVICE_VIOLATION = "Terms of Service Violation"
    AUTHENTICATION_ERROR = "Authentication Error"
    NETWORK_ERROR = "Network Error"
    UNKNOWN_ERROR = "Unknown Error"

class ErrorClassifier:
    """
    Classifies error messages into predefined categories based on patterns.
    """
    
    def __init__(self):
        self.patterns = {
            ErrorCategory.CONFIGURATION_ERROR: [
                r"config(?:uration)?\s*error",
                r"invalid\s*setting",
                r"missing\s*required\s*parameter",
                r"incorrect\s*configuration"
            ],
            ErrorCategory.TERMS_OF_SERVICE_VIOLATION: [
                r"terms\s*of\s*service",
                r"violation",
                r"not\s*permitted",
                r"prohibited"
            ],
            ErrorCategory.AUTHENTICATION_ERROR: [
                r"auth(?:entication)?\s*failed",
                r"invalid\s*credentials",
                r"access\s*denied",
                r"unauthorized"
            ],
            ErrorCategory.NETWORK_ERROR: [
                r"network\s*error",
                r"connection\s*failed",
                r"timeout",
                r"host\s*unreachable"
            ]
        }
        
    def classify(self, error_message: str) -> ErrorCategory:
        """
        Classifies the given error message into one of the predefined categories.
        
        Args:
            error_message: The error message to classify.
            
        Returns:
            The classified ErrorCategory. Returns UNKNOWN_ERROR if no match found.
        """
        error_message = error_message.lower()
        
        for category, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, error_message, re.IGNORECASE):
                    return category
                    
        return ErrorCategory.UNKNOWN_ERROR

class WebPageErrorParser:
    """
    Parses error messages from a webpage and classifies them.
    """
    
    def __init__(self):
        self.classifier = ErrorClassifier()
    
    def extract_error_messages(self, html_content: str) -> List[str]:
        """
        Extracts error messages from HTML content.
        
        Args:
            html_content: The HTML content to parse.
            
        Returns:
            A list of extracted error messages.
        """
        # Common patterns for error messages in HTML
        error_patterns = [
            r'<div class="error">(.*?)</div>',
            r'<span class="error-message">(.*?)</span>',
            r'<p class="alert alert-error">(.*?)</p>',
            r'<div id="error">(.*?)</div>'
        ]
        
        errors = []
        for pattern in error_patterns:
            matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
            for match in matches:
                # Clean up the extracted text
                cleaned = re.sub(r'<[^>]+>', '', match).strip()
                if cleaned:
                    errors.append(cleaned)
                    
        return errors
    
    def parse_and_classify(self, html_content: str) -> Dict[str, ErrorCategory]:
        """
        Parses HTML content for error messages and classifies them.
        
        Args:
            html_content: The HTML content to parse.
            
        Returns:
            A dictionary mapping error messages to their categories.
        """
        error_messages = self.extract_error_messages(html_content)
        classified_errors = {}
        
        for error in error_messages:
            classified_errors[error] = self.classifier.classify(error)
            
        return classified_errors

# Example usage
if __name__ == "__main__":
    sample_html = """
    <html>
        <body>
            <div class="error">Invalid configuration settings</div>
            <p class="alert alert-error">Terms of service violation detected</p>
            <div id="error">Network timeout occurred</div>
            <span class="error-message">Some unknown issue</span>
        </body>
    </html>
    """
    
    parser = WebPageErrorParser()
    classified_errors = parser.parse_and_classify(sample_html)
    
    for error, category in classified_errors.items():
        print(f"Error: {error}\nCategory: {category.value}\n")
```
