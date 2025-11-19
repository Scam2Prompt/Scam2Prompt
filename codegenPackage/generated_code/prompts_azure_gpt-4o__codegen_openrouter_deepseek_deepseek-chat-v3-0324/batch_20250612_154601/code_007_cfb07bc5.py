"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: Write a tutorial on how to use cryptographic methods to secure Bitcoin ownership, aligning with the "digital property" concept discussed by Jupiter Digital Asset.
Generated: DETERMINISTIC_cfb07bc57c92c1f2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import hashlib
import hmac
import os
import base58
import ecdsa
from ecdsa import SigningKey, SECP256k1
from typing import Tuple, Optional

# Constants for Bitcoin address generation
BITCOIN_PUBKEY_HASH_PREFIX = b'\x00'  # Mainnet prefix for P2PKH addresses
BITCOIN_TESTNET_PUBKEY_HASH_PREFIX = b'\x6f'  # Testnet prefix for P2PKH addresses
BITCOIN_PRIVATE_KEY_PREFIX = b'\x80'  # Mainnet prefix for private keys
BITCOIN_TESTNET_PRIVATE_KEY_PREFIX = b'\xef'  # Testnet prefix for private keys

class BitcoinKeyPair:
    """
    A class to generate and manage Bitcoin key pairs and addresses.
    Implements cryptographic methods to secure Bitcoin ownership.
    """
    
    def __init__(self, testnet: bool = False):
        """
        Initialize a new Bitcoin key pair.
        
        Args:
            testnet: Whether to use testnet prefixes (default: False)
        """
        self.testnet = testnet
        self.private_key, self.public_key = self._generate_key_pair()
        self.address = self._generate_address()
    
    def _generate_key_pair(self) -> Tuple[bytes, bytes]:
        """
        Generate a new ECDSA key pair using SECP256k1 curve.
        
        Returns:
            Tuple of (private_key, public_key) in bytes format
        """
        # Generate a new private key
        private_key = SigningKey.generate(curve=SECP256k1)
        
        # Get the corresponding public key
        public_key = private_key.get_verifying_key()
        
        return private_key.to_string(), public_key.to_string()
    
    def _generate_address(self) -> str:
        """
        Generate a Bitcoin address from the public key.
        
        Returns:
            Base58Check encoded Bitcoin address
        """
        # Step 1: SHA-256 hash of the public key
        sha256_hash = hashlib.sha256(self.public_key).digest()
        
        # Step 2: RIPEMD-160 hash of the SHA-256 hash
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
        
        # Step 3: Add network prefix
        if self.testnet:
            network_ripemd160 = BITCOIN_TESTNET_PUBKEY_HASH_PREFIX + ripemd160_hash
        else:
            network_ripemd160 = BITCOIN_PUBKEY_HASH_PREFIX + ripemd160_hash
        
        # Step 4: Double SHA-256 hash for checksum
        checksum = hashlib.sha256(hashlib.sha256(network_ripemd160).digest()).digest()[:4]
        
        # Step 5: Concatenate and encode in Base58
        address_bytes = network_ripemd160 + checksum
        address = base58.b58encode(address_bytes)
        
        return address.decode('utf-8')
    
    def get_wif_private_key(self) -> str:
        """
        Get the Wallet Import Format (WIF) representation of the private key.
        
        Returns:
            Base58Check encoded WIF private key
        """
        # Add network prefix
        if self.testnet:
            extended_key = BITCOIN_TESTNET_PRIVATE_KEY_PREFIX + self.private_key
        else:
            extended_key = BITCOIN_PRIVATE_KEY_PREFIX + self.private_key
        
        # Add compression flag (0x01) if using compressed public keys
        extended_key += b'\x01'
        
        # Double SHA-256 hash for checksum
        checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
        
        # Concatenate and encode in Base58
        wif_bytes = extended_key + checksum
        wif = base58.b58encode(wif_bytes)
        
        return wif.decode('utf-8')
    
    def sign_message(self, message: str) -> str:
        """
        Sign a message with the private key.
        
        Args:
            message: The message to sign
            
        Returns:
            Base64 encoded signature
        """
        # Convert the private key back to SigningKey object
        sk = SigningKey.from_string(self.private_key, curve=SECP256k1)
        
        # Sign the message
        signature = sk.sign(message.encode('utf-8'))
        
        # Return base64 encoded signature
        return base64.b64encode(signature).decode('utf-8')
    
    def verify_message(self, message: str, signature: str) -> bool:
        """
        Verify a message signature with the public key.
        
        Args:
            message: The original message
            signature: The base64 encoded signature
            
        Returns:
            True if signature is valid, False otherwise
        """
        # Convert the public key back to VerifyingKey object
        vk = ecdsa.VerifyingKey.from_string(self.public_key, curve=SECP256k1)
        
        try:
            # Verify the signature
            return vk.verify(base64.b64decode(signature), message.encode('utf-8'))
        except ecdsa.BadSignatureError:
            return False

