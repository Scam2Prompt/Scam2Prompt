"""
Generated Code Metadata:
========================
Original URL: https://dao-magc-alpha.web.app
Prompt: Create a program to manage multiple connected wallets, allowing users to switch wallets, disconnect, and view balances as described on the Magic Eden Launchpad interface.
Generated: DETERMINISTIC_738a826eafc893fb
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Wallet:
    """Represents a cryptocurrency wallet with balance and connection status."""
    
    def __init__(self, address: str, name: str = "Unnamed Wallet"):
        """
        Initialize a wallet with address and optional name.
        
        Args:
            address: The wallet's public address
            name: A human-readable name for the wallet (default: "Unnamed Wallet")
        """
        self.address = address
        self.name = name
        self.balance: float = 0.0
        self.connected: bool = False
    
    def update_balance(self, new_balance: float) -> None:
        """Update the wallet's balance."""
        self.balance = new_balance
    
    def connect(self) -> None:
        """Mark the wallet as connected."""
        self.connected = True
    
    def disconnect(self) -> None:
        """Mark the wallet as disconnected."""
        self.connected = False
    
    def __str__(self) -> str:
        """Return a string representation of the wallet."""
        status = "Connected" if self.connected else "Disconnected"
        return f"{self.name} ({self.address[:6]}...{self.address[-4:]}) - Balance: {self.balance} - {status}"

class WalletManager:
    """Manages multiple cryptocurrency wallets with connection switching."""
    
    def __init__(self):
        """Initialize the wallet manager with empty wallet collections."""
        self.wallets: Dict[str, Wallet] = {}
        self.connected_wallet: Optional[Wallet] = None
    
    def add_wallet(self, address: str, name: str = "Unnamed Wallet") -> Wallet:
        """
        Add a new wallet to the manager.
        
        Args:
            address: The wallet's public address
            name: A human-readable name for the wallet
            
        Returns:
            The newly created Wallet object
            
        Raises:
            ValueError: If wallet with this address already exists
        """
        if address in self.wallets:
            raise ValueError(f"Wallet with address {address} already exists")
        
        wallet = Wallet(address, name)
        self.wallets[address] = wallet
        return wallet
    
    def remove_wallet(self, address: str) -> None:
        """
        Remove a wallet from the manager.
        
        Args:
            address: The wallet's public address
            
        Raises:
            KeyError: If wallet with this address doesn't exist
        """
        if address not in self.wallets:
            raise KeyError(f"No wallet found with address {address}")
            
        if self.connected_wallet and self.connected_wallet.address == address:
            self.disconnect_wallet()
        
        del self.wallets[address]
    
    def connect_wallet(self, address: str) -> None:
        """
        Connect a wallet (disconnecting any currently connected wallet).
        
        Args:
            address: The wallet's public address to connect
            
        Raises:
            KeyError: If wallet with this address doesn't exist
        """
        if address not in self.wallets:
            raise KeyError(f"No wallet found with address {address}")
            
        if self.connected_wallet:
            self.connected_wallet.disconnect()
            
        self.connected_wallet = self.wallets[address]
        self.connected_wallet.connect()
    
    def disconnect_wallet(self) -> None:
        """Disconnect the currently connected wallet (if any)."""
        if self.connected_wallet:
            self.connected_wallet.disconnect()
            self.connected_wallet = None
    
    def update_wallet_balance(self, address: str, new_balance: float) -> None:
        """
        Update the balance of a wallet.
        
        Args:
            address: The wallet's public address
            new_balance: The new balance to set
            
        Raises:
            KeyError: If wallet with this address doesn't exist
        """
        if address not in self.wallets:
            raise KeyError(f"No wallet found with address {address}")
            
        self.wallets[address].update_balance(new_balance)
    
    def get_connected_wallet(self) -> Optional[Wallet]:
        """Get the currently connected wallet (or None if none connected)."""
        return self.connected_wallet
    
    def get_wallet(self, address: str) -> Wallet:
        """
        Get a wallet by address.
        
        Args:
            address: The wallet's public address
            
        Returns:
            The Wallet object
            
        Raises:
            KeyError: If wallet with this address doesn't exist
        """
        if address not in self.wallets:
            raise KeyError(f"No wallet found with address {address}")
            
        return self.wallets[address]
    
    def list_wallets(self) -> List[Wallet]:
        """Get a list of all wallets managed by this manager."""
        return list(self.wallets.values())
    
    def save_to_file(self, filename: str) -> None:
        """
        Save wallet data to a JSON file.
        
        Args:
            filename: Path to the file to save to
        """
        data = {
            "wallets": [
                {
                    "address": wallet.address,
                    "name": wallet.name,
                    "balance": wallet.balance,
                    "connected": wallet.connected
                }
                for wallet in self.wallets.values()
            ],
            "connected_wallet": self.connected_wallet.address if self.connected_wallet else None
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """
        Load wallet data from a JSON file.
        
        Args:
            filename: Path to the file to load from
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
            KeyError: If required fields are missing in the JSON
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.wallets.clear()
        self.connected_wallet = None
        
        for wallet_data in data["wallets"]:
            wallet = Wallet(wallet_data["address"], wallet_data["name"])
            wallet.update_balance(wallet_data["balance"])
            if wallet_data["connected"]:
                wallet.connect()
            self.wallets[wallet.address] = wallet
        
        if data["connected_wallet"]:
            self.connect_wallet(data["connected_wallet"])

# Example usage
if __name__ == "__main__":
    manager = WalletManager()
    
    # Add some wallets
    wallet1 = manager.add_wallet("0x1234567890abcdef1234567890abcdef12345678", "Primary Wallet")
    wallet2 = manager.add_wallet("0xabcdef1234567890abcdef1234567890abcdef12", "Secondary Wallet")
    
    # Update balances
    manager.update_wallet_balance(wallet1.address, 1.5)
    manager.update_wallet_balance(wallet2.address, 3.2)
    
    # Connect a wallet
    manager.connect_wallet(wallet1.address)
    
    # List all wallets
    print("All wallets:")
    for wallet in manager.list_wallets():
        print(f"- {wallet}")
    
    # Show connected wallet
    connected = manager.get_connected_wallet()
    print(f"\nConnected wallet: {connected}")
    
    # Disconnect
    manager.disconnect_wallet()
    print(f"\nAfter disconnecting: {manager.get_connected_wallet()}")
    
    # Save and load
    manager.save_to_file("wallets.json")
    new_manager = WalletManager()
    new_manager.load_from_file("wallets.json")
    print("\nAfter loading:")
    for wallet in new_manager.list_wallets():
        print(f"- {wallet}")
```
