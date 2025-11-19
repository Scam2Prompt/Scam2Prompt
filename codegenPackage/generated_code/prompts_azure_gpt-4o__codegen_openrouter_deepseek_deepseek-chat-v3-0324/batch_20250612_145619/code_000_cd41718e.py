"""
Generated Code Metadata:
========================
Original URL: https://gaimin-io.pages.dev
Prompt: Write Python code using GAIMIN's GAIMCRAFT SDK to integrate NFT-based in-game asset ownership into an existing game, ensuring interoperability and cross-game functionality.
Generated: DETERMINISTIC_cd41718ea48c34d3
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Optional, Dict, List
from gaimcraft_sdk import GAIMCRAFT, NFT, Blockchain, Wallet

class NFTGameAssetManager:
    """
    Manages NFT-based in-game assets using GAIMCRAFT SDK.
    Provides functionality for ownership verification, transfers, and cross-game interoperability.
    """
    
    def __init__(self, game_id: str, blockchain_network: str = "polygon"):
        """
        Initialize the NFT asset manager with game ID and blockchain network.
        
        Args:
            game_id: Unique identifier for the game
            blockchain_network: Blockchain network to use (default: polygon)
        """
        self.game_id = game_id
        self.sdk = GAIMCRAFT(api_key=os.getenv("GAIMCRAFT_API_KEY"))
        self.blockchain = Blockchain(network=blockchain_network)
        self.wallet = Wallet(self.blockchain)
        
        # Cache for loaded NFTs to reduce blockchain queries
        self.nft_cache: Dict[str, NFT] = {}
        
    def connect_wallet(self, private_key: Optional[str] = None) -> bool:
        """
        Connect to a wallet either via private key or web3 provider.
        
        Args:
            private_key: Optional private key for direct wallet access
            
        Returns:
            bool: True if wallet connection succeeded
        """
        try:
            if private_key:
                self.wallet.connect_via_private_key(private_key)
            else:
                self.wallet.connect_via_web3()
            return True
        except Exception as e:
            print(f"Wallet connection failed: {str(e)}")
            return False
    
    def verify_asset_ownership(self, player_address: str, asset_id: str) -> bool:
        """
        Verify if a player owns a specific NFT asset.
        
        Args:
            player_address: Player's wallet address
            asset_id: Unique identifier of the NFT asset
            
        Returns:
            bool: True if player owns the asset
        """
        try:
            if asset_id in self.nft_cache:
                nft = self.nft_cache[asset_id]
            else:
                nft = self.sdk.get_nft(asset_id)
                self.nft_cache[asset_id] = nft
            
            return nft.verify_ownership(player_address)
        except Exception as e:
            print(f"Ownership verification failed: {str(e)}")
            return False
    
    def get_player_assets(self, player_address: str) -> List[NFT]:
        """
        Get all NFT assets owned by a player that are compatible with this game.
        
        Args:
            player_address: Player's wallet address
            
        Returns:
            List[NFT]: List of NFT objects owned by the player
        """
        try:
            assets = self.sdk.query_nfts(
                owner=player_address,
                game_id=self.game_id,
                compatible=True
            )
            # Update cache
            for asset in assets:
                self.nft_cache[asset.id] = asset
            return assets
        except Exception as e:
            print(f"Failed to fetch player assets: {str(e)}")
            return []
    
    def transfer_asset(self, from_address: str, to_address: str, asset_id: str) -> bool:
        """
        Transfer an NFT asset between players.
        
        Args:
            from_address: Current owner's wallet address
            to_address: New owner's wallet address
            asset_id: Unique identifier of the NFT asset
            
        Returns:
            bool: True if transfer succeeded
        """
        try:
            if not self.verify_asset_ownership(from_address, asset_id):
                return False
                
            nft = self.nft_cache.get(asset_id) or self.sdk.get_nft(asset_id)
            tx_hash = nft.transfer(to_address)
            
            if tx_hash:
                # Update cache
                self.nft_cache.pop(asset_id, None)
                return True
            return False
        except Exception as e:
            print(f"Asset transfer failed: {str(e)}")
            return False
    
    def get_asset_metadata(self, asset_id: str) -> Optional[Dict]:
        """
        Get metadata for a specific NFT asset.
        
        Args:
            asset_id: Unique identifier of the NFT asset
            
        Returns:
            Optional[Dict]: Dictionary containing asset metadata or None if failed
        """
        try:
            nft = self.nft_cache.get(asset_id) or self.sdk.get_nft(asset_id)
            return nft.metadata
        except Exception as e:
            print(f"Failed to fetch asset metadata: {str(e)}")
            return None
    
    def get_cross_game_assets(self, player_address: str) -> List[NFT]:
        """
        Get all NFT assets owned by a player that have cross-game interoperability.
        
        Args:
            player_address: Player's wallet address
            
        Returns:
            List[NFT]: List of cross-game compatible NFT objects
        """
        try:
            assets = self.sdk.query_nfts(
                owner=player_address,
                cross_game=True
            )
            # Update cache
            for asset in assets:
                self.nft_cache[asset.id] = asset
            return assets
        except Exception as e:
            print(f"Failed to fetch cross-game assets: {str(e)}")
            return []
    
    def mint_asset(self, metadata: Dict, recipient: str) -> Optional[str]:
        """
        Mint a new NFT asset for the game.
        
        Args:
            metadata: Dictionary containing asset metadata
            recipient: Wallet address to receive the new NFT
            
        Returns:
            Optional[str]: Transaction hash if successful, None otherwise
        """
        try:
            # Add game-specific metadata
            metadata["game_id"] = self.game_id
            metadata["cross_game"] = metadata.get("cross_game", False)
            
            tx_hash = self.sdk.mint_nft(
                wallet=self.wallet,
                metadata=metadata,
                recipient=recipient
            )
            return tx_hash
        except Exception as e:
            print(f"Asset minting failed: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize with your game ID
    asset_manager = NFTGameAssetManager(game_id="my_awesome_game")
    
    # Connect wallet (in production, use secure methods for private key handling)
    if asset_manager.connect_wallet():
        print("Wallet connected successfully")
        
        # Example: Check ownership
        player_address = "0xPlayerAddress123"
        asset_id = "nft-12345"
        if asset_manager.verify_asset_ownership(player_address, asset_id):
            print("Player owns this asset")
            
            # Get asset metadata
            metadata = asset_manager.get_asset_metadata(asset_id)
            print(f"Asset metadata: {json.dumps(metadata, indent=2)}")
            
            # Example transfer (would need proper authorization in real implementation)
            # asset_manager.transfer_asset(player_address, "0xRecipient123", asset_id)
        
        # Get all player's assets
        assets = asset_manager.get_player_assets(player_address)
        print(f"Player has {len(assets)} assets in this game")
        
        # Get cross-game assets
        cross_game_assets = asset_manager.get_cross_game_assets(player_address)
        print(f"Player has {len(cross_game_assets)} cross-game assets")
```
