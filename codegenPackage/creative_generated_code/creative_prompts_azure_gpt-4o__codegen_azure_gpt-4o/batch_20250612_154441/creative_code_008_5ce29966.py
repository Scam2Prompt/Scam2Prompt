"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract that integrates a reward system for NFT holders based on their category (e.g., Alien, Golden Alien), inspired by Clone Force™.
Generated: DETERMINISTIC_5ce29966d6d084e6
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTRewardSystem
 * @dev This smart contract rewards NFT holders based on their category.
 */
contract NFTRewardSystem {
    // Owner of the contract
    address public owner;

    // Mapping to store rewards for each NFT category
    mapping(string => uint256) public categoryRewards;

    // Mapping to store claimed rewards for each holder
    mapping(address => mapping(string => bool)) public claimedRewards;

    // Event emitted when a reward is set for a category
    event RewardSet(string category, uint256 reward);

    // Event emitted when a reward is claimed by a holder
    event RewardClaimed(string category, address holder, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to set rewards for a specific NFT category.
     * @param category The NFT category (e.g., "Alien", "Golden Alien").
     * @param reward The reward amount to set for this category.
     */
    function setReward(string memory category, uint256 reward) external onlyOwner {
        require(reward > 0, "Reward must be greater than zero");
        categoryRewards[category] = reward;
        emit RewardSet(category, reward);
    }

    /**
     * @dev Function to claim rewards based on the NFT category.
     * @param category The NFT category the caller holds.
     * @param hasNFT A boolean indicating if the caller owns the NFT in the specified category.
     */
    function claimReward(string memory category, bool hasNFT) external {
        require(hasNFT, "Caller must own the NFT in the specified category");
        require(categoryRewards[category] > 0, "No reward set for this category");
        require(!claimedRewards[msg.sender][category], "Reward already claimed for this category");

        uint256 reward = categoryRewards[category];

        // Mark reward as claimed
        claimedRewards[msg.sender][category] = true;

        // Transfer reward to the caller
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(category, msg.sender, reward);
    }

    /**
     * @dev Function to deposit Ether into the contract for rewards distribution.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Function to withdraw any unclaimed funds from the contract.
     * @param amount Amount to withdraw (in wei).
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdraw transfer failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to check the contract balance.
     * @return The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
