"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a script to automate the process of selecting residential carpets based on user input for room type and traffic flow, using the guidelines provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_79b9b1fb38f49355
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_selector.py

class Carpet:
    def __init__(self, name, description, traffic_flow, room_types):
        """
        Initialize a Carpet object.

        Args:
            name (str): Carpet name.
            description (str): Carpet description.
            traffic_flow (str): Recommended traffic flow for the carpet.
            room_types (list): List of recommended room types for the carpet.
        """
        self.name = name
        self.description = description
        self.traffic_flow = traffic_flow
        self.room_types = room_types

class CarpetSelector:
    def __init__(self):
        """
        Initialize a CarpetSelector object with a list of available carpets.
        """
        self.carpets = [
            Carpet(
                "Low Traffic Carpet",
                "Perfect for bedrooms and guest rooms.",
                "Low",
                ["bedroom", "guest room"]
            ),
            Carpet(
                "Medium Traffic Carpet",
                "Suitable for living rooms and dining rooms.",
                "Medium",
                ["living room", "dining room"]
            ),
            Carpet(
                "High Traffic Carpet",
                "Designed for hallways, stairs, and playrooms.",
                "High",
                ["hallway", "stair", "playroom"]
            ),
            Carpet(
                "Ultra High Traffic Carpet",
                "Ideal for busy households with multiple entry points.",
                "Ultra High",
                ["busy household"]
            )
        ]

    def get_carpets_by_room_type(self, room_type):
        """
        Get a list of carpets suitable for a given room type.

        Args:
            room_type (str): Room type.

        Returns:
            list: List of suitable carpets.
        """
        return [carpet for carpet in self.carpets if room_type.lower() in [rt.lower() for rt in carpet.room_types]]

    def get_carpets_by_traffic_flow(self, traffic_flow):
        """
        Get a list of carpets suitable for a given traffic flow.

        Args:
            traffic_flow (str): Traffic flow.

        Returns:
            list: List of suitable carpets.
        """
        return [carpet for carpet in self.carpets if traffic_flow.lower() == carpet.traffic_flow.lower()]

    def select_carpet(self, room_type, traffic_flow):
        """
        Select a carpet based on room type and traffic flow.

        Args:
            room_type (str): Room type.
            traffic_flow (str): Traffic flow.

        Returns:
            Carpet: Selected carpet or None if no match found.
        """
        suitable_carpets = self.get_carpets_by_room_type(room_type)
        suitable_carpets = [carpet for carpet in suitable_carpets if traffic_flow.lower() == carpet.traffic_flow.lower()]
        if suitable_carpets:
            return suitable_carpets[0]
        else:
            return None

def main():
    selector = CarpetSelector()
    print("Perfect Melbourne Carpet Selector")
    print("----------------------------------")

    room_types = ["bedroom", "living room", "hallway", "playroom", "dining room", "guest room", "stair", "busy household"]
    traffic_flows = ["Low", "Medium", "High", "Ultra High"]

    room_type = input("Enter room type (e.g., bedroom, living room): ")
    while room_type not in room_types:
        print("Invalid room type. Please choose from:")
        for rt in room_types:
            print(rt)
        room_type = input("Enter room type: ")

    traffic_flow = input("Enter traffic flow (e.g., Low, Medium, High): ")
    while traffic_flow not in traffic_flows:
        print("Invalid traffic flow. Please choose from:")
        for tf in traffic_flows:
            print(tf)
        traffic_flow = input("Enter traffic flow: ")

    selected_carpet = selector.select_carpet(room_type, traffic_flow)
    if selected_carpet:
        print(f"Recommended carpet: {selected_carpet.name}")
        print(f"Description: {selected_carpet.description}")
    else:
        print("No suitable carpet found.")

if __name__ == "__main__":
    main()
```
