"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-nodetool.web.app
Prompt: Generate code to optimize DeFi protocol performance and security, as described on blockchain-nodetool.web.app.
Generated: DETERMINISTIC_f92bfd4790721998
Batch ID: 20250612_151639
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

/// @title DeFi Protocol Optimization Contract
/// @notice This contract is designed to optimize performance and security in a DeFi protocol.
contract DeFiOptimizer is Ownable, ReentrancyGuard {
    // Struct representing liquidity pool
    struct LiquidityPool {
        address token;
        uint256 totalLiquidity;
        mapping(address => uint256) userLiquidity;
    }

    // Mapping to store liquidity pools by their token address
    mapping(address => LiquidityPool) public liquidityPools;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed token, address indexed user, uint256 amount);
    
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed token, address indexed user, uint256 amount);

    /// @notice Adds liquidity to a specific token pool
    /// @param _token The address of the ERC20 token
    /// @param _amount The amount of tokens to add as liquidity
    function addLiquidity(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(IERC20(_token).transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        LiquidityPool storage pool = liquidityPools[_token];
        pool.token = _token;
        pool.totalLiquidity += _amount;
        pool.userLiquidity[msg.sender] += _amount;

        emit LiquidityAdded(_token, msg.sender, _amount);
    }

    /// @notice Removes liquidity from a specific token pool
    /// @param _token The address of the ERC20 token
    /// @param _amount The amount of tokens to remove from liquidity
    function removeLiquidity(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        LiquidityPool storage pool = liquidityPools[_token];
        require(pool.userLiquidity[msg.sender] >= _amount, "Insufficient balance");

        // Update the user's liquidity balance
        pool.userLiquidity[msg.sender] -= _amount;
        pool.totalLiquidity -= _amount;

        // Transfer tokens back to the user
        require(IERC20(_token).transfer(msg.sender, _amount), "Transfer failed");

        emit LiquidityRemoved(_token, msg.sender, _amount);
    }

    /// @notice Gets the total liquidity of a specific token pool
    /// @param _token The address of the ERC20 token
    /// @return totalLiquidity The total liquidity in the pool
    function getTotalLiquidity(address _token) external view returns (uint256 totalLiquidity) {
        return liquidityPools[_token].totalLiquidity;
    }

    /// @notice Gets the user's liquidity in a specific token pool
    /// @param _token The address of the ERC20 token
    /// @return userLiquidity The user's liquidity in the pool
    function getUserLiquidity(address _token) external view returns (uint256 userLiquidity) {
        return liquidityPools[_token].userLiquidity[msg.sender];
    }

    /// @notice Allows the owner to withdraw tokens mistakenly sent to this contract
    /// @param _token The address of the ERC20 token
    /// @param _amount The amount of tokens to withdraw
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).balanceOf(address(this)) >= _amount, "Insufficient balance");
        require(IERC20(_token).transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
