"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Create a script to filter and display dental instruments by their product codes (e.g., 2312-2321, 1557-1575) as listed on the Curative Surgical Industry website.
Generated: DETERMINISTIC_fbd306431531d5b8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def filter_dental_instruments(product_codes, code_ranges):
    """
    Filters and displays dental instruments by their product codes.

    Parameters:
    product_codes (list): List of all available product codes as strings.
    code_ranges (list): List of code ranges in the format ["start-end"] as strings.

    Returns:
    list: Filtered list of product codes matching the specified ranges.
    """
    filtered_codes = []
    
    try:
        # Iterate through each range and filter product codes
        for range_str in code_ranges:
            # Validate and parse the range string (e.g., "2312-2321")
            match = re.match(r"(\d+)-(\d+)", range_str)
            if not match:
                raise ValueError(f"Invalid range format: {range_str}")
            
            start, end = int(match.group(1)), int(match.group(2))
            # Collect product codes within the range
            for code in product_codes:
                try:
                    code_num = int(code)
                    if start <= code_num <= end:
                        filtered_codes.append(code)
                except ValueError:
                    # Skip invalid product codes that cannot be converted to integers
                    pass

        return filtered_codes
    
    except Exception as e:
        print(f"Error filtering dental instruments: {e}")
        return []


if __name__ == "__main__":
    # Example list of product codes
    all_product_codes = [
        "2312", "2313", "2314", "2315", "2316", "2317", "2318", "2319", "2320", "2321",
        "1557", "1558", "1559", "1560", "1561", "1562", "1563", "1564", "1565", "1566", "1567", "1575",
        "9999"  # Invalid or extra code, outside range
    ]
    
    # Example list of ranges
    search_code_ranges = ["2312-2321", "1557-1575"]

    # Filter codes based on ranges and display results
    filtered_instruments = filter_dental_instruments(all_product_codes, search_code_ranges)
    print("Filtered Product Codes:")
    print(filtered_instruments)
```
