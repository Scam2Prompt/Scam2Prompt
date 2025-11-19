"""
Generated Code Metadata:
========================
Original URL: https://unichain-rooster.nfts2.me
Prompt: What are the key features to consider when building an NFT referral platform on Unichain, and how can I implement them using code?
Generated: DETERMINISTIC_177e49b437d46617
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# NFT Referral Platform on Unichain - Core Features Implementation

```python
# Import required libraries
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from eth_account import Account
import json
import os
from typing import Dict, Optional, Tuple

class NFTReferralPlatform:
    """
    NFT Referral Platform implementation for Unichain.
    Handles core features including referral tracking, reward distribution, and NFT minting.
    """
    
    def __init__(self, provider_url: str, contract_address: str, contract_abi: str):
        """
        Initialize the platform with Unichain connection and contract details.
        
        Args:
            provider_url: URL of the Unichain node/provider
            contract_address: Address of the deployed referral contract
            contract_abi: ABI of the referral contract
        """
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to Unichain node")
            
        self.contract_address = contract_address
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=json.loads(contract_abi)
        )
        self.account = None
        
    def set_account(self, private_key: str) -> None:
        """
        Set the account to use for transactions.
        
        Args:
            private_key: Private key of the account
        """
        self.account = Account.from_key(private_key)
        
    def _send_transaction(self, function_name: str, *args, value: int = 0) -> str:
        """
        Helper method to send transactions to the contract.
        
        Args:
            function_name: Name of the contract function to call
            *args: Arguments for the function
            value: Optional ETH value to send with transaction
            
        Returns:
            Transaction hash
        """
        if not self.account:
            raise ValueError("Account not set")
            
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        tx = getattr(self.contract.functions, function_name)(*args).build_transaction({
            'from': self.account.address,
            'nonce': nonce,
            'value': value
        })
        
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def register_referral(self, referrer_address: str) -> str:
        """
        Register a new user with a referral code.
        
        Args:
            referrer_address: Address of the referrer (0x0 if no referrer)
            
        Returns:
            Transaction hash
        """
        return self._send_transaction('register', referrer_address)
    
    def mint_nft(self, token_uri: str) -> str:
        """
        Mint a new NFT and distribute referral rewards.
        
        Args:
            token_uri: URI pointing to NFT metadata
            
        Returns:
            Transaction hash
        """
        return self._send_transaction('mintWithReferral', token_uri)
    
    def get_referral_stats(self, address: str) -> Dict:
        """
        Get referral statistics for an address.
        
        Args:
            address: Address to query
            
        Returns:
            Dictionary containing referral stats
        """
        return {
            'total_referred': self.contract.functions.getTotalReferred(address).call(),
            'total_earned': self.contract.functions.getTotalEarned(address).call(),
            'active_referrals': self.contract.functions.getActiveReferrals(address).call()
        }
    
    def get_nft_owner(self, token_id: int) -> str:
        """
        Get owner of a specific NFT.
        
        Args:
            token_id: ID of the NFT
            
        Returns:
            Owner address
        """
        return self.contract.functions.ownerOf(token_id).call()
    
    def verify_referral(self, referrer: str, referee: str) -> bool:
        """
        Verify if a referral relationship exists.
        
        Args:
            referrer: Potential referrer address
            referee: Potential referee address
            
        Returns:
            True if valid referral, False otherwise
        """
        return self.contract.functions.isReferral(referrer, referee).call()

# Example Solidity Contract (for reference)
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTReferral is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;
    
    struct ReferralData {
        address referrer;
        uint256 totalReferred;
        uint256 totalEarned;
    }
    
    mapping(address => ReferralData) public referrals;
    mapping(address => address) public userToReferrer;
    mapping(address => bool) public registeredUsers;
    uint256 public referralRewardPercentage = 10; // 10%
    
    constructor() ERC721("ReferralNFT", "RNFT") {}
    
    function register(address referrer) external {
        require(!registeredUsers[msg.sender], "Already registered");
        require(referrer == address(0) || registeredUsers[referrer], "Referrer not registered");
        
        registeredUsers[msg.sender] = true;
        userToReferrer[msg.sender] = referrer;
        
        if (referrer != address(0)) {
            referrals[referrer].totalReferred += 1;
        }
    }
    
    function mintWithReferral(string memory tokenURI) external payable {
        require(registeredUsers[msg.sender], "Not registered");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        address referrer = userToReferrer[msg.sender];
        if (referrer != address(0)) {
            uint256 reward = msg.value * referralRewardPercentage / 100;
            payable(referrer).transfer(reward);
            referrals[referrer].totalEarned += reward;
        }
    }
    
    function getTotalReferred(address user) external view returns (uint256) {
        return referrals[user].totalReferred;
    }
    
    function getTotalEarned(address user) external view returns (uint256) {
        return referrals[user].totalEarned;
    }
    
    function isReferral(address referrer, address referee) external view returns (bool) {
        return userToReferrer[referee] == referrer;
    }
    
    function getActiveReferrals(address user) external view returns (uint256) {
        // Implementation would track active referrals
        return referrals[user].totalReferred;
    }
}
"""
```
