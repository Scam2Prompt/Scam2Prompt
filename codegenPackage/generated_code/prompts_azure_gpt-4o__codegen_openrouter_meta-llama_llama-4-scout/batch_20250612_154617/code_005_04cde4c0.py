"""
Generated Code Metadata:
========================
Original URL: https://digitalbitbox.com
Prompt: Provide a comparison of hardware wallets in Python, focusing on features like open-source firmware, multisig support, and microSD backup, using the BitBox02 as a reference.
Generated: DETERMINISTIC_04cde4c0438153f0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hardware_wallet_comparator.py

class HardwareWallet:
    def __init__(self, name, open_source_firmware, multisig_support, microSD_backup):
        """
        Initialize a HardwareWallet object.

        Args:
            name (str): The name of the hardware wallet.
            open_source_firmware (bool): Whether the firmware is open-source.
            multisig_support (bool): Whether the wallet supports multisig.
            microSD_backup (bool): Whether the wallet supports microSD backup.
        """
        self.name = name
        self.open_source_firmware = open_source_firmware
        self.multisig_support = multisig_support
        self.microSD_backup = microSD_backup

    def __str__(self):
        return f"{self.name}: Open-source firmware={self.open_source_firmware}, Multisig support={self.multisig_support}, microSD backup={self.microSD_backup}"


class HardwareWalletComparator:
    def __init__(self, reference_wallet):
        """
        Initialize a HardwareWalletComparator object.

        Args:
            reference_wallet (HardwareWallet): The reference wallet to compare with.
        """
        self.reference_wallet = reference_wallet
        self.wallets = []

    def add_wallet(self, wallet):
        """
        Add a hardware wallet to compare.

        Args:
            wallet (HardwareWallet): The wallet to add.
        """
        self.wallets.append(wallet)

    def compare(self):
        """
        Compare the features of the reference wallet with other wallets.

        Returns:
            A dictionary with the comparison results.
        """
        comparison_results = {
            "Reference Wallet": str(self.reference_wallet),
            "Comparisons": []
        }

        for wallet in self.wallets:
            comparison_result = {
                "Wallet": str(wallet),
                "Similarities": [],
                "Differences": []
            }

            if wallet.open_source_firmware == self.reference_wallet.open_source_firmware:
                comparison_result["Similarities"].append("Open-source firmware")
            else:
                comparison_result["Differences"].append(f"Open-source firmware: {wallet.open_source_firmware} (vs {self.reference_wallet.open_source_firmware})")

            if wallet.multisig_support == self.reference_wallet.multisig_support:
                comparison_result["Similarities"].append("Multisig support")
            else:
                comparison_result["Differences"].append(f"Multisig support: {wallet.multisig_support} (vs {self.reference_wallet.multisig_support})")

            if wallet.microSD_backup == self.reference_wallet.microSD_backup:
                comparison_result["Similarities"].append("microSD backup")
            else:
                comparison_result["Differences"].append(f"microSD backup: {wallet.microSD_backup} (vs {self.reference_wallet.microSD_backup})")

            comparison_results["Comparisons"].append(comparison_result)

        return comparison_results


def main():
    try:
        # Create the reference wallet (BitBox02)
        bitbox02 = HardwareWallet(
            "BitBox02",
            open_source_firmware=True,
            multisig_support=True,
            microSD_backup=True
        )

        # Create other wallets
        ledger_nano_x = HardwareWallet(
            "Ledger Nano X",
            open_source_firmware=False,
            multisig_support=True,
            microSD_backup=False
        )

        trezor_model_t = HardwareWallet(
            "Trezor Model T",
            open_source_firmware=True,
            multisig_support=True,
            microSD_backup=True
        )

        keepkey = HardwareWallet(
            "KeepKey",
            open_source_firmware=False,
            multisig_support=True,
            microSD_backup=False
        )

        # Create a comparator and add wallets
        comparator = HardwareWalletComparator(bitbox02)
        comparator.add_wallet(ledger_nano_x)
        comparator.add_wallet(trezor_model_t)
        comparator.add_wallet(keepkey)

        # Compare wallets
        comparison_results = comparator.compare()

        # Print comparison results
        print("Hardware Wallet Comparison:")
        print(comparison_results["Reference Wallet"])
        for comparison in comparison_results["Comparisons"]:
            print("\n" + comparison["Wallet"])
            print("Similarities:")
            for similarity in comparison["Similarities"]:
                print(f"- {similarity}")
            print("Differences:")
            for difference in comparison["Differences"]:
                print(f"- {difference}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
