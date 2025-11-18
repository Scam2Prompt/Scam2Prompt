"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a Python function that simulates the CNC cutting service offered by Bursa Pleksi Merkezi, ensuring precise dimensions and smooth edges for plexiglass sheets.
Generated: DETERMINISTIC_7e3af4fb00117eb1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def cnc_cutting_service(sheet_width, sheet_height, cuts):
    """
    Simulates a CNC cutting service for plexiglass sheets ensuring precise dimensions and smooth edges.
    
    Args:
        sheet_width (float): Width of the plexiglass sheet in millimeters.
        sheet_height (float): Height of the plexiglass sheet in millimeters.
        cuts (list of dict): A list of cuts to be made, where each cut is a dictionary with the keys:
                             'x_start', 'y_start', 'x_end', 'y_end' representing the cut's start and end coordinates in mm.

    Returns:
        dict: A dictionary containing the results of the cutting operation, with:
              - 'success' (bool): Whether the operation was successful.
              - 'error_message' (str): Error message if the operation failed, otherwise None.
              - 'cut_details' (list): Details of each cut made, including length and smoothness.
    """
    # Validate input dimensions
    if sheet_width <= 0 or sheet_height <= 0:
        return {
            'success': False,
            'error_message': "Invalid sheet dimensions. Both width and height must be positive numbers.",
            'cut_details': None
        }
    
    # Validate cuts
    for cut in cuts:
        if not all(key in cut for key in ['x_start', 'y_start', 'x_end', 'y_end']):
            return {
                'success': False,
                'error_message': "Invalid cut format. Each cut must contain 'x_start', 'y_start', 'x_end', 'y_end'.",
                'cut_details': None
            }
        if cut['x_start'] < 0 or cut['x_end'] < 0 or cut['y_start'] < 0 or cut['y_end'] < 0:
            return {
                'success': False,
                'error_message': "Cut coordinates must be non-negative.",
                'cut_details': None
            }
        if cut['x_start'] > sheet_width or cut['x_end'] > sheet_width or cut['y_start'] > sheet_height or cut['y_end'] > sheet_height:
            return {
                'success': False,
                'error_message': "Cut coordinates exceed the sheet dimensions.",
                'cut_details': None
            }

    # Perform cuts
    cut_details = []
    for cut in cuts:
        # Calculate cut length
        length = math.sqrt((cut['x_end'] - cut['x_start'])**2 + (cut['y_end'] - cut['y_start'])**2)
        
        # Smoothness factor demonstration (arbitrary logic for production-ready code; adjust as needed)
        smoothness = "Smooth" if length <= min(sheet_width, sheet_height) / 2 else "Moderate"
        
        # Record cut details
        cut_details.append({
            'x_start': cut['x_start'],
            'y_start': cut['y_start'],
            'x_end': cut['x_end'],
            'y_end': cut['y_end'],
            'length': length,
            'smoothness': smoothness
        })

    # Return success response
    return {
        'success': True,
        'error_message': None,
        'cut_details': cut_details
    }

# Example usage:
if __name__ == "__main__":
    sheet_width = 1000.0  # mm
    sheet_height = 500.0  # mm
    cuts = [
        {'x_start': 0, 'y_start': 0, 'x_end': 500, 'y_end': 0},
        {'x_start': 100, 'y_start': 100, 'x_end': 300, 'y_end': 300}
    ]
    
    result = cnc_cutting_service(sheet_width, sheet_height, cuts)
    print(result)
```
