"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.lu
Prompt: How do I wire a Tekonsha trailer brake controller in my vehicle? Provide a detailed wiring diagram.
Generated: DETERMINISTIC_1e441eb1253cefdc
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Trailer Brake Controller Wiring Diagram Generator

This script generates a simple text-based wiring diagram for a Tekonsha trailer brake controller.
It includes the necessary connections and their descriptions.

Usage:
1. Run the script to display the wiring diagram.
2. Follow the instructions to wire the trailer brake controller in your vehicle.
"""

def generate_wiring_diagram():
    """
    Generate and print the wiring diagram for a Tekonsha trailer brake controller.
    """
    wiring_diagram = {
        "Tekonsha Brake Controller": {
            "Red Wire": "12V Power Source (fused)",
            "Black Wire": "Ground",
            "White Wire": "To Trailer Brake Output",
            "Blue Wire": "To Tow Vehicle's Brake Switch",
            "Green Wire": "To Trailer's Brake Lights (if needed)"
        },
        "Tow Vehicle Connections": {
            "Brake Switch": "Connect to the Blue Wire of the brake controller",
            "Battery": "Connect the Red Wire of the brake controller to a fused 12V power source",
            "Ground": "Connect the Black Wire of the brake controller to a good chassis ground"
        },
        "Trailer Connections": {
            "Electric Brakes": "Connect the White Wire of the brake controller to the trailer's brake output"
        }
    }

    print("\n--- Tekonsha Trailer Brake Controller Wiring Diagram ---\n")
    
    for controller, connections in wiring_diagram.items():
        print(f"{controller}:")
        for wire_color, connection in connections.items():
            print(f"  {wire_color}: {connection}")
        print()  # Add a newline for better readability

def main():
    """
    Main function to execute the wiring diagram generator.
    """
    try:
        generate_wiring_diagram()
    except Exception as e:
        print(f"An error occurred while generating the wiring diagram: {e}")

if __name__ == "__main__":
    main()
```
