"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdappsconnectprotocol.pages.dev
Prompt: Provide an example of using the "CLAIM REWARD CHOOSE" functionality in a smart contract for distributing rewards to cryptocurrency wallet users.
Generated: DETERMINISTIC_3ea31dfcc62ec790
Batch ID: 20250612_150440
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

contract RewardDistributor {
    // Using a mapping to track rewards for each user
    mapping(address => uint256) private rewards;
    
    // Event to notify when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Function to add rewards for a user
    // Only the contract owner can distribute rewards
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        rewards[user] += amount;
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance to prevent re-entrancy attacks
        rewards[msg.sender] = 0;

        // Transfer the reward amount to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to check the rewards balance of a user
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    // Modifier to restrict access to only the owner of the contract
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Owner address
    address private owner;

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to withdraw leftover funds to the owner
    function withdraw() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
}
```
