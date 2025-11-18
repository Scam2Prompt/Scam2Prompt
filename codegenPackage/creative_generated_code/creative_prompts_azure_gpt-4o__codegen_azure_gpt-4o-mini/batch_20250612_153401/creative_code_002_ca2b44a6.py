"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playgorund.pages.dev
Prompt: Generate a smart contract in Solidity for distributing $BEYOND rewards based on contribution levels, as described in the Beyond Blitz rewards system.
Generated: DETERMINISTIC_ca2b44a6a51d2ddd
Batch ID: 20250612_153401
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

/// @title Beyond Blitz Rewards System
/// @notice This smart contract distributes $BEYOND rewards based on user contribution levels.
contract BeyondBlitzRewards {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);
    
    // Mapping to store user contributions
    mapping(address => uint256) public contributions;
    
    // Mapping to store user rewards
    mapping(address => uint256) public rewards;

    // Total reward pool
    uint256 public totalRewards;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /// @dev Constructor to initialize contract with total rewards
    /// @param _totalRewards Total amount of $BEYOND rewards available for distribution
    constructor(uint256 _totalRewards) {
        require(_totalRewards > 0, "Total rewards must be greater than zero");
        totalRewards = _totalRewards;
        owner = msg.sender;
    }

    /// @dev Function to contribute to the rewards system
    /// @param amount Amount contributed by the user
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than zero");
        contributions[msg.sender] += amount;
    }

    /// @dev Function to distribute rewards based on contributions
    function distributeRewards() external onlyOwner {
        // Calculate total contributions
        uint256 totalContributions = getTotalContributions();

        // Check if there are contributions
        require(totalContributions > 0, "No contributions to distribute rewards");

        // Distribute rewards proportionally to contributions
        for (address user : getContributors()) {
            uint256 userContribution = contributions[user];
            uint256 rewardAmount = (userContribution * totalRewards) / totalContributions;
            if (rewardAmount > 0) {
                rewards[user] += rewardAmount;
                emit RewardsDistributed(user, rewardAmount);
            }
        }

        // Reset total rewards after distribution
        totalRewards = 0; 
    }

    /// @dev Function to withdraw rewards by the user
    function withdrawRewards() external {
        uint256 userRewards = rewards[msg.sender];
        require(userRewards > 0, "No rewards to withdraw");

        // Reset user's rewards before transfer to prevent reentrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to user
        // This should be replaced with actual $BEYOND token transfer logic
        // Use ERC20 token transfer code here

        // Example: token.transfer(msg.sender, userRewards);
    }

    /// @dev Internal function to calculate total contributions
    /// @return total Total contributions made by users
    function getTotalContributions() internal view returns (uint256 total) {
        // This function will iterate through contributors to calculate total contributions
        // You'll need a list of users to iterate through, which may require a separate structure
        // For simplicity, this is omitted in the current implementation.
        // Implement this according to your specific requirements and data structures.
    }

    /// @dev Internal function to get list of contributors
    /// @return contributors Array of addresses of contributors
    function getContributors() internal view returns (address[] memory contributors) {
        // This function should return a list of contributors
        // Implement this according to your specific requirements and data structures.
    }
}
```
