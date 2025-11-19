"""
Generated Code Metadata:
========================
Original URL: https://bafybeiasw5dmpfqqr7panrkqsibus7vxltxmiroh4lh37diiwwftj6sz3e.ipfs.dweb.link
Prompt: Write a script to explore and scan the Bittensor network for active nodes and their staking activity, as described in the documentation.
Generated: DETERMINISTIC_c1d67f26d0fa3eb3
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import time
from typing import Dict, List, Optional

import bittensor as bt
from bittensor import subtensor


class BittensorNetworkScanner:
    """
    A class to scan and explore the Bittensor network for active nodes and their staking activity.
    """

    def __init__(self, network: str = "finney"):
        """
        Initialize the scanner with the specified Bittensor network.

        Args:
            network (str): The Bittensor network to connect to (default: "finney")
        """
        self.network = network
        self.subtensor = subtensor(network=network)
        self.metagraph = None

    def refresh_metagraph(self) -> None:
        """Refresh the metagraph data from the network."""
        try:
            self.metagraph = bt.metagraph(network=self.network)
            bt.logging.success("Successfully refreshed metagraph data")
        except Exception as e:
            bt.logging.error(f"Failed to refresh metagraph: {str(e)}")
            raise

    def get_active_nodes(self) -> List[Dict]:
        """
        Get a list of active nodes in the network.

        Returns:
            List[Dict]: List of active nodes with their details
        """
        if not self.metagraph:
            self.refresh_metagraph()

        active_nodes = []
        for uid in range(self.metagraph.n.item()):
            if self.metagraph.validator_permit[uid] or self.metagraph.total_stake[uid] > 0:
                node_info = {
                    "uid": uid,
                    "hotkey": self.metagraph.hotkeys[uid],
                    "coldkey": self.metagraph.coldkeys[uid],
                    "stake": float(self.metagraph.total_stake[uid]),
                    "validator_permit": bool(self.metagraph.validator_permit[uid]),
                    "incentive": float(self.metagraph.incentive[uid]),
                    "dividends": float(self.metagraph.dividends[uid]),
                    "last_update": int(self.metagraph.last_update[uid]),
                }
                active_nodes.append(node_info)

        return active_nodes

    def get_node_staking_history(self, hotkey: str, max_blocks: int = 100) -> Optional[List[Dict]]:
        """
        Get staking history for a specific node.

        Args:
            hotkey (str): The hotkey of the node to query
            max_blocks (int): Maximum number of blocks to look back (default: 100)

        Returns:
            Optional[List[Dict]]: List of staking events or None if not found
        """
        try:
            staking_events = self.subtensor.get_staking_history(hotkey, max_blocks)
            if staking_events:
                return [
                    {
                        "block": event["block"],
                        "amount": float(event["amount"]),
                        "from_hotkey": event["from_hotkey"],
                        "to_hotkey": event["to_hotkey"],
                        "timestamp": event["timestamp"],
                    }
                    for event in staking_events
                ]
            return None
        except Exception as e:
            bt.logging.error(f"Failed to get staking history for {hotkey}: {str(e)}")
            return None

    def scan_network(self, output_file: Optional[str] = None) -> Dict:
        """
        Perform a full network scan and return results.

        Args:
            output_file (Optional[str]): Path to save JSON output (default: None)

        Returns:
            Dict: Network scan results
        """
        scan_time = int(time.time())
        self.refresh_metagraph()

        results = {
            "network": self.network,
            "block": self.metagraph.block.item(),
            "scan_time": scan_time,
            "total_nodes": self.metagraph.n.item(),
            "active_nodes": [],
        }

        active_nodes = self.get_active_nodes()
        results["active_nodes_count"] = len(active_nodes)
        results["total_stake"] = sum(node["stake"] for node in active_nodes)

        for node in active_nodes:
            staking_history = self.get_node_staking_history(node["hotkey"])
            if staking_history:
                node["staking_history"] = staking_history
            results["active_nodes"].append(node)

        if output_file:
            try:
                with open(output_file, "w") as f:
                    json.dump(results, f, indent=2)
                bt.logging.success(f"Results saved to {output_file}")
            except Exception as e:
                bt.logging.error(f"Failed to save results: {str(e)}")

        return results


def main():
    parser = argparse.ArgumentParser(description="Bittensor Network Scanner")
    parser.add_argument(
        "--network",
        type=str,
        default="finney",
        help="Bittensor network to scan (default: finney)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save results (JSON format)",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Refresh data before scanning",
    )
    args = parser.parse_args()

    bt.logging.set_debug(True)
    scanner = BittensorNetworkScanner(network=args.network)

    if args.refresh:
        scanner.refresh_metagraph()

    results = scanner.scan_network(output_file=args.output)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
```
