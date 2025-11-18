"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Create a script that generates assembly instructions for UDIZINE's modular shelving systems, including Vertik and Palo systems, based on user-selected configurations.
Generated: DETERMINISTIC_4852c9d52f631fed
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define the modular shelving systems and their components
MODULAR_SYSTEMS = {
    "Vertik": {
        "description": "A vertical shelving system with customizable height and shelves.",
        "components": {
            "uprights": "Vertical support poles",
            "shelves": "Flat panels for storage",
            "screws": "Fasteners for assembly",
            "brackets": "Shelf support hardware"
        }
    },
    "Palo": {
        "description": "A flexible shelving system with wooden poles and connectors.",
        "components": {
            "wooden_poles": "Wooden poles of various lengths",
            "connectors": "Plastic or metal joints for connecting poles",
            "shelves": "Flat panels for storage",
            "fasteners": "Fasteners for securing shelves"
        }
    }
}

# Error class for invalid configurations
class InvalidConfigurationError(Exception):
    pass

def get_user_configuration():
    """
    Simulates user input for configuration.
    Replace this function with actual user input handling in a production environment.
    """
    print("Available systems: Vertik, Palo")
    system = input("Select a system (Vertik/Palo): ").strip()
    if system not in MODULAR_SYSTEMS:
        raise InvalidConfigurationError("Invalid shelving system selected.")

    # Simulate part selection for demonstration purposes
    num_uprights = int(input("Enter number of uprights (for Vertik only): ").strip()) if system == "Vertik" else None
    num_shelves = int(input("Enter number of shelves: ").strip())
    num_poles = int(input("Enter number of wooden poles (for Palo only): ").strip()) if system == "Palo" else None
    num_connectors = int(input("Enter number of connectors (for Palo only): ").strip()) if system == "Palo" else None

    return {
        "system": system,
        "components": {
            "uprights": num_uprights,
            "shelves": num_shelves,
            "wooden_poles": num_poles,
            "connectors": num_connectors
        }
    }

def generate_assembly_instructions(config):
    """
    Generates assembly instructions based on user configuration.

    Parameters:
        config (dict): User configuration for the shelving system.

    Returns:
        str: Assembly instructions.
    """
    system_name = config["system"]
    components = config["components"]
    system_data = MODULAR_SYSTEMS[system_name]
    
    instructions = []
    instructions.append(f"Assembly Instructions for UDIZINE {system_name} System")
    instructions.append(f"Description: {system_data['description']}")
    instructions.append("\nSteps:")
    
    # Add specific steps for each system
    if system_name == "Vertik":
        if components["uprights"] is None or components["uprights"] < 1:
            raise InvalidConfigurationError("Vertik system requires at least one upright.")
        instructions.append(f"1. Assemble {components['uprights']} upright(s) using provided screws.")
        instructions.append(f"2. Attach {components['shelves']} shelf/shelves using brackets.")
    elif system_name == "Palo":
        if components["wooden_poles"] is None or components["connectors"] is None:
            raise InvalidConfigurationError("Palo system requires wooden poles and connectors.")
        instructions.append(f"1. Connect {components['wooden_poles']} wooden pole(s) using {components['connectors']} connector(s).")
        instructions.append(f"2. Secure {components['shelves']} shelf/shelves using fasteners.")
    else:
        raise InvalidConfigurationError("Unsupported system selected.")

    instructions.append("\nEnsure all components are securely fastened before use.")
    return "\n".join(instructions)

def main():
    """
    Main entry point for the script.
    Handles user input and generates assembly instructions.
    """
    try:
        # Get user configuration
        user_config = get_user_configuration()
        
        # Generate assembly instructions
        instructions = generate_assembly_instructions(user_config)
        
        # Output instructions
        print("\nGenerated Assembly Instructions:")
        print(instructions)
    except InvalidConfigurationError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
