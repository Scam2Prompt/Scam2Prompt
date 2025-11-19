"""
Generated Code Metadata:
========================
Original URL: https://arweave.ar
Prompt: Can you provide an example of how to implement the ans104UnbundleFilter in a project using Arweave's supported manifest versions?
Generated: DETERMINISTIC_6d1a54ab7b90aff6
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ANS104UnbundleFilter:
    """
    A class to handle ANS-104 unbundling and filtering of transactions based on supported manifest versions.
    """

    SUPPORTED_MANIFEST_VERSIONS = ["0.1.0", "0.2.0"]

    def __init__(self, arweave_client):
        """
        Initialize the filter with an Arweave client instance.

        Args:
            arweave_client: An instance of Arweave client to interact with the network.
        """
        self.arweave_client = arweave_client

    def is_supported_manifest_version(self, manifest_version: str) -> bool:
        """
        Check if the manifest version is supported.

        Args:
            manifest_version: The manifest version to check.

        Returns:
            bool: True if supported, False otherwise.
        """
        return manifest_version in self.SUPPORTED_MANIFEST_VERSIONS

    def get_manifest(self, tx_id: str) -> Optional[Dict]:
        """
        Retrieve and parse the manifest for a given transaction ID.

        Args:
            tx_id: The transaction ID to fetch manifest for.

        Returns:
            Optional[Dict]: The parsed manifest if found and valid, None otherwise.
        """
        try:
            tx_data = self.arweave_client.transactions.get_data(tx_id)
            manifest = json.loads(tx_data)
            return manifest if self._validate_manifest(manifest) else None
        except Exception as e:
            print(f"Error fetching/parsing manifest for tx {tx_id}: {str(e)}")
            return None

    def _validate_manifest(self, manifest: Dict) -> bool:
        """
        Validate the manifest structure and version.

        Args:
            manifest: The manifest dictionary to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            version = manifest.get("manifest")
            return version in self.SUPPORTED_MANIFEST_VERSIONS
        except Exception:
            return False

    def filter_bundled_transactions(self, bundle_tx_id: str) -> List[Dict]:
        """
        Filter bundled transactions by supported manifest versions.

        Args:
            bundle_tx_id: The bundle transaction ID to process.

        Returns:
            List[Dict]: List of valid transactions with supported manifest versions.
        """
        valid_transactions = []
        try:
            bundle_data = self.arweave_client.transactions.get_data(bundle_tx_id)
            bundle_items = json.loads(bundle_data).get("items", [])

            for item in bundle_items:
                tx_id = item.get("id")
                manifest = self.get_manifest(tx_id)
                if manifest:
                    valid_transactions.append({
                        "tx_id": tx_id,
                        "manifest": manifest
                    })

        except Exception as e:
            print(f"Error processing bundle {bundle_tx_id}: {str(e)}")

        return valid_transactions

    def process_bundle(self, bundle_tx_id: str) -> Dict:
        """
        Process a bundle and return filtered results.

        Args:
            bundle_tx_id: The bundle transaction ID to process.

        Returns:
            Dict: Result containing filtered transactions and metadata.
        """
        filtered_txs = self.filter_bundled_transactions(bundle_tx_id)
        return {
            "bundle_tx_id": bundle_tx_id,
            "total_transactions": len(filtered_txs),
            "transactions": filtered_txs,
            "supported_versions": self.SUPPORTED_MANIFEST_VERSIONS
        }
```
