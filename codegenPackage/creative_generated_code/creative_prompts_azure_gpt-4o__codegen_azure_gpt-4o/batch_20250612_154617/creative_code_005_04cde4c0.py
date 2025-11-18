"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalbitbox.com
Prompt: Provide a comparison of hardware wallets in Python, focusing on features like open-source firmware, multisig support, and microSD backup, using the BitBox02 as a reference.
Generated: DETERMINISTIC_04cde4c0438153f0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script compares hardware wallets based on specific features: open-source firmware,
multisig support, and microSD backup. The BitBox02 is used as a reference in the comparison.
"""

# Import necessary libraries
import json

# Define a class to represent a hardware wallet
class HardwareWallet:
    """
    Represents a hardware wallet with specific features.
    """
    def __init__(self, name, open_source_firmware, multisig_support, microSD_backup):
        """
        Initialize a hardware wallet instance.

        :param name: The name of the hardware wallet
        :param open_source_firmware: Whether the firmware is open-source (True/False)
        :param multisig_support: Whether the wallet supports multisig (True/False)
        :param microSD_backup: Whether the wallet supports microSD backup (True/False)
        """
        self.name = name
        self.open_source_firmware = open_source_firmware
        self.multisig_support = multisig_support
        self.microSD_backup = microSD_backup

    def to_dict(self):
        """
        Convert the hardware wallet object into a dictionary.

        :return: A dictionary representation of the wallet
        """
        return {
            "name": self.name,
            "open_source_firmware": self.open_source_firmware,
            "multisig_support": self.multisig_support,
            "microSD_backup": self.microSD_backup
        }

# Define a function to compare hardware wallets
def compare_hardware_wallets(wallets, reference_wallet_name):
    """
    Compare hardware wallets against a reference wallet.

    :param wallets: List of HardwareWallet objects to compare
    :param reference_wallet_name: The name of the reference wallet
    :return: Comparison results as a dictionary
    """
    comparison_results = []

    # Find the reference wallet
    reference_wallet = next((w for w in wallets if w.name == reference_wallet_name), None)
    if not reference_wallet:
        raise ValueError(f"Reference wallet '{reference_wallet_name}' not found.")

    # Perform the comparison
    for wallet in wallets:
        comparison_results.append({
            "name": wallet.name,
            "comparison_with_reference": {
                "open_source_firmware_matches": wallet.open_source_firmware == reference_wallet.open_source_firmware,
                "multisig_support_matches": wallet.multisig_support == reference_wallet.multisig_support,
                "microSD_backup_matches": wallet.microSD_backup == reference_wallet.microSD_backup
            }
        })

    return comparison_results

# Main function to demonstrate the comparison
def main():
    """
    Main function to set up wallets and perform a comparison.
    """
    # Define hardware wallets to compare
    wallets = [
        HardwareWallet("BitBox02", True, True, True),  # Reference wallet
        HardwareWallet("Ledger Nano X", False, True, False),
        HardwareWallet("Trezor Model T", True, True, False),
        HardwareWallet("Coldcard Mk4", True, True, True)
    ]

    # Perform the comparison
    try:
        reference_wallet_name = "BitBox02"
        comparison_results = compare_hardware_wallets(wallets, reference_wallet_name)

        # Print the comparison results in JSON format for readability
        print(json.dumps(comparison_results, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
