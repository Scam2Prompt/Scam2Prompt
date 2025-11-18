"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Write a smart contract snippet for managing token rewards on the Manta CeDeFi platform, ensuring compatibility with assets like BTC, ETH, USDT, and USDC.
Generated: DETERMINISTIC_808a91d74d352c96
Batch ID: 20250612_153648
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

// Importing required interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenRewardManager
 * @dev A smart contract to manage token rewards on the Manta CeDeFi platform.
 */
contract TokenRewardManager is Ownable {
    // Mapping to store the balance of rewards for each user
    mapping(address => mapping(address => uint256)) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed token, address indexed user, uint256 amount);

    /**
     * @dev Distributes rewards to a user.
     * @param token The address of the ERC20 token to distribute.
     * @param user The address of the user receiving rewards.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(address token, address user, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the rewards from the contract to the user
        IERC20(token).transferFrom(msg.sender, user, amount);

        // Update the user's reward balance
        rewards[user][token] += amount;

        emit RewardsDistributed(token, user, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     * @param token The address of the ERC20 token to claim rewards.
     */
    function claimRewards(address token) external {
        require(token != address(0), "Invalid token address");
        uint256 rewardAmount = rewards[msg.sender][token];

        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance
        rewards[msg.sender][token] = 0;

        // Transfer the rewards to the user
        IERC20(token).transfer(msg.sender, rewardAmount);
    }

    /**
     * @dev Retrieve the reward balance of a user for a specific token.
     * @param user The address of the user to query.
     * @param token The address of the ERC20 token to query.
     * @return The reward balance of the user for the specified token.
     */
    function getRewardBalance(address user, address token) external view returns (uint256) {
        return rewards[user][token];
    }
}
```
