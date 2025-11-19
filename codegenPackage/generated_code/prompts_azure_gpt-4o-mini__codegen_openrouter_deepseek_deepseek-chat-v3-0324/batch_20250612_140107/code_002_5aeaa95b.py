"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: What are the best practices for managing digital inventory in the entertainment industry to enhance commercial sales support?
Generated: DETERMINISTIC_5aeaa95b06e7870b
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Inventory Management System for Entertainment Industry

This module provides functionalities to manage digital inventory 
to enhance commercial sales support in the entertainment industry.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MediaType(Enum):
    """Enum representing different types of media in inventory."""
    MOVIE = "Movie"
    TV_SHOW = "TV Show"
    MUSIC = "Music"
    EBOOK = "EBook"
    GAME = "Game"

class DigitalAsset:
    """Class representing a digital asset in inventory."""
    
    def __init__(
        self,
        asset_id: str,
        title: str,
        media_type: MediaType,
        release_date: datetime,
        price: float,
        metadata: Dict,
        available_licenses: int = 0
    ):
        """
        Initialize a digital asset.
        
        Args:
            asset_id: Unique identifier for the asset
            title: Title of the asset
            media_type: Type of media (from MediaType enum)
            release_date: Date when asset was released
            price: Price of the asset
            metadata: Additional metadata about the asset
            available_licenses: Number of available licenses
        """
        self.asset_id = asset_id
        self.title = title
        self.media_type = media_type
        self.release_date = release_date
        self.price = price
        self.metadata = metadata
        self.available_licenses = available_licenses
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert asset to dictionary for serialization."""
        return {
            "asset_id": self.asset_id,
            "title": self.title,
            "media_type": self.media_type.value,
            "release_date": self.release_date.isoformat(),
            "price": self.price,
            "metadata": self.metadata,
            "available_licenses": self.available_licenses,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    def update_licenses(self, delta: int) -> bool:
        """
        Update available licenses.
        
        Args:
            delta: Change in license count (positive or negative)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if self.available_licenses + delta < 0:
            logger.warning(f"Insufficient licenses for {self.title}")
            return False
        
        self.available_licenses += delta
        self.updated_at = datetime.now()
        logger.info(f"Updated licenses for {self.title}. New count: {self.available_licenses}")
        return True

class DigitalInventoryManager:
    """Class to manage digital inventory for commercial sales support."""
    
    def __init__(self, storage_file: str = "inventory.json"):
        """
        Initialize inventory manager.
        
        Args:
            storage_file: Path to JSON file for persistent storage
        """
        self.storage_file = storage_file
        self.inventory: Dict[str, DigitalAsset] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory from storage file."""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                for asset_data in data.get('assets', []):
                    try:
                        asset = DigitalAsset(
                            asset_id=asset_data['asset_id'],
                            title=asset_data['title'],
                            media_type=MediaType(asset_data['media_type']),
                            release_date=datetime.fromisoformat(asset_data['release_date']),
                            price=asset_data['price'],
                            metadata=asset_data['metadata'],
                            available_licenses=asset_data['available_licenses']
                        )
                        asset.created_at = datetime.fromisoformat(asset_data['created_at'])
                        asset.updated_at = datetime.fromisoformat(asset_data['updated_at'])
                        self.inventory[asset.asset_id] = asset
                    except (KeyError, ValueError) as e:
                        logger.error(f"Error loading asset: {e}")
            logger.info(f"Inventory loaded from {self.storage_file}")
        except FileNotFoundError:
            logger.info("No existing inventory file found. Starting with empty inventory.")
        except json.JSONDecodeError:
            logger.error("Invalid JSON in inventory file. Starting with empty inventory.")
    
    def _save_inventory(self) -> None:
        """Save inventory to storage file."""
        data = {
            "assets": [asset.to_dict() for asset in self.inventory.values()]
        }
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Inventory saved to {self.storage_file}")
        except IOError as e:
            logger.error(f"Error saving inventory: {e}")
    
    def add_asset(
        self,
        title: str,
        media_type: MediaType,
        release_date: datetime,
        price: float,
        metadata: Dict,
        available_licenses: int = 0
    ) -> str:
        """
        Add a new asset to inventory.
        
        Args:
            title: Title of the asset
            media_type: Type of media
            release_date: Release date
            price: Price of asset
            metadata: Additional metadata
            available_licenses: Number of available licenses
            
        Returns:
            str: ID of the newly created asset
        """
        asset_id = str(uuid.uuid4())
        asset = DigitalAsset(
            asset_id=asset_id,
            title=title,
            media_type=media_type,
            release_date=release_date,
            price=price,
            metadata=metadata,
            available_licenses=available_licenses
        )
        self.inventory[asset_id] = asset
        self._save_inventory()
        logger.info(f"Added new asset: {title} ({asset_id})")
        return asset_id
    
    def get_asset(self, asset_id: str) -> Optional[DigitalAsset]:
        """
        Get asset by ID.
        
        Args:
            asset_id: ID of the asset to retrieve
            
        Returns:
            Optional[DigitalAsset]: The asset if found, None otherwise
        """
        return self.inventory.get(asset_id)
    
    def update_asset(
        self,
        asset_id: str,
        title: Optional[str] = None,
        price: Optional[float] = None,
        metadata: Optional[Dict] = None,
        available_licenses: Optional[int] = None
    ) -> bool:
        """
        Update asset properties.
        
        Args:
            asset_id: ID of asset to update
            title: New title (optional)
            price: New price (optional)
            metadata: New metadata (optional)
            available_licenses: New license count (optional)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        asset = self.get_asset(asset_id)
        if not asset:
            logger.warning(f"Asset {asset_id} not found for update")
            return False
        
        if title is not None:
            asset.title = title
        if price is not None:
            asset.price = price
        if metadata is not None:
            asset.metadata = metadata
        if available_licenses is not None:
            asset.available_licenses = available_licenses
        
        asset.updated_at = datetime.now()
        self._save_inventory()
        logger.info(f"Updated asset {asset_id}")
        return True
    
    def remove_asset(self, asset_id: str) -> bool:
        """
        Remove asset from inventory.
        
        Args:
            asset_id: ID of asset to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        if asset_id not in self.inventory:
            logger.warning(f"Asset {asset_id} not found for removal")
            return False
        
        del self.inventory[asset_id]
        self._save_inventory()
        logger.info(f"Removed asset {asset_id}")
        return True
    
    def search_assets(
        self,
        title: Optional[str] = None,
        media_type: Optional[MediaType] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        available_only: bool = False
    ) -> List[DigitalAsset]:
        """
        Search assets based on criteria.
        
        Args:
            title: Title substring to match (optional)
            media_type: Media type to filter by (optional)
            min_price: Minimum price (optional)
            max_price: Maximum price (optional)
            available_only: Only return assets with available licenses
            
        Returns:
            List[DigitalAsset]: List of matching assets
        """
        results = []
        for asset in self.inventory.values():
            if title and title.lower() not in asset.title.lower():
                continue
            if media_type and asset.media_type != media_type:
                continue
            if min
