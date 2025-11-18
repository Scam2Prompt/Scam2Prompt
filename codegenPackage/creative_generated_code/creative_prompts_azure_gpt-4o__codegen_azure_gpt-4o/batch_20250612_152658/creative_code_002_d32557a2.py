"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-sophon.com
Prompt: Generate a smart contract example for deploying a loyalty program on the Sophon Chain that rewards users with SOPH tokens based on engagement metrics.
Generated: DETERMINISTIC_d32557a220492bba
Batch ID: 20250612_152658
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
 * @title LoyaltyProgram
 * @dev A smart contract for a loyalty program deployed on the Sophon Chain.
 * Users are rewarded with SOPH tokens based on their engagement metrics.
 */
contract LoyaltyProgram {
    
    // Address of the SOPH token contract
    address public tokenAddress;
    
    // Owner of the contract
    address public owner;

    // Mapping of user addresses to their engagement points
    mapping(address => uint256) public engagementPoints;

    // Event for logging reward distribution
    event RewardDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress The address of the SOPH token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to update engagement points for a user.
     * @param user The address of the user.
     * @param points The number of engagement points to add.
     */
    function updateEngagementPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than 0");
        engagementPoints[user] += points;
    }

    /**
     * @dev Function to calculate and reward a user with SOPH tokens based on engagement points.
     * @param user The address of the user to reward.
     * @param rewardRate The reward rate (conversion from points to SOPH tokens).
     */
    function rewardUser(address user, uint256 rewardRate) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardRate > 0, "Reward rate must be greater than 0");
        uint256 userPoints = engagementPoints[user];
        require(userPoints > 0, "User has no engagement points");

        uint256 rewardAmount = userPoints * rewardRate;
        engagementPoints[user] = 0; // Reset points after rewarding

        // Transfer SOPH tokens to the user
        require(ERC20(tokenAddress).transfer(user, rewardAmount), "Token transfer failed");

        emit RewardDistributed(user, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to the contract.
     * @param token The address of the token contract.
     * @param amount The amount to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        require(ERC20(token).transfer(owner, amount), "Token transfer failed");
    }
}

// Minimal ERC20 interface
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
