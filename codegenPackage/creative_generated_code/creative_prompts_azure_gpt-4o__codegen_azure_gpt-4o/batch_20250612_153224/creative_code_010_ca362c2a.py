"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Suggest software tools for designing and constructing robust infrastructure tailored to the oil and gas industry, as described in C&M Pinnacle's services.
Generated: DETERMINISTIC_ca362c2a8226c107
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

def suggest_tools(industry: str) -> dict:
    """
    Suggest software tools tailored to the specified industry.
    
    Args:
        industry (str): The industry for which tools are being suggested.

    Returns:
        dict: A dictionary containing suggested tools and descriptions.
    """
    try:
        # Validate the input
        if not isinstance(industry, str) or industry.strip() == "":
            raise ValueError("Industry must be a non-empty string.")

        # Define tools specific to the oil and gas industry
        tools_database = {
            "oil_and_gas": [
                {
                    "name": "AutoCAD Plant 3D",
                    "description": "Specialized tool for designing piping and instrumentation diagrams (P&ID) and 3D modeling of plants."
                },
                {
                    "name": "AVEVA E3D Design",
                    "description": "Advanced engineering and design software for complex infrastructure in the oil and gas industry."
                },
                {
                    "name": "Aspen HYSYS",
                    "description": "Process simulation software used for optimizing oil and gas production systems."
                },
                {
                    "name": "Petrel E&P Software Platform",
                    "description": "Tool for subsurface modeling, analysis, and simulation tailored for oil exploration and production."
                },
                {
                    "name": "Bentley OpenPlant",
                    "description": "Comprehensive software for plant design and construction management, ensuring robust infrastructure."
                }
            ]
        }

        # Map industry name to tools category (case-insensitive match)
        industry_key = industry.lower().replace(" ", "_")
        
        # Check if tools are available for the given industry
        if industry_key in tools_database:
            return {"industry": industry, "tools": tools_database[industry_key]}
        else:
            # Return a message if no tools are available for the industry
            return {"industry": industry, "message": "No tools found for the specified industry."}

    except Exception as e:
        # Handle any unexpected errors
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Industry input
    industry_name = "oil and gas"
    
    # Fetch and display suggested tools
    suggestions = suggest_tools(industry_name)
    
    # Display the result in a readable format
    print(json.dumps(suggestions, indent=4))
```
