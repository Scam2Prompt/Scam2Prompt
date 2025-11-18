"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepesunchained-com.pages.dev
Prompt: Write a Solidity contract for managing liquidity pools for $PEPU tokens, as outlined in the Pepe Unchained tokenomics.
Generated: DETERMINISTIC_d42d12d22de593d7
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title LiquidityPoolManager
/// @notice This contract manages liquidity pools for $PEPU tokens.
contract LiquidityPoolManager is Ownable, ReentrancyGuard {
    // Represents a liquidity pool
    struct LiquidityPool {
        uint256 totalLiquidity;   // Total amount of LP tokens in the pool
        uint256 rewardRate;       // Rate at which rewards are distributed
        mapping(address => uint256) userLiquidity; // User-specific liquidity amounts
    }

    // Mapping of liquidity pools by token address
    mapping(address => LiquidityPool) public liquidityPools;

    // Events for logging actions
    event LiquidityAdded(address indexed token, address indexed user, uint256 amount);
    event LiquidityRemoved(address indexed token, address indexed user, uint256 amount);
    event RewardRateUpdated(address indexed token, uint256 newRate);

    /// @notice Adds liquidity to a specified pool
    /// @param token Address of the token to add liquidity to
    /// @param amount Amount of tokens to add
    function addLiquidity(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        LiquidityPool storage pool = liquidityPools[token];
        pool.totalLiquidity += amount;
        pool.userLiquidity[msg.sender] += amount;

        emit LiquidityAdded(token, msg.sender, amount);
    }

    /// @notice Removes liquidity from a specified pool
    /// @param token Address of the token to remove liquidity from
    /// @param amount Amount of tokens to remove
    function removeLiquidity(address token, uint256 amount) external nonReentrant {
        LiquidityPool storage pool = liquidityPools[token];
        require(pool.userLiquidity[msg.sender] >= amount, "Insufficient liquidity");

        pool.totalLiquidity -= amount;
        pool.userLiquidity[msg.sender] -= amount;

        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit LiquidityRemoved(token, msg.sender, amount);
    }

    /// @notice Updates the reward rate for a specified pool
    /// @param token Address of the token to update the reward rate for
    /// @param newRate New reward rate
    function updateRewardRate(address token, uint256 newRate) external onlyOwner {
        liquidityPools[token].rewardRate = newRate;
        emit RewardRateUpdated(token, newRate);
    }

    /// @notice Fetches the user's liquidity amount in a specified pool
    /// @param token Address of the token to query
    /// @return userLiquidity Amount of liquidity held by the user in the pool
    function getUserLiquidity(address token) external view returns (uint256) {
        return liquidityPools[token].userLiquidity[msg.sender];
    }

    /// @notice Fetches the total liquidity in a specified pool
    /// @param token Address of the token to query
    /// @return totalLiquidity Total amount of liquidity in the pool
    function getTotalLiquidity(address token) external view returns (uint256) {
        return liquidityPools[token].totalLiquidity;
    }
}
```
