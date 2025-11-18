"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Develop a program to recommend SCOUT attachments (e.g., soil tillers, mulchers, trailers) based on user-selected tractor models and intended operations, as described on the SCOUT.kz website.
Generated: DETERMINISTIC_db0b31b838868432
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define tractor and attachment data
# In a production-ready implementation, this data would ideally come from a database or API.
TRACTORS = {
    "SCOUT T-224": {
        "supported_attachments": ["plow", "trailer", "mulcher"],
        "operations": ["tilling", "hauling", "mulching"]
    },
    "SCOUT T-15": {
        "supported_attachments": ["trailer", "harrow"],
        "operations": ["hauling", "leveling"]
    },
    "SCOUT T-12": {
        "supported_attachments": ["soil tiller", "mulcher"],
        "operations": ["tilling", "mulching"]
    }
}

ATTACHMENTS = {
    "plow": {
        "operation": "tilling",
        "description": "Used for turning over soil to prepare it for planting."
    },
    "trailer": {
        "operation": "hauling",
        "description": "Used for transporting goods and materials."
    },
    "mulcher": {
        "operation": "mulching",
        "description": "Used for cutting and shredding vegetation."
    },
    "harrow": {
        "operation": "leveling",
        "description": "Used for smoothing and breaking up soil."
    },
    "soil tiller": {
        "operation": "tilling",
        "description": "Used for preparing the soil for planting crops."
    }
}

# Function to recommend attachments based on tractor model and intended operation
def recommend_attachments(tractor_model, intended_operation):
    """
    Recommend SCOUT attachments based on the tractor model and intended operation.

    Args:
    - tractor_model (str): The model of the tractor.
    - intended_operation (str): The intended operation (e.g., tilling, hauling, mulching).

    Returns:
    - list: Recommended attachments for the given tractor model and operation.
    """
    try:
        # Validate tractor model
        if tractor_model not in TRACTORS:
            return {
                "error": f"Invalid tractor model '{tractor_model}'. Please select a valid model."
            }
        
        # Filter attachments based on operation and tractor compatibility
        tractor_data = TRACTORS[tractor_model]
        compatible_attachments = [
            attachment for attachment in tractor_data["supported_attachments"]
            if ATTACHMENTS[attachment]["operation"] == intended_operation
        ]
        
        # Handle case where no attachments are found for the operation
        if not compatible_attachments:
            return {
                "error": f"No compatible attachments found for {tractor_model} and operation '{intended_operation}'."
            }
        
        # Prepare recommendation response
        response = {
            "tractor_model": tractor_model,
            "operation": intended_operation,
            "recommended_attachments": [
                {
                    "name": attachment,
                    "description": ATTACHMENTS[attachment]["description"]
                }
                for attachment in compatible_attachments
            ]
        }
        return response
    
    except Exception as e:
        # Return error details in case of unexpected failure
        return {
            "error": f"An unexpected error occurred: {str(e)}"
        }

# Main function to interact with the program
def main():
    """
    Main function to run the SCOUT attachment recommendation program.
    """
    print("Welcome to the SCOUT Attachment Recommendation Program!")
    
    try:
        # Get user input for tractor model and operation
        tractor_model = input("Enter the tractor model (e.g., SCOUT T-224, SCOUT T-15, SCOUT T-12): ")
        intended_operation = input("Enter the intended operation (e.g., tilling, hauling, mulching): ")
        
        # Get recommendations
        recommendations = recommend_attachments(tractor_model, intended_operation)
        
        # Display recommendations or error messages
        if "error" in recommendations:
            print(f"Error: {recommendations['error']}")
        else:
            print("\nRecommended Attachments:")
            for attachment in recommendations["recommended_attachments"]:
                print(f"- {attachment['name']} ({attachment['description']})")
    
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
```
