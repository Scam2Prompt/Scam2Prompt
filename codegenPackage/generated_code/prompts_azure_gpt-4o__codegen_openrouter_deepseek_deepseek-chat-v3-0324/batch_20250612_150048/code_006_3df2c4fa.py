"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-evista-software.com
Prompt: Write code to integrate a blockchain-based lending solution into a decentralized finance platform, inspired by Bitcoin Evista's inclusive investment channels.
Generated: DETERMINISTIC_3df2c4fad4e33ab0
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_lending.py

import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import logging
from eth_abi import encode_abi
from eth_utils import keccak, to_checksum_address

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class LoanTerms:
    principal: int
    interest_rate: int
    duration: int
    collateral_amount: int
    collateral_token: str
    borrower: str

@dataclass
class LoanApplication:
    loan_id: str
    terms: LoanTerms
    status: str
    created_at: int

class BlockchainLendingPlatform:
    """
    A decentralized lending platform that integrates with EVM-compatible blockchains.
    Inspired by Bitcoin Evista's inclusive investment channels.
    """
    
    def __init__(self, rpc_url: str, contract_address: str, contract_abi: str):
        """
        Initialize the lending platform with blockchain connection details.
        
        Args:
            rpc_url: URL of the Ethereum node RPC endpoint
            contract_address: Address of the lending smart contract
            contract_abi: ABI of the lending smart contract
        """
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        
        # Support for POA networks
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.contract_address = to_checksum_address(contract_address)
        self.contract_abi = json.loads(contract_abi)
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Verify connection
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to blockchain node")
        
        logger.info("Successfully connected to blockchain and initialized contract")

    def apply_for_loan(self, loan_terms: LoanTerms, private_key: str) -> str:
        """
        Submit a loan application to the blockchain.
        
        Args:
            loan_terms: Terms of the loan application
            private_key: Private key of the borrower for signing
            
        Returns:
            Transaction hash of the loan application
        """
        try:
            account = self.w3.eth.account.from_key(private_key)
            nonce = self.w3.eth.get_transaction_count(account.address)
            
            tx = self.contract.functions.applyForLoan(
                loan_terms.principal,
                loan_terms.interest_rate,
                loan_terms.duration,
                loan_terms.collateral_amount,
                loan_terms.collateral_token
            ).build_transaction({
                'from': account.address,
                'nonce': nonce,
                'gas': 500000,
                'gasPrice': self.w3.eth.gas_price
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Loan application submitted with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
        
        except Exception as e:
            logger.error(f"Error submitting loan application: {str(e)}")
            raise

    def fund_loan(self, loan_id: str, lender_private_key: str, amount: int) -> str:
        """
        Fund an existing loan application.
        
        Args:
            loan_id: ID of the loan to fund
            lender_private_key: Private key of the lender
            amount: Amount to fund (in wei)
            
        Returns:
            Transaction hash of the funding operation
        """
        try:
            account = self.w3.eth.account.from_key(lender_private_key)
            nonce = self.w3.eth.get_transaction_count(account.address)
            
            tx = self.contract.functions.fundLoan(loan_id).build_transaction({
                'from': account.address,
                'value': amount,
                'nonce': nonce,
                'gas': 500000,
                'gasPrice': self.w3.eth.gas_price
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, lender_private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Loan funded with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
        
        except Exception as e:
            logger.error(f"Error funding loan: {str(e)}")
            raise

    def repay_loan(self, loan_id: str, borrower_private_key: str, amount: int) -> str:
        """
        Repay a portion or all of an outstanding loan.
        
        Args:
            loan_id: ID of the loan to repay
            borrower_private_key: Private key of the borrower
            amount: Amount to repay (in wei)
            
        Returns:
            Transaction hash of the repayment
        """
        try:
            account = self.w3.eth.account.from_key(borrower_private_key)
            nonce = self.w3.eth.get_transaction_count(account.address)
            
            tx = self.contract.functions.repayLoan(loan_id, amount).build_transaction({
                'from': account.address,
                'nonce': nonce,
                'gas': 500000,
                'gasPrice': self.w3.eth.gas_price
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, borrower_private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Loan repayment submitted with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
        
        except Exception as e:
            logger.error(f"Error repaying loan: {str(e)}")
            raise

    def liquidate_collateral(self, loan_id: str, liquidator_private_key: str) -> str:
        """
        Liquidate collateral for a defaulted loan.
        
        Args:
            loan_id: ID of the loan to liquidate
            liquidator_private_key: Private key of the liquidator
            
        Returns:
            Transaction hash of the liquidation
        """
        try:
            account = self.w3.eth.account.from_key(liquidator_private_key)
            nonce = self.w3.eth.get_transaction_count(account.address)
            
            tx = self.contract.functions.liquidateCollateral(loan_id).build_transaction({
                'from': account.address,
                'nonce': nonce,
                'gas': 500000,
                'gasPrice': self.w3.eth.gas_price
            })
            
            signed_tx = self.w3.eth.account.sign_transaction(tx, liquidator_private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            logger.info(f"Collateral liquidation submitted with tx hash: {tx_hash.hex()}")
            return tx_hash.hex()
        
        except Exception as e:
            logger.error(f"Error liquidating collateral: {str(e)}")
            raise

    def get_loan_details(self, loan_id: str) -> Dict[str, Any]:
        """
        Retrieve details of a specific loan.
        
        Args:
            loan_id: ID of the loan to query
            
        Returns:
            Dictionary containing loan details
        """
        try:
            loan_data = self.contract.functions.getLoanDetails(loan_id).call()
            
            return {
                'loan_id': loan_id,
                'principal': loan_data[0],
                'interest_rate': loan_data[1],
                'duration': loan_data[2],
                'amount_repaid': loan_data[3],
                'collateral_amount': loan_data[4],
                'collateral_token': loan_data[5],
                'borrower': loan_data[6],
                'lender': loan_data[7],
                'status': loan_data[8],
                'created_at': loan_data[9],
                'due_date': loan_data[10]
            }
        
        except Exception as e:
            logger.error(f"Error fetching loan details: {str(e)}")
            raise

    def get_active_loans(self) -> List[Dict[str, Any]]:
        """
        Retrieve all active loans on the platform.
        
        Returns:
            List of dictionaries containing active loan details
        """
        try:
            loan_ids = self.contract.functions.getActiveLoanIds().call()
            return [self.get_loan_details(loan_id) for loan_id in loan_ids]
        
        except Exception as e:
            logger.error(f"Error fetching active loans: {str(e)}")
            raise

    def calculate_interest(self, principal: int, interest_rate: int, duration: int) -> int:
        """
        Calculate the total interest for a loan.
        
        Args:
            principal: Loan principal amount
            interest_rate: Annual interest rate (in basis points)
            duration: Loan duration in seconds
            
        Returns:
            Total
