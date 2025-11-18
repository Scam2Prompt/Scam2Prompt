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
ElectricProjectSimulator - A Python module to suggest tools and libraries for designing and simulating electric projects, with a focus on strong and weak current systems.

Author: eControl SA
Date: 2023-10-01
"""

import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricProjectSimulator:
    """
    A class to encapsulate the functionality of recommending tools for electric project simulation.
    """

    def __init__(self):
        # Initialize the list of recommended tools and libraries
        self.tools = {
            "strong_current": [
                {"name": "ETAP", "description": "Power system analysis and simulation"},
                {"name": "PowerWorld", "description": "Visualization and simulation of power systems"},
                {"name": "DIgSILENT PowerFactory", "description": "Comprehensive tool for power system analysis"},
            ],
            "weak_current": [
                {"name": "AutoCAD Electrical", "description": "Electrical design software for automation"},
                {"name": "EPLAN Electric P8", "description": "Planning and documentation of electrical engineering projects"},
                {"name": "MATLAB/Simulink", "description": "Model-based design for control systems and simulations"},
            ]
        }

    def get_tools(self, current_type):
        """
        Retrieve recommended tools based on the current type (strong or weak).
        
        Parameters:
        current_type (str): Type of current ('strong_current' or 'weak_current')
        
        Returns:
        list: A list of recommended tools and their descriptions
        
        Raises:
        ValueError: If an invalid current type is provided.
        """
        if current_type not in self.tools:
            logging.error(f"Invalid current type: {current_type}")
            raise ValueError(f"Invalid current type: {current_type}. Must be 'strong_current' or 'weak_current'.")

        logging.info(f"Retrieving tools for current type: {current_type}")
        return self.tools[current_type]

def main():
    """
    Main function to run the ElectricProjectSimulator and display recommended tools.
    """
    simulator = ElectricProjectSimulator()
    
    try:
        # Example: Get tools for strong current system
        strong_current_tools = simulator.get_tools('strong_current')
        logging.info("Recommended tools for strong current systems:")
        for tool in strong_current_tools:
            print(f"{tool['name']}: {tool['description']}")

        # Example: Get tools for weak current system
        weak_current_tools = simulator.get_tools('weak_current')
        logging.info("Recommended tools for weak current systems:")
        for tool in weak_current_tools:
            print(f"{tool['name']}: {tool['description']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
