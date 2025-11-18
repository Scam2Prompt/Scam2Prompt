"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Write a Python program to derive child keys from a parent extended private key using the BIP32 derivation path `m/44'/0'/0'`, and output the derived addresses in CSV format.
Generated: DETERMINISTIC_9f64c5e3b426af9a
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List
from bip32utils import BIP32, BIP32Node
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinAddress

# Select the Bitcoin mainnet parameters
SelectParams('mainnet')

def derive_addresses_from_xpriv(xpriv: str, derivation_path: str, num_addresses: int) -> List[str]:
    """
    Derives child addresses from an extended private key (xpriv) using a given derivation path.
    
    Args:
        xpriv (str): The parent extended private key.
        derivation_path (str): The BIP32 derivation path.
        num_addresses (int): Number of child addresses to derive.

    Returns:
        List[str]: A list of derived Bitcoin addresses.
    """
    try:
        # Parse the derivation path
        path_parts = derivation_path.split('/')
        assert path_parts[0] == 'm', "Invalid derivation path. It must start with 'm'."
        
        # Create BIP32 object from the extended private key
        root_key = BIP32Node.fromExtendedKey(xpriv)
        
        # Derive the base path
        for part in path_parts[1:]:
            hardened = "'" in part
            index = int(part.replace("'", ""))
            root_key = root_key.ChildKey(index + (BIP32.HARDENED if hardened else 0))
        
        # Generate and return the child addresses
        return [CBitcoinAddress.from_pubkey(root_key.ChildKey(i).PublicKey()) for i in range(num_addresses)]
    
    except Exception as e:
        raise ValueError(f"Error during address derivation: {str(e)}")

def write_addresses_to_csv(addresses: List[str], filename: str) -> None:
    """
    Writes a list of Bitcoin addresses to a CSV file.

    Args:
        addresses (List[str]): A list of Bitcoin addresses.
        filename (str): The name of the output CSV file.
    """
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Index", "Address"])  # Add header
            for index, address in enumerate(addresses):
                writer.writerow([index, address])
        print(f"Addresses successfully written to {filename}")
    except Exception as e:
        raise ValueError(f"Error writing to CSV file: {str(e)}")

# Main function to execute the program
def main():
    # User inputs
    parent_xpriv = input("Enter the parent extended private key (xpriv): ").strip()
    derivation_path = "m/44'/0'/0'"  # Fixed derivation path
    num_addresses = int(input("Enter the number of addresses to derive: ").strip())
    output_filename = input("Enter the name of the output CSV file: ").strip()
    
    try:
        # Derive addresses
        addresses = derive_addresses_from_xpriv(parent_xpriv, derivation_path, num_addresses)
        
        # Write to CSV
        write_addresses_to_csv(addresses, output_filename)
        
    except ValueError as e:
        print(f"Error: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
- Ensure the `bip32utils` and `bitcoin` libraries are installed in your environment. Use `pip install bip32utils` and `pip install bitcoin`.
- The parent xpriv must be valid, and the derivation path must conform to BIP44.
- This program includes error handling for invalid inputs and issues during derivation or CSV writing.
