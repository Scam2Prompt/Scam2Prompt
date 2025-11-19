"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalbitbox.com
Prompt: What are the unique security features of the BitBox02 hardware wallet compared to other wallets like Ledger and Trezor?
Generated: DETERMINISTIC_7625d945faf26b72
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HardwareWallet:
    """
    A base class representing a generic hardware wallet.
    """

    def __init__(self, name):
        self.name = name

    def unique_security_features(self):
        """Returns unique security features. To be implemented by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class BitBox02(HardwareWallet):
    """
    Represents the BitBox02 hardware wallet with unique security features.
    """

    def __init__(self):
        super().__init__("BitBox02")

    def unique_security_features(self):
        """
        Returns a list of unique security features specific to the BitBox02.
        """
        return [
            "Secure Element: Uses a dedicated secure chip for cryptographic operations.",
            "Dual-Channel Communication: Features USB-C and MicroSD for secure data transfer.",
            "Open Source: Software and hardware designs are fully open source, allowing community audits.",
            "User-Driven Recovery: Allows users to create a backup using a MicroSD card.",
            "Minimal Attack Surface: Designed to minimize exposure to potential attacks."
        ]


class Ledger(HardwareWallet):
    """
    Represents the Ledger hardware wallet with unique security features.
    """

    def __init__(self):
        super().__init__("Ledger")

    def unique_security_features(self):
        """
        Returns a list of unique security features specific to Ledger.
        """
        return [
            "Secure Element: Utilizes a secure chip for private key storage.",
            "Multi-Currency Support: Supports a wide range of cryptocurrencies.",
            "Ledger Live: Companion app for managing crypto assets and transactions.",
            "Firmware Verification: Firmware updates are verified and signed for authenticity."
        ]


class Trezor(HardwareWallet):
    """
    Represents the Trezor hardware wallet with unique security features.
    """

    def __init__(self):
        super().__init__("Trezor")

    def unique_security_features(self):
        """
        Returns a list of unique security features specific to Trezor.
        """
        return [
            "Password Manager: Integrated password management functionality.",
            "Recovery Seed: Supports recovery via a 12, 18, or 24-word mnemonic seed.",
            "Web-Based Interface: Easy access to the wallet through a web interface.",
            "Strong Two-Factor Authentication: Enhanced security with optional 2FA."
        ]


def print_unique_features(wallet):
    """
    Prints unique security features of the given wallet.

    :param wallet: An instance of HardwareWallet or its subclasses.
    :raises TypeError: If the provided wallet is not an instance of HardwareWallet.
    """
    if not isinstance(wallet, HardwareWallet):
        raise TypeError("Expected an instance of HardwareWallet or its subclasses.")

    features = wallet.unique_security_features()
    print(f"Unique security features of {wallet.name}:")
    for feature in features:
        print(f"- {feature}")


def main():
    """
    Main function to demonstrate unique security features of different hardware wallets.
    """
    try:
        wallets = [BitBox02(), Ledger(), Trezor()]
        for wallet in wallets:
            print_unique_features(wallet)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
