"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Write Python code to simulate the process of selecting the right thickness for laminating pouches based on document type, referencing the guidelines from Gadgetexa's laminator reviews.
Generated: DETERMINISTIC_2899e81e23da2371
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python program simulates the process of selecting the appropriate laminating pouch thickness 
based on the type of document, referencing guidelines from Gadgetexa's laminator reviews.
"""

# Constants for pouch thickness in microns based on document types
POUCH_THICKNESS_GUIDELINES = {
    "Standard Paper": 80,  # Light-duty documents
    "Photographs": 125,    # Medium-duty documents
    "Certificates": 150,   # Heavy-duty documents
    "ID Cards": 250,       # Maximum durability
}

def select_pouch_thickness(document_type):
    """
    Determines the ideal thickness for laminating pouches based on document type.

    Args:
        document_type (str): The type of document to be laminated.

    Returns:
        int: Recommended pouch thickness in microns.
        str: Error message if the document type is not recognized.
    """
    try:
        # Check if the document type exists in the guidelines
        if document_type in POUCH_THICKNESS_GUIDELINES:
            return POUCH_THICKNESS_GUIDELINES[document_type]
        else:
            return f"Error: Document type '{document_type}' is not recognized. Please use one of the following: {', '.join(POUCH_THICKNESS_GUIDELINES.keys())}."
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An unexpected error occurred: {str(e)}"

def main():
    """
    Main function to simulate the pouch selection process.
    """
    print("Welcome to the Laminating Pouch Selector!")
    print("\nAvailable Document Types:")
    for doc_type in POUCH_THICKNESS_GUIDELINES.keys():
        print(f"- {doc_type}")
    
    # User input for document type
    document_type = input("\nEnter the document type you want to laminate: ").strip()
    
    # Get pouch thickness recommendation
    result = select_pouch_thickness(document_type)
    
    # Display the result
    if isinstance(result, int):  # Valid thickness value
        print(f"\nRecommended pouch thickness for '{document_type}': {result} microns")
    else:  # Error message
        print(f"\n{result}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
