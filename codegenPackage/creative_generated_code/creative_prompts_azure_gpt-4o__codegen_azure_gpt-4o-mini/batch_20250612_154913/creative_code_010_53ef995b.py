"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pabshq.com
Prompt: Generate code for a decentralized "reward payout" system that distributes $PABS tokens based on user activity metrics, inspired by the roadmap features of Pabs HQ.
Generated: DETERMINISTIC_53ef995bb52836bb
Batch ID: 20250612_154913
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title PABS Token
// @dev Implementation of a reward payout system that distributes $PABS tokens based on user activity metrics
contract PABSToken is ERC20, Ownable {
    // Mapping to track user activity metrics
    mapping(address => uint256) public userActivityMetrics;

    // Event that is emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PABS Token", "PABS") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to the contract owner
    }

    // @dev Function to update user activity metrics
    // @param user The address of the user
    // @param activityScore The score representing user activity
    function updateUserActivity(address user, uint256 activityScore) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(activityScore > 0, "Activity score must be greater than zero");

        userActivityMetrics[user] += activityScore;
    }

    // @dev Function to distribute rewards based on user activity
    // @param user The address of the user to reward
    function distributeRewards(address user) external onlyOwner {
        require(userActivityMetrics[user] > 0, "No activity metrics to reward");
        
        // Calculate reward amount based on activity metrics
        uint256 rewardAmount = calculateReward(userActivityMetrics[user]);
        
        // Ensure the contract has enough balance to distribute the reward
        require(balanceOf(address(this)) >= rewardAmount, "Insufficient balance to distribute rewards");

        // Transfer rewards to the user
        _transfer(address(this), user, rewardAmount);
        emit RewardsDistributed(user, rewardAmount);

        // Reset the user's activity metrics after rewarding
        userActivityMetrics[user] = 0;
    }

    // @dev Internal function to calculate reward based on activity metrics
    // @param activityScore The activity score of the user
    // @return The calculated reward amount
    function calculateReward(uint256 activityScore) internal pure returns (uint256) {
        // Simple reward logic: 1 token per activity score point
        return activityScore * 1 ether; // Adjust the multiplier as needed
    }

    // @dev Function to allow the contract owner to withdraw tokens from the contract
    // @param amount The amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");

        _transfer(address(this), msg.sender, amount);
    }
}
```
