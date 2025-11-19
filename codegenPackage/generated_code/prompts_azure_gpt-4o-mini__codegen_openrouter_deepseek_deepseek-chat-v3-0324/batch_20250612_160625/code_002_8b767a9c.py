"""
Generated Code Metadata:
========================
Original URL: https://a68.net
Prompt: Write a Python function that implements ID verification, inspired by the techniques used on a68.net.
Generated: DETERMINISTIC_8b767a9c5e1d8045
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime

def verify_id(id_number: str) -> dict:
    """
    Verify the validity of a Chinese ID number (18 digits).
    
    Args:
        id_number (str): The ID number to verify.
        
    Returns:
        dict: A dictionary containing the verification result and parsed information.
              Keys:
                  - 'is_valid' (bool): Whether the ID is valid.
                  - 'error' (str): Error message if invalid.
                  - 'gender' (str): 'Male' or 'Female' if valid.
                  - 'birth_date' (str): Birth date in 'YYYY-MM-DD' format if valid.
                  - 'region' (str): Region code if valid.
    """
    result = {
        'is_valid': False,
        'error': None,
        'gender': None,
        'birth_date': None,
        'region': None
    }
    
    # Basic format check
    if not re.match(r'^\d{17}[\dXx]$', id_number):
        result['error'] = 'Invalid format. Must be 18 digits ending with digit or X.'
        return result
    
    # Extract components
    region_code = id_number[:6]
    birth_date_str = id_number[6:14]
    sequence_code = id_number[14:17]
    checksum = id_number[-1].upper()
    
    # Verify region code (simple check for existence)
    if not region_code.isdigit() or region_code == '000000':
        result['error'] = 'Invalid region code.'
        return result
    
    # Verify birth date
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y%m%d')
        if birth_date > datetime.now():
            result['error'] = 'Birth date cannot be in the future.'
            return result
        result['birth_date'] = birth_date.strftime('%Y-%m-%d')
    except ValueError:
        result['error'] = 'Invalid birth date.'
        return result
    
    # Verify sequence code (gender)
    if not sequence_code.isdigit():
        result['error'] = 'Invalid sequence code.'
        return result
    
    gender_num = int(sequence_code[-1])
    result['gender'] = 'Male' if gender_num % 2 == 1 else 'Female'
    
    # Verify checksum
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    
    total = 0
    for i in range(17):
        total += int(id_number[i]) * weights[i]
    
    calculated_checksum = checksum_map[total % 11]
    
    if calculated_checksum != checksum:
        result['error'] = 'Checksum verification failed.'
        return result
    
    # If all checks passed
    result['is_valid'] = True
    result['region'] = region_code
    return result
```
