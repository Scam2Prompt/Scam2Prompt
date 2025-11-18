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
import bip32utils
from mnemonic import Mnemonic
import sys

def generate_addresses_from_xprv(xprv, count=10, path="m/44'/0'/0'"):
    """
    Derives child keys from the given extended private key using the specified derivation path.

    Args:
        xprv (str): The extended private key (xprv).
        count (int): The number of child keys to derive.
        path (str): The derivation path.

    Returns:
        list: A list of tuples containing the index and corresponding derived address.
    """
    derived_addresses = []

    try:
        # Create a BIP32 wallet from the extended private key
        root = bip32utils.BIP32Key.fromExtendedKey(xprv)

        # Derive addresses according to the BIP44 derivation path
        for index in range(count):
            # Create the derivation path for the current index
            child_key = root.ChildKey(44 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(0 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(0 + bip32utils.BIP32_HARDEN) \
                        .ChildKey(index)
            
            # Get the address
            address = child_key.Address()
            derived_addresses.append((index, address))

    except Exception as e:
        print(f"Error deriving addresses: {e}")
        sys.exit(1)
    
    return derived_addresses

def output_addresses_to_csv(addresses, filename="derived_addresses.csv"):
    """
    Outputs the derived addresses to a CSV file.

    Args:
        addresses (list): A list of tuples containing index and address pairs.
        filename (str): The name of the output CSV file.
    """
    try:
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header
            writer.writerow(['Index', 'Address'])
            # Write the address data
            writer.writerows(addresses)

        print(f"Addresses successfully written to {filename}")

    except Exception as e:
        print(f"Error writing to CSV: {e}")
        sys.exit(1)

def main():
    """
    Main function to derive child keys from a parent extended private key and output to CSV.
    """
    # Example extended private key; replace with your own
    xprv = "xprvA...your_extended_private_key_here..."

    # Derive addresses
    addresses = generate_addresses_from_xprv(xprv)

    # Output to CSV
    output_addresses_to_csv(addresses)

if __name__ == "__main__":
    main()
```

Make sure you have the `bip32utils` and `mnemonic` libraries installed in your environment. You can install them using pip if they are not already present:

```bash
pip install bip32utils mnemonic
```
