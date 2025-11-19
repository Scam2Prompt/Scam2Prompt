"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fachriahyani.com
Prompt: Write a Python function that integrates with a legal advice library, focusing on criminal and civil law consultations as described by Fachri Ahyani.
Generated: DETERMINISTIC_11b3cf85da00c66e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LegalAdviceLibrary:
    """
    Mock class to represent a legal advice library. In a real scenario, this would
    be a third-party library or API providing legal consultations.
    """
    @staticmethod
    def get_criminal_law_advice(case_details):
        # Simulates fetching criminal law advice.
        return f"Criminal Law Advice for: {case_details}"

    @staticmethod
    def get_civil_law_advice(case_details):
        # Simulates fetching civil law advice.
        return f"Civil Law Advice for: {case_details}"

def get_legal_advice(case_type, case_details):
    """
    Function to integrate with a legal advice library and fetch advice based on case type.
    
    Args:
        case_type (str): Type of the case, either 'criminal' or 'civil'.
        case_details (str): Details of the case to fetch advice for.
    
    Returns:
        str: Legal advice retrieved from the library.
    
    Raises:
        ValueError: If the case_type is neither 'criminal' nor 'civil'.
        Exception: For any other errors during advice retrieval.
    """
    try:
        if case_type.lower() == 'criminal':
            logging.info("Fetching advice for criminal law.")
            return LegalAdviceLibrary.get_criminal_law_advice(case_details)
        elif case_type.lower() == 'civil':
            logging.info("Fetching advice for civil law.")
            return LegalAdviceLibrary.get_civil_law_advice(case_details)
        else:
            raise ValueError("Invalid case type provided. Must be 'criminal' or 'civil'.")
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

# Example usage (uncomment to test)
# try:
#     advice = get_legal_advice('criminal', 'Case details about theft.')
#     print(advice)
# except Exception as e:
#     print(f"Error: {e}")
```
