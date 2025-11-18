"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a script to automate the process of selecting residential carpets based on user input for room type and traffic flow, using the guidelines provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_79b9b1fb38f49355
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarpetSelector:
    def __init__(self):
        # Load carpet options from a JSON file
        self.carpet_options = self.load_carpet_options('carpet_options.json')

    def load_carpet_options(self, file_path):
        """Load carpet options from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")
            return {}

    def select_carpet(self, room_type, traffic_flow):
        """Select carpet options based on the room type and traffic flow."""
        if room_type not in self.carpet_options:
            print(f"Error: Unrecognized room type '{room_type}'.")
            return []

        room_carpet_options = self.carpet_options[room_type]
        suitable_carpets = []

        for carpet in room_carpet_options:
            if carpet['traffic_flow'] == traffic_flow:
                suitable_carpets.append(carpet)

        if not suitable_carpets:
            print(f"No suitable carpets found for {room_type} with traffic flow '{traffic_flow}'.")
        return suitable_carpets

def main():
    """Main function to run the carpet selection process."""
    selector = CarpetSelector()
    
    # User input for room type and traffic flow
    room_type = input("Enter the room type (e.g., bedroom, living room, hallway): ").strip().lower()
    traffic_flow = input("Enter the traffic flow (e.g., low, medium, high): ").strip().lower()
    
    # Get selected carpets
    selected_carpets = selector.select_carpet(room_type, traffic_flow)
    
    if selected_carpets:
        print("Recommended carpets:")
        for carpet in selected_carpets:
            print(f"- {carpet['name']} (Material: {carpet['material']}, Color: {carpet['color']})")

if __name__ == "__main__":
    main()
```

**Example JSON file structure (carpet_options.json):**
```json
{
    "bedroom": [
        {
            "name": "Soft Touch",
            "material": "Nylon",
            "color": "Light Grey",
            "traffic_flow": "low"
        },
        {
            "name": "Cozy Comfort",
            "material": "Wool",
            "color": "Cream",
            "traffic_flow": "medium"
        }
    ],
    "living room": [
        {
            "name": "Elegant Weave",
            "material": "Polyester",
            "color": "Beige",
            "traffic_flow": "high"
        }
    ],
    "hallway": [
        {
            "name": "Durable Runner",
            "material": "Nylon",
            "color": "Dark Brown",
            "traffic_flow": "high"
        }
    ]
}
```
