"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: What are the key factors to consider when selecting a cleaning process for different contaminants, according to the guidelines from Sonic Solutions?
Generated: DETERMINISTIC_92e76f91e445d9b4
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines the key factors to consider when selecting a cleaning process 
for different contaminants, based on guidelines from Sonic Solutions. The data is 
stored in a dictionary for easy retrieval and can be expanded as needed.
"""

# Import necessary modules
import sys

def get_cleaning_factors(contaminant):
    """
    Retrieves the key factors to consider for cleaning a specific contaminant.

    Args:
        contaminant (str): The name of the contaminant.

    Returns:
        list: A list of key factors for cleaning the contaminant.
    """
    # Dictionary containing contaminants and their cleaning factors
    cleaning_guidelines = {
        "oil": [
            "Temperature of cleaning solution",
            "Type of detergent used",
            "Ultrasonic frequency",
            "Duration of cleaning process"
        ],
        "grease": [
            "Concentration of cleaning solution",
            "Mechanical agitation",
            "Pre-soaking requirements",
            "Rinse process"
        ],
        "rust": [
            "Acidity of cleaning solution",
            "Use of rust inhibitors",
            "Material compatibility",
            "Post-cleaning treatment"
        ],
        "organic matter": [
            "Enzymatic cleaning agents",
            "Water temperature",
            "Cleaning cycle duration",
            "Drying process"
        ]
    }

    # Error handling for unknown contaminants
    if contaminant.lower() not in cleaning_guidelines:
        raise ValueError(f"Contaminant '{contaminant}' not found in guidelines. Please provide a valid contaminant.")

    return cleaning_guidelines[contaminant.lower()]

def main():
    """
    Main function to interact with the user and display cleaning factors.
    """
    try:
        # Prompt user for input
        contaminant = input("Enter the name of the contaminant (e.g., oil, grease, rust, organic matter): ").strip()
        
        # Retrieve cleaning factors
        factors = get_cleaning_factors(contaminant)
        
        # Display the results
        print(f"\nKey factors to consider for cleaning '{contaminant}':")
        for idx, factor in enumerate(factors, start=1):
            print(f"{idx}. {factor}")
    
    except ValueError as ve:
        # Handle invalid contaminant input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
