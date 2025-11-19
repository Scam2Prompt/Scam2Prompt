"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Write a function to compare the cargo dimensions of the Boeing 767-300 and Boeing 777-200 models, using the specifications provided on the 星飞园 website.
Generated: DETERMINISTIC_6446ad87b6eb7938
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def compare_cargo_dimensions():
    """
    Compares the cargo dimensions of Boeing 767-300 and Boeing 777-200 models.
    Data sourced from 星飞园 website specifications.
    
    Returns:
        dict: A dictionary containing the comparison results with keys:
            - 'models': List of compared aircraft models
            - 'cargo_hold_volume': Cargo hold volume in cubic meters
            - 'cargo_door_dimensions': Cargo door dimensions in meters (height x width)
            - 'max_payload': Maximum payload in kilograms
    """
    # Aircraft specifications from 星飞园
    boeing_767_300 = {
        'model': 'Boeing 767-300',
        'cargo_hold_volume': 114.1,  # m³
        'cargo_door_dimensions': (1.70, 3.40),  # height x width in meters
        'max_payload': 43817  # kg
    }
    
    boeing_777_200 = {
        'model': 'Boeing 777-200',
        'cargo_hold_volume': 158.9,  # m³
        'cargo_door_dimensions': (1.78, 3.40),  # height x width in meters
        'max_payload': 65854  # kg
    }
    
    comparison = {
        'models': [boeing_767_300['model'], boeing_777_200['model']],
        'cargo_hold_volume': {
            boeing_767_300['model']: boeing_767_300['cargo_hold_volume'],
            boeing_777_200['model']: boeing_777_200['cargo_hold_volume']
        },
        'cargo_door_dimensions': {
            boeing_767_300['model']: boeing_767_300['cargo_door_dimensions'],
            boeing_777_200['model']: boeing_777_200['cargo_door_dimensions']
        },
        'max_payload': {
            boeing_767_300['model']: boeing_767_300['max_payload'],
            boeing_777_200['model']: boeing_777_200['max_payload']
        }
    }
    
    return comparison
```
