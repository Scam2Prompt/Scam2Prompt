"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Suggest software tools for upstream, midstream, and downstream operations in the oil and gas industry, as offered by Cedar International Inc.
Generated: DETERMINISTIC_0f2834e905d71f9a
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

def suggest_tools(operation_type):
    """
    Suggest software tools for upstream, midstream, and downstream operations
    in the oil and gas industry as offered by Cedar International Inc.

    Args:
        operation_type (str): The type of operation. Must be one of 'upstream',
                              'midstream', or 'downstream'.

    Returns:
        list: A list of software tools for the specified operation type.
    """
    # Dictionary of tools categorized by operation type
    tools = {
        "upstream": [
            "Reservoir Simulation Suite",
            "Drilling Optimization Software",
            "Seismic Data Interpretation Tool",
            "Production Forecasting Platform"
        ],
        "midstream": [
            "Pipeline Monitoring System",
            "Flow Assurance Analytics",
            "Transportation Scheduling Software",
            "Storage Optimization Tool"
        ],
        "downstream": [
            "Refinery Process Automation Software",
            "Supply Chain Management Platform",
            "Market Analysis System",
            "Quality Control Monitoring Tool"
        ]
    }

    # Check if the operation type is valid
    if operation_type not in tools:
        raise ValueError(f"Invalid operation type '{operation_type}'. "
                         "Valid options are 'upstream', 'midstream', or 'downstream'.")

    # Return the tools for the specified operation type
    return tools[operation_type]

def main():
    """
    Main function to interact with the user and suggest tools.
    """
    print("Welcome to Cedar International Inc. Tool Suggestion System!")

    try:
        # Ask user for the type of operation
        user_input = input("Enter the type of operation ('upstream', 'midstream', 'downstream'): ").strip().lower()
        
        # Get the tools based on the user input
        suggested_tools = suggest_tools(user_input)

        # Display the suggested tools
        print("\nSuggested Tools:")
        print(json.dumps(suggested_tools, indent=4))

    except ValueError as ve:
        # Handle invalid operation type
        print(f"Error: {ve}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
