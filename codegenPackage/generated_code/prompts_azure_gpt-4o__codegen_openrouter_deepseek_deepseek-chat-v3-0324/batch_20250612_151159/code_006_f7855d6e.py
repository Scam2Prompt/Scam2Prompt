"""
Generated Code Metadata:
========================
Original URL: https://u-ep5.pages.dev
Prompt: Generate code to design a quest campaign that combines onchain and offchain user actions, referencing Layer3's storytelling-driven approach.
Generated: DETERMINISTIC_f7855d6ed182fa9a
Batch ID: 20250612_151159
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-api-service.com/v1": {
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
import json
from typing import Dict, List, Optional
from enum import Enum
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
import requests

# Configuration
CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
    "quest_contract_address": "0x...",
    "quest_contract_abi": [...],  # ABI of your quest contract
    "api_base_url": "https://your-api-service.com/v1",
    "api_key": "your_api_key_here"
}

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(CONFIG["rpc_url"]))
if not w3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum node")

# Initialize contract
quest_contract = w3.eth.contract(
    address=CONFIG["quest_contract_address"],
    abi=CONFIG["quest_contract_abi"]
)

class QuestStatus(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    FAILED = 3

class QuestStepType(Enum):
    ONCHAIN = "onchain"
    OFFCHAIN = "offchain"

class QuestStep:
    def __init__(
        self,
        step_id: int,
        name: str,
        description: str,
        step_type: QuestStepType,
        action_data: Dict,
        is_required: bool = True
    ):
        self.step_id = step_id
        self.name = name
        self.description = description
        self.step_type = step_type
        self.action_data = action_data
        self.is_required = is_required

class Quest:
    def __init__(
        self,
        quest_id: int,
        title: str,
        description: str,
        steps: List[QuestStep],
        rewards: Dict,
        creator: str
    ):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.steps = steps
        self.rewards = rewards
        self.creator = creator

class QuestCampaign:
    def __init__(self, campaign_id: str, name: str, description: str, quests: List[Quest]):
        self.campaign_id = campaign_id
        self.name = name
        self.description = description
        self.quests = quests

    def get_quest_by_id(self, quest_id: int) -> Optional[Quest]:
        for quest in self.quests:
            if quest.quest_id == quest_id:
                return quest
        return None

class QuestManager:
    def __init__(self):
        self.campaigns: Dict[str, QuestCampaign] = {}
        self.user_progress: Dict[str, Dict[str, Dict[int, QuestStatus]]] = {}

    def add_campaign(self, campaign: QuestCampaign):
        self.campaigns[campaign.campaign_id] = campaign

    def start_quest(self, user_address: str, campaign_id: str, quest_id: int) -> bool:
        if campaign_id not in self.campaigns:
            raise ValueError("Campaign not found")
        
        quest = self.campaigns[campaign_id].get_quest_by_id(quest_id)
        if not quest:
            raise ValueError("Quest not found")
        
        if user_address not in self.user_progress:
            self.user_progress[user_address] = {}
        
        if campaign_id not in self.user_progress[user_address]:
            self.user_progress[user_address][campaign_id] = {}
        
        if quest_id in self.user_progress[user_address][campaign_id]:
            current_status = self.user_progress[user_address][campaign_id][quest_id]
            if current_status != QuestStatus.NOT_STARTED:
                return False
        
        self.user_progress[user_address][campaign_id][quest_id] = QuestStatus.IN_PROGRESS
        return True

    def verify_onchain_step(
        self,
        user_address: str,
        campaign_id: str,
        quest_id: int,
        step_id: int,
        tx_hash: str
    ) -> bool:
        try:
            tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
            if not tx_receipt:
                return False
            
            if tx_receipt["from"].lower() != user_address.lower():
                return False
            
            quest = self.campaigns[campaign_id].get_quest_by_id(quest_id)
            if not quest:
                return False
            
            step = next((s for s in quest.steps if s.step_id == step_id), None)
            if not step or step.step_type != QuestStepType.ONCHAIN:
                return False
            
            # Verify transaction matches expected action
            if not self._verify_onchain_action(tx_receipt, step.action_data):
                return False
            
            return True
        except TransactionNotFound:
            return False
        except Exception as e:
            print(f"Error verifying onchain step: {e}")
            return False

    def _verify_onchain_action(self, tx_receipt: Dict, expected_action: Dict) -> bool:
        # Implement specific verification logic based on your contract
        try:
            logs = quest_contract.events.QuestAction().process_receipt(tx_receipt)
            for log in logs:
                if log["args"]["actionType"] == expected_action["action_type"]:
                    return True
            return False
        except Exception as e:
            print(f"Error processing transaction logs: {e}")
            return False

    def verify_offchain_step(
        self,
        user_address: str,
        campaign_id: str,
        quest_id: int,
        step_id: int,
        proof_data: Dict
    ) -> bool:
        try:
            quest = self.campaigns[campaign_id].get_quest_by_id(quest_id)
            if not quest:
                return False
            
            step = next((s for s in quest.steps if s.step_id == step_id), None)
            if not step or step.step_type != QuestStepType.OFFCHAIN:
                return False
            
            # Verify offchain action with API
            headers = {
                "Authorization": f"Bearer {CONFIG['api_key']}",
                "Content-Type": "application/json"
            }
            response = requests.post(
                f"{CONFIG['api_base_url']}/verify-offchain-action",
                headers=headers,
                json={
                    "user_address": user_address,
                    "action_data": step.action_data,
                    "proof_data": proof_data
                }
            )
            
            if response.status_code == 200:
                return response.json().get("verified", False)
            return False
        except Exception as e:
            print(f"Error verifying offchain step: {e}")
            return False

    def complete_quest_step(
        self,
        user_address: str,
        campaign_id: str,
        quest_id: int,
        step_id: int
    ) -> bool:
        try:
            if user_address not in self.user_progress:
                return False
            
            if campaign_id not in self.user_progress[user_address]:
                return False
            
            if quest_id not in self.user_progress[user_address][campaign_id]:
                return False
            
            if self.user_progress[user_address][campaign_id][quest_id] != QuestStatus.IN_PROGRESS:
                return False
            
            quest = self.campaigns[campaign_id].get_quest_by_id(quest_id)
            if not quest:
                return False
            
            step = next((s for s in quest.steps if s.step_id == step_id), None)
            if not step:
                return False
            
            # Check if all required steps are completed
            all_steps_completed = True
            for s in quest.steps:
                if s.is_required and s.step_id != step_id:
                    # In a real implementation, you'd track completed steps
                    all_steps_completed = False
                    break
            
            if all_steps_completed:
                self.user_progress[user_address][campaign_id][quest_id] = QuestStatus.COMPLETED
                self._distribute_rewards(user_address, quest.rewards)
                return True
            
            return False
        except Exception as e:
            print(f"Error completing quest step: {e}")
            return False

    def _distribute_rewards(self, user_address: str, rewards: Dict):
        try:
            if "tokens" in rewards:
                for token in rewards["tokens"]:
                    tx = quest_contract.functions.mintToken(
                        user_address,
                        token["amount"],
                        token["tokenId"] if "tokenId" in token else 0
                    ).build_transaction({
                        "from": CONFIG["quest_contract_address"],
                        "gas": 200000
                    })
                    signed_tx = w3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
                    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    w3.eth.wait_for_transaction_receipt(tx_hash)
            
            if "nfts"
