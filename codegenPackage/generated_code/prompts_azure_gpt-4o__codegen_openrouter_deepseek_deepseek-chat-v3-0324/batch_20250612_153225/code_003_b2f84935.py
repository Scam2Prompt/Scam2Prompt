"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Create a program to facilitate the representation of commercial entities in international trade, including licensing and permit management, based on the services offered by GlobalChain SAS.
Generated: DETERMINISTIC_b2f849353e4e3068
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Commercial Entity Representation System for International Trade

This module provides functionality to manage commercial entities, their licenses,
and permits for international trade operations, as per GlobalChain SAS services.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Union
import uuid
from enum import Enum, auto


class EntityType(Enum):
    """Enumeration of commercial entity types."""
    MANUFACTURER = auto()
    DISTRIBUTOR = auto()
    RETAILER = auto()
    IMPORTER = auto()
    EXPORTER = auto()
    BROKER = auto()


class LicenseStatus(Enum):
    """Enumeration of license statuses."""
    ACTIVE = auto()
    PENDING = auto()
    EXPIRED = auto()
    REVOKED = auto()
    SUSPENDED = auto()


class PermitType(Enum):
    """Enumeration of permit types."""
    IMPORT = auto()
    EXPORT = auto()
    TRANSPORT = auto()
    STORAGE = auto()
    OPERATIONAL = auto()


class CommercialEntity:
    """Represents a commercial entity in international trade."""
    
    def __init__(self, name: str, entity_type: EntityType, tax_id: str, country: str):
        """
        Initialize a commercial entity.
        
        Args:
            name: Name of the entity
            entity_type: Type of entity (from EntityType enum)
            tax_id: Tax identification number
            country: Country of registration
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.entity_type = entity_type
        self.tax_id = tax_id
        self.country = country
        self.licenses: List[License] = []
        self.permits: List[Permit] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def add_license(self, license_data: Dict) -> 'License':
        """Add a new license to the entity."""
        license_obj = License(**license_data)
        self.licenses.append(license_obj)
        self.updated_at = datetime.utcnow()
        return license_obj
    
    def add_permit(self, permit_data: Dict) -> 'Permit':
        """Add a new permit to the entity."""
        permit_obj = Permit(**permit_data)
        self.permits.append(permit_obj)
        self.updated_at = datetime.utcnow()
        return permit_obj
    
    def get_active_licenses(self) -> List['License']:
        """Return all active licenses."""
        return [lic for lic in self.licenses if lic.status == LicenseStatus.ACTIVE]
    
    def get_active_permits(self) -> List['Permit']:
        """Return all active permits."""
        return [perm for perm in self.permits if perm.is_valid()]
    
    def to_dict(self) -> Dict:
        """Convert entity data to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'entity_type': self.entity_type.name,
            'tax_id': self.tax_id,
            'country': self.country,
            'licenses': [lic.to_dict() for lic in self.licenses],
            'permits': [perm.to_dict() for perm in self.permits],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class License:
    """Represents a trade license for a commercial entity."""
    
    def __init__(self, license_number: str, issuing_authority: str, 
                 issue_date: str, expiry_date: str, status: LicenseStatus,
                 description: Optional[str] = None):
        """
        Initialize a trade license.
        
        Args:
            license_number: Official license number
            issuing_authority: Authority that issued the license
            issue_date: Date of issue (YYYY-MM-DD)
            expiry_date: Date of expiry (YYYY-MM-DD)
            status: Current status of the license
            description: Optional description of the license
        """
        self.license_number = license_number
        self.issuing_authority = issuing_authority
        self.issue_date = datetime.strptime(issue_date, '%Y-%m-%d').date()
        self.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
        self.status = status
        self.description = description
        self.created_at = datetime.utcnow()
    
    def is_valid(self) -> bool:
        """Check if license is currently valid."""
        today = datetime.utcnow().date()
        return (self.status == LicenseStatus.ACTIVE and 
                self.issue_date <= today <= self.expiry_date)
    
    def to_dict(self) -> Dict:
        """Convert license data to dictionary."""
        return {
            'license_number': self.license_number,
            'issuing_authority': self.issuing_authority,
            'issue_date': self.issue_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat(),
            'status': self.status.name,
            'description': self.description,
            'is_valid': self.is_valid(),
            'created_at': self.created_at.isoformat()
        }


class Permit:
    """Represents a trade permit for a commercial entity."""
    
    def __init__(self, permit_number: str, permit_type: PermitType, 
                 issuing_authority: str, issue_date: str, expiry_date: str,
                 countries: List[str], description: Optional[str] = None):
        """
        Initialize a trade permit.
        
        Args:
            permit_number: Official permit number
            permit_type: Type of permit (from PermitType enum)
            issuing_authority: Authority that issued the permit
            issue_date: Date of issue (YYYY-MM-DD)
            expiry_date: Date of expiry (YYYY-MM-DD)
            countries: List of countries where permit is valid
            description: Optional description of the permit
        """
        self.permit_number = permit_number
        self.permit_type = permit_type
        self.issuing_authority = issuing_authority
        self.issue_date = datetime.strptime(issue_date, '%Y-%m-%d').date()
        self.expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
        self.countries = countries
        self.description = description
        self.created_at = datetime.utcnow()
    
    def is_valid(self) -> bool:
        """Check if permit is currently valid."""
        today = datetime.utcnow().date()
        return self.issue_date <= today <= self.expiry_date
    
    def is_valid_for_country(self, country: str) -> bool:
        """Check if permit is valid for a specific country."""
        return self.is_valid() and country in self.countries
    
    def to_dict(self) -> Dict:
        """Convert permit data to dictionary."""
        return {
            'permit_number': self.permit_number,
            'permit_type': self.permit_type.name,
            'issuing_authority': self.issuing_authority,
            'issue_date': self.issue_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat(),
            'countries': self.countries,
            'description': self.description,
            'is_valid': self.is_valid(),
            'created_at': self.created_at.isoformat()
        }


class TradeRegistry:
    """Main registry for managing commercial entities and their documents."""
    
    def __init__(self):
        """Initialize an empty trade registry."""
        self.entities: Dict[str, CommercialEntity] = {}
    
    def add_entity(self, entity_data: Dict) -> CommercialEntity:
        """Add a new commercial entity to the registry."""
        entity_type = EntityType[entity_data['entity_type']]
        entity = CommercialEntity(
            name=entity_data['name'],
            entity_type=entity_type,
            tax_id=entity_data['tax_id'],
            country=entity_data['country']
        )
        self.entities[entity.id] = entity
        return entity
    
    def get_entity(self, entity_id: str) -> Optional[CommercialEntity]:
        """Retrieve an entity by its ID."""
        return self.entities.get(entity_id)
    
    def search_entities(self, name: Optional[str] = None, 
                       entity_type: Optional[EntityType] = None,
                       country: Optional[str] = None) -> List[CommercialEntity]:
        """Search for entities matching the given criteria."""
        results = list(self.entities.values())
        
        if name:
            results = [e for e in results if name.lower() in e.name.lower()]
        if entity_type:
            results = [e for e in results if e.entity_type == entity_type]
        if country:
            results = [e for e in results if e.country.lower() == country.lower()]
        
        return results
    
    def validate_entity_for_trade(self, entity_id: str, 
                                 target_country: str) -> Dict[str, Union[bool, List[str]]]:
        """
        Validate if an entity has all required documents for trade with a target country.
        
        Returns:
            Dictionary with validation results and missing requirements
        """
        entity = self
