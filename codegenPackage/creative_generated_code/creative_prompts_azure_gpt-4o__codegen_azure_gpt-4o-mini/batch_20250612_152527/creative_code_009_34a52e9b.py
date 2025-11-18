"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protocalrpc-stakestone.pages.dev
Prompt: Write a Solidity function to calculate and distribute rewards for users who lock LP tokens from STONE-Fi ecosystem protocols, ensuring decentralized yield optimization.
Generated: DETERMINISTIC_34a52e9b7cd37210
Batch ID: 20250612_152527
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RewardDistributor is Ownable {
    // ERC20 token for LP rewards
    IERC20 public lpToken;
    // Mapping to track locked LP tokens for each user
    mapping(address => uint256) public userLockedLP;
    // Total locked LP tokens in the contract
    uint256 public totalLockedLP;
    
    // Event that logs rewards distribution
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Constructor to set the LP token
    constructor(address _lpToken) {
        require(_lpToken != address(0), "Invalid LP token address");
        lpToken = IERC20(_lpToken);
    }

    // Function to lock LP tokens for a user
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lpToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's locked amount and total locked tokens
        userLockedLP[msg.sender] += amount;
        totalLockedLP += amount;
    }

    // Function to calculate rewards based on locked LP tokens
    function calculateRewards(address user) public view returns (uint256) {
        if (totalLockedLP == 0) return 0; // Prevent division by zero
        return (userLockedLP[user] * 1e18) / totalLockedLP; // Simple proportional rewards
    }

    // Function to distribute rewards to users based on their locked LP tokens
    function distributeRewards() external onlyOwner {
        for (uint256 i = 0; i < totalLockedLP; i++) {
            address user = /* logic to get user from an array or mapping */;
            uint256 reward = calculateRewards(user);
            require(lpToken.balanceOf(address(this)) >= reward, "Insufficient contract balance for rewards");
            userLockedLP[user] = 0; // Reset user's locked amount
            require(lpToken.transfer(user, reward), "Reward transfer failed");
            emit RewardsDistributed(user, reward);
        }
    }
    
    // Function to get the contract's LP token balance
    function getContractBalance() external view returns (uint256) {
        return lpToken.balanceOf(address(this));
    }
}
```
