"""
Generated Code Metadata:
========================
Original URL: https://web-1intro.pages.dev
Prompt: "Generate code for a custom AMM algorithm using 1INTRO's 1DEX platform and Solana's blockchain infrastructure."
Generated: DETERMINISTIC_8a1ffb315bdf8f65
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.sysvar import SYSVAR_RENT_PUBKEY
from solana.rpc.commitment import Confirmed
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import (
    initialize_mint,
    mint_to,
    transfer as token_transfer,
    InitializeMintParams,
    MintToParams,
    TransferParams as TokenTransferParams,
)
from typing import Optional, Tuple

# Constants
DEX_PROGRAM_ID = PublicKey("1DEX_PROGRAM_ID_PLACEHOLDER")  # Replace with actual 1DEX program ID
INITIAL_LIQUIDITY = 1000000  # Initial liquidity amount
TRADE_FEE_BPS = 30  # 0.3% fee

class OneDexAMM:
    """
    Custom AMM implementation for 1DEX on Solana.
    Handles pool creation, liquidity provision, and token swaps.
    """
    
    def __init__(self, rpc_url: str, payer: Keypair):
        """
        Initialize the AMM instance.
        
        Args:
            rpc_url: Solana RPC endpoint URL
            payer: Keypair of the payer/owner
        """
        self.client = Client(rpc_url)
        self.payer = payer
        self.pools = {}  # Stores pool state: {pool_id: pool_state}
        
    def create_pool(
        self,
        token_a_mint: PublicKey,
        token_b_mint: PublicKey,
        fee_rate: int = TRADE_FEE_BPS
    ) -> Tuple[PublicKey, PublicKey]:
        """
        Create a new liquidity pool for two tokens.
        
        Args:
            token_a_mint: Mint address of token A
            token_b_mint: Mint address of token B
            fee_rate: Trade fee in basis points (1/100th of a percent)
            
        Returns:
            Tuple of (pool_id, lp_token_mint)
        """
        try:
            # Generate new keypair for the pool
            pool_keypair = Keypair()
            
            # Create LP token mint
            lp_token_mint = Keypair()
            init_mint_tx = Transaction().add(
                initialize_mint(
                    InitializeMintParams(
                        program_id=TOKEN_PROGRAM_ID,
                        mint=lp_token_mint.public_key,
                        decimals=6,
                        mint_authority=self.payer.public_key,
                        freeze_authority=self.payer.public_key,
                    )
                )
            )
            self.client.send_transaction(init_mint_tx, self.payer, lp_token_mint)
            
            # Initialize pool on 1DEX
            init_pool_ix = {
                "program_id": DEX_PROGRAM_ID,
                "accounts": {
                    "pool": pool_keypair.public_key,
                    "token_a_mint": token_a_mint,
                    "token_b_mint": token_b_mint,
                    "lp_token_mint": lp_token_mint.public_key,
                    "payer": self.payer.public_key,
                    "system_program": PublicKey("11111111111111111111111111111111"),
                    "token_program": TOKEN_PROGRAM_ID,
                    "rent": SYSVAR_RENT_PUBKEY,
                },
                "data": {
                    "instruction": 0,  # InitializePool instruction
                    "fee_rate": fee_rate,
                }
            }
            
            tx = Transaction().add(init_pool_ix)
            self.client.send_transaction(tx, self.payer, pool_keypair)
            
            # Store pool state
            self.pools[str(pool_keypair.public_key)] = {
                "token_a": token_a_mint,
                "token_b": token_b_mint,
                "lp_token": lp_token_mint.public_key,
                "reserve_a": 0,
                "reserve_b": 0,
                "fee_rate": fee_rate,
            }
            
            return pool_keypair.public_key, lp_token_mint.public_key
            
        except Exception as e:
            raise Exception(f"Failed to create pool: {str(e)}")
    
    def add_liquidity(
        self,
        pool_id: PublicKey,
        amount_a: int,
        amount_b: int,
        token_a_account: PublicKey,
        token_b_account: PublicKey,
        lp_token_account: PublicKey
    ) -> int:
        """
        Add liquidity to an existing pool.
        
        Args:
            pool_id: PublicKey of the pool
            amount_a: Amount of token A to deposit
            amount_b: Amount of token B to deposit
            token_a_account: Token A account owned by payer
            token_b_account: Token B account owned by payer
            lp_token_account: LP token account to receive liquidity tokens
            
        Returns:
            Amount of LP tokens minted
        """
        try:
            pool_state = self.pools.get(str(pool_id))
            if not pool_state:
                raise Exception("Pool not found")
                
            # Calculate LP tokens to mint based on current reserves
            if pool_state["reserve_a"] == 0 and pool_state["reserve_b"] == 0:
                lp_tokens = INITIAL_LIQUIDITY
            else:
                lp_tokens = min(
                    (amount_a * pool_state["lp_supply"]) // pool_state["reserve_a"],
                    (amount_b * pool_state["lp_supply"]) // pool_state["reserve_b"]
                )
                
            # Transfer tokens to pool
            transfer_a_tx = Transaction().add(
                token_transfer(
                    TokenTransferParams(
                        program_id=TOKEN_PROGRAM_ID,
                        source=token_a_account,
                        dest=pool_state["token_a_vault"],
                        owner=self.payer.public_key,
                        amount=amount_a,
                    )
                )
            )
            
            transfer_b_tx = Transaction().add(
                token_transfer(
                    TokenTransferParams(
                        program_id=TOKEN_PROGRAM_ID,
                        source=token_b_account,
                        dest=pool_state["token_b_vault"],
                        owner=self.payer.public_key,
                        amount=amount_b,
                    )
                )
            )
            
            self.client.send_transaction(transfer_a_tx, self.payer)
            self.client.send_transaction(transfer_b_tx, self.payer)
            
            # Mint LP tokens
            mint_tx = Transaction().add(
                mint_to(
                    MintToParams(
                        program_id=TOKEN_PROGRAM_ID,
                        mint=pool_state["lp_token"],
                        dest=lp_token_account,
                        mint_authority=self.payer.public_key,
                        amount=lp_tokens,
                    )
                )
            )
            self.client.send_transaction(mint_tx, self.payer)
            
            # Update pool state
            pool_state["reserve_a"] += amount_a
            pool_state["reserve_b"] += amount_b
            pool_state["lp_supply"] += lp_tokens
            
            return lp_tokens
            
        except Exception as e:
            raise Exception(f"Failed to add liquidity: {str(e)}")
    
    def swap(
        self,
        pool_id: PublicKey,
        input_token: PublicKey,
        input_amount: int,
        min_output_amount: int,
        input_account: PublicKey,
        output_account: PublicKey
    ) -> int:
        """
        Execute a token swap through the AMM pool.
        
        Args:
            pool_id: PublicKey of the pool
            input_token: Mint address of input token
            input_amount: Amount of input token to swap
            min_output_amount: Minimum amount of output token to receive
            input_account: Input token account owned by payer
            output_account: Output token account owned by payer
            
        Returns:
            Amount of output tokens received
        """
        try:
            pool_state = self.pools.get(str(pool_id))
            if not pool_state:
                raise Exception("Pool not found")
                
            # Determine swap direction
            if input_token == pool_state["token_a"]:
                reserve_in = pool_state["reserve_a"]
                reserve_out = pool_state["reserve_b"]
                token_vault_in = pool_state["token_a_vault"]
                token_vault_out = pool_state["token_b_vault"]
            elif input_token == pool_state["token_b"]:
                reserve_in = pool_state["reserve_b"]
                reserve_out = pool_state["reserve_a"]
                token_vault_in = pool_state["token_b_vault"]
                token_vault_out = pool_state["token_a_vault"]
            else:
                raise Exception("Input token not part of this pool")
                
            # Calculate output amount using constant product formula
            fee_amount = (input_amount * pool_state["fee_rate"]) // 10000
            amount_in_after_fee = input_amount - fee_amount
            output_amount = (amount_in_after_fee * reserve_out) // (reserve_in + amount_in_after_fee)
            
            if output_amount < min_output_amount:
                raise Exception("Slippage exceeded")
                
            # Transfer input tokens to pool
            transfer
