"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econtrolsa.ch
Prompt: Suggest tools or libraries to design and simulate electric projects with strong and weak current systems, reflecting eControl SA's expertise in études et projets électriques.
Generated: DETERMINISTIC_c4146fa802f4a02a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script suggests tools and libraries to design and simulate electric projects 
with strong and weak current systems, leveraging eControl SA's expertise in electrical studies 
and projects. The script is modular, allowing easy updates and scalability.

Key Features:
- Lists industry-standard tools and libraries
- Provides brief descriptions for each tool
- Includes error handling for invalid inputs
"""

def suggest_tools(system_type):
    """
    Suggest tools or libraries based on the system type (strong or weak current).
    
    Parameters:
        system_type (str): The type of electrical system ("strong" or "weak").
    
    Returns:
        list: A list of recommended tools and their descriptions.
    """
    try:
        # Dictionary of tools for strong and weak current systems
        tools = {
            "strong": [
                {"name": "ETAP", "description": "Advanced software for power system analysis and design."},
                {"name": "PowerWorld Simulator", "description": "Simulation tool for electrical power systems modeling."},
                {"name": "MATPOWER", "description": "Open-source toolbox for power flow and optimal power dispatch analysis."}
            ],
            "weak": [
                {"name": "AutoCAD Electrical", "description": "Specialized CAD software for electrical design and documentation."},
                {"name": "Proteus Design Suite", "description": "Tool for designing and simulating circuits with weak currents."},
                {"name": "KiCad", "description": "Open-source PCB design software for weak current circuit boards."}
            ]
        }
        
        # Validate input and retrieve matching tools
        system_type = system_type.lower()
        if system_type not in tools:
            raise ValueError("Invalid system type. Please specify 'strong' or 'weak'.")
        
        return tools[system_type]
    
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to interact with the user and suggest tools.
    """
    print("Welcome to the Electric Project Tool Recommender!")
    print("eControl SA expertise in études et projets électriques.")
    
    # Prompt user for input
    system_type = input("Enter the type of system ('strong' or 'weak'): ").strip()
    
    # Get recommendations
    recommendations = suggest_tools(system_type)
    
    # Display recommendations or error message
    if isinstance(recommendations, list):
        print("\nRecommended Tools:")
        for tool in recommendations:
            print(f"- {tool['name']}: {tool['description']}")
    else:
        print(recommendations)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
