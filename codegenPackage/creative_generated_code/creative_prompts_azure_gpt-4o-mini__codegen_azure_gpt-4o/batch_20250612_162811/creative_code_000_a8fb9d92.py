"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: How can I implement a referral system for an NFT minting platform similar to Zora Air Spring that allows users to earn ETH for referrals?
Generated: DETERMINISTIC_a8fb9d929fb40c83
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title NFT Minting Referral System
 * @dev This contract allows users to mint NFTs and earn ETH through referrals.
 * Users can refer others, and referrers receive a reward when their referrals mint an NFT.
 */
contract NFTMintingReferral {
    // ========== State Variables ==========
    
    address public owner; // Owner of the contract
    uint256 public nftPrice; // Price to mint an NFT (in wei)
    uint256 public referralReward; // Reward for referrers (in wei)
    
    mapping(address => uint256) public balance; // Tracks user balances for withdrawals
    mapping(uint256 => address) public nftOwners; // Tracks owners of minted NFTs
    uint256 public nftCounter; // Tracks the total NFTs minted
    
    // ========== Events ==========
    
    event NFTMinted(address indexed minter, uint256 indexed tokenId, address indexed referrer);
    event RewardPaid(address indexed referrer, uint256 reward);
    event Withdrawal(address indexed user, uint256 amount);

    // ========== Modifiers ==========
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // ========== Constructor ==========
    
    constructor(uint256 _nftPrice, uint256 _referralReward) {
        owner = msg.sender;
        nftPrice = _nftPrice;
        referralReward = _referralReward;
    }

    // ========== Public Functions ==========
    
    /**
     * @dev Mint an NFT. Optionally provide a referrer address to earn rewards.
     * @param referrer Address of the referrer (optional).
     */
    function mintNFT(address referrer) external payable {
        // Ensure the correct NFT price is paid
        require(msg.value == nftPrice, "Incorrect ETH sent");
        
        // Increment NFT counter and assign ownership
        nftCounter++;
        nftOwners[nftCounter] = msg.sender;

        // Emit NFT minting event
        emit NFTMinted(msg.sender, nftCounter, referrer);

        // Handle referral rewards
        if (referrer != address(0) && referrer != msg.sender) {
            balance[referrer] += referralReward;
            emit RewardPaid(referrer, referralReward);
        }
    }
    
    /**
     * @dev Withdraw accumulated referral rewards.
     */
    function withdrawRewards() external {
        uint256 amount = balance[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset balance before transferring to prevent re-entrancy
        balance[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    // ========== Owner Functions ==========
    
    /**
     * @dev Update the price of minting an NFT.
     * @param _nftPrice New NFT price in wei.
     */
    function setNFTPrice(uint256 _nftPrice) external onlyOwner {
        nftPrice = _nftPrice;
    }

    /**
     * @dev Update the referral reward.
     * @param _referralReward New referral reward in wei.
     */
    function setReferralReward(uint256 _referralReward) external onlyOwner {
        referralReward = _referralReward;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    // ========== Fallback Functions ==========
    
    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {}
}
```
