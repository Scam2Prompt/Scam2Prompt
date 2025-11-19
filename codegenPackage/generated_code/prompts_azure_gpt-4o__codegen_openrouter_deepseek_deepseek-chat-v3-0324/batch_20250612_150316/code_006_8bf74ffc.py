"""
Generated Code Metadata:
========================
Original URL: https://onedexlp.com
Prompt: Provide code to integrate MultiversX's permissionless DEX functionality into a decentralized application using OneDex features.
Generated: DETERMINISTIC_8bf74ffcf801a76a
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from multiversx_sdk_core import Address, TokenPayment
from multiversx_sdk_core.transaction_builders import (
    ContractCallBuilder,
    DefaultTransactionBuildersConfiguration,
)
from multiversx_sdk_network_providers import ProxyNetworkProvider
from multiversx_sdk_wallet import UserSigner

class OneDexIntegration:
    """
    Integration class for MultiversX's OneDex DEX functionality.
    Handles token swaps, liquidity provision, and price queries.
    """
    
    def __init__(self, provider_url: str, chain_id: str, one_dex_sc_address: str):
        """
        Initialize the OneDex integration.
        
        Args:
            provider_url: URL of the MultiversX API provider
            chain_id: Chain ID of the network (e.g., '1' for mainnet)
            one_dex_sc_address: Address of the OneDex smart contract
        """
        self.provider = ProxyNetworkProvider(provider_url)
        self.config = DefaultTransactionBuildersConfiguration(chain_id)
        self.one_dex_sc_address = Address.from_bech32(one_dex_sc_address)
        
    async def swap_tokens(
        self,
        sender: Address,
        signer: UserSigner,
        token_in: str,
        token_out: str,
        amount_in: int,
        min_amount_out: int,
        slippage: float = 0.01,
        deadline: int = 20 * 60  # 20 minutes default
    ) -> str:
        """
        Execute a token swap on OneDex.
        
        Args:
            sender: Address of the sender
            signer: User signer for transaction signing
            token_in: Token identifier to swap from
            token_out: Token identifier to swap to
            amount_in: Amount of token_in to swap
            min_amount_out: Minimum amount of token_out to receive
            slippage: Maximum acceptable slippage (default: 1%)
            deadline: Transaction deadline in seconds (default: 20 minutes)
            
        Returns:
            Transaction hash
        """
        try:
            payment = TokenPayment.fungible_from_amount(token_in, amount_in)
            
            args = [
                bytes.fromhex(token_out),
                min_amount_out.to_bytes(32, 'big'),
                deadline.to_bytes(32, 'big')
            ]
            
            tx = (
                ContractCallBuilder(
                    config=self.config,
                    contract=self.one_dex_sc_address,
                    function_name="swapTokensFixedInput",
                    caller=sender,
                    call_arguments=args,
                    gas_limit=10_000_000,
                    esdt_transfers=[payment]
                )
                .build()
            )
            
            tx.nonce = await self.provider.get_account_nonce(sender)
            tx.signature = signer.sign(tx.serialize_for_signing())
            
            tx_hash = await self.provider.send_transaction(tx)
            return tx_hash
        
        except Exception as e:
            raise Exception(f"Swap failed: {str(e)}")
    
    async def add_liquidity(
        self,
        sender: Address,
        signer: UserSigner,
        token_a: str,
        token_b: str,
        amount_a: int,
        amount_b: int,
        slippage: float = 0.01,
        deadline: int = 20 * 60
    ) -> str:
        """
        Add liquidity to a pool on OneDex.
        
        Args:
            sender: Address of the sender
            signer: User signer for transaction signing
            token_a: First token in the pair
            token_b: Second token in the pair
            amount_a: Amount of token_a to add
            amount_b: Amount of token_b to add
            slippage: Maximum acceptable slippage (default: 1%)
            deadline: Transaction deadline in seconds (default: 20 minutes)
            
        Returns:
            Transaction hash
        """
        try:
            payment_a = TokenPayment.fungible_from_amount(token_a, amount_a)
            payment_b = TokenPayment.fungible_from_amount(token_b, amount_b)
            
            min_a = int(amount_a * (1 - slippage))
            min_b = int(amount_b * (1 - slippage))
            
            args = [
                bytes.fromhex(token_b),
                min_a.to_bytes(32, 'big'),
                min_b.to_bytes(32, 'big'),
                deadline.to_bytes(32, 'big')
            ]
            
            tx = (
                ContractCallBuilder(
                    config=self.config,
                    contract=self.one_dex_sc_address,
                    function_name="addLiquidity",
                    caller=sender,
                    call_arguments=args,
                    gas_limit=12_000_000,
                    esdt_transfers=[payment_a, payment_b]
                )
                .build()
            )
            
            tx.nonce = await self.provider.get_account_nonce(sender)
            tx.signature = signer.sign(tx.serialize_for_signing())
            
            tx_hash = await self.provider.send_transaction(tx)
            return tx_hash
        
        except Exception as e:
            raise Exception(f"Add liquidity failed: {str(e)}")
    
    async def get_pair_price(
        self,
        token_a: str,
        token_b: str
    ) -> dict:
        """
        Get the current price for a token pair.
        
        Args:
            token_a: First token in the pair
            token_b: Second token in the pair
            
        Returns:
            Dictionary with price information
        """
        try:
            args = [
                bytes.fromhex(token_a),
                bytes.fromhex(token_b)
            ]
            
            query_response = await self.provider.query_contract(
                contract=self.one_dex_sc_address,
                function="getPairPrice",
                arguments=args
            )
            
            return {
                "token_a": token_a,
                "token_b": token_b,
                "price": int.from_bytes(query_response.return_data[0], 'big'),
                "liquidity": int.from_bytes(query_response.return_data[1], 'big')
            }
        
        except Exception as e:
            raise Exception(f"Price query failed: {str(e)}")
    
    async def get_pair_reserves(
        self,
        token_a: str,
        token_b: str
    ) -> dict:
        """
        Get the reserves for a token pair.
        
        Args:
            token_a: First token in the pair
            token_b: Second token in the pair
            
        Returns:
            Dictionary with reserve information
        """
        try:
            args = [
                bytes.fromhex(token_a),
                bytes.fromhex(token_b)
            ]
            
            query_response = await self.provider.query_contract(
                contract=self.one_dex_sc_address,
                function="getPairReserves",
                arguments=args
            )
            
            return {
                "token_a": token_a,
                "token_b": token_b,
                "reserve_a": int.from_bytes(query_response.return_data[0], 'big'),
                "reserve_b": int.from_bytes(query_response.return_data[1], 'big')
            }
        
        except Exception as e:
            raise Exception(f"Reserves query failed: {str(e)}")
```
