"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigoo2ajgc5d32j7sqglri2pqwtnmpnm6g2yfmlmcdzm2oyww2ny3u.ipfs.dweb.link
Prompt: Write a script to convert $PUMP Token allocations from Mantle and zkLink into a summarized report in JSON format.
Generated: DETERMINISTIC_1274450774dcb37d
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Function to fetch and convert token allocations
def convert_token_allocations(mantle_allocations, zklink_allocations):
    """
    Converts $PUMP Token allocations from Mantle and zkLink into summarized JSON report.

    Parameters:
        mantle_allocations (dict): Token allocations from Mantle as a dictionary.
        zklink_allocations (dict): Token allocations from zkLink as a dictionary.

    Returns:
        str: A JSON-formatted string summarizing the combined allocations.
    """
    try:
        # Verify input types
        if not isinstance(mantle_allocations, dict) or not isinstance(zklink_allocations, dict):
            raise ValueError("Allocations must be provided as dictionaries.")

        # Combine allocations from Mantle and zkLink
        combined_allocations = {}
        
        for key, value in mantle_allocations.items():
            combined_allocations[key] = combined_allocations.get(key, 0) + value
        
        for key, value in zklink_allocations.items():
            combined_allocations[key] = combined_allocations.get(key, 0) + value

        # Create summarized report
        summary_report = {
            "total_addresses": len(combined_allocations),
            "total_allocation": sum(combined_allocations.values()),
            "allocations": combined_allocations
        }

        # Generate JSON output
        return json.dumps(summary_report, indent=4)

    except ValueError as ve:
        # Handle incorrect input type
        return json.dumps({"error": str(ve)})

    except Exception as e:
        # Handle all other errors gracefully
        return json.dumps({"error": f"An unexpected error occurred: {str(e)}"})


# Example Mantle and zkLink allocations
mantle_allocations = {
    "0x123": 1000,
    "0x456": 500,
    "0x789": 1200
}

zklink_allocations = {
    "0x123": 800,
    "0x456": 200,
    "0xABC": 700
}

# Generate summarized report
report = convert_token_allocations(mantle_allocations, zklink_allocations)
print(report)
```
