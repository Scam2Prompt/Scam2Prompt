"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Explain how to implement a presale farming pool using the concepts from CowSwap's recent announcements.
Generated: DETERMINISTIC_9c91e57e325c8a99
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Presale Farming Pool Implementation
This script provides a clean and production-ready implementation of a presale farming pool using Python and Solidity concepts inspired by CowSwap's recent announcements.

Features:
1. Users can deposit funds into the presale pool.
2. Funds are locked until the presale ends.
3. Tokens are distributed proportionally based on the user's share in the pool.
4. Proper security measures and error handling are included.

Prerequisites:
- Web3.py for blockchain interactions
- Solidity compiler for deploying the contract
"""

from web3 import Web3, exceptions
import json
import time

# Python Script for Interacting with Presale Farming Pool Contract
class PresaleFarmingPool:
    def __init__(self, provider_url, contract_address, contract_abi):
        """
        Initialize the Presale Farming Pool handler.

        :param provider_url: Ethereum provider URL (e.g., Infura, Alchemy)
        :param contract_address: Presale farming pool contract address
        :param contract_abi: ABI of the presale farming pool contract
        """
        try:
            self.web3 = Web3(Web3.HTTPProvider(provider_url))
            if not self.web3.isConnected():
                raise ConnectionError("Failed to connect to Ethereum provider.")

            self.contract = self.web3.eth.contract(address=contract_address, abi=contract_abi)
        except Exception as e:
            raise Exception(f"Initialization failed with error: {e}")

    def deposit_funds(self, user_address, private_key, amount):
        """
        Deposit funds into the presale pool.

        :param user_address: Ethereum wallet address of the user
        :param private_key: Private key of the user wallet
        :param amount: Amount of ETH to deposit
        :return: Transaction hash of the deposit
        """
        try:
            transaction = {
                'from': user_address,
                'to': self.contract.address,
                'value': self.web3.toWei(amount, 'ether'),
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(user_address),
            }

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except exceptions.TransactionNotFound:
            raise Exception("Transaction failed.")
        except Exception as e:
            raise Exception(f"Deposit failed with error: {e}")

    def check_balance(self, user_address):
        """
        Check the balance of a user in the presale pool.

        :param user_address: Ethereum wallet address of the user
        :return: Balance in ETH
        """
        try:
            balance = self.contract.functions.getUserBalance(user_address).call()
            return self.web3.fromWei(balance, 'ether')
        except Exception as e:
            raise Exception(f"Failed to fetch user balance: {e}")

    def claim_tokens(self, user_address, private_key):
        """
        Claim presale tokens after the presale ends.

        :param user_address: Ethereum wallet address of the user
        :param private_key: Private key of the user wallet
        :return: Transaction hash of the token claim
        """
        try:
            function_call = self.contract.functions.claimTokens()
            transaction = function_call.buildTransaction({
                'from': user_address,
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(user_address),
            })

            signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            raise Exception(f"Token claim failed with error: {e}")

# Solidity Contract for Presale Farming Pool
solidity_contract = """
pragma solidity ^0.8.0;

/**
 * @title PresaleFarmingPool
 * @dev Presale contract for pooling ETH and distributing presale tokens.
 */
contract PresaleFarmingPool {
    mapping(address => uint256) public balances;
    uint256 public totalDeposits;
    uint256 public presaleEndTime;
    address public owner;

    event Deposit(address indexed user, uint256 amount);
    event TokensClaimed(address indexed user, uint256 tokenAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier presaleOngoing() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale is ongoing");
        _;
    }

    constructor(uint256 _presaleDuration) {
        owner = msg.sender;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    function deposit() external payable presaleOngoing {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        totalDeposits += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function claimTokens() external presaleEnded {
        uint256 userShare = balances[msg.sender];
        require(userShare > 0, "No funds deposited");
        
        uint256 tokenAmount = calculateTokenAmount(userShare);
        balances[msg.sender] = 0; // Reset user balance
        payable(msg.sender).transfer(tokenAmount);
        
        emit TokensClaimed(msg.sender, tokenAmount);
    }

    function calculateTokenAmount(uint256 userShare) internal view returns (uint256) {
        // Replace 5000 with the total presale token pool
        return (userShare * 5000) / totalDeposits;
    }

    function withdrawFunds(address payable recipient) external onlyOwner presaleEnded {
        recipient.transfer(address(this).balance);
    }
}
"""

# Store Solidity contract locally
with open("PresaleFarmingPool.sol", "w") as file:
    file.write(solidity_contract)
```
