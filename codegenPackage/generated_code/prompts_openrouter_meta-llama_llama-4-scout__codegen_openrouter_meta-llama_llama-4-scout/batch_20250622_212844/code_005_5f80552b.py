"""
Generated Code Metadata:
========================
Original URL: https://m.caimaosheng.com
Prompt: Compare the features of TPWallet with other popular digital wallets in terms of security, supported cryptocurrencies, and user experience.
Generated: DETERMINISTIC_5f80552b24d23a3a
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_wallets_comparator.py

class DigitalWallet:
    def __init__(self, name, supported_cryptocurrencies, security_features, user_experience_rating):
        """
        Initialize a digital wallet.

        Args:
        - name (str): The name of the digital wallet.
        - supported_cryptocurrencies (list): A list of supported cryptocurrencies.
        - security_features (list): A list of security features.
        - user_experience_rating (int): A rating of the user experience (1-10).
        """
        self.name = name
        self.supported_cryptocurrencies = supported_cryptocurrencies
        self.security_features = security_features
        self.user_experience_rating = user_experience_rating

    def __str__(self):
        return f"{self.name} - Supported Cryptocurrencies: {', '.join(self.supported_cryptocurrencies)}"


class DigitalWalletComparator:
    def __init__(self):
        self.digital_wallets = []

    def add_digital_wallet(self, digital_wallet):
        """
        Add a digital wallet to the comparator.

        Args:
        - digital_wallet (DigitalWallet): The digital wallet to add.
        """
        self.digital_wallets.append(digital_wallet)

    def compare_security_features(self):
        """
        Compare the security features of the digital wallets.

        Returns:
        - A dictionary with the digital wallet names as keys and their security features as values.
        """
        security_features_comparison = {}
        for digital_wallet in self.digital_wallets:
            security_features_comparison[digital_wallet.name] = digital_wallet.security_features
        return security_features_comparison

    def compare_supported_cryptocurrencies(self):
        """
        Compare the supported cryptocurrencies of the digital wallets.

        Returns:
        - A dictionary with the digital wallet names as keys and their supported cryptocurrencies as values.
        """
        supported_cryptocurrencies_comparison = {}
        for digital_wallet in self.digital_wallets:
            supported_cryptocurrencies_comparison[digital_wallet.name] = digital_wallet.supported_cryptocurrencies
        return supported_cryptocurrencies_comparison

    def compare_user_experience(self):
        """
        Compare the user experience ratings of the digital wallets.

        Returns:
        - A dictionary with the digital wallet names as keys and their user experience ratings as values.
        """
        user_experience_comparison = {}
        for digital_wallet in self.digital_wallets:
            user_experience_comparison[digital_wallet.name] = digital_wallet.user_experience_rating
        return user_experience_comparison


def main():
    try:
        comparator = DigitalWalletComparator()

        # Create digital wallets
        tp_wallet = DigitalWallet(
            "TPWallet",
            ["Bitcoin", "Ethereum", "Litecoin"],
            ["2FA", "Encryption", "Multi-Sig"],
            8
        )

        coinbase_wallet = DigitalWallet(
            "Coinbase Wallet",
            ["Bitcoin", "Ethereum", "Litecoin", "Bitcoin Cash"],
            ["2FA", "Encryption", "Multi-Sig", "Insurance"],
            9
        )

        metamask_wallet = DigitalWallet(
            "MetaMask",
            ["Ethereum", "ERC-20 tokens"],
            ["Encryption", "Multi-Sig"],
            7
        )

        # Add digital wallets to the comparator
        comparator.add_digital_wallet(tp_wallet)
        comparator.add_digital_wallet(coinbase_wallet)
        comparator.add_digital_wallet(metamask_wallet)

        # Compare digital wallets
        security_features_comparison = comparator.compare_security_features()
        supported_cryptocurrencies_comparison = comparator.compare_supported_cryptocurrencies()
        user_experience_comparison = comparator.compare_user_experience()

        # Print comparisons
        print("Security Features Comparison:")
        for wallet, features in security_features_comparison.items():
            print(f"{wallet}: {', '.join(features)}")

        print("\nSupported Cryptocurrencies Comparison:")
        for wallet, cryptocurrencies in supported_cryptocurrencies_comparison.items():
            print(f"{wallet}: {', '.join(cryptocurrencies)}")

        print("\nUser Experience Comparison:")
        for wallet, rating in user_experience_comparison.items():
            print(f"{wallet}: {rating}/10")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
