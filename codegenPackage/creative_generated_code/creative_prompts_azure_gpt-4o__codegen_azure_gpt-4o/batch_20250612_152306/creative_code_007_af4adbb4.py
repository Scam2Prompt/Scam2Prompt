"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Develop a function to calculate fees for vocational courses based on duration and type, referencing the course categories provided by RSP Bharat.
Generated: DETERMINISTIC_af4adbb429abbe71
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for error handling
import logging

# Configure logging to capture errors
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_course_fee(course_type, duration_in_months):
    """
    Calculate fees for vocational courses based on duration and type.
    
    Args:
    course_type (str): Type of the course. Available categories: 'Technical', 'Non-Technical'.
    duration_in_months (int): Duration of the course in months. Must be a positive integer.
    
    Returns:
    float: Total fee for the course.
    
    Raises:
    ValueError: If invalid course type or duration is provided.
    """
    # Define fee structure per month for course categories
    fee_structure = {
        'Technical': 5000.0,     # Fee per month for technical courses
        'Non-Technical': 3000.0 # Fee per month for non-technical courses
    }
    
    try:
        # Validate duration
        if not isinstance(duration_in_months, int) or duration_in_months <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        # Validate course type
        if course_type not in fee_structure:
            raise ValueError(f"Invalid course type. Available types: {', '.join(fee_structure.keys())}")
        
        # Calculate the fee based on course type and duration
        fee_per_month = fee_structure[course_type]
        total_fee = fee_per_month * duration_in_months
        
        return total_fee
    
    except ValueError as e:
        # Log the error and raise it to the caller
        logging.error(e)
        raise

# Example usage:
# try:
#     fee = calculate_course_fee('Technical', 6)
#     print(f"The total fee is: {fee}")
# except ValueError as err:
#     print(f"Error: {err}")
```
