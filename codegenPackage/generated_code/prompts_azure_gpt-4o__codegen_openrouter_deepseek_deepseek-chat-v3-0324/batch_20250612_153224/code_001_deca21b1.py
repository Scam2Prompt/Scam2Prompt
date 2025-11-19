"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Generate a script to create a customizable 3D virtual convention center with sponsor exhibits, incorporating features like product displays and customer chat, as outlined by Virtual Media Events.
Generated: DETERMINISTIC_deca21b130719a6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional

class Exhibit:
    """Represents a sponsor exhibit in the virtual convention center."""
    
    def __init__(self, sponsor_name: str, booth_id: str, products: List[Dict], position: Dict):
        """
        Initialize an exhibit with sponsor details, products, and position.
        
        Args:
            sponsor_name: Name of the sponsor
            booth_id: Unique identifier for the booth
            products: List of products to display
            position: 3D coordinates (x, y, z) in the virtual space
        """
        self.sponsor_name = sponsor_name
        self.booth_id = booth_id
        self.products = products
        self.position = position
        self.visitors = []
        self.chat_messages = []
    
    def add_visitor(self, visitor_id: str) -> None:
        """Add a visitor to the exhibit's visitor list."""
        if visitor_id not in self.visitors:
            self.visitors.append(visitor_id)
    
    def remove_visitor(self, visitor_id: str) -> None:
        """Remove a visitor from the exhibit's visitor list."""
        if visitor_id in self.visitors:
            self.visitors.remove(visitor_id)
    
    def add_chat_message(self, sender: str, message: str) -> None:
        """Add a chat message to the exhibit's chat log."""
        self.chat_messages.append({"sender": sender, "message": message})
    
    def get_chat_history(self) -> List[Dict]:
        """Return the chat history for this exhibit."""
        return self.chat_messages
    
    def to_dict(self) -> Dict:
        """Convert exhibit data to dictionary for serialization."""
        return {
            "sponsor_name": self.sponsor_name,
            "booth_id": self.booth_id,
            "products": self.products,
            "position": self.position,
            "visitors": self.visitors,
            "chat_messages": self.chat_messages
        }

