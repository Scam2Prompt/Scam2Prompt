"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity contract that uses `IUniswapV2Factory` and `IUniswapV2Pair` to identify new Uniswap liquidity pool contracts, similar to the functionality described in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_cb1eec9a43d12726
Batch ID: 20250612_154809
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

// Interface for the Uniswap V2 Factory contract
interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

// Interface for the Uniswap V2 Pair contract
interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract UniswapLiquidityTracker {
    IUniswapV2Factory public uniswapFactory;

    // Event to log new liquidity pools
    event NewLiquidityPool(address indexed token0, address indexed token1, address pair);

    // Constructor to initialize the Uniswap factory address
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    // Function to create a new liquidity pair
    function createLiquidityPair(address tokenA, address tokenB) external returns (address pair) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(tokenA != tokenB, "Tokens must be different");

        // Create a new pair and emit an event
        pair = uniswapFactory.createPair(tokenA, tokenB);
        emit NewLiquidityPool(tokenA, tokenB, pair);
    }

    // Function to retrieve the existing liquidity pair address
    function getLiquidityPair(address tokenA, address tokenB) external view returns (address pair) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(tokenA != tokenB, "Tokens must be different");

        pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Liquidity pair does not exist");
    }
}
```
