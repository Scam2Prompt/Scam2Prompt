"""
Generated Code Metadata:
========================
Original URL: https://ton-448f1f.webflow.io
Prompt: Develop a decentralized application (dApp) for TON Capital that allows users to acquire Node Licenses, stake nodes, and track their airdrop rewards in real-time.
Generated: DETERMINISTIC_7b3df455a883546c
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.ton.dev": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import os
from tonclient.client import TonClient
from tonclient.types import ParamsOfQuery, KeyPair, Signer, Abi, CallSet, ParamsOfEncodeMessage, ParamsOfProcessMessage

# Configuration
CONFIG = {
    "network": {
        "endpoints": ["https://mainnet.ton.dev"],
        "timeout": 30000
    },
    "contracts": {
        "node_license": "0:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        "staking": "0:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
        "airdrop": "0:7890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456"
    },
    "gas_limit": 1000000
}

# Initialize TON client
ton_client = TonClient(
    config=CONFIG["network"],
    is_async=False
)

# Data models
@dataclass
class NodeLicense:
    license_id: str
    owner_address: str
    purchase_date: datetime
    is_active: bool
    expiration_date: datetime

@dataclass
class StakedNode:
    node_id: str
    license_id: str
    staked_amount: int
    staked_at: datetime
    last_reward_date: datetime

@dataclass
class AirdropReward:
    reward_id: str
    user_address: str
    amount: int
    claimable: bool
    claimed_at: Optional[datetime]

# Helper functions
def generate_keypair() -> KeyPair:
    """Generate a new keypair for wallet operations"""
    return ton_client.crypto.generate_random_sign_keys()

def get_contract_abi(contract_name: str) -> Abi:
    """Load contract ABI from file"""
    abi_path = os.path.join(os.path.dirname(__file__), f"abis/{contract_name}.abi.json")
    with open(abi_path, "r") as f:
        return Abi.from_json(f.read())

def calculate_contract_address(abi: Abi, keypair: KeyPair) -> str:
    """Calculate contract address from ABI and keypair"""
    encode_params = ParamsOfEncodeMessage(
        abi=abi,
        signer=Signer.Keys(keypair),
        deploy_set=None,
        call_set=None
    )
    result = ton_client.abi.encode_message(encode_params)
    return result.address

# Core dApp functions
class TONCapitaldApp:
    def __init__(self):
        self.user_keypair = None
        self.user_address = None

    def connect_wallet(self, keypair: KeyPair) -> None:
        """Connect user wallet to dApp"""
        self.user_keypair = keypair
        self.user_address = calculate_contract_address(
            get_contract_abi("wallet"),
            keypair
        )

    def purchase_node_license(self, license_type: str, amount: int) -> str:
        """Purchase a node license"""
        if not self.user_keypair:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("node_license")
        call_set = CallSet(
            function_name="purchaseLicense",
            input={
                "licenseType": license_type,
                "amount": str(amount)
            }
        )

        params = ParamsOfProcessMessage(
            abi=abi,
            signer=Signer.Keys(self.user_keypair),
            address=CONFIG["contracts"]["node_license"],
            call_set=call_set,
            processing_try_index=1
        )

        result = ton_client.processing.process_message(params)
        return result.transaction["id"]

    def stake_node(self, license_id: str, amount: int) -> str:
        """Stake a node with the given license"""
        if not self.user_keypair:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("staking")
        call_set = CallSet(
            function_name="stakeNode",
            input={
                "licenseId": license_id,
                "amount": str(amount)
            }
        )

        params = ParamsOfProcessMessage(
            abi=abi,
            signer=Signer.Keys(self.user_keypair),
            address=CONFIG["contracts"]["staking"],
            call_set=call_set,
            processing_try_index=1
        )

        result = ton_client.processing.process_message(params)
        return result.transaction["id"]

    def unstake_node(self, node_id: str) -> str:
        """Unstake a node"""
        if not self.user_keypair:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("staking")
        call_set = CallSet(
            function_name="unstakeNode",
            input={"nodeId": node_id}
        )

        params = ParamsOfProcessMessage(
            abi=abi,
            signer=Signer.Keys(self.user_keypair),
            address=CONFIG["contracts"]["staking"],
            call_set=call_set,
            processing_try_index=1
        )

        result = ton_client.processing.process_message(params)
        return result.transaction["id"]

    def claim_airdrop_rewards(self, reward_ids: List[str]) -> str:
        """Claim airdrop rewards"""
        if not self.user_keypair:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("airdrop")
        call_set = CallSet(
            function_name="claimRewards",
            input={"rewardIds": reward_ids}
        )

        params = ParamsOfProcessMessage(
            abi=abi,
            signer=Signer.Keys(self.user_keypair),
            address=CONFIG["contracts"]["airdrop"],
            call_set=call_set,
            processing_try_index=1
        )

        result = ton_client.processing.process_message(params)
        return result.transaction["id"]

    def get_node_licenses(self) -> List[NodeLicense]:
        """Get all node licenses owned by user"""
        if not self.user_address:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("node_license")
        query = """
            query getLicenses($owner: String!) {
                licenses(owner: $owner) {
                    id
                    owner
                    purchaseDate
                    isActive
                    expirationDate
                }
            }
        """
        variables = {"owner": self.user_address}

        result = ton_client.net.query(
            ParamsOfQuery(
                query=query,
                variables=variables
            )
        )

        return [
            NodeLicense(
                license_id=license["id"],
                owner_address=license["owner"],
                purchase_date=datetime.fromtimestamp(int(license["purchaseDate"])),
                is_active=license["isActive"],
                expiration_date=datetime.fromtimestamp(int(license["expirationDate"]))
            )
            for license in result.result["data"]["licenses"]
        ]

    def get_staked_nodes(self) -> List[StakedNode]:
        """Get all staked nodes for user"""
        if not self.user_address:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("staking")
        query = """
            query getStakedNodes($owner: String!) {
                stakedNodes(owner: $owner) {
                    id
                    licenseId
                    stakedAmount
                    stakedAt
                    lastRewardDate
                }
            }
        """
        variables = {"owner": self.user_address}

        result = ton_client.net.query(
            ParamsOfQuery(
                query=query,
                variables=variables
            )
        )

        return [
            StakedNode(
                node_id=node["id"],
                license_id=node["licenseId"],
                staked_amount=int(node["stakedAmount"]),
                staked_at=datetime.fromtimestamp(int(node["stakedAt"])),
                last_reward_date=datetime.fromtimestamp(int(node["lastRewardDate"]))
            )
            for node in result.result["data"]["stakedNodes"]
        ]

    def get_airdrop_rewards(self) -> List[AirdropReward]:
        """Get all airdrop rewards for user"""
        if not self.user_address:
            raise ValueError("Wallet not connected")

        abi = get_contract_abi("airdrop")
        query = """
            query getAirdropRewards($user: String!) {
                rewards(user: $user) {
                    id
                    user
                    amount
                    claimable
                    claimedAt
                }
            }
        """
        variables = {"user": self.user_address}

        result = ton_client.net.query(
            ParamsOfQuery(
                query=query,
                variables=variables
            )
        )

        return [
            AirdropReward(
                reward_id=reward["id"],
                user_address=reward["user"],
                amount=int(reward["amount"]),
                claimable=reward["claimable"],
                claimed_at=datetime.fromtimestamp(int(reward["claimedAt"])) if reward["claimedAt"] else None
            )
