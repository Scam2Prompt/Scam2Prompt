"""
Generated Code Metadata:
========================
Original URL: https://chaintether.web.app
Prompt: "Create an API library for interacting with a decentralized IDO launchpad that uses blockchain and DeFi principles for non-custodial transactions."
Generated: DETERMINISTIC_5c02c96817e11ea3
Batch ID: 20250622_205348
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
from typing import Optional, Dict, Any, List
from eth_account import Account
from eth_typing import ChecksumAddress

# Constants
DEFAULT_GAS_LIMIT = 200000
DEFAULT_GAS_PRICE = Web3.to_wei('50', 'gwei')

class IDOLaunchpadAPI:
    """
    A non-custodial API for interacting with decentralized IDO launchpads.
    Handles blockchain interactions, contract calls, and event listening.
    """
    
    def __init__(
        self,
        provider_url: str,
        contract_address: str,
        abi_path: str,
        chain_id: int
    ):
        """
        Initialize the IDO Launchpad API.
        
        Args:
            provider_url: URL of the blockchain node provider
            contract_address: Address of the IDO launchpad contract
            abi_path: Path to the contract ABI JSON file
            chain_id: Chain ID of the blockchain network
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to blockchain node")
        
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.chain_id = chain_id
        
        with open(abi_path) as f:
            abi = json.load(f)
        
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=abi
        )
    
    def _get_nonce(self, address: ChecksumAddress) -> int:
        """Get the current nonce for an address."""
        return self.web3.eth.get_transaction_count(address)
    
    def _sign_and_send_transaction(
        self,
        private_key: str,
        tx: Dict[str, Any]
    ) -> str:
        """
        Sign and send a transaction.
        
        Args:
            private_key: Private key of the sender
            tx: Transaction dictionary
            
        Returns:
            Transaction hash
        """
        account = Account.from_key(private_key)
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def _build_transaction(
        self,
        function_name: str,
        args: List[Any],
        value: int = 0,
        gas_limit: int = DEFAULT_GAS_LIMIT,
        gas_price: int = DEFAULT_GAS_PRICE,
        nonce: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Build a transaction dictionary.
        
        Args:
            function_name: Name of the contract function to call
            args: Arguments to pass to the function
            value: Amount of native token to send (in wei)
            gas_limit: Gas limit for the transaction
            gas_price: Gas price for the transaction
            nonce: Nonce for the transaction
            
        Returns:
            Transaction dictionary
        """
        if nonce is None:
            raise ValueError("Nonce must be provided")
        
        tx = {
            'chainId': self.chain_id,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
            'value': value
        }
        
        function = getattr(self.contract.functions, function_name)
        built_tx = function(*args).build_transaction(tx)
        return built_tx
    
    def participate_in_ido(
        self,
        private_key: str,
        project_id: int,
        amount: int
    ) -> str:
        """
        Participate in an IDO by contributing funds.
        
        Args:
            private_key: Private key of the participant
            project_id: ID of the IDO project
            amount: Amount of tokens to contribute (in wei)
            
        Returns:
            Transaction hash
        """
        sender_address = Account.from_key(private_key).address
        nonce = self._get_nonce(sender_address)
        
        try:
            tx = self._build_transaction(
                function_name="participate",
                args=[project_id, amount],
                value=amount,
                nonce=nonce
            )
            return self._sign_and_send_transaction(private_key, tx)
        except ContractLogicError as e:
            raise ValueError(f"Contract logic error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to participate in IDO: {e}") from e
    
    def claim_tokens(
        self,
        private_key: str,
        project_id: int
    ) -> str:
        """
        Claim tokens after IDO concludes.
        
        Args:
            private_key: Private key of the participant
            project_id: ID of the IDO project
            
        Returns:
            Transaction hash
        """
        sender_address = Account.from_key(private_key).address
        nonce = self._get_nonce(sender_address)
        
        try:
            tx = self._build_transaction(
                function_name="claimTokens",
                args=[project_id],
                nonce=nonce
            )
            return self._sign_and_send_transaction(private_key, tx)
        except ContractLogicError as e:
            raise ValueError(f"Contract logic error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to claim tokens: {e}") from e
    
    def get_project_details(
        self,
        project_id: int
    ) -> Dict[str, Any]:
        """
        Get details of an IDO project.
        
        Args:
            project_id: ID of the IDO project
            
        Returns:
            Dictionary containing project details
        """
        try:
            project = self.contract.functions.getProjectDetails(project_id).call()
            return {
                'id': project[0],
                'token_address': project[1],
                'token_price': project[2],
                'total_supply': project[3],
                'remaining_supply': project[4],
                'start_time': project[5],
                'end_time': project[6],
                'min_contribution': project[7],
                'max_contribution': project[8],
                'is_active': project[9]
            }
        except ContractLogicError as e:
            raise ValueError(f"Contract logic error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to get project details: {e}") from e
    
    def get_user_allocation(
        self,
        user_address: str,
        project_id: int
    ) -> Dict[str, Any]:
        """
        Get a user's allocation in an IDO project.
        
        Args:
            user_address: Address of the user
            project_id: ID of the IDO project
            
        Returns:
            Dictionary containing user allocation details
        """
        try:
            user_address = Web3.to_checksum_address(user_address)
            allocation = self.contract.functions.getUserAllocation(
                user_address,
                project_id
            ).call()
            return {
                'contribution_amount': allocation[0],
                'token_amount': allocation[1],
                'claimed': allocation[2]
            }
        except ContractLogicError as e:
            raise ValueError(f"Contract logic error: {e}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to get user allocation: {e}") from e
    
    def get_transaction_receipt(
        self,
        tx_hash: str
    ) -> Dict[str, Any]:
        """
        Get the receipt for a transaction.
        
        Args:
            tx_hash: Transaction hash
            
        Returns:
            Transaction receipt dictionary
        """
        try:
            receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            if receipt is None:
                raise TransactionNotFound(f"Transaction {tx_hash} not found")
            return dict(receipt)
        except Exception as e:
            raise RuntimeError(f"Failed to get transaction receipt: {e}") from e
    
    def listen_for_events(
        self,
        event_name: str,
        from_block: int = 0,
        to_block: str = 'latest',
        filter_args: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """
        Listen for contract events.
        
        Args:
            event_name: Name of the event to listen for
            from_block: Starting block number
            to_block: Ending block number or 'latest'
            filter_args: Dictionary of filter arguments
            
        Returns:
            List of event logs
        """
        try:
            event = getattr(self.contract.events, event_name)
            event_filter = event.create_filter(
                fromBlock=from_block,
                toBlock=to_block,
                argument_filters=filter_args or {}
            )
            logs = event_filter.get_all_entries()
            return [dict(log) for log in logs]
        except Exception as e:
            raise RuntimeError(f"Failed to listen for events: {e}") from e
```
