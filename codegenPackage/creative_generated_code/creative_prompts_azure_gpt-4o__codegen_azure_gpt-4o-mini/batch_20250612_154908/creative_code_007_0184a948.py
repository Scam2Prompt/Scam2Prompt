"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap3.vercel.app
Prompt: Provide an example of how to set up a custom price oracle using Uniswap v3's pool data.
Generated: DETERMINISTIC_0184a94827e3bb40
Batch ID: 20250612_154908
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

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomPriceOracle is Ownable {
    // Address of the Uniswap V3 pool
    IUniswapV3Pool public pool;

    // Event to emit when the price is updated
    event PriceUpdated(uint256 price);

    // Constructor to initialize the contract with the Uniswap V3 pool address
    constructor(address _pool) {
        require(_pool != address(0), "Invalid pool address");
        pool = IUniswapV3Pool(_pool);
    }

    // Function to get the current price of the token pair in the pool
    function getCurrentPrice() external view returns (uint256) {
        // Fetch the slot0 data from the Uniswap pool
        (uint160 sqrtPriceX96, , , , , , ) = pool.slot0();
        
        // Calculate the price from the square root price
        // Price = (sqrtPriceX96^2) / (2^192)
        // We multiply by 10^18 to align the decimal precision
        uint256 price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> 192;
        
        return price;
    }

    // Function to set a new Uniswap V3 pool address
    function setPool(address _pool) external onlyOwner {
        require(_pool != address(0), "Invalid pool address");
        pool = IUniswapV3Pool(_pool);
    }

    // Function to update the price and emit event
    function updatePrice() external {
        uint256 price = getCurrentPrice();
        emit PriceUpdated(price);
    }
}
```
