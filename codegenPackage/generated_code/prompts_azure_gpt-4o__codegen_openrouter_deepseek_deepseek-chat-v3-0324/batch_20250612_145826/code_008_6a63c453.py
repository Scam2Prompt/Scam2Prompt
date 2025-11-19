"""
Generated Code Metadata:
========================
Original URL: https://polymarket.vercel.app
Prompt: Create a CLI tool using the PolyMarket GitHub codebase to manage prediction markets, including creating, updating, and resolving markets.
Generated: DETERMINISTIC_6a63c453f3497d71
Batch ID: 20250612_145826
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
CLI tool for managing PolyMarket prediction markets.
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Optional

import requests
from web3 import Web3


class PolyMarketCLI:
    """
    Command-line interface for interacting with PolyMarket prediction markets.
    """

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the CLI with configuration.
        
        Args:
            config_path: Path to configuration file.
        """
        self.config = self._load_config(config_path)
        self.w3 = Web3(Web3.HTTPProvider(self.config["rpc_url"]))
        self._validate_connection()

    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from file.
        
        Args:
            config_path: Path to configuration file.
            
        Returns:
            Loaded configuration dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            ValueError: If config is invalid.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path) as f:
            config = json.load(f)

        required_keys = ["rpc_url", "contract_address", "private_key"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required config key: {key}")

        return config

    def _validate_connection(self):
        """
        Validate connection to Ethereum node.
        
        Raises:
            ConnectionError: If connection fails.
        """
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")

    def _get_contract(self):
        """
        Get the PolyMarket contract instance.
        
        Returns:
            Contract instance.
            
        Raises:
            ValueError: If contract ABI is invalid.
        """
        try:
            with open("PolyMarketABI.json") as f:
                abi = json.load(f)
            return self.w3.eth.contract(
                address=self.config["contract_address"],
                abi=abi
            )
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load contract ABI: {str(e)}")

    def _send_transaction(self, tx):
        """
        Send a signed transaction to the network.
        
        Args:
            tx: Transaction to send.
            
        Returns:
            Transaction receipt.
            
        Raises:
            ValueError: If transaction fails.
        """
        try:
            signed_tx = self.w3.eth.account.sign_transaction(
                tx,
                private_key=self.config["private_key"]
            )
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.w3.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as e:
            raise ValueError(f"Transaction failed: {str(e)}")

    def create_market(
        self,
        question: str,
        outcomes: List[str],
        end_time: int,
        metadata: Optional[Dict] = None
    ) -> Dict:
        """
        Create a new prediction market.
        
        Args:
            question: Market question.
            outcomes: Possible outcomes.
            end_time: Unix timestamp for market resolution.
            metadata: Optional metadata.
            
        Returns:
            Transaction receipt.
        """
        contract = self._get_contract()
        tx = contract.functions.createMarket(
            question,
            outcomes,
            end_time,
            metadata or {}
        ).build_transaction({
            "from": self.w3.eth.account.from_key(self.config["private_key"]).address,
            "nonce": self.w3.eth.get_transaction_count(
                self.w3.eth.account.from_key(self.config["private_key"]).address
            ),
        })
        return self._send_transaction(tx)

    def update_market(
        self,
        market_id: int,
        question: Optional[str] = None,
        outcomes: Optional[List[str]] = None,
        end_time: Optional[int] = None,
        metadata: Optional[Dict] = None
    ) -> Dict:
        """
        Update an existing prediction market.
        
        Args:
            market_id: ID of market to update.
            question: New question (optional).
            outcomes: New outcomes (optional).
            end_time: New end time (optional).
            metadata: New metadata (optional).
            
        Returns:
            Transaction receipt.
        """
        contract = self._get_contract()
        tx = contract.functions.updateMarket(
            market_id,
            question or "",
            outcomes or [],
            end_time or 0,
            metadata or {}
        ).build_transaction({
            "from": self.w3.eth.account.from_key(self.config["private_key"]).address,
            "nonce": self.w3.eth.get_transaction_count(
                self.w3.eth.account.from_key(self.config["private_key"]).address
            ),
        })
        return self._send_transaction(tx)

    def resolve_market(self, market_id: int, outcome_index: int) -> Dict:
        """
        Resolve a prediction market.
        
        Args:
            market_id: ID of market to resolve.
            outcome_index: Index of winning outcome.
            
        Returns:
            Transaction receipt.
        """
        contract = self._get_contract()
        tx = contract.functions.resolveMarket(
            market_id,
            outcome_index
        ).build_transaction({
            "from": self.w3.eth.account.from_key(self.config["private_key"]).address,
            "nonce": self.w3.eth.get_transaction_count(
                self.w3.eth.account.from_key(self.config["private_key"]).address
            ),
        })
        return self._send_transaction(tx)

    def get_market(self, market_id: int) -> Dict:
        """
        Get market details.
        
        Args:
            market_id: ID of market to fetch.
            
        Returns:
            Market details.
        """
        contract = self._get_contract()
        return contract.functions.markets(market_id).call()

    def list_markets(self, limit: int = 10) -> List[Dict]:
        """
        List available markets.
        
        Args:
            limit: Maximum number of markets to return.
            
        Returns:
            List of market details.
        """
        contract = self._get_contract()
        market_count = contract.functions.marketCount().call()
        markets = []
        for i in range(min(market_count, limit)):
            markets.append(self.get_market(i))
        return markets


def main():
    parser = argparse.ArgumentParser(description="PolyMarket CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create market command
    create_parser = subparsers.add_parser("create", help="Create a new market")
    create_parser.add_argument("question", help="Market question")
    create_parser.add_argument("outcomes", nargs="+", help="Possible outcomes")
    create_parser.add_argument("end_time", type=int, help="Unix timestamp for market end")
    create_parser.add_argument("--metadata", help="JSON metadata", default="{}")

    # Update market command
    update_parser = subparsers.add_parser("update", help="Update an existing market")
    update_parser.add_argument("market_id", type=int, help="Market ID to update")
    update_parser.add_argument("--question", help="New question")
    update_parser.add_argument("--outcomes", nargs="+", help="New outcomes")
    update_parser.add_argument("--end-time", type=int, help="New end time")
    update_parser.add_argument("--metadata", help="New metadata", default="{}")

    # Resolve market command
    resolve_parser = subparsers.add_parser("resolve", help="Resolve a market")
    resolve_parser.add_argument("market_id", type=int, help="Market ID to resolve")
    resolve_parser.add_argument("outcome_index", type=int, help="Index of winning outcome")

    # Get market command
    get_parser = subparsers.add_parser("get", help="Get market details")
    get_parser.add_argument("market_id", type=int, help="Market ID to fetch")

    # List markets command
    list_parser = subparsers.add_parser("list", help="List markets")
    list_parser.add_argument("--limit", type=int, default=10, help="Maximum number of markets to list")

    args = parser.parse_args()

    try:
        cli = PolyMarketCLI()

        if args.command == "create":
            metadata = json.loads(args.metadata)
            receipt = cli.create_market(
                args.question,
                args.outcomes,
                args.end_time,
                metadata
            )
            print(f"Market created: {receipt['transactionHash'].hex()}")

        elif args.command == "update":
            metadata = json.loads(args.metadata)
            receipt = cli.update_market(
                args.market_id,
                args.question,
                args.outcomes,
                args.end_time,
                metadata
            )
            print(f"Market updated: {receipt['transactionHash'].hex()}")

        elif args.command == "resolve":
