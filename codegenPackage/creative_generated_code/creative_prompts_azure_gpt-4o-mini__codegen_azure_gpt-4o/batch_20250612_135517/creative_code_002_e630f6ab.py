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
from bitcoinaddress import Wallet  # Install with `pip install bitcoinaddress`
import hashlib
import base58

def generate_multisig_address(public_keys, required_signatures):
    """
    Generates a P2SH (Pay-to-Script-Hash) multisignature Bitcoin address.

    :param public_keys: List of public keys involved in the multisig wallet.
    :param required_signatures: Number of required signatures to unlock funds.
    :return: A P2SH Bitcoin address.
    """
    try:
        # Construct the redeem script
        # OP_M <pubkey1> ... <pubkeyN> OP_N OP_CHECKMULTISIG
        redeem_script = bytearray()
        redeem_script.append(0x50 + required_signatures)  # OP_M
        for pubkey in public_keys:
            pubkey_bytes = bytes.fromhex(pubkey)
            redeem_script.append(len(pubkey_bytes))
            redeem_script.extend(pubkey_bytes)
        redeem_script.append(0x50 + len(public_keys))  # OP_N
        redeem_script.append(0xAE)  # OP_CHECKMULTISIG

        # Hash the redeem script (SHA256 then RIPEMD-160)
        sha256_hash = hashlib.sha256(redeem_script).digest()
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

        # Create payload for P2SH address (0x05 prefix for Bitcoin mainnet)
        payload = b'\x05' + ripemd160_hash

        # Add checksum (first 4 bytes of double-SHA256 of payload)
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        address_bytes = payload + checksum

        # Encode in Base58
        p2sh_address = base58.b58encode(address_bytes).decode('utf-8')
        return p2sh_address
    except Exception as e:
        raise ValueError(f"Error generating multisig address: {e}")


def generate_bitcoin_qr_code(address, amount):
    """
    Generates a QR code for a Bitcoin transaction.

    :param address: Bitcoin address to send funds to.
    :param amount: Amount of Bitcoin to send.
    :return: Bitcoin QR code image object.
    """
    try:
        # Build the Bitcoin URI
        bitcoin_uri = f"bitcoin:{address}?amount={amount}"

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(bitcoin_uri)
        qr.make(fit=True)

        # Render the QR code image
        qr_image = qr.make_image(fill="black", back_color="white")
        return qr_image
    except Exception as e:
        raise ValueError(f"Error generating QR code: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Example public keys (compressed format, 33 bytes each)
        public_keys = [
            "022c5b6e0c8e372eae5f4d8a9c19dca9f3b1e9d3ef8b3c3850be9f7d231f1f3fc9",
            "03a34f4f5f2e6b7f6a4e6f7d9c9b7f6f8a5b7c4e5d3f7b8c9a3f7f6f9a2e5b7f6f"
        ]
        required_signatures = 2  # Number of required signatures

        # Generate multisig address
        multisig_address = generate_multisig_address(public_keys, required_signatures)
        print(f"Generated P2SH Multisig Address: {multisig_address}")

        # Generate Bitcoin QR code
        amount_to_send = 0.01  # Amount in BTC
        qr_image = generate_bitcoin_qr_code(multisig_address, amount_to_send)
        qr_image.show()  # Display the QR code
    except Exception as e:
        print(f"Error: {e}")
```

### Notes:
1. Install dependencies with:
   - `pip install qrcode`
   - `pip install bitcoinaddress`
   - `pip install base58`
2. Replace example public keys with actual compressed public keys.
3. Ensure you use the correct Bitcoin network prefix (`0x05` is for mainnet P2SH). For testnet, use `0xC4`.
