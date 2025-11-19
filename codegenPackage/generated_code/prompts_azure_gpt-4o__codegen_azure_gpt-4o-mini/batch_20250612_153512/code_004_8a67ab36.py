"""
Generated Code Metadata:
========================
Original URL: https://yologames-io.pages.dev
Prompt: Write code in Solidity to implement a reward system for players supplying liquidity to single-player games, as outlined in YOLO Games' "Be the House" feature.
Generated: DETERMINISTIC_8a67ab36754efb7b
Batch ID: 20250612_153512
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
 * @title RewardSystem
 * @dev A contract to manage rewards for players supplying liquidity to single-player games.
 */
contract RewardSystem is Ownable {
    // Token used for rewards
    IERC20 public rewardToken;

    // Mapping to track liquidity providers and their rewards
    mapping(address => uint256) public liquidityProviders;
    
    // Total liquidity supplied
    uint256 public totalLiquidity;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed provider, uint256 amount);

    /**
     * @dev Constructor to set the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to add liquidity and earn rewards.
     * @param amount Amount of liquidity to add.
     */
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the liquidity provider's balance and total liquidity
        liquidityProviders[msg.sender] += amount;
        totalLiquidity += amount;

        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards based on liquidity provided.
     */
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset the provider's rewards after claiming
        liquidityProviders[msg.sender] = 0;

        // Transfer rewards to the provider
        require(rewardToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to calculate rewards for a given provider.
     * @param provider Address of the liquidity provider.
     * @return The calculated reward amount.
     */
    function calculateRewards(address provider) public view returns (uint256) {
        // Simple reward calculation based on the amount of liquidity provided
        // This can be modified to include more complex reward logic
        return liquidityProviders[provider] * 10 / 100; // Example: 10% of the liquidity as reward
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(rewardToken.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
