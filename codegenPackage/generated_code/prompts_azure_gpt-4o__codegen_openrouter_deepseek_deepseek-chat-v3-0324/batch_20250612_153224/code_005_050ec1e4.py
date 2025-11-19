"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a script to model the safety protocols for underground construction sites, referencing services like BOZP and OPP offered by URANPRES.
Generated: DETERMINISTIC_050ec1e425f37c06
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
from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional

class SafetyProtocolType(Enum):
    """Enum representing different types of safety protocols."""
    BOZP = "BOZP"  # Bezpečnost a ochrana zdraví při práci
    OPP = "OPP"    # Ochrana před požáry
    GENERAL = "GENERAL"

class SafetyProtocol:
    """Class representing a safety protocol for underground construction."""
    
    def __init__(
        self,
        protocol_id: str,
        protocol_type: SafetyProtocolType,
        title: str,
        description: str,
        requirements: List[str],
        last_updated: datetime,
        is_active: bool = True
    ):
        """Initialize a safety protocol.
        
        Args:
            protocol_id: Unique identifier for the protocol.
            protocol_type: Type of protocol (BOZP, OPP, etc.).
            title: Title of the protocol.
            description: Detailed description.
            requirements: List of safety requirements.
            last_updated: Last update timestamp.
            is_active: Whether the protocol is currently active.
        """
        self.protocol_id = protocol_id
        self.protocol_type = protocol_type
        self.title = title
        self.description = description
        self.requirements = requirements
        self.last_updated = last_updated
        self.is_active = is_active
    
    def to_dict(self) -> Dict:
        """Convert protocol to dictionary for serialization."""
        return {
            "protocol_id": self.protocol_id,
            "protocol_type": self.protocol_type.value,
            "title": self.title,
            "description": self.description,
            "requirements": self.requirements,
            "last_updated": self.last_updated.isoformat(),
            "is_active": self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SafetyProtocol':
        """Create protocol from dictionary."""
        return cls(
            protocol_id=data["protocol_id"],
            protocol_type=SafetyProtocolType(data["protocol_type"]),
            title=data["title"],
            description=data["description"],
            requirements=data["requirements"],
            last_updated=datetime.fromisoformat(data["last_updated"]),
            is_active=data["is_active"]
        )

class ConstructionSite:
    """Class representing an underground construction site with safety protocols."""
    
    def __init__(self, site_id: str, name: str, location: str):
        """Initialize a construction site.
        
        Args:
            site_id: Unique identifier for the site.
            name: Name of the construction site.
            location: Geographic location.
        """
        self.site_id = site_id
        self.name = name
        self.location = location
        self.protocols: Dict[str, SafetyProtocol] = {}
    
    def add_protocol(self, protocol: SafetyProtocol) -> None:
        """Add a safety protocol to the site.
        
        Args:
            protocol: SafetyProtocol instance to add.
        
        Raises:
            ValueError: If protocol with same ID already exists.
        """
        if protocol.protocol_id in self.protocols:
            raise ValueError(f"Protocol with ID {protocol.protocol_id} already exists")
        self.protocols[protocol.protocol_id] = protocol
    
    def remove_protocol(self, protocol_id: str) -> None:
        """Remove a safety protocol from the site.
        
        Args:
            protocol_id: ID of protocol to remove.
        
        Raises:
            KeyError: If protocol doesn't exist.
        """
        if protocol_id not in self.protocols:
            raise KeyError(f"Protocol with ID {protocol_id} not found")
        del self.protocols[protocol_id]
    
    def get_protocols_by_type(self, protocol_type: SafetyProtocolType) -> List[SafetyProtocol]:
        """Get all protocols of a specific type.
        
        Args:
            protocol_type: Type of protocols to retrieve.
        
        Returns:
            List of matching SafetyProtocol instances.
        """
        return [p for p in self.protocols.values() if p.protocol_type == protocol_type]
    
    def to_dict(self) -> Dict:
        """Convert site to dictionary for serialization."""
        return {
            "site_id": self.site_id,
            "name": self.name,
            "location": self.location,
            "protocols": [p.to_dict() for p in self.protocols.values()]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ConstructionSite':
        """Create site from dictionary."""
        site = cls(
            site_id=data["site_id"],
            name=data["name"],
            location=data["location"]
        )
        for protocol_data in data["protocols"]:
            site.add_protocol(SafetyProtocol.from_dict(protocol_data))
        return site

class SafetyProtocolManager:
    """Manager class for handling safety protocols across multiple sites."""
    
    def __init__(self):
        """Initialize the manager."""
        self.sites: Dict[str, ConstructionSite] = {}
    
    def add_site(self, site: ConstructionSite) -> None:
        """Add a construction site to the manager.
        
        Args:
            site: ConstructionSite instance to add.
        
        Raises:
            ValueError: If site with same ID already exists.
        """
        if site.site_id in self.sites:
            raise ValueError(f"Site with ID {site.site_id} already exists")
        self.sites[site.site_id] = site
    
    def remove_site(self, site_id: str) -> None:
        """Remove a construction site from the manager.
        
        Args:
            site_id: ID of site to remove.
        
        Raises:
            KeyError: If site doesn't exist.
        """
        if site_id not in self.sites:
            raise KeyError(f"Site with ID {site_id} not found")
        del self.sites[site_id]
    
    def get_site(self, site_id: str) -> Optional[ConstructionSite]:
        """Get a construction site by ID.
        
        Args:
            site_id: ID of site to retrieve.
        
        Returns:
            ConstructionSite instance or None if not found.
        """
        return self.sites.get(site_id)
    
    def save_to_file(self, file_path: str) -> None:
        """Save all sites and protocols to a JSON file.
        
        Args:
            file_path: Path to save file.
        
        Raises:
            IOError: If file operations fail.
        """
        try:
            data = {
                "sites": [site.to_dict() for site in self.sites.values()],
                "timestamp": datetime.now().isoformat()
            }
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to save data to file: {str(e)}")
    
    def load_from_file(self, file_path: str) -> None:
        """Load sites and protocols from a JSON file.
        
        Args:
            file_path: Path to load file from.
        
        Raises:
            IOError: If file operations fail.
            ValueError: If data is invalid.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.sites.clear()
            for site_data in data["sites"]:
                site = ConstructionSite.from_dict(site_data)
                self.add_site(site)
                
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load data from file: {str(e)}")
        except KeyError as e:
            raise ValueError(f"Invalid data format: missing key {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a protocol manager
    manager = SafetyProtocolManager()
    
    # Create a construction site
    site = ConstructionSite(
        site_id="site-001",
        name="Uranpres Metro Expansion",
        location="Prague, Czech Republic"
    )
    
    # Add BOZP protocol
    bozp_protocol = SafetyProtocol(
        protocol_id="proto-001",
        protocol_type=SafetyProtocolType.BOZP,
        title="Underground Work Safety",
        description="Safety measures for underground construction workers",
        requirements=[
            "Hard hats required at all times",
            "Safety harnesses for elevated work",
            "Regular air quality checks"
        ],
        last_updated=datetime.now(),
        is_active=True
    )
    
    # Add OPP protocol
    opp_protocol = SafetyProtocol(
        protocol_id="proto-002",
        protocol_type=SafetyProtocolType.OPP,
        title="Fire Prevention Measures",
        description="Fire safety protocols for underground sites",
        requirements=[
            "Fire extinguishers every 50 meters",
            "No smoking policy",
            "Emergency exits clearly marked"
        ],
        last_updated=datetime.now(),
        is_active=True
    )
    
    # Add protocols to site
    site.add_protocol(bozp_protocol)
    site.add_protocol(opp_protocol)
    
    # Add site to manager
    manager.add_site(site)
    
    # Save to
