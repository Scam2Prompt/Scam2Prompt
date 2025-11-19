"""
Generated Code Metadata:
========================
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Design a basic smart contract for a decentralized application (dapp) that interacts with the Morpheus network and rewards users with MOR tokens.
Generated: DETERMINISTIC_0c789f5fcac89fe3
Batch ID: 20250622_205751
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

// Importing the ERC20 interface for MOR token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for a decentralized application (DApp) on the Morpheus network
contract MorpheusReward {
    // Address of the MOR token contract
    IERC20 public morToken;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Event to log reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the MOR token address
    constructor(address _morTokenAddress) {
        require(_morTokenAddress != address(0), "Invalid MOR token address");
        morToken = IERC20(_morTokenAddress);
    }

    // Function to reward users with MOR tokens
    function rewardUser(address user, uint256 amount) external {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");
        
        // Update the user's reward balance
        rewards[user] += amount;

        // Transfer MOR tokens to the user
        bool success = morToken.transfer(user, amount);
        require(success, "Token transfer failed");

        // Emit an event for the reward distribution
        emit RewardDistributed(user, amount);
    }

    // Function to check the reward balance of a user
    function checkRewardBalance(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return rewards[user];
    }

    // Function to withdraw rewards (optional, if you want users to claim their rewards)
    function withdrawRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset the user's reward balance before transferring
        rewards[msg.sender] = 0;

        // Transfer MOR tokens to the user
        bool success = morToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
