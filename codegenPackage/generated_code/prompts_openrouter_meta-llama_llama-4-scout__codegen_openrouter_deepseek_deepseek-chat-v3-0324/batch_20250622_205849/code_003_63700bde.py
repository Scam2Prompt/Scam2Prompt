"""
Generated Code Metadata:
========================
Original URL: https://aethir.ai
Prompt: "Design a high-level architecture for a decentralized AI agent economy platform using Aethir's APhone and Web3 Infra solutions."
Generated: DETERMINISTIC_63700bdedb6d7daa
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# decentralized_ai_agent_economy.py
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError
from eth_account import Account
from eth_typing import Address, ChecksumAddress
from aethir_sdk import APhoneClient, Web3InfraClient

class AgentStatus(Enum):
    """Enum representing the status of an AI agent."""
    AVAILABLE = 0
    BUSY = 1
    OFFLINE = 2

@dataclass
class AIAgent:
    """Data class representing an AI agent in the economy."""
    agent_id: str
    owner_address: ChecksumAddress
    capabilities: List[str]
    status: AgentStatus
    price_per_task: int  # in wei
    reputation_score: float

class DecentralizedAIEconomy:
    """Main class for the decentralized AI agent economy platform."""
    
    def __init__(self, web3_provider: str, contract_address: str, contract_abi: str):
        """
        Initialize the decentralized AI economy platform.
        
        Args:
            web3_provider: URL of the Web3 provider
            contract_address: Address of the smart contract
            contract_abi: ABI of the smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=json.loads(contract_abi)
        )
        self.aphone_client = APhoneClient()
        self.web3_infra = Web3InfraClient()
        self.agents: Dict[str, AIAgent] = {}
        
    def register_agent(
        self,
        private_key: str,
        capabilities: List[str],
        price_per_task: int
    ) -> str:
        """
        Register a new AI agent in the economy.
        
        Args:
            private_key: Private key of the agent owner
            capabilities: List of agent capabilities
            price_per_task: Price per task in wei
            
        Returns:
            Transaction hash of the registration
            
        Raises:
            ValueError: If registration fails
            ContractLogicError: If contract call fails
        """
        account = Account.from_key(private_key)
        
        try:
            tx = self.contract.functions.registerAgent(
                ",".join(capabilities),
                price_per_task
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            # Wait for transaction receipt
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise ValueError("Transaction failed")
                
            return tx_hash.hex()
            
        except ContractLogicError as e:
            raise ValueError(f"Contract error: {e}") from e
            
    def get_agent(self, agent_id: str) -> Optional[AIAgent]:
        """
        Retrieve an AI agent by its ID.
        
        Args:
            agent_id: ID of the agent to retrieve
            
        Returns:
            AIAgent object if found, None otherwise
        """
        if agent_id in self.agents:
            return self.agents[agent_id]
            
        try:
            agent_data = self.contract.functions.getAgent(agent_id).call()
            if not agent_data:
                return None
                
            agent = AIAgent(
                agent_id=agent_id,
                owner_address=agent_data[0],
                capabilities=agent_data[1].split(","),
                status=AgentStatus(agent_data[2]),
                price_per_task=agent_data[3],
                reputation_score=agent_data[4] / 100  # Assuming stored as integer percentage
            )
            self.agents[agent_id] = agent
            return agent
            
        except ContractLogicError:
            return None
            
    def request_agent_service(
        self,
        private_key: str,
        agent_id: str,
        task_description: str
    ) -> str:
        """
        Request service from an AI agent.
        
        Args:
            private_key: Private key of the requester
            agent_id: ID of the agent to request
            task_description: Description of the task
            
        Returns:
            Transaction hash of the service request
            
        Raises:
            ValueError: If request fails
            ContractLogicError: If contract call fails
        """
        account = Account.from_key(private_key)
        agent = self.get_agent(agent_id)
        
        if not agent:
            raise ValueError("Agent not found")
            
        if agent.status != AgentStatus.AVAILABLE:
            raise ValueError("Agent is not available")
            
        try:
            # Use APhone to establish secure communication
            comm_channel = self.aphone_client.create_channel(
                sender_address=account.address,
                receiver_address=agent.owner_address
            )
            
            # Store task metadata using Web3 Infra
            task_metadata = {
                "description": task_description,
                "requester": account.address,
                "agent": agent_id,
                "price": agent.price_per_task
            }
            task_ref = self.web3_infra.store_data(json.dumps(task_metadata))
            
            tx = self.contract.functions.requestService(
                agent_id,
                task_ref,
                comm_channel.channel_id
            ).build_transaction({
                'from': account.address,
                'value': agent.price_per_task,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise ValueError("Transaction failed")
                
            return tx_hash.hex()
            
        except ContractLogicError as e:
            raise ValueError(f"Contract error: {e}") from e
            
    def update_agent_status(
        self,
        private_key: str,
        agent_id: str,
        new_status: AgentStatus
    ) -> str:
        """
        Update the status of an AI agent.
        
        Args:
            private_key: Private key of the agent owner
            agent_id: ID of the agent to update
            new_status: New status for the agent
            
        Returns:
            Transaction hash of the status update
            
        Raises:
            ValueError: If update fails
            ContractLogicError: If contract call fails
        """
        account = Account.from_key(private_key)
        agent = self.get_agent(agent_id)
        
        if not agent:
            raise ValueError("Agent not found")
            
        if agent.owner_address != account.address:
            raise ValueError("Only owner can update agent status")
            
        try:
            tx = self.contract.functions.updateAgentStatus(
                agent_id,
                new_status.value
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise ValueError("Transaction failed")
                
            # Update local cache
            if agent_id in self.agents:
                self.agents[agent_id].status = new_status
                
            return tx_hash.hex()
            
        except ContractLogicError as e:
            raise ValueError(f"Contract error: {e}") from e
            
    def rate_agent(
        self,
        private_key: str,
        agent_id: str,
        task_id: str,
        rating: int
    ) -> str:
        """
        Rate an AI agent after task completion.
        
        Args:
            private_key: Private key of the rater
            agent_id: ID of the agent to rate
            task_id: ID of the completed task
            rating: Rating score (1-5)
            
        Returns:
            Transaction hash of the rating
            
        Raises:
            ValueError: If rating fails
            ContractLogicError: If contract call fails
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
            
        account = Account.from_key(private_key)
        
        try:
            tx = self.contract.functions.rateAgent(
                agent_id,
                task_id,
                rating
            ).build_transaction({
                'from': account.address,
                'nonce': self.web3.eth.get_transaction_count(account.address),
                'gas': 2000000
            })
            
            signed_tx = self.web3.
