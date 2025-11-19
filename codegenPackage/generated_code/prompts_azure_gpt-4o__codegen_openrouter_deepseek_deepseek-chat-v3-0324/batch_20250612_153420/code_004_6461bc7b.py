"""
Generated Code Metadata:
========================
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a script to interact with a Ledger hardware wallet for adding an additional security layer to a dapp, similar to the functionality mentioned on the webpage.
Generated: DETERMINISTIC_6461bc7bcb49984a
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Optional, Tuple
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LedgerWallet:
    """
    A class to interact with a Ledger hardware wallet for secure transaction signing.
    """
    
    def __init__(self, derivation_path: str = "44'/60'/0'/0/0"):
        """
        Initialize the Ledger wallet connection.
        
        Args:
            derivation_path: The BIP44 derivation path for the Ethereum account.
        """
        self.derivation_path = derivation_path
        self.dongle = None
        
    def connect(self) -> bool:
        """
        Establish connection with the Ledger device.
        
        Returns:
            bool: True if connection is successful, False otherwise.
        """
        try:
            self.dongle = getDongle(True)
            logger.info("Successfully connected to Ledger device")
            return True
        except CommException as e:
            logger.error(f"Failed to connect to Ledger device: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error connecting to Ledger: {str(e)}")
            return False
    
    def disconnect(self) -> None:
        """Close the connection with the Ledger device."""
        if self.dongle:
            try:
                self.dongle.close()
                logger.info("Disconnected from Ledger device")
            except Exception as e:
                logger.error(f"Error disconnecting from Ledger: {str(e)}")
    
    def get_public_key(self) -> Optional[str]:
        """
        Retrieve the public key from the Ledger device.
        
        Returns:
            Optional[str]: The public key in hex format, or None if failed.
        """
        if not self.dongle:
            logger.error("Not connected to Ledger device")
            return None
            
        try:
            # APDU command to get public key
            apdu = self._get_public_key_apdu()
            response = self.dongle.exchange(apdu)
            
            # Parse response (first byte is response length)
            offset = 1 + response[0]
            public_key = response[offset + 1: offset + 1 + response[offset]]
            return public_key.hex()
        except CommException as e:
            logger.error(f"Failed to get public key: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error getting public key: {str(e)}")
            return None
    
    def sign_transaction(self, transaction_hash: bytes) -> Optional[Tuple[int, bytes, bytes]]:
        """
        Sign a transaction hash with the Ledger device.
        
        Args:
            transaction_hash: The 32-byte transaction hash to sign.
            
        Returns:
            Optional[Tuple[int, bytes, bytes]]: A tuple containing (v, r, s) signature components,
            or None if signing failed.
        """
        if not self.dongle:
            logger.error("Not connected to Ledger device")
            return None
            
        if len(transaction_hash) != 32:
            logger.error("Transaction hash must be 32 bytes")
            return None
            
        try:
            # APDU command to sign transaction
            apdu = self._sign_transaction_apdu(transaction_hash)
            response = self.dongle.exchange(apdu)
            
            # Parse signature (format: [v][r][s])
            if len(response) < 65:
                logger.error("Invalid signature response from Ledger")
                return None
                
            v = response[0]
            r = response[1:33]
            s = response[33:65]
            return (v, r, s)
        except CommException as e:
            logger.error(f"Failed to sign transaction: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error signing transaction: {str(e)}")
            return None
    
    def _get_public_key_apdu(self) -> bytes:
        """Generate APDU command to get public key."""
        # Convert derivation path to bytes
        path_bytes = self._bip44_path_to_bytes(self.derivation_path)
        
        # APDU format: [CLA][INS][P1][P2][LC][DATA]
        return bytes.fromhex("e0") + bytes.fromhex("02") + bytes.fromhex("00") + \
               bytes.fromhex("00") + bytes([len(path_bytes)]) + path_bytes
    
    def _sign_transaction_apdu(self, transaction_hash: bytes) -> bytes:
        """Generate APDU command to sign transaction."""
        # Convert derivation path to bytes
        path_bytes = self._bip44_path_to_bytes(self.derivation_path)
        
        # Prepare data: derivation path + transaction hash
        data = path_bytes + transaction_hash
        
        # APDU format: [CLA][INS][P1][P2][LC][DATA]
        return bytes.fromhex("e0") + bytes.fromhex("04") + bytes.fromhex("00") + \
               bytes.fromhex("00") + bytes([len(data)]) + data
    
    @staticmethod
    def _bip44_path_to_bytes(path: str) -> bytes:
        """
        Convert BIP44 derivation path to bytes for APDU command.
        
        Args:
            path: The BIP44 derivation path (e.g., "44'/60'/0'/0/0")
            
        Returns:
            bytes: The path converted to bytes format.
        """
        elements = path.split('/')
        if len(elements) != 5:
            raise ValueError("Invalid BIP44 path format")
            
        result = bytes([len(elements)])
        for element in elements:
            if element.endswith("'"):
                num = int(element[:-1]) | 0x80000000
            else:
                num = int(element)
            result += num.to_bytes(4, byteorder='big')
        return result

# Example usage
if __name__ == "__main__":
    wallet = LedgerWallet()
    if wallet.connect():
        try:
            public_key = wallet.get_public_key()
            if public_key:
                logger.info(f"Public Key: {public_key}")
                
                # Example transaction hash (in real usage, this would come from your dapp)
                tx_hash = bytes.fromhex("2a" * 32)
                signature = wallet.sign_transaction(tx_hash)
                if signature:
                    v, r, s = signature
                    logger.info(f"Signature - v: {v}, r: {r.hex()}, s: {s.hex()}")
        finally:
            wallet.disconnect()
```
