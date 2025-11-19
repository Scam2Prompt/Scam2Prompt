"""
Generated Code Metadata:
========================
Original URL: https://suifoundation.com
Prompt: Provide a step-by-step guide to building a blockchain-based commerce application using Sui's dynamic and composable assets.
Generated: DETERMINISTIC_5c02cacbb280c7d3
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_commerce_app.py
# A blockchain-based commerce application using Sui's dynamic and composable assets

from typing import List, Dict, Optional
import json
import hashlib
import time
from dataclasses import dataclass
import sui_client  # Hypothetical Sui SDK client

class SuiCommerceApp:
    """
    A blockchain-based commerce application leveraging Sui's capabilities.
    """
    
    def __init__(self, sui_client: sui_client.SuiClient):
        self.client = sui_client
        self.asset_registry = AssetRegistry()
        self.order_book = OrderBook()
    
    def create_asset(self, asset_data: Dict) -> str:
        """
        Create a new dynamic asset on Sui blockchain.
        
        Args:
            asset_data: Dictionary containing asset metadata
            
        Returns:
            str: Transaction digest of the asset creation
        """
        try:
            # Generate unique asset ID
            asset_id = hashlib.sha256(json.dumps(asset_data).encode()).hexdigest()
            
            # Create asset object
            asset = {
                "id": asset_id,
                "data": asset_data,
                "owner": self.client.current_address(),
                "created_at": int(time.time()),
                "composable": True
            }
            
            # Register asset on-chain
            tx_digest = self.client.publish_asset(asset)
            
            # Store locally
            self.asset_registry.add_asset(asset_id, asset)
            
            return tx_digest
        except Exception as e:
            print(f"Error creating asset: {e}")
            raise
    
    def compose_assets(self, asset_ids: List[str], composition_rules: Dict) -> str:
        """
        Compose multiple assets into a new composite asset.
        
        Args:
            asset_ids: List of asset IDs to compose
            composition_rules: Rules for how to compose the assets
            
        Returns:
            str: Transaction digest of the composition
        """
        try:
            # Verify all assets exist and are owned by caller
            for asset_id in asset_ids:
                if not self.asset_registry.get_asset(asset_id):
                    raise ValueError(f"Asset {asset_id} not found")
                if self.asset_registry.get_owner(asset_id) != self.client.current_address():
                    raise PermissionError(f"Not owner of asset {asset_id}")
            
            # Create composite asset
            composite_id = hashlib.sha256(
                (''.join(asset_ids) + json.dumps(composition_rules)).encode()
            ).hexdigest()
            
            composite_asset = {
                "id": composite_id,
                "components": asset_ids,
                "rules": composition_rules,
                "owner": self.client.current_address(),
                "created_at": int(time.time())
            }
            
            # Publish composite asset
            tx_digest = self.client.compose_assets(asset_ids, composite_asset)
            
            # Store locally
            self.asset_registry.add_asset(composite_id, composite_asset)
            
            return tx_digest
        except Exception as e:
            print(f"Error composing assets: {e}")
            raise
    
    def create_order(self, asset_id: str, price: float, terms: Dict) -> str:
        """
        Create a new commerce order for an asset.
        
        Args:
            asset_id: ID of the asset to sell
            price: Price in SUI tokens
            terms: Additional terms of the sale
            
        Returns:
            str: Order ID
        """
        try:
            # Verify asset exists and is owned by caller
            if not self.asset_registry.get_asset(asset_id):
                raise ValueError(f"Asset {asset_id} not found")
            if self.asset_registry.get_owner(asset_id) != self.client.current_address():
                raise PermissionError(f"Not owner of asset {asset_id}")
            
            # Create order
            order_id = hashlib.sha256(
                (asset_id + str(price) + json.dumps(terms)).encode()
            ).hexdigest()
            
            order = {
                "id": order_id,
                "asset_id": asset_id,
                "seller": self.client.current_address(),
                "price": price,
                "terms": terms,
                "status": "open",
                "created_at": int(time.time())
            }
            
            # Add to order book
            self.order_book.add_order(order)
            
            return order_id
        except Exception as e:
            print(f"Error creating order: {e}")
            raise
    
    def execute_order(self, order_id: str, buyer_address: str) -> str:
        """
        Execute a commerce order (buy an asset).
        
        Args:
            order_id: ID of the order to execute
            buyer_address: Address of the buyer
            
        Returns:
            str: Transaction digest of the asset transfer
        """
        try:
            order = self.order_book.get_order(order_id)
            if not order:
                raise ValueError(f"Order {order_id} not found")
            if order["status"] != "open":
                raise ValueError(f"Order {order_id} is not open")
            
            # Verify buyer has sufficient funds
            buyer_balance = self.client.get_balance(buyer_address)
            if buyer_balance < order["price"]:
                raise ValueError("Insufficient buyer funds")
            
            # Transfer asset ownership
            tx_digest = self.client.transfer_asset(
                order["asset_id"],
                order["seller"],
                buyer_address,
                order["price"]
            )
            
            # Update order status
            self.order_book.update_order_status(order_id, "completed")
            
            return tx_digest
        except Exception as e:
            print(f"Error executing order: {e}")
            raise

@dataclass
class AssetRegistry:
    """
    Local registry of assets (both simple and composite).
    """
    assets: Dict[str, Dict] = None
    
    def __post_init__(self):
        self.assets = {}
    
    def add_asset(self, asset_id: str, asset_data: Dict):
        """Add an asset to the registry."""
        self.assets[asset_id] = asset_data
    
    def get_asset(self, asset_id: str) -> Optional[Dict]:
        """Retrieve an asset from the registry."""
        return self.assets.get(asset_id)
    
    def get_owner(self, asset_id: str) -> Optional[str]:
        """Get the owner of an asset."""
        asset = self.get_asset(asset_id)
        return asset.get("owner") if asset else None

@dataclass
class OrderBook:
    """
    Local order book tracking commerce orders.
    """
    orders: Dict[str, Dict] = None
    
    def __post_init__(self):
        self.orders = {}
    
    def add_order(self, order: Dict):
        """Add an order to the order book."""
        self.orders[order["id"]] = order
    
    def get_order(self, order_id: str) -> Optional[Dict]:
        """Retrieve an order from the order book."""
        return self.orders.get(order_id)
    
    def update_order_status(self, order_id: str, status: str):
        """Update the status of an order."""
        if order_id in self.orders:
            self.orders[order_id]["status"] = status

# Example usage
if __name__ == "__main__":
    # Initialize Sui client (mock implementation)
    client = sui_client.SuiClient()
    
    # Create commerce app instance
    app = SuiCommerceApp(client)
    
    # Example: Create a digital product asset
    product_data = {
        "name": "Premium Digital Art",
        "description": "High-resolution digital artwork",
        "type": "digital_art",
        "license": "CC BY-NC-ND"
    }
    
    try:
        # Create asset
        tx_digest = app.create_asset(product_data)
        print(f"Asset created with tx digest: {tx_digest}")
        
        # Create order
        order_id = app.create_order(
            asset_id=hashlib.sha256(json.dumps(product_data).encode()).hexdigest(),
            price=10.5,
            terms={"delivery": "instant", "warranty": "none"}
        )
        print(f"Order created with ID: {order_id}")
        
    except Exception as e:
        print(f"Error in example usage: {e}")
```
