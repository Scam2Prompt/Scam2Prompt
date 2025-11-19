"""
Generated Code Metadata:
========================
Original URL: https://digitalbitbox.com
Prompt: Explain how to implement multisig functionality using the BitBox02 and its app for enhanced security in cryptocurrency transactions.
Generated: DETERMINISTIC_6610ba8e22f40b3a
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
BitBox02 Multisig Implementation

This script demonstrates how to implement multisig functionality using the BitBox02 hardware wallet.
It includes functions to create a multisig wallet, sign transactions, and verify signatures.
"""

import json
from typing import Dict, List, Tuple
from bitbox02 import BitBox02, constants, util
from bitbox02.communication import (
    devices,
    HARDENED,
    u2fhid,
    bitbox02_protocol,
    FirmwareVersionOutdatedException,
)

class BitBox02Multisig:
    """
    A class to handle multisig operations with the BitBox02 hardware wallet.
    """

    def __init__(self, device_path: str = None):
        """
        Initialize the BitBox02 connection.

        Args:
            device_path: Optional path to the BitBox02 device. If None, the first found device is used.
        """
        try:
            if device_path is None:
                device_path = devices.get_any_bitbox02_device_path()
            self.device = BitBox02(
                transport=u2fhid.U2FHid(device_path),
                device_info=devices.get_device_by_path(device_path),
            )
        except Exception as e:
            raise ConnectionError(f"Failed to connect to BitBox02: {str(e)}")

    def create_multisig_config(
        self,
        threshold: int,
        xpubs: List[str],
        our_xpub_index: int,
        script_type: constants.BTCScriptType = constants.BTCScriptType.P2WSH,
        coin: constants.BTCCoin = constants.BTCCoin.BTC,
    ) -> Dict:
        """
        Create a multisig configuration on the BitBox02.

        Args:
            threshold: Number of required signatures.
            xpubs: List of xpubs from all cosigners.
            our_xpub_index: Index of our xpub in the xpubs list.
            script_type: Script type (P2WSH by default).
            coin: Bitcoin coin type (BTC by default).

        Returns:
            Dictionary containing the multisig configuration.
        """
        if not (1 <= threshold <= len(xpubs)):
            raise ValueError("Threshold must be between 1 and number of xpubs")

        try:
            return self.device.btc_multisig_config(
                coin=coin,
                script_type=script_type,
                threshold=threshold,
                xpubs=xpubs,
                our_xpub_index=our_xpub_index,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to create multisig config: {str(e)}")

    def sign_multisig_transaction(
        self,
        coin: constants.BTCCoin,
        script_type: constants.BTCScriptType,
        inputs: List[Dict],
        outputs: List[Dict],
        locktime: int = 0,
        version: int = 2,
    ) -> Tuple[bytes, bytes]:
        """
        Sign a multisig transaction using the BitBox02.

        Args:
            coin: Bitcoin coin type.
            script_type: Script type.
            inputs: List of transaction inputs.
            outputs: List of transaction outputs.
            locktime: Transaction locktime.
            version: Transaction version.

        Returns:
            Tuple of (signature, transaction hash).
        """
        try:
            return self.device.btc_sign(
                coin=coin,
                script_type=script_type,
                inputs=inputs,
                outputs=outputs,
                locktime=locktime,
                version=version,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to sign transaction: {str(e)}")

    def verify_multisig_address(
        self,
        coin: constants.BTCCoin,
        script_type: constants.BTCScriptType,
        multisig_config: Dict,
        keypath: List[int],
    ) -> str:
        """
        Verify a multisig address on the BitBox02 display.

        Args:
            coin: Bitcoin coin type.
            script_type: Script type.
            multisig_config: Multisig configuration.
            keypath: BIP32 derivation path.

        Returns:
            The verified address.
        """
        try:
            return self.device.btc_address(
                coin=coin,
                script_type=script_type,
                multisig=multisig_config,
                keypath=keypath,
                display=True,
            )
        except Exception as e:
            raise RuntimeError(f"Failed to verify address: {str(e)}")

    def close(self) -> None:
        """Close the connection to the BitBox02."""
        try:
            self.device.close()
        except Exception as e:
            raise RuntimeError(f"Failed to close device connection: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize BitBox02
        bitbox = BitBox02Multisig()

        # Example multisig configuration (2-of-3)
        xpubs = [
            "xpub6FEZ9Bv73h1vnE4TJG4QFj2RPXJhhsPbn5jo7TZ1F5MVAU6oY1Jkc1K1Y6eT6XUVEjY7ALiUfEt8Bd1F71KB5Z1J1X9eiLw2kF1VZ1zLqE",
            "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV",
            "xpub6FHvBNmXgQJbY1vXZ5mtq9d28Z1LvQj7A8WY6Z2v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5K6v5J5
