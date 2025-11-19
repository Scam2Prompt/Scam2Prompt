"""
Generated Code Metadata:
========================
Original URL: https://tonbox.top
Prompt: Generate a smart contract code in Solidity to manage the claiming and distribution of rewards for NFT owners, specifically for the "TONLUCKY NFT" project.
Generated: DETERMINISTIC_6e200715f8378327
Batch ID: 20250622_204846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TONLUCKY NFT Rewards Distribution Contract
 * @dev This contract manages the claiming and distribution of rewards for TONLUCKY NFT owners.
 */
contract TONLUCKYRewards {
    // Address of the contract owner
    address public owner;

    // Mapping to store rewards for each NFT ID
    mapping(uint256 => uint256) public rewards;

    // Mapping to track claimed rewards for each NFT ID
    mapping(uint256 => bool) public claimed;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 indexed nftId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(uint256 indexed nftId, address indexed claimer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure rewards are not already claimed
    modifier notClaimed(uint256 nftId) {
        require(!claimed[nftId], "Rewards already claimed for this NFT");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to a specific NFT ID.
     * @param nftId The ID of the NFT to distribute rewards to.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(uint256 nftId, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than zero");
        rewards[nftId] = amount;
        emit RewardsDistributed(nftId, amount);
    }

    /**
     * @dev Function for NFT owners to claim their rewards.
     * @param nftId The ID of the NFT to claim rewards for.
     */
    function claimRewards(uint256 nftId) external notClaimed(nftId) {
        uint256 rewardAmount = rewards[nftId];
        require(rewardAmount > 0, "No rewards available for this NFT");

        // Mark rewards as claimed
        claimed[nftId] = true;

        // Transfer rewards to the caller
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(nftId, msg.sender, rewardAmount);
    }

    /**
     * @dev Function to deposit Ether into the contract for rewards distribution.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Function to withdraw any remaining Ether from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract's current balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
