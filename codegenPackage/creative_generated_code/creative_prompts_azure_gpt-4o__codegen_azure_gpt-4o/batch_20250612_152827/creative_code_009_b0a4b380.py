"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinite-v2.vercel.app
Prompt: Develop a program to calculate and compare the risk factor of vaults managed by Infinite Trading across multiple networks.
Generated: DETERMINISTIC_b0a4b3807fe171b2
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Vault:
    """
    Class representing a vault in the Infinite Trading system.
    """
    def __init__(self, name, network, assets_under_management, risk_score):
        """
        Initializes the Vault object.

        :param name: Name of the vault
        :param network: Network the vault operates on
        :param assets_under_management: Total assets managed by the vault
        :param risk_score: Risk score of the vault
        """
        self.name = name
        self.network = network
        self.assets_under_management = assets_under_management
        self.risk_score = risk_score

    def get_risk_factor(self):
        """
        Calculates the risk factor based on risk score and assets under management.

        :return: Risk factor of the vault
        """
        try:
            if self.assets_under_management <= 0:
                raise ValueError("Assets under management must be greater than 0.")

            # Risk factor formula: (Risk Score / Assets Under Management) * 100
            return (self.risk_score / self.assets_under_management) * 100
        except ZeroDivisionError as e:
            logging.error("Division by zero encountered while calculating risk factor.")
            raise e
        except ValueError as e:
            logging.error(f"Invalid value encountered: {e}")
            raise e


class VaultRiskAnalyzer:
    """
    Class for analyzing and comparing risk factors of multiple vaults across networks.
    """
    def __init__(self):
        """
        Initializes the VaultRiskAnalyzer object.
        """
        self.vaults = []

    def add_vault(self, vault):
        """
        Adds a vault to the analyzer.

        :param vault: Vault object to be added
        """
        if not isinstance(vault, Vault):
            logging.error("Provided object is not a Vault instance.")
            raise TypeError("Expected a Vault instance.")
        self.vaults.append(vault)

    def compare_risk_factors(self):
        """
        Compares risk factors across all vaults and prints the results.

        :return: None
        """
        if not self.vaults:
            logging.warning("No vaults available for comparison.")
            return

        logging.info("Comparing risk factors across vaults...")
        try:
            sorted_vaults = sorted(self.vaults, key=lambda v: v.get_risk_factor(), reverse=True)

            print("Vault Risk Factor Comparison:")
            for vault in sorted_vaults:
                print(f"Vault Name: {vault.name}")
                print(f"Network: {vault.network}")
                print(f"Assets Under Management: {vault.assets_under_management}")
                print(f"Risk Score: {vault.risk_score}")
                print(f"Risk Factor: {vault.get_risk_factor():.2f}%")
                print("-" * 40)
        except Exception as e:
            logging.error(f"An error occurred while comparing risk factors: {e}")
            raise e


# Example usage
if __name__ == "__main__":
    try:
        # Creating vault instances
        vault1 = Vault("Vault A", "Ethereum", 1000000, 50)
        vault2 = Vault("Vault B", "Binance Smart Chain", 500000, 80)
        vault3 = Vault("Vault C", "Polygon", 250000, 30)

        # Adding vaults to the risk analyzer
        analyzer = VaultRiskAnalyzer()
        analyzer.add_vault(vault1)
        analyzer.add_vault(vault2)
        analyzer.add_vault(vault3)

        # Comparing risk factors
        analyzer.compare_risk_factors()
    except Exception as e:
        logging.critical(f"Critical error occurred: {e}")
```
