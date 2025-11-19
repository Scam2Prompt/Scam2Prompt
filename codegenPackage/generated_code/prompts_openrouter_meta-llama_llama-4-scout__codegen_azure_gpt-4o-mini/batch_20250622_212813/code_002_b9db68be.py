"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: "Design a smart contract to implement a perpetual incentive structure for social engagement, inspired by Loud's experiment."
Generated: DETERMINISTIC_b9db68be106af56c
Batch ID: 20250622_212813
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PerpetualIncentive
 * @dev A smart contract to implement a perpetual incentive structure for social engagement.
 */
contract PerpetualIncentive is Ownable {
    // Token used for incentives
    IERC20 public incentiveToken;

    // Mapping to track user engagement scores
    mapping(address => uint256) public engagementScores;

    // Event emitted when a user engages
    event UserEngaged(address indexed user, uint256 score);

    // Event emitted when incentives are distributed
    event IncentivesDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the incentive token address
    constructor(IERC20 _incentiveToken) {
        incentiveToken = _incentiveToken;
    }

    /**
     * @dev Function to record user engagement.
     * @param user The address of the user engaging.
     * @param score The score to be added to the user's engagement.
     */
    function recordEngagement(address user, uint256 score) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(score > 0, "Score must be greater than zero");

        // Update the user's engagement score
        engagementScores[user] += score;

        // Emit an event for the engagement
        emit UserEngaged(user, score);
    }

    /**
     * @dev Function to distribute incentives based on engagement scores.
     * @param user The address of the user to distribute incentives to.
     */
    function distributeIncentives(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        uint256 score = engagementScores[user];
        require(score > 0, "No engagement score to distribute incentives");

        // Calculate the incentive amount (1 token per score point)
        uint256 incentiveAmount = score;

        // Ensure the contract has enough tokens to distribute
        require(incentiveToken.balanceOf(address(this)) >= incentiveAmount, "Insufficient tokens in contract");

        // Transfer the incentive tokens to the user
        bool success = incentiveToken.transfer(user, incentiveAmount);
        require(success, "Token transfer failed");

        // Emit an event for the incentive distribution
        emit IncentivesDistributed(user, incentiveAmount);

        // Reset the user's engagement score after distribution
        engagementScores[user] = 0;
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(incentiveToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer the specified amount of tokens to the owner
        bool success = incentiveToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to check the contract's token balance.
     * @return The balance of the incentive token in the contract.
     */
    function checkTokenBalance() external view returns (uint256) {
        return incentiveToken.balanceOf(address(this));
    }
}
```
