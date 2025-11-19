"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: "Write a Python script to interact with the FlokiFi Locker protocol for securing digital assets, including functions to lock LP tokens, NFTs, and fungible tokens."
Generated: DETERMINISTIC_c0b6cfb0f15f8dc7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from typing import Optional, Dict, Any, Union

# Configuration class for FlokiFi Locker settings
class FlokiFiLockerConfig:
    """
    Configuration for interacting with the FlokiFi Locker protocol.
    """
    def __init__(
        self,
        rpc_url: str,
        locker_contract_address: str,
        erc20_abi_path: str = "erc20_abi.json",
        erc721_abi_path: str = "erc721_abi.json",
        locker_abi_path: str = "flokifi_locker_abi.json",
        gas_limit: int = 200000,
        gas_price: Optional[int] = None,
    ):
        self.rpc_url = rpc_url
        self.locker_contract_address = locker_contract_address
        self.erc20_abi_path = erc20_abi_path
        self.erc721_abi_path = erc721_abi_path
        self.locker_abi_path = locker_abi_path
        self.gas_limit = gas_limit
        self.gas_price = gas_price

# Main FlokiFi Locker interaction class
class FlokiFiLocker:
    """
    A class to interact with the FlokiFi Locker protocol for securing digital assets.
    Supports locking LP tokens, NFTs, and fungible tokens.
    """
    
    def __init__(self, config: FlokiFiLockerConfig):
        self.config = config
        self.web3 = Web3(Web3.HTTPProvider(config.rpc_url))
        
        # Load contract ABIs
        with open(config.erc20_abi_path) as f:
            self.erc20_abi = json.load(f)
        
        with open(config.erc721_abi_path) as f:
            self.erc721_abi = json.load(f)
        
        with open(config.locker_abi_path) as f:
            self.locker_abi = json.load(f)
        
        # Initialize contracts
        self.locker_contract = self.web3.eth.contract(
            address=Web3.to_checksum_address(config.locker_contract_address),
            abi=self.locker_abi
        )
    
    def _get_token_contract(self, token_address: str, is_erc721: bool = False):
        """
        Internal method to get token contract instance.
        """
        abi = self.erc721_abi if is_erc721 else self.erc20_abi
        return self.web3.eth.contract(
            address=Web3.to_checksum_address(token_address),
            abi=abi
        )
    
    def _send_transaction(self, private_key: str, tx_function) -> str:
        """
        Internal method to send a transaction and return the tx hash.
        """
        account = self.web3.eth.account.from_key(private_key)
        nonce = self.web3.eth.get_transaction_count(account.address)
        
        tx_params = {
            'from': account.address,
            'nonce': nonce,
            'gas': self.config.gas_limit,
        }
        
        if self.config.gas_price:
            tx_params['gasPrice'] = self.config.gas_price
        
        try:
            tx = tx_function.build_transaction(tx_params)
            signed_tx = account.sign_transaction(tx)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except ContractLogicError as e:
            raise Exception(f"Contract logic error: {str(e)}")
        except Exception as e:
            raise Exception(f"Transaction failed: {str(e)}")
    
    def check_allowance(
        self,
        token_address: str,
        owner_address: str,
        is_erc721: bool = False
    ) -> int:
        """
        Check the allowance/spending approval for a token.
        """
        token_contract = self._get_token_contract(token_address, is_erc721)
        
        if is_erc721:
            # For ERC721, check if approved for all
            is_approved = token_contract.functions.isApprovedForAll(
                Web3.to_checksum_address(owner_address),
                Web3.to_checksum_address(self.config.locker_contract_address)
            ).call()
            return 1 if is_approved else 0
        else:
            # For ERC20, check allowance
            return token_contract.functions.allowance(
                Web3.to_checksum_address(owner_address),
                Web3.to_checksum_address(self.config.locker_contract_address)
            ).call()
    
    def approve_token(
        self,
        private_key: str,
        token_address: str,
        amount: Optional[int] = None,
        is_erc721: bool = False
    ) -> str:
        """
        Approve the locker contract to spend tokens on behalf of the user.
        """
        account = self.web3.eth.account.from_key(private_key)
        token_contract = self._get_token_contract(token_address, is_erc721)
        
        if is_erc721:
            # For ERC721, set approval for all
            tx_function = token_contract.functions.setApprovalForAll(
                Web3.to_checksum_address(self.config.locker_contract_address),
                True
            )
        else:
            # For ERC20, approve specific amount
            if amount is None:
                raise ValueError("Amount must be specified for ERC20 tokens")
            
            tx_function = token_contract.functions.approve(
                Web3.to_checksum_address(self.config.locker_contract_address),
                amount
            )
        
        return self._send_transaction(private_key, tx_function)
    
    def lock_lp_token(
        self,
        private_key: str,
        lp_token_address: str,
        amount: int,
        unlock_date: int,
        fee_in_eth: bool = True
    ) -> str:
        """
        Lock LP tokens in the FlokiFi Locker.
        """
        # First check if we have approval
        account = self.web3.eth.account.from_key(private_key)
        allowance = self.check_allowance(lp_token_address, account.address)
        
        if allowance < amount:
            raise Exception(f"Insufficient allowance. Current allowance: {allowance}, required: {amount}")
        
        tx_function = self.locker_contract.functions.lockLPToken(
            Web3.to_checksum_address(lp_token_address),
            amount,
            unlock_date,
            fee_in_eth
        )
        
        return self._send_transaction(private_key, tx_function)
    
    def lock_token(
        self,
        private_key: str,
        token_address: str,
        amount: int,
        unlock_date: int,
        fee_in_eth: bool = True
    ) -> str:
        """
        Lock fungible tokens in the FlokiFi Locker.
        """
        # First check if we have approval
        account = self.web3.eth.account.from_key(private_key)
        allowance = self.check_allowance(token_address, account.address)
        
        if allowance < amount:
            raise Exception(f"Insufficient allowance. Current allowance: {allowance}, required: {amount}")
        
        tx_function = self.locker_contract.functions.lockToken(
            Web3.to_checksum_address(token_address),
            amount,
            unlock_date,
            fee_in_eth
        )
        
        return self._send_transaction(private_key, tx_function)
    
    def lock_nft(
        self,
        private_key: str,
        nft_address: str,
        token_id: int,
        unlock_date: int,
        fee_in_eth: bool = True
    ) -> str:
        """
        Lock an NFT in the FlokiFi Locker.
        """
        # First check if we have approval
        account = self.web3.eth.account.from_key(private_key)
        allowance = self.check_allowance(nft_address, account.address, is_erc721=True)
        
        if allowance == 0:
            raise Exception("NFT not approved for transfer")
        
        tx_function = self.locker_contract.functions.lockNFT(
            Web3.to_checksum_address(nft_address),
            token_id,
            unlock_date,
            fee_in_eth
        )
        
        return self._send_transaction(private_key, tx_function)
    
    def get_locked_assets(
        self,
        owner_address: str,
        asset_type: str = "all"
    ) -> Dict[str, Any]:
        """
        Get locked assets for a specific owner.
        asset_type can be "lp", "token", "nft", or "all"
        """
        owner_address = Web3.to_checksum_address(owner_address)
        result = {
            "lp_tokens": [],
            "tokens": [],
            "nfts": []
        }
        
        if asset_type in ["all", "lp"]:
            # Get locked LP tokens
            lp_token_count = self.locker_contract.functions.lpLockCountForUser(owner_address).call()
            for i in range(lp_token_count):
                lock_id = self.locker_contract.functions.lpLockIdsForUser(owner_address, i).call()
                lock_data = self
