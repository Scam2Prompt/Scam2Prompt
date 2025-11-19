"""
Generated Code Metadata:
========================
Original URL: https://looksrare.tech
Prompt: Write a Solidity contract that implements a reward distribution system for early adopters, similar to the token distribution model described for LOOKS tokens on LooksRare.
Generated: DETERMINISTIC_73be225ef7fd8c75
Batch ID: 20250612_145121
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
 * @title RewardDistribution
 * @dev A contract for distributing rewards to early adopters.
 */
contract RewardDistribution is Ownable {
    // Token to be distributed as rewards
    IERC20 public rewardToken;

    // Mapping to track the amount of rewards for each user
    mapping(address => uint256) public rewards;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token to be used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to distribute rewards to a list of users.
     * @param users Array of addresses to receive rewards.
     * @param amounts Array of reward amounts corresponding to each user.
     */
    function distributeRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Users and amounts length mismatch");

        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid user address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            rewards[users[i]] += amounts[i];
            totalRewardsDistributed += amounts[i];

            emit RewardsDistributed(users[i], amounts[i]);
        }

        // Transfer the total amount of rewards from the contract to the users
        require(rewardToken.balanceOf(address(this)) >= totalRewardsDistributed, "Insufficient token balance in contract");
        for (uint256 i = 0; i < users.length; i++) {
            rewardToken.transfer(users[i], amounts[i]);
        }
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to the contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        token.transfer(owner(), amount);
    }

    /**
     * @dev Function to check the reward balance of a user.
     * @param user Address of the user to check.
     * @return The amount of rewards available for the user.
     */
    function checkRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
