"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write a Python script to manage a network of community centers, like the ones operated by Sophia Loisirs & Vie, including their locations and contact information.
Generated: DETERMINISTIC_92691c19c3ea0a1a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class CommunityCenter:
    """Represents a community center with its details."""
    
    def __init__(self, name: str, address: str, city: str, postal_code: str, 
                 phone: str, email: str, manager: str, capacity: int):
        """
        Initialize a CommunityCenter instance.
        
        Args:
            name: Name of the center
            address: Street address
            city: City
            postal_code: Postal code
            phone: Contact phone number
            email: Contact email
            manager: Name of the manager
            capacity: Maximum capacity of the center
        """
        self.name = name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.manager = manager
        self.capacity = capacity
    
    def to_dict(self) -> Dict:
        """Convert the CommunityCenter object to a dictionary."""
        return {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'email': self.email,
            'manager': self.manager,
            'capacity': self.capacity
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CommunityCenter':
        """Create a CommunityCenter object from a dictionary."""
        return cls(
            name=data['name'],
            address=data['address'],
            city=data['city'],
            postal_code=data['postal_code'],
            phone=data['phone'],
            email=data['email'],
            manager=data['manager'],
            capacity=data['capacity']
        )

class CommunityCenterManager:
    """Manages a collection of community centers."""
    
    def __init__(self, data_file: str = 'community_centers.json'):
        """
        Initialize the CommunityCenterManager.
        
        Args:
            data_file: Path to JSON file storing center data
        """
        self.data_file = data_file
        self.centers: Dict[str, CommunityCenter] = {}
        self.load_centers()
    
    def add_center(self, center: CommunityCenter) -> None:
        """Add a new community center to the manager."""
        if center.name in self.centers:
            raise ValueError(f"Center '{center.name}' already exists")
        self.centers[center.name] = center
        self.save_centers()
    
    def update_center(self, name: str, **kwargs) -> None:
        """Update an existing community center."""
        if name not in self.centers:
            raise ValueError(f"Center '{name}' not found")
        
        center = self.centers[name]
        for key, value in kwargs.items():
            if hasattr(center, key):
                setattr(center, key, value)
            else:
                raise AttributeError(f"Invalid attribute '{key}'")
        
        self.save_centers()
    
    def remove_center(self, name: str) -> None:
        """Remove a community center."""
        if name not in self.centers:
            raise ValueError(f"Center '{name}' not found")
        del self.centers[name]
        self.save_centers()
    
    def get_center(self, name: str) -> Optional[CommunityCenter]:
        """Get a community center by name."""
        return self.centers.get(name)
    
    def list_centers(self) -> List[CommunityCenter]:
        """List all community centers."""
        return list(self.centers.values())
    
    def search_centers(self, city: Optional[str] = None, 
                       min_capacity: Optional[int] = None) -> List[CommunityCenter]:
        """
        Search centers by city and/or minimum capacity.
        
        Args:
            city: City to filter by
            min_capacity: Minimum capacity to filter by
            
        Returns:
            List of matching centers
        """
        results = []
        for center in self.centers.values():
            if city and center.city.lower() != city.lower():
                continue
            if min_capacity and center.capacity < min_capacity:
                continue
            results.append(center)
        return results
    
    def load_centers(self) -> None:
        """Load centers from the data file."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.centers = {
                    name: CommunityCenter.from_dict(center_data)
                    for name, center_data in data.items()
                }
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Error loading centers: {str(e)}")
    
    def save_centers(self) -> None:
        """Save centers to the data file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(
                    {name: center.to_dict() for name, center in self.centers.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise RuntimeError(f"Error saving centers: {str(e)}")

def main():
    """Example usage of the CommunityCenterManager."""
    manager = CommunityCenterManager()
    
    # Example operations
    try:
        # Add a new center
        center1 = CommunityCenter(
            name="Sophia Loisirs Nord",
            address="123 Main Street",
            city="Sophia Antipolis",
            postal_code="06410",
            phone="+33 4 93 00 00 01",
            email="nord@sophialoisirs.fr",
            manager="Jean Dupont",
            capacity=150
        )
        manager.add_center(center1)
        
        # Add another center
        center2 = CommunityCenter(
            name="Sophia Loisirs Sud",
            address="456 Oak Avenue",
            city="Sophia Antipolis",
            postal_code="06410",
            phone="+33 4 93 00 00 02",
            email="sud@sophialoisirs.fr",
            manager="Marie Curie",
            capacity=200
        )
        manager.add_center(center2)
        
        # Update a center
        manager.update_center("Sophia Loisirs Nord", capacity=180)
        
        # Search centers
        print("Centers in Sophia Antipolis:")
        for center in manager.search_centers(city="Sophia Antipolis"):
            print(f"- {center.name} (Capacity: {center.capacity})")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
