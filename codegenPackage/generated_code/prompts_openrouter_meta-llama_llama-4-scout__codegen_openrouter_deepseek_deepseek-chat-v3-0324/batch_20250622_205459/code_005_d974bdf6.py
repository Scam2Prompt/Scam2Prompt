"""
Generated Code Metadata:
========================
Original URL: https://e-pad.xyz
Prompt: "Develop a token presale API for Ethereum and Solana with softcap and hardcap limits."
Generated: DETERMINISTIC_d974bdf6fc7afbf6
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, validator
from typing import Optional
from web3 import Web3
from solana.rpc.api import Client as SolanaClient
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
import os
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Token Presale API", version="1.0.0")

# Configuration models
class EthereumConfig(BaseModel):
    rpc_url: str = Field(..., description="Ethereum RPC URL")
    presale_contract_address: str = Field(..., description="Presale contract address")
    token_contract_address: str = Field(..., description="Token contract address")
    admin_private_key: str = Field(..., description="Admin private key (for signing transactions)")

class SolanaConfig(BaseModel):
    rpc_url: str = Field(..., description="Solana RPC URL")
    presale_program_id: str = Field(..., description="Presale program ID")
    token_mint_address: str = Field(..., description="Token mint address")
    admin_private_key: str = Field(..., description="Admin private key (for signing transactions)")

class PresaleConfig(BaseModel):
    softcap: float = Field(..., description="Softcap amount in ETH/SOL")
    hardcap: float = Field(..., description="Hardcap amount in ETH/SOL")
    start_time: datetime = Field(..., description="Presale start time")
    end_time: datetime = Field(..., description="Presale end time")
    token_price: float = Field(..., description="Price per token in ETH/SOL")
    min_contribution: float = Field(..., description="Minimum contribution amount")
    max_contribution: float = Field(..., description="Maximum contribution amount")

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError("End time must be after start time")
        return v

# Load configuration from environment variables
def load_config():
    try:
        eth_config = EthereumConfig(
            rpc_url=os.getenv("ETH_RPC_URL"),
            presale_contract_address=os.getenv("ETH_PRESALE_CONTRACT"),
            token_contract_address=os.getenv("ETH_TOKEN_CONTRACT"),
            admin_private_key=os.getenv("ETH_ADMIN_PRIVATE_KEY")
        )
        
        sol_config = SolanaConfig(
            rpc_url=os.getenv("SOL_RPC_URL"),
            presale_program_id=os.getenv("SOL_PRESALE_PROGRAM_ID"),
            token_mint_address=os.getenv("SOL_TOKEN_MINT_ADDRESS"),
            admin_private_key=os.getenv("SOL_ADMIN_PRIVATE_KEY")
        )
        
        presale_config = PresaleConfig(
            softcap=float(os.getenv("PRESALE_SOFTCAP")),
            hardcap=float(os.getenv("PRESALE_HARDCAP")),
            start_time=datetime.fromisoformat(os.getenv("PRESALE_START_TIME")),
            end_time=datetime.fromisoformat(os.getenv("PRESALE_END_TIME")),
            token_price=float(os.getenv("TOKEN_PRICE")),
            min_contribution=float(os.getenv("MIN_CONTRIBUTION")),
            max_contribution=float(os.getenv("MAX_CONTRIBUTION"))
        )
        
        return eth_config, sol_config, presale_config
    except Exception as e:
        logger.error(f"Failed to load configuration: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to load configuration"
        )

# Initialize Ethereum and Solana clients
eth_config, sol_config, presale_config = load_config()
web3 = Web3(Web3.HTTPProvider(eth_config.rpc_url))
solana_client = SolanaClient(sol_config.rpc_url)

# Contribution models
class EthereumContribution(BaseModel):
    contributor_address: str = Field(..., description="Ethereum wallet address")
    amount: float = Field(..., description="Amount in ETH")

    @validator('contributor_address')
    def validate_address(cls, v):
        if not web3.is_address(v):
            raise ValueError("Invalid Ethereum address")
        return web3.to_checksum_address(v)

class SolanaContribution(BaseModel):
    contributor_address: str = Field(..., description="Solana wallet address")
    amount: float = Field(..., description="Amount in SOL")

    @validator('contributor_address')
    def validate_address(cls, v):
        try:
            PublicKey(v)
            return v
        except:
            raise ValueError("Invalid Solana address")

# Response models
class ContributionResponse(BaseModel):
    transaction_hash: str = Field(..., description="Transaction hash")
    tokens_purchased: float = Field(..., description="Tokens purchased")
    remaining_cap: float = Field(..., description="Remaining cap")

class PresaleStatusResponse(BaseModel):
    total_raised: float = Field(..., description="Total raised amount")
    softcap_reached: bool = Field(..., description="Whether softcap is reached")
    hardcap_reached: bool = Field(..., description="Whether hardcap is reached")
    remaining_cap: float = Field(..., description="Remaining cap")
    presale_active: bool = Field(..., description="Whether presale is active")

# Helper functions
def check_presale_active():
    now = datetime.now()
    return presale_config.start_time <= now <= presale_config.end_time

def check_contribution_amount(amount: float):
    if amount < presale_config.min_contribution:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Contribution below minimum ({presale_config.min_contribution})"
        )
    if amount > presale_config.max_contribution:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Contribution above maximum ({presale_config.max_contribution})"
        )

# Ethereum presale functions
async def process_ethereum_contribution(contribution: EthereumContribution):
    try:
        if not check_presale_active():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Presale is not active"
            )
        
        check_contribution_amount(contribution.amount)
        
        # Convert ETH to Wei
        amount_wei = web3.to_wei(contribution.amount, 'ether')
        
        # Get contract instance (simplified - would need ABI in production)
        presale_contract = web3.eth.contract(
            address=eth_config.presale_contract_address,
            abi=[]  # Would need actual ABI
        )
        
        # Get current total raised
        total_raised = presale_contract.functions.totalRaised().call()
        
        # Check hardcap
        if total_raised + contribution.amount > presale_config.hardcap:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Contribution would exceed hardcap"
            )
        
        # Build transaction
        tx = presale_contract.functions.contribute().build_transaction({
            'from': contribution.contributor_address,
            'value': amount_wei,
            'gas': 200000,
            'gasPrice': web3.to_wei('50', 'gwei'),
            'nonce': web3.eth.get_transaction_count(contribution.contributor_address),
        })
        
        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=eth_config.admin_private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Calculate tokens purchased
        tokens_purchased = contribution.amount / presale_config.token_price
        
        return ContributionResponse(
            transaction_hash=tx_hash.hex(),
            tokens_purchased=tokens_purchased,
            remaining_cap=presale_config.hardcap - (total_raised + contribution.amount)
        )
    except Exception as e:
        logger.error(f"Ethereum contribution failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process Ethereum contribution"
        )

# Solana presale functions
async def process_solana_contribution(contribution: SolanaContribution):
    try:
        if not check_presale_active():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Presale is not active"
            )
        
        check_contribution_amount(contribution.amount)
        
        # Convert SOL to lamports
        amount_lamports = int(contribution.amount
