"""
Generated Code Metadata:
========================
Original URL: https://broccoliclaim.web.app
Prompt: Create a smart contract for managing token rewards distribution, inspired by the Broccoli platform's single-transaction claim functionality.
Generated: DETERMINISTIC_6cf040b545fec229
Batch ID: 20250612_154542
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
 * @title TokenRewards
 * @dev A smart contract for managing token rewards distribution.
 * Inspired by the Broccoli platform's single-transaction claim functionality.
 */
contract TokenRewards is Ownable {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Mapping to track the rewards for each user
    mapping(address => uint256) private rewards;

    // The ERC20 token used for rewards
    IERC20 public rewardToken;

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to add rewards for a user.
     * @param user Address of the user to whom rewards will be added.
     * @param amount Amount of rewards to be added.
     */
    function addRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;
    }

    /**
     * @dev Function for users to claim their rewards in a single transaction.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards before transferring to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to check the rewards of a user.
     * @param user Address of the user.
     * @return The amount of rewards available for the user.
     */
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    /**
     * @dev Function to withdraw tokens from the contract in case of emergency.
     * Only the owner can call this function.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