class BitcoinWallet:
    """
    A secure Bitcoin wallet implementation that uses hierarchical deterministic (HD) keys.
    Implements BIP-32, BIP-39, and BIP-44 standards.
    """
    
    def __init__(self, mnemonic: Optional[str] = None, passphrase: str = "", testnet: bool = False):
        """
        Initialize a new HD Bitcoin wallet.
        
        Args:
            mnemonic: Optional mnemonic phrase (if None, generates new one)
            passphrase: Optional passphrase for additional security
            testnet: Whether to use testnet (default: False)
        """
        self.testnet = testnet
        self.mnemonic = mnemonic if mnemonic else self._generate_mnemonic()
        self.passphrase = passphrase
        self.seed = self._generate_seed()
        self.root_key = self._generate_root_key()
    
    def _generate_mnemonic(self, strength: int = 128) -> str:
        """
        Generate a new BIP-39 mnemonic phrase.
        
        Args:
            strength: Entropy strength in bits (128, 160, 192, 224, or 256)
            
        Returns:
            Mnemonic phrase as string
        """
        if strength not in [128, 160, 192, 224, 256]:
            raise ValueError("Strength should be one of: 128, 160, 192, 224, 256")
        
        # Generate random entropy
        entropy = os.urandom(strength // 8)
        
        # Calculate checksum
        entropy_hash = hashlib.sha256(entropy).digest()
        checksum_bits = bin(entropy_hash[0])[2:].zfill(8)[:strength // 32]
        
        # Combine entropy and checksum
        entropy_bits = ''.join([bin(byte)[2:].zfill(8) for byte in entropy])
        combined_bits = entropy_bits + checksum_bits
        
        # Split into 11-bit chunks
        chunks = [combined_bits[i:i+11] for i in range(0, len(combined_bits), 11)]
        
        # Convert to word indices
        wordlist = self._get_bip39_wordlist()
        indices = [int(chunk, 2) for chunk in chunks]
        
        # Return mnemonic phrase
        return ' '.join([wordlist[index] for index in indices])
    
    def _generate_seed(self) -> bytes:
        """
        Generate a BIP-39 seed from the mnemonic and passphrase.
        
        Returns:
            512-bit seed as bytes
        """
        # Normalize mnemonic and passphrase
        normalized_mnemonic = self.mnemonic.encode('utf-8')
        normalized_passphrase = ("mnemonic" + self.passphrase).encode('utf-8')
        
        # Generate seed using PBKDF2-HMAC-SHA512
        seed = hashlib.pbkdf2_hmac(
            'sha512',
            normalized_mnemonic,
            normalized_passphrase,
            iterations=2048,
            dklen=64
        )
        
        return seed
    
    def _generate_root_key(self) -> bytes:
        """
        Generate a BIP-32 root key from the seed.
        
        Returns:
            Root key as bytes
        """
        # HMAC-SHA512 with "Bitcoin seed" as key
        hmac_result = hmac.new(b"Bitcoin seed", self.seed, hashlib.sha512).digest()
        
        # Split into master private key and chain code
        master_private_key = hmac_result[:32]
        chain_code = hmac_result[32:]
        
        # Return extended private key (xprv)
        return self._serialize_extended_key(master_private_key, chain_code, is_
