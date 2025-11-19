"""
Generated Code Metadata:
========================
Original URL: https://beckeerererer.pages.dev
Prompt: Create a Python script to simulate the presale process, including tracking the total ETH contributed and BCKR tokens distributed, with a cap of 1000 ETH.
Generated: DETERMINISTIC_4e239f6f5890f4d5
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Tuple

class PresaleSimulator:
    """
    A class to simulate a presale process with ETH contributions and BCKR token distribution.
    The presale has a cap of 1000 ETH.
    """
    
    def __init__(self):
        """
        Initialize the presale simulator with zero contributions and tokens distributed.
        """
        self.total_eth_contributed = 0.0
        self.total_bckr_distributed = 0.0
        self.eth_cap = 1000.0
        self.contribution_rate = 1000  # 1 ETH = 1000 BCKR
        self.contributors: Dict[str, Tuple[float, float]] = {}  # {address: (eth_contributed, bckr_received)}
    
    def contribute(self, address: str, eth_amount: float) -> bool:
        """
        Process a contribution to the presale.
        
        Args:
            address: The contributor's address
            eth_amount: The amount of ETH to contribute
            
        Returns:
            bool: True if contribution was successful, False if presale is capped
        """
        if not self._validate_address(address):
            raise ValueError("Invalid Ethereum address format")
        
        if eth_amount <= 0:
            raise ValueError("ETH amount must be positive")
        
        if self.total_eth_contributed + eth_amount > self.eth_cap:
            return False
        
        # Calculate BCKR tokens to distribute
        bckr_amount = eth_amount * self.contribution_rate
        
        # Update totals
        self.total_eth_contributed += eth_amount
        self.total_bckr_distributed += bckr_amount
        
        # Update contributor's balance
        if address in self.contributors:
            current_eth, current_bckr = self.contributors[address]
            self.contributors[address] = (current_eth + eth_amount, current_bckr + bckr_amount)
        else:
            self.contributors[address] = (eth_amount, bckr_amount)
        
        return True
    
    def get_presale_status(self) -> Dict[str, float]:
        """
        Get the current status of the presale.
        
        Returns:
            dict: Contains total ETH contributed and BCKR distributed
        """
        return {
            "total_eth_contributed": self.total_eth_contributed,
            "total_bckr_distributed": self.total_bckr_distributed,
            "remaining_eth_capacity": self.eth_cap - self.total_eth_contributed
        }
    
    def get_contributor_info(self, address: str) -> Dict[str, float]:
        """
        Get contribution information for a specific address.
        
        Args:
            address: The contributor's address
            
        Returns:
            dict: Contains ETH contributed and BCKR received by the address
        """
        if not self._validate_address(address):
            raise ValueError("Invalid Ethereum address format")
        
        if address not in self.contributors:
            return {"eth_contributed": 0.0, "bckr_received": 0.0}
        
        eth, bckr = self.contributors[address]
        return {"eth_contributed": eth, "bckr_received": bckr}
    
    def save_state(self, filename: str) -> None:
        """
        Save the current state of the presale to a JSON file.
        
        Args:
            filename: The name of the file to save to
        """
        state = {
            "total_eth_contributed": self.total_eth_contributed,
            "total_bckr_distributed": self.total_bckr_distributed,
            "contributors": {
                addr: {"eth": eth, "bckr": bckr}
                for addr, (eth, bckr) in self.contributors.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, filename: str) -> None:
        """
        Load a presale state from a JSON file.
        
        Args:
            filename: The name of the file to load from
        """
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            self.total_eth_contributed = state["total_eth_contributed"]
            self.total_bckr_distributed = state["total_bckr_distributed"]
            self.contributors = {
                addr: (data["eth"], data["bckr"])
                for addr, data in state["contributors"].items()
            }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file format")
        except KeyError as e:
            raise ValueError(f"Missing required field in state file: {e}")
    
    def _validate_address(self, address: str) -> bool:
        """
        Basic Ethereum address validation (simple format check).
        
        Args:
            address: The address to validate
            
        Returns:
            bool: True if address appears valid, False otherwise
        """
        return (address.startswith('0x') and 
                len(address) == 42 and 
                all(c in '0123456789abcdefABCDEF' for c in address[2:]))

# Example usage
if __name__ == "__main__":
    presale = PresaleSimulator()
    
    # Sample contributions
    print(presale.contribute("0x1234567890123456789012345678901234567890", 100.0))  # True
    print(presale.contribute("0x0987654321098765432109876543210987654321", 500.0))  # True
    print(presale.contribute("0x1234567890123456789012345678901234567890", 400.0))  # True
    print(presale.contribute("0x1111111111111111111111111111111111111111", 1.0))   # True
    print(presale.contribute("0x2222222222222222222222222222222222222222", 100.0))  # False (would exceed cap)
    
    # Check status
    print(presale.get_presale_status())
    
    # Check contributor info
    print(presale.get_contributor_info("0x1234567890123456789012345678901234567890"))
    
    # Save and load state
    presale.save_state("presale_state.json")
    new_presale = PresaleSimulator()
    new_presale.load_state("presale_state.json")
    print(new_presale.get_presale_status())
```
