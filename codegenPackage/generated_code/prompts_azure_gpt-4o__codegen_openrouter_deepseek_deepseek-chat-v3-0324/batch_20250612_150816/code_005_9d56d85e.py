"""
Generated Code Metadata:
========================
Original URL: https://fuel-explorer.vercel.app
Prompt: Create a script to interact with the FuelVM environment and deploy a smart contract using the Fuel Labs documentation.
Generated: DETERMINISTIC_9d56d85e5a514a04
Batch ID: 20250612_150816
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
Script to deploy a smart contract to the FuelVM environment using Fuel Labs SDK.
"""

import os
from pathlib import Path
from typing import Optional

from fuels import (
    Account,
    Contract,
    Provider,
    Wallet,
    WalletUnlocked,
    setup_test_client,
)
from fuels.exceptions import ContractIdFormatError, TransactionExecutionError
from fuels.types import ContractId


class FuelContractDeployer:
    """
    A class to handle the deployment of smart contracts to the FuelVM environment.
    """

    def __init__(
        self,
        private_key: Optional[str] = None,
        provider_url: Optional[str] = None,
    ):
        """
        Initialize the FuelContractDeployer.

        Args:
            private_key: Optional private key for the deployer wallet.
                        If not provided, a new wallet will be generated.
            provider_url: Optional URL for the Fuel provider.
                         If not provided, a local test client will be used.
        """
        self.provider = (
            Provider.connect(provider_url) if provider_url else setup_test_client()
        )
        self.wallet = (
            WalletUnlocked.from_private_key(private_key, provider=self.provider)
            if private_key
            else Wallet.generate(provider=self.provider)
        )

    def deploy_contract(
        self, contract_path: str, storage_slots_path: Optional[str] = None
    ) -> ContractId:
        """
        Deploy a smart contract to the FuelVM environment.

        Args:
            contract_path: Path to the compiled contract binary file.
            storage_slots_path: Optional path to the storage slots file.

        Returns:
            The deployed contract ID.

        Raises:
            FileNotFoundError: If contract file or storage slots file not found.
            ContractIdFormatError: If contract ID is invalid.
            TransactionExecutionError: If contract deployment fails.
        """
        if not os.path.exists(contract_path):
            raise FileNotFoundError(f"Contract file not found: {contract_path}")

        if storage_slots_path and not os.path.exists(storage_slots_path):
            raise FileNotFoundError(
                f"Storage slots file not found: {storage_slots_path}"
            )

        try:
            contract = Contract.load_from(
                contract_path,
                storage_slots_path=storage_slots_path,
                wallet=self.wallet,
            )
            contract_id = contract.deploy()

            if not ContractId.is_valid(contract_id):
                raise ContractIdFormatError(f"Invalid contract ID: {contract_id}")

            return contract_id

        except TransactionExecutionError as e:
            raise TransactionExecutionError(
                f"Failed to deploy contract: {e}"
            ) from e

    def get_contract_instance(self, contract_id: ContractId) -> Contract:
        """
        Get a contract instance for an already deployed contract.

        Args:
            contract_id: The ID of the deployed contract.

        Returns:
            A Contract instance.

        Raises:
            ContractIdFormatError: If contract ID is invalid.
        """
        if not ContractId.is_valid(contract_id):
            raise ContractIdFormatError(f"Invalid contract ID: {contract_id}")

        return Contract.from_id(contract_id, wallet=self.wallet)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Deploy a smart contract to the FuelVM environment."
    )
    parser.add_argument(
        "contract_path",
        type=str,
        help="Path to the compiled contract binary file",
    )
    parser.add_argument(
        "--storage-slots",
        type=str,
        help="Path to the storage slots file (optional)",
    )
    parser.add_argument(
        "--private-key",
        type=str,
        help="Private key for the deployer wallet (optional)",
    )
    parser.add_argument(
        "--provider-url",
        type=str,
        help="URL for the Fuel provider (optional)",
    )

    args = parser.parse_args()

    try:
        deployer = FuelContractDeployer(
            private_key=args.private_key, provider_url=args.provider_url
        )
        contract_id = deployer.deploy_contract(
            args.contract_path, args.storage_slots
        )
        print(f"Contract deployed successfully! Contract ID: {contract_id}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except ContractIdFormatError as e:
        print(f"Error: {e}")
        exit(1)
    except TransactionExecutionError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)
```
