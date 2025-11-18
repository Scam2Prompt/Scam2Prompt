"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dvisi.pro
Prompt: Write a function in Python to parse and display lottery results for "HK SIANG" and "SYDNEY" in the format provided by PANSOS4D.
Generated: DETERMINISTIC_3ba8924c1b93e71f
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def parse_lottery_results(input_text):
    """
    Parses and displays lottery results for "HK SIANG" and "SYDNEY"
    in the format provided by PANSOS4D.

    Args:
        input_text (str): Raw lottery result string.

    Returns:
        dict: A dictionary containing parsed results for "HK SIANG" and "SYDNEY".
    """
    # Define regex patterns for extracting lottery results
    patterns = {
        "HK SIANG": r"(?i)HK SIANG:\s*(\d{4})",
        "SYDNEY": r"(?i)SYDNEY:\s*(\d{4})"
    }

    # Initialize result dictionary
    lottery_results = {
        "HK SIANG": None,
        "SYDNEY": None
    }

    try:
        # Extract lottery results from input_text
        for key, pattern in patterns.items():
            match = re.search(pattern, input_text)
            if match:
                lottery_results[key] = match.group(1)

        # Display the parsed results
        print("Lottery Results:")
        for key, value in lottery_results.items():
            if value:
                print(f"{key}: {value}")
            else:
                print(f"{key}: No result found")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while parsing lottery results: {str(e)}")

    return lottery_results


# Example usage:
if __name__ == "__main__":
    # Sample input string
    raw_input = """
    Lottery Results:
    HK SIANG: 1234
    SYDNEY: 5678
    """
    # Call the function to parse and display results
    parse_lottery_results(raw_input)
```
