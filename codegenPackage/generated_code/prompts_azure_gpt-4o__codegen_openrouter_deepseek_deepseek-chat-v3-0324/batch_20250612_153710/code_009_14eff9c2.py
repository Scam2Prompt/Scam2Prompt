"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Create a manuscript schema in Chainbase to unify data access models across Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_14eff9c21d303f6d
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, validator
from enum import Enum

class ChainType(str, Enum):
    ETHEREUM = "ethereum"
    BINANCE_SMART_CHAIN = "binance_smart_chain"

class Transaction(BaseModel):
    """
    Unified transaction model for both Ethereum and Binance Smart Chain.
    """
    chain: ChainType
    hash: str = Field(..., description="Transaction hash")
    from_address: str = Field(..., alias="from", description="Sender address")
    to_address: Optional[str] = Field(None, alias="to", description="Recipient address")
    value: str = Field(..., description="Transaction value in wei")
    gas: str = Field(..., description="Gas limit")
    gas_price: str = Field(..., alias="gasPrice", description="Gas price in wei")
    input: Optional[str] = Field(None, description="Input data")
    nonce: str = Field(..., description="Transaction nonce")
    block_hash: Optional[str] = Field(None, alias="blockHash", description="Block hash")
    block_number: Optional[str] = Field(None, alias="blockNumber", description="Block number")
    transaction_index: Optional[str] = Field(None, alias="transactionIndex", description="Transaction index in block")

    @validator('from_address', 'to_address', pre=True)
    def validate_address(cls, v):
        if v is None:
            return v
        if not isinstance(v, str):
            raise ValueError("Address must be a string")
        if len(v) != 42 or not v.startswith('0x'):
            raise ValueError("Invalid address format")
        return v.lower()

class Block(BaseModel):
    """
    Unified block model for both Ethereum and Binance Smart Chain.
    """
    chain: ChainType
    hash: str = Field(..., description="Block hash")
    number: str = Field(..., description="Block number")
    parent_hash: str = Field(..., alias="parentHash", description="Parent block hash")
    nonce: str = Field(..., description="Block nonce")
    sha3_uncles: str = Field(..., alias="sha3Uncles", description="SHA3 of uncles")
    logs_bloom: Optional[str] = Field(None, alias="logsBloom", description="Logs bloom filter")
    transactions_root: str = Field(..., alias="transactionsRoot", description="Transactions root hash")
    state_root: str = Field(..., alias="stateRoot", description="State root hash")
    receipts_root: str = Field(..., alias="receiptsRoot", description="Receipts root hash")
    miner: str = Field(..., description="Miner address")
    difficulty: str = Field(..., description="Block difficulty")
    total_difficulty: str = Field(..., alias="totalDifficulty", description="Total difficulty")
    extra_data: str = Field(..., alias="extraData", description="Extra data")
    size: str = Field(..., description="Block size")
    gas_limit: str = Field(..., alias="gasLimit", description="Gas limit")
    gas_used: str = Field(..., alias="gasUsed", description="Gas used")
    timestamp: str = Field(..., description="Block timestamp")
    transactions: List[Union[str, Transaction]] = Field(..., description="List of transaction hashes or full transactions")
    uncles: List[str] = Field(..., description="List of uncle hashes")

class Log(BaseModel):
    """
    Unified log model for both Ethereum and Binance Smart Chain.
    """
    chain: ChainType
    address: str = Field(..., description="Contract address")
    topics: List[str] = Field(..., description="List of topics")
    data: str = Field(..., description="Log data")
    block_number: str = Field(..., alias="blockNumber", description="Block number")
    transaction_hash: str = Field(..., alias="transactionHash", description="Transaction hash")
    transaction_index: str = Field(..., alias="transactionIndex", description="Transaction index")
    block_hash: str = Field(..., alias="blockHash", description="Block hash")
    log_index: str = Field(..., alias="logIndex", description="Log index")
    removed: bool = Field(..., description="Whether log was removed")

class TransactionReceipt(BaseModel):
    """
    Unified transaction receipt model for both Ethereum and Binance Smart Chain.
    """
    chain: ChainType
    transaction_hash: str = Field(..., alias="transactionHash", description="Transaction hash")
    transaction_index: str = Field(..., alias="transactionIndex", description="Transaction index")
    block_hash: str = Field(..., alias="blockHash", description="Block hash")
    block_number: str = Field(..., alias="blockNumber", description="Block number")
    from_address: str = Field(..., alias="from", description="Sender address")
    to_address: Optional[str] = Field(None, alias="to", description="Recipient address")
    cumulative_gas_used: str = Field(..., alias="cumulativeGasUsed", description="Cumulative gas used")
    gas_used: str = Field(..., alias="gasUsed", description="Gas used")
    contract_address: Optional[str] = Field(None, alias="contractAddress", description="Contract address if created")
    logs: List[Log] = Field(..., description="List of logs")
    logs_bloom: str = Field(..., alias="logsBloom", description="Logs bloom filter")
    status: Optional[str] = Field(None, description="Transaction status (1 for success, 0 for failure)")

class ChainData(BaseModel):
    """
    Unified data model containing all chain information.
    """
    chain: ChainType
    blocks: List[Block] = Field(..., description="List of blocks")
    transactions: List[Transaction] = Field(..., description="List of transactions")
    receipts: List[TransactionReceipt] = Field(..., description="List of transaction receipts")
    logs: List[Log] = Field(..., description="List of logs")

class ChainbaseResponse(BaseModel):
    """
    Standard response format for Chainbase API.
    """
    status: str = Field(..., description="Response status")
    message: str = Field(..., description="Response message")
    data: Optional[Union[ChainData, Dict]] = Field(None, description="Response data")
    error: Optional[Dict] = Field(None, description="Error details if any")

    @validator('status')
    def validate_status(cls, v):
        if v not in ['success', 'error']:
            raise ValueError("Status must be either 'success' or 'error'")
        return v
```
