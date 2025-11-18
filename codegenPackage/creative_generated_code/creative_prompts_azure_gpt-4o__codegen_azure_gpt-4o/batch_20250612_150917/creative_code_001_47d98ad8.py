"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.specialmetal.ir
Prompt: Generate a script to calculate the chemical composition of cobalt-based superalloys, such as ALLOY N 155, using laboratory analysis data and match it with JIS standards.
Generated: DETERMINISTIC_47d98ad881c18c06
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def match_alloy_composition(lab_data, jis_standards):
    """
    Matches the chemical composition of an alloy based on lab data
    with JIS standards.

    Args:
        lab_data (dict): Dictionary containing the chemical composition from lab analysis.
                         Example: {"C": 0.12, "Cr": 20.5, "Co": 55.0, "Ni": 19.0, "Fe": 4.0}
        jis_standards (dict): Dictionary containing JIS standard ranges for the alloy.
                              Example: {"C": (0.10, 0.15), "Cr": (19.0, 21.0), "Co": (50.0, 60.0), "Ni": (18.0, 20.0), "Fe": (3.0, 5.0)}

    Returns:
        dict: Results indicating if each element matches standards and overall alloy match.
              Example: {"C": True, "Cr": True, "Co": True, "Ni": True, "Fe": False, "overall_match": False}
    """
    results = {}
    overall_match = True

    for element, value in lab_data.items():
        if element in jis_standards:
            min_val, max_val = jis_standards[element]
            results[element] = min_val <= value <= max_val
            if not results[element]:
                overall_match = False
        else:
            results[element] = False
            overall_match = False

    results["overall_match"] = overall_match
    return results


def main():
    """
    Main function to load data, perform analysis, and output results.
    """
    try:
        # Example lab data (replace with actual laboratory analysis results)
        lab_data = {
            "C": 0.12,
            "Cr": 20.5,
            "Co": 55.0,
            "Ni": 19.0,
            "Fe": 4.0
        }

        # Example JIS standards for ALLOY N 155 (replace with actual standards if needed)
        jis_standards = {
            "C": (0.10, 0.15),
            "Cr": (19.0, 21.0),
            "Co": (50.0, 60.0),
            "Ni": (18.0, 20.0),
            "Fe": (3.0, 5.0)
        }

        # Match lab data with JIS standards
        results = match_alloy_composition(lab_data, jis_standards)

        # Output results
        print("Chemical Composition Analysis Results:")
        print(json.dumps(results, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
