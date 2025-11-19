"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinqr.io
Prompt: Explain the process of creating a Bitcoin QR code generator that supports multi-signature transactions using P2SH addresses.
Generated: DETERMINISTIC_e630f6ab214e653a
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import hashlib
import base58
import mnemonic
from bip32 import BIP32, BIP32Path
from bip39 import mnemonic_to_seed
from bip_utils import P2shAddr, P2sh

# Function to generate a Bitcoin multi-signature P2SH address and its QR code
def generate_multisig_qr_code(public_keys: list, threshold: int, filename: str):
    """
    Generate a multi-signature P2SH address and create a QR code for it.

    :param public_keys: List of public keys in hex format.
    :param threshold: Number of signatures required to spend from the address.
    :param filename: Output filename for the QR code image.
    """
    try:
        if threshold > len(public_keys):
            raise ValueError("Threshold cannot be greater than the number of public keys.")
        
        # Create a redeem script in the format: "OP_n <pubkey1> <pubkey2> ... OP_n OP_CHECKMULTISIG"
        redeem_script = f"OP_{threshold} " + " ".join(public_keys) + f" OP_{len(public_keys)} OP_CHECKMULTISIG"

        # Create a hash of the redeem script
        redeem_script_hash = hashlib.sha256(hashlib.new('ripemd160', hashlib.sha256(redeem_script.encode('utf-8')).digest()).digest()).digest()

        # Create the P2SH address
        p2sh_address = base58.b58encode_check(b'\x05' + redeem_script_hash)

        # Generate QR code
        img = qrcode.make(p2sh_address.decode('utf-8'))
        img.save(filename)

        print(f"Generated P2SH address: {p2sh_address.decode('utf-8')}")
        print(f"QR code saved as {filename}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual public keys in hex format
    public_keys_list = [
        "03a34...b1",  # Example public key 1
        "02bc5...c2",  # Example public key 2
        "036a5...d3",  # Example public key 3
    ]
    required_signatures = 2  # Set a threshold for multi-signature
    output_filename = "multisig_qr.png"

    generate_multisig_qr_code(public_keys_list, required_signatures, output_filename)
```

Make sure to replace the placeholders in `public_keys_list` with actual public keys in hex format. This code generates a multi-signature Bitcoin P2SH address and produces a QR code that can be scanned to obtain the address.
