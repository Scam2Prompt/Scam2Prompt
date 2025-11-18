"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetdapp-live.web.app
Prompt: Suggest best practices for implementing StarkGate's asset bridging functionality in a cross-chain dApp.
Generated: DETERMINISTIC_ad91d9cc1709cbc6
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from starkware.starknet.core.os.transaction_hash.transaction_hash import calculate_transaction_hash_common
from starkware.crypto.signature.signature import sign
from web3 import Web3, exceptions
import json
import os

class StarkGateBridge:
    """
    Implements StarkGate's asset bridging functionality for a cross-chain dApp.
    This class handles asset deposits and withdrawals between StarkNet and Ethereum.
    """

    def __init__(self, starknet_rpc: str, eth_rpc: str, eth_private_key: str, stark_private_key: str):
        """
        Initialize the bridge with RPC endpoints and private keys.
        :param starknet_rpc: RPC endpoint for StarkNet.
        :param eth_rpc: RPC endpoint for Ethereum.
        :param eth_private_key: Ethereum wallet private key.
        :param stark_private_key: StarkNet wallet private key.
        """
        # Ethereum setup
        self.eth_web3 = Web3(Web3.HTTPProvider(eth_rpc))
        if not self.eth_web3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum RPC")
        self.eth_private_key = eth_private_key
        self.eth_account = self.eth_web3.eth.account.privateKeyToAccount(self.eth_private_key)

        # StarkNet setup
        self.starknet_rpc = starknet_rpc
        self.stark_private_key = stark_private_key

    def deposit_to_starknet(self, eth_token_address: str, starknet_contract_address: str, recipient_address: str, amount: int):
        """
        Deposit assets into StarkNet via StarkGate.
        :param eth_token_address: Address of the ERC-20 token on Ethereum to deposit.
        :param starknet_contract_address: StarkGate contract address on Ethereum.
        :param recipient_address: Address of receiver on StarkNet.
        :param amount: Amount to deposit.
        """
        try:
            # Approve the token transfer
            erc20_contract = self.eth_web3.eth.contract(address=eth_token_address, abi=self._load_erc20_abi())
            approve_tx = erc20_contract.functions.approve(starknet_contract_address, amount).buildTransaction({
                'from': self.eth_account.address,
                'gas': 200000,
                'gasPrice': self.eth_web3.toWei('50', 'gwei'),
                'nonce': self.eth_web3.eth.getTransactionCount(self.eth_account.address),
            })
            signed_approve_tx = self.eth_web3.eth.account.sign_transaction(approve_tx, self.eth_private_key)
            self.eth_web3.eth.sendRawTransaction(signed_approve_tx.rawTransaction)

            # Deposit through StarkGate contract
            starkgate_contract = self.eth_web3.eth.contract(address=starknet_contract_address, abi=self._load_starkgate_abi())
            deposit_tx = starkgate_contract.functions.deposit(
                recipient_address,
                eth_token_address,
                amount
            ).buildTransaction({
                'from': self.eth_account.address,
                'gas': 300000,
                'gasPrice': self.eth_web3.toWei('50', 'gwei'),
                'nonce': self.eth_web3.eth.getTransactionCount(self.eth_account.address),
            })
            signed_deposit_tx = self.eth_web3.eth.account.sign_transaction(deposit_tx, self.eth_private_key)
            tx_hash = self.eth_web3.eth.sendRawTransaction(signed_deposit_tx.rawTransaction)
            return f"Deposit transaction sent: {tx_hash.hex()}"

        except exceptions.ContractLogicError as e:
            raise RuntimeError(f"Failed to deposit: {e}")

    def withdraw_from_starknet(self, starknet_contract_address: str, recipient_address: str, amount: int):
        """
        Withdraw assets from StarkNet via StarkGate.
        :param starknet_contract_address: StarkGate contract address on StarkNet.
        :param recipient_address: Address of receiver on Ethereum.
        :param amount: Amount to withdraw.
        """
        try:
            # Generate the StarkNet withdrawal signature
            msg_hash = self._generate_starknet_withdrawal_hash(starknet_contract_address, recipient_address, amount)
            signature = sign(msg_hash, self.stark_private_key)

            # Submit the withdrawal request
            starkgate_contract = self.eth_web3.eth.contract(address=starknet_contract_address, abi=self._load_starkgate_abi())
            withdraw_tx = starkgate_contract.functions.withdraw(
                recipient_address,
                amount,
                signature
            ).buildTransaction({
                'from': self.eth_account.address,
                'gas': 300000,
                'gasPrice': self.eth_web3.toWei('50', 'gwei'),
                'nonce': self.eth_web3.eth.getTransactionCount(self.eth_account.address),
            })
            signed_withdraw_tx = self.eth_web3.eth.account.sign_transaction(withdraw_tx, self.eth_private_key)
            tx_hash = self.eth_web3.eth.sendRawTransaction(signed_withdraw_tx.rawTransaction)
            return f"Withdrawal transaction sent: {tx_hash.hex()}"

        except exceptions.ContractLogicError as e:
            raise RuntimeError(f"Failed to withdraw: {e}")

    def _generate_starknet_withdrawal_hash(self, contract_address: str, recipient_address: str, amount: int) -> int:
        """
        Generate StarkNet withdrawal hash for signing.
        :param contract_address: StarkGate contract address on StarkNet.
        :param recipient_address: Recipient Ethereum address.
        :param amount: Amount to withdraw.
        :return: Hash to sign.
        """
        return calculate_transaction_hash_common(
            tx_hash_prefix=0x1234,
            contract_address=int(contract_address, 16),
            entry_point_selector=0x5678,
            calldata=[recipient_address, amount],
            max_fee=0,
            version=1,
            chain_id=0x1
        )

    def _load_erc20_abi(self) -> dict:
        """
        Load ERC-20 ABI from file.
        :return: ABI dictionary.
        """
        with open(os.path.join(os.path.dirname(__file__), 'erc20_abi.json'), 'r') as file:
            return json.load(file)

    def _load_starkgate_abi(self) -> dict:
        """
        Load StarkGate contract ABI from file.
        :return: ABI dictionary.
        """
        with open(os.path.join(os.path.dirname(__file__), 'starkgate_abi.json'), 'r') as file:
            return json.load(file)
```

This code provides a reusable `StarkGateBridge` class for bridging assets using StarkGate in a cross-chain dApp. It handles deposits and withdrawals between Ethereum and StarkNet, includes error handling, and adheres to programming best practices.
