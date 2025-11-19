"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algebra-finance.pages.dev
Prompt: Generate a code snippet to implement a DEX using Algebra's Core-Plugins architecture, focusing on concentrated liquidity pools.
Generated: DETERMINISTIC_2dbe0d6285a05dd7
Batch ID: 20250612_160940
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

// Import required interfaces and libraries from Algebra's Core-Plugins
import "@algebra/core/contracts/interfaces/INonfungiblePositionManager.sol";
import "@algebra/core/contracts/interfaces/ILiquidityPool.sol";
import "@algebra/core/contracts/interfaces/IERC20.sol";
import "@algebra/core/contracts/libraries/Errors.sol";

// DEX contract for creating and managing concentrated liquidity pools
contract ConcentratedLiquidityDEX {
    // State variables
    INonfungiblePositionManager public positionManager;
    ILiquidityPool public liquidityPool;

    // Events for logging
    event LiquidityAdded(address indexed provider, uint256 tokenId, uint256 amount0, uint256 amount1);
    event LiquidityRemoved(address indexed provider, uint256 tokenId, uint256 amount0, uint256 amount1);

    // Constructor to initialize the DEX with position manager and liquidity pool addresses
    constructor(address _positionManager, address _liquidityPool) {
        require(_positionManager != address(0), "Invalid position manager address");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");

        positionManager = INonfungiblePositionManager(_positionManager);
        liquidityPool = ILiquidityPool(_liquidityPool);
    }

    // Function to add liquidity to the pool
    function addLiquidity(
        uint256 tokenId,
        uint256 amount0,
        uint256 amount1
    ) external {
        require(amount0 > 0 || amount1 > 0, "Invalid liquidity amounts");
        
        // Transfer tokens to the contract
        IERC20(liquidityPool.token0()).transferFrom(msg.sender, address(this), amount0);
        IERC20(liquidityPool.token1()).transferFrom(msg.sender, address(this), amount1);

        // Approve position manager to spend tokens
        IERC20(liquidityPool.token0()).approve(address(positionManager), amount0);
        IERC20(liquidityPool.token1()).approve(address(positionManager), amount1);

        // Mint position and get tokenId
        (uint256 mintedTokenId, ) = positionManager.mint(tokenId, amount0, amount1);

        // Emit event on successful liquidity addition
        emit LiquidityAdded(msg.sender, mintedTokenId, amount0, amount1);
    }

    // Function to remove liquidity from the pool
    function removeLiquidity(uint256 tokenId, uint256 liquidityAmount) external {
        require(liquidityAmount > 0, "Invalid liquidity amount");
        
        // Transfer the token to the position manager for liquidity removal
        positionManager.burn(tokenId, liquidityAmount);
        
        // Get the amount of tokens returned
        (uint256 amount0, uint256 amount1) = positionManager.collect(tokenId, msg.sender);

        // Emit event on successful liquidity removal
        emit LiquidityRemoved(msg.sender, tokenId, amount0, amount1);
    }

    // Fallback function to receive Ether (if needed)
    receive() external payable {}
    
    // Fallback function for other calls
    fallback() external {
        revert("Fallback function not supported");
    }
}
```
