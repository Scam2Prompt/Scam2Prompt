"""
Generated Code Metadata:
========================
Original URL: https://in.ton-telegram.network
Prompt: "Generate code to interact with The Open Network (TON) blockchain using Toncoin."
Generated: DETERMINISTIC_28a4c5b1df4b0c71
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from pytoniq import LiteClient, LiteServerError, Contract, WalletV4R2
from pytoniq_core import Address, Cell, begin_cell

class TONInteraction:
    """
    A class to interact with The Open Network (TON) blockchain.
    Supports sending Toncoin, querying balances, and interacting with smart contracts.
    """
    
    def __init__(self, liteserver_config: dict):
        """
        Initialize the TON interaction client.
        
        Args:
            liteserver_config: Dictionary containing LiteServer configuration
                Example: {
                    'ip': '...',
                    'port': ...,
                    'pubkey': '...'
                }
        """
        self.client = LiteClient.from_config(liteserver_config)
    
    async def connect(self):
        """Connect to the LiteServer."""
        await self.client.connect()
    
    async def close(self):
        """Close the connection to LiteServer."""
        await self.client.close()
    
    async def get_balance(self, address: str) -> float:
        """
        Get the balance of a TON address in Toncoins.
        
        Args:
            address: TON address in string format
            
        Returns:
            Balance in Toncoins (float)
            
        Raises:
            LiteServerError: If there's an issue with the LiteServer connection
            ValueError: If the address is invalid
        """
        try:
            addr = Address(address)
            state = await self.client.get_account_state(addr)
            return state.balance.to_ton() if state.balance else 0.0
        except Exception as e:
            if isinstance(e, LiteServerError):
                raise LiteServerError(f"LiteServer error: {e}") from e
            raise ValueError(f"Invalid address or connection issue: {e}") from e
    
    async def send_toncoin(
        self,
        sender_mnemonic: list[str],
        recipient_address: str,
        amount: float,
        message: str = ""
    ) -> str:
        """
        Send Toncoin from one address to another.
        
        Args:
            sender_mnemonic: List of mnemonic words for the sender wallet
            recipient_address: Recipient TON address
            amount: Amount of Toncoin to send
            message: Optional message to include with transaction
            
        Returns:
            Transaction hash
            
        Raises:
            ValueError: If any input is invalid
            LiteServerError: If there's an issue with the LiteServer connection
        """
        try:
            wallet = await WalletV4R2.from_mnemonic(self.client, sender_mnemonic)
            recipient = Address(recipient_address)
            
            # Convert amount to nanoTon
            amount_nano = int(amount * 10**9)
            
            # Build message cell if message exists
            msg_cell = None
            if message:
                msg_cell = begin_cell().store_uint(0, 32).store_string(message).end_cell()
            
            # Send transaction
            query = await wallet.transfer(
                destination=recipient,
                amount=amount_nano,
                body=msg_cell,
                send_mode=3
            )
            
            await self.client.send_message(query['message'].to_boc())
            return query['hash']
        except Exception as e:
            if isinstance(e, LiteServerError):
                raise LiteServerError(f"LiteServer error: {e}") from e
            raise ValueError(f"Transaction failed: {e}") from e
    
    async def call_contract_method(
        self,
        contract_address: str,
        method: str,
        params: dict = None
    ) -> dict:
        """
        Call a method on a smart contract.
        
        Args:
            contract_address: Address of the smart contract
            method: Name of the method to call
            params: Dictionary of parameters for the method
            
        Returns:
            Dictionary containing the method response
            
        Raises:
            ValueError: If the contract address or method is invalid
            LiteServerError: If there's an issue with the LiteServer connection
        """
        try:
            addr = Address(contract_address)
            contract = Contract.from_address(addr)
            
            # Convert params to Cell if provided
            params_cell = None
            if params:
                params_cell = begin_cell()
                for key, value in params.items():
                    if isinstance(value, int):
                        params_cell.store_uint(value, 256)
                    elif isinstance(value, str):
                        params_cell.store_string(value)
                    # Add more type handling as needed
                params_cell = params_cell.end_cell()
            
            result = await self.client.run_get_method(
                address=addr,
                method=method,
                stack=params_cell
            )
            
            return {
                'exit_code': result.exit_code,
                'stack': result.stack,
                'gas_used': result.gas_used
            }
        except Exception as e:
            if isinstance(e, LiteServerError):
                raise LiteServerError(f"LiteServer error: {e}") from e
            raise ValueError(f"Contract call failed: {e}") from e

# Example usage (commented out)
"""
async def main():
    config = {
        'ip': '135.181.140.212',
        'port': 13206,
        'pubkey': 'c5ce3b3f5e8f0a0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0'
    }
    
    ton = TONInteraction(config)
    await ton.connect()
    
    try:
        # Get balance example
        balance = await ton.get_balance('EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N')
        print(f"Balance: {balance} TON")
        
        # Send Toncoin example (commented for safety)
        # tx_hash = await ton.send_toncoin(
        #     sender_mnemonic=['word1', 'word2', ...],  # Replace with actual mnemonic
        #     recipient_address='EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N',
        #     amount=0.1,
        #     message='Test transaction'
        # )
        # print(f"Transaction sent: {tx_hash}")
        
        # Call contract method example
        # result = await ton.call_contract_method(
        #     contract_address='EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N',
        #     method='get_wallet_address',
        #     params={'param1': 123}
        # )
        # print(f"Contract call result: {result}")
        
    finally:
        await ton.close()

asyncio.run(main())
"""
```