class VirtualConventionCenter:
    """Main class representing the 3D virtual convention center."""
    
    def __init__(self, name: str, dimensions: Dict):
        """
        Initialize the virtual convention center.
        
        Args:
            name: Name of the convention center
            dimensions: Dictionary with width, height, depth of the space
        """
        self.name = name
        self.dimensions = dimensions
        self.exhibits = {}
        self.visitors = {}
    
    def add_exhibit(self, exhibit: Exhibit) -> None:
        """Add an exhibit to the convention center."""
        if exhibit.booth_id in self.exhibits:
            raise ValueError(f"Exhibit with booth ID {exhibit.booth_id} already exists")
        self.exhibits[exhibit.booth_id] = exhibit
    
    def remove_exhibit(self, booth_id: str) -> None:
        """Remove an exhibit from the convention center."""
        if booth_id not in self.exhibits:
            raise ValueError(f"No exhibit found with booth ID {booth_id}")
        del self.exhibits[booth_id]
    
    def get_exhibit(self, booth_id: str) -> Optional[Exhibit]:
        """Get an exhibit by its booth ID."""
        return self.exhibits.get(booth_id)
    
    def add_visitor(self, visitor_id: str, visitor_data: Dict) -> None:
        """Add a visitor to the convention center."""
        if visitor_id in self.visitors:
            raise ValueError(f"Visitor with ID {visitor_id} already exists")
        self.visitors[visitor_id] = visitor_data
    
    def remove_visitor(self, visitor_id: str) -> None:
        """Remove a visitor from the convention center."""
        if visitor_id not in self.visitors:
            raise ValueError(f"No visitor found with ID {visitor_id}")
        del self.visitors[visitor_id]
    
    def move_visitor_to_exhibit(self, visitor_id: str, booth_id: str) -> None:
        """
        Move a visitor to a specific exhibit.
        
        Args:
            visitor_id: ID of the visitor
            booth_id: ID of the target exhibit
        """
        if visitor_id not in self.visitors:
            raise ValueError(f"No visitor found with ID {visitor_id}")
        if booth_id not in self.exhibits:
            raise ValueError(f"No exhibit found with booth ID {booth_id}")
        
        # Remove visitor from all exhibits first
        for exhibit in self.exhibits.values():
            exhibit.remove_visitor(visitor_id)
        
        # Add visitor to the target exhibit
        self.exhibits[booth_id].add_visitor(visitor_id)
    
    def send_chat_message(self, booth_id: str, sender: str, message: str) -> None:
        """
        Send a chat message to an exhibit's chat.
        
        Args:
            booth_id: ID of the target exhibit
            sender: Name/ID of the message sender
            message: Content of the message
        """
        if booth_id not in self.exhibits:
            raise ValueError(f"No exhibit found with booth ID {booth_id}")
        self.exhibits[booth_id].add_chat_message(sender, message)
    
    def generate_random_layout(self, num_exhibits: int) -> None:
        """
        Generate a random layout of exhibits in the convention center.
        
        Args:
            num_exhibits: Number of exhibits to generate
        """
        for i in range(num_exhibits):
            booth_id = f"booth_{i+1}"
            sponsor_name = f"Sponsor {i+1}"
            products = [{"id": f"prod_{j+1}", "name": f"Product {j+1}"} for j in range(random.randint(1, 5))]
            
            # Generate random position within convention center dimensions
            position = {
                "x": random.uniform(0, self.dimensions["width"]),
                "y": 0,  # Assuming exhibits are on ground level
                "z": random.uniform(0, self.dimensions["depth"])
            }
            
            exhibit = Exhibit(sponsor_name, booth_id, products, position)
            self.add_exhibit(exhibit)
    
    def save_to_file(self, filename: str) -> None:
        """Save the convention center data to a JSON file."""
        data = {
            "name": self.name,
            "dimensions": self.dimensions,
            "exhibits": {bid: exhibit.to_dict() for bid, exhibit in self.exhibits.items()},
            "visitors": self.visitors
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'VirtualConventionCenter':
        """Load a convention center from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        vcc = cls(data["name"], data["dimensions"])
        
        for bid, exhibit_data in data["exhibits"].items():
            exhibit = Exhibit(
                exhibit_data["sponsor_name"],
                bid,
                exhibit_data["products"],
                exhibit_data["position"]
            )
            exhibit.visitors = exhibit_data["visitors"]
            exhibit.chat_messages = exhibit_data["chat_messages"]
            vcc.exhibits[bid] = exhibit
        
        vcc.visitors = data["visitors"]
        return vcc

# Example usage
if __name__ == "__main__":
    # Create a new virtual convention center
    vcc = VirtualConventionCenter(
        name="Virtual Media Expo 2023",
        dimensions={"width": 100, "height": 20, "depth": 100}
    )
    
    # Generate random exhibits
    vcc.generate_random_layout(10)
    
    # Add some visitors
    vcc.add_visitor("visitor_1", {"name": "Alice"})
    vcc.add_visitor("visitor_2", {"name": "Bob"})
    
    # Move visitors to exhibits
    vcc.move_visitor_to_exhibit("visitor_1", "booth_1")
    vcc.move_visitor_to_exhibit("visitor_2", "booth_3")
    
    # Send some chat messages
    vcc.send_chat_message("booth_1", "Alice", "Hello, I'm interested in your products!")
    vcc.send_chat_message("booth_1", "Sponsor 1", "Welcome to our exhibit! How can we help?")
    
    # Save to file
    vcc.save_to_file("virtual_convention_center.json")
    
    # Load from file
    loaded_vcc = VirtualConventionCenter.load_from_file("virtual_convention_center.json")
    print(f"Loaded convention center: {loaded_vcc.name}")
```
