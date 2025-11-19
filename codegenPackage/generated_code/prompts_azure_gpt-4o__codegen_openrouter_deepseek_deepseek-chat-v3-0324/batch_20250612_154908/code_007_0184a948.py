"""
Generated Code Metadata:
========================
Original URL: https://uniswap3.vercel.app
Prompt: Provide an example of how to set up a custom price oracle using Uniswap v3's pool data.
Generated: DETERMINISTIC_0184a94827e3bb40
Batch ID: 20250612_154908
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

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-core/contracts/libraries/TickMath.sol";
import "@uniswap/v3-core/contracts/libraries/FixedPoint96.sol";
import "@uniswap/v3-core/contracts/libraries/FullMath.sol";

contract UniswapV3PriceOracle {
    IUniswapV3Pool public immutable pool;
    uint32 public immutable twapInterval;

    constructor(IUniswapV3Pool _pool, uint32 _twapInterval) {
        require(address(_pool) != address(0), "Invalid pool address");
        require(_twapInterval > 0, "Interval must be positive");
        pool = _pool;
        twapInterval = _twapInterval;
    }

    function getSqrtTwapX96() public view returns (uint160 sqrtPriceX96) {
        uint32[] memory secondsAgos = new uint32[](2);
        secondsAgos[0] = twapInterval;
        secondsAgos[1] = 0;

        (int56[] memory tickCumulatives, ) = pool.observe(secondsAgos);
        int56 tickCumulativeDelta = tickCumulatives[1] - tickCumulatives[0];
        int56 twapTick = tickCumulativeDelta / int56(int32(twapInterval));
        sqrtPriceX96 = TickMath.getSqrtRatioAtTick(int24(twapTick));
    }

    function getPriceX96(address tokenIn) external view returns (uint256 priceX96) {
        uint160 sqrtPriceX96 = getSqrtTwapX96();
        uint256 price = FullMath.mulDiv(
            uint256(sqrtPriceX96) * uint256(sqrtPriceX96),
            FixedPoint96.Q96,
            FixedPoint96.Q96
        );

        (address token0, ) = (pool.token0(), pool.token1());
        priceX96 = tokenIn == token0 ? price : FullMath.mulDiv(FixedPoint96.Q96, FixedPoint96.Q96, price);
    }

    function getPrice(address tokenIn, uint8 decimalsOut) external view returns (uint256) {
        uint256 priceX96 = getPriceX96(tokenIn);
        return FullMath.mulDiv(priceX96, 10**decimalsOut, FixedPoint96.Q96);
    }
}
```
