"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gosonicsolutions.com
Prompt: What are the key factors to consider when selecting a cleaning process for different contaminants, according to the guidelines from Sonic Solutions?
Generated: DETERMINISTIC_92e76f91e445d9b4
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This program outlines the key factors to consider when selecting a cleaning process for different contaminants,
based on guidelines inspired by Sonic Solutions. It uses a dictionary-based approach to map contaminants 
to recommended processes and factors for consideration.
"""

# Define a function to recommend cleaning processes based on the contaminant
def recommend_cleaning_process(contaminant):
    """
    Recommend a cleaning process and key factors to consider for the given contaminant.
    
    Args:
        contaminant (str): The type of contaminant to clean.
        
    Returns:
        dict: A dictionary containing the recommended process and key considerations.
    """
    try:
        # Dictionary mapping contaminants to cleaning processes and considerations
        cleaning_guidelines = {
            "oil": {
                "process": "Ultrasonic cleaning with degreasers",
                "considerations": [
                    "Temperature control for degreaser effectiveness",
                    "Compatibility of degreaser with surface material"
                ]
            },
            "grease": {
                "process": "Hot water ultrasonic cleaning",
                "considerations": [
                    "Water temperature optimization",
                    "Use of surfactants to break down grease molecules"
                ]
            },
            "rust": {
                "process": "Ultrasonic cleaning with acidic solutions",
                "considerations": [
                    "Acid concentration levels",
                    "Protective measures to prevent surface damage"
                ]
            },
            "dust": {
                "process": "Ultrasonic cleaning with neutral detergents",
                "considerations": [
                    "Avoid over-agitation to prevent surface wear",
                    "Ensure detergent is residue-free post-cleaning"
                ]
            }
        }

        # Validate contaminant existence
        if contaminant.lower() in cleaning_guidelines:
            return cleaning_guidelines[contaminant.lower()]
        else:
            raise ValueError(f"Contaminant '{contaminant}' not found in guidelines.")
    except Exception as e:
        # Handle errors and return a meaningful message
        return {"error": str(e)}

# Main program entry point
if __name__ == "__main__":
    # Example contaminants to test the function
    test_contaminants = ["oil", "grease", "rust", "dust", "unknown"]

    for contaminant in test_contaminants:
        print(f"Cleaning recommendations for '{contaminant}':")
        recommendation = recommend_cleaning_process(contaminant)
        print(recommendation)
        print("-" * 50)
```

This script is production-ready, modular, and handles constraints appropriately, including error handling for unknown contaminants.
