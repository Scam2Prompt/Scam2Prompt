"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Provide a Python implementation for detecting and marking personal sensitive information in user data, as described in STELLAR TECHNOLOGY LIMITED's privacy policy.
Generated: DETERMINISTIC_c494729100a8a9c0
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Optional, Union
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SensitiveInfo:
    """Class to represent detected sensitive information."""
    type: str
    value: str
    start_pos: int
    end_pos: int

class PII_Detector:
    """Class to detect and mark Personally Identifiable Information (PII)."""
    
    def __init__(self):
        # Regular expressions for common PII patterns
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'(\+\d{1,3}\s?)?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
            'credit_card': r'\b(?:\d[ -]*?){13,16}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        }
        
        # Custom patterns can be added here
        self.custom_patterns = {}
        
    def add_custom_pattern(self, name: str, pattern: str) -> None:
        """Add a custom detection pattern."""
        if not name or not pattern:
            raise ValueError("Name and pattern must be provided")
        self.custom_patterns[name] = pattern
        
    def detect(self, text: str) -> List[SensitiveInfo]:
        """Detect sensitive information in the given text."""
        if not text:
            return []
            
        detected = []
        
        # Check standard patterns
        for pii_type, pattern in self.patterns.items():
            try:
                for match in re.finditer(pattern, text):
                    detected.append(SensitiveInfo(
                        type=pii_type,
                        value=match.group(),
                        start_pos=match.start(),
                        end_pos=match.end()
                    ))
            except re.error as e:
                logger.error(f"Regex error for {pii_type}: {e}")
                
        # Check custom patterns
        for pii_type, pattern in self.custom_patterns.items():
            try:
                for match in re.finditer(pattern, text):
                    detected.append(SensitiveInfo(
                        type=pii_type,
                        value=match.group(),
                        start_pos=match.start(),
                        end_pos=match.end()
                    ))
            except re.error as e:
                logger.error(f"Regex error for custom pattern {pii_type}: {e}")
                
        return detected
    
    def mask(self, text: str, mask_char: str = '*') -> str:
        """Mask detected sensitive information in the text."""
        if not text:
            return text
            
        detected = self.detect(text)
        if not detected:
            return text
            
        # Sort by start position in reverse to avoid position shifting issues
        detected.sort(key=lambda x: x.start_pos, reverse=True)
        
        masked_text = text
        for info in detected:
            masked_value = mask_char * len(info.value)
            masked_text = masked_text[:info.start_pos] + masked_value + masked_text[info.end_pos:]
            
        return masked_text

class DataProcessor:
    """Class to process user data and handle PII detection/masking."""
    
    def __init__(self):
        self.detector = PII_Detector()
        
    def process_data(self, data: Union[str, Dict, List]) -> Union[str, Dict, List]:
        """Process data to detect and mask PII."""
        if isinstance(data, str):
            return self.detector.mask(data)
        elif isinstance(data, dict):
            return {k: self.process_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.process_data(item) for item in data]
        else:
            return data
            
    def get_detected_pii(self, data: Union[str, Dict, List]) -> List[SensitiveInfo]:
        """Get all detected PII in the data."""
        if isinstance(data, str):
            return self.detector.detect(data)
        elif isinstance(data, dict):
            detected = []
            for v in data.values():
                detected.extend(self.get_detected_pii(v))
            return detected
        elif isinstance(data, list):
            detected = []
            for item in data:
                detected.extend(self.get_detected_pii(item))
            return detected
        else:
            return []

def example_usage():
    """Example usage of the PII detection and masking system."""
    processor = DataProcessor()
    
    # Example text with PII
    sample_text = """
    John Doe's contact info:
    Email: john.doe@example.com
    Phone: +1 (555) 123-4567
    SSN: 123-45-6789
    Credit Card: 4111 1111 1111 1111
    IP: 192.168.1.1
    """
    
    # Detect PII
    detected = processor.get_detected_pii(sample_text)
    print(f"Detected {len(detected)} PII items:")
    for pii in detected:
        print(f"- {pii.type}: {pii.value}")
    
    # Mask PII
    masked_text = processor.process_data(sample_text)
    print("\nMasked text:")
    print(masked_text)

if __name__ == "__main__":
    example_usage()
```
