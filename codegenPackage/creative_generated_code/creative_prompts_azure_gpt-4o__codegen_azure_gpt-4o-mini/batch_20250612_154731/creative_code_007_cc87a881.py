"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Write a Solidity contract that allows users to earn GHST tokens as rewards for competitive gaming events.
Generated: DETERMINISTIC_cc87a881bd2c53c0
Batch ID: 20250612_154731
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

// Importing the ERC20 interface to interact with the GHST token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract allows users to earn GHST tokens for participating in competitive gaming events
contract GamingRewards is Ownable {
    // Token instance for GHST
    IERC20 public ghstToken;

    // Mapping to track rewards for each user
    mapping(address => uint256) public rewards;

    // Events
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the GHST token address
    constructor(address _ghstTokenAddress) {
        require(_ghstTokenAddress != address(0), "Invalid token address");
        ghstToken = IERC20(_ghstTokenAddress);
    }

    // Function to distribute rewards to a user
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's reward balance
        rewards[user] += amount;

        // Emit an event for rewards distribution
        emit RewardsDistributed(user, amount);
    }

    // Function for users to claim their accumulated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];

        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero
        rewards[msg.sender] = 0;

        // Transfer GHST tokens to the user
        require(ghstToken.transfer(msg.sender, rewardAmount), "Token transfer failed");

        // Emit an event for reward claim
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to check the rewards of a user
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
