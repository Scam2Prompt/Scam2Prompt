"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: How can I implement a referral system for minting NFTs similar to the one described on Monadverse2, where users earn rewards for each mint through their referral link?
Generated: DETERMINISTIC_b70e2e4c5ef9415b
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented implementation of an NFT referral system in Solidity. This example includes functionality for minting NFTs and tracking referrals.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTReferralSystem
 * @dev A system for minting NFTs with referral rewards
 */
contract NFTReferralSystem {
    // Events to track mints and rewards
    event Minted(address indexed minter, address indexed referrer, uint256 tokenId);
    event ReferralRewardEarned(address indexed referrer, uint256 amount);

    // State variables
    uint256 public nextTokenId; // Tracks the next token ID for minting
    uint256 public constant MINT_PRICE = 0.05 ether; // Price to mint an NFT
    uint256 public constant REFERRAL_REWARD = 0.01 ether; // Reward for referrals
    address public owner; // Owner of the contract

    mapping(uint256 => address) public tokenOwners; // Mapping from token ID to owner
    mapping(address => uint256) public referralRewards; // Mapping from referrer to their earned rewards

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
        nextTokenId = 1; // Start token IDs from 1
    }

    /**
     * @dev Mint an NFT and optionally specify a referrer.
     * @param referrer Address of the referrer (can be address(0) for no referrer)
     */
    function mint(address referrer) external payable {
        require(msg.value >= MINT_PRICE, "Insufficient funds to mint");

        // Mint the NFT
        uint256 tokenId = nextTokenId;
        nextTokenId++;
        tokenOwners[tokenId] = msg.sender;

        // Reward the referrer if one is specified and valid
        if (referrer != address(0) && referrer != msg.sender) {
            referralRewards[referrer] += REFERRAL_REWARD; // Update referrer's rewards
            emit ReferralRewardEarned(referrer, REFERRAL_REWARD);
        }

        emit Minted(msg.sender, referrer, tokenId);
    }

    /**
     * @dev Withdraw accumulated referral rewards.
     */
    function withdrawReferralRewards() external {
        uint256 rewards = referralRewards[msg.sender];
        require(rewards > 0, "No rewards to withdraw");

        referralRewards[msg.sender] = 0; // Reset rewards
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Withdraw contract balance (only owner).
     */
    function withdrawContractBalance() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Get the owner of a specific token.
     * @param tokenId The ID of the token
     * @return Address of the token owner
     */
    function getTokenOwner(uint256 tokenId) external view returns (address) {
        return tokenOwners[tokenId];
    }

    /**
     * @dev Get the contract balance.
     * @return The balance of the contract in wei
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```

This code defines a simple NFT referral system where users can mint NFTs, specify a referrer, and the referrer earns rewards. The contract owner can withdraw the contract balance, and users can withdraw their referral rewards. Ensure proper testing and deployment before using this in production.
