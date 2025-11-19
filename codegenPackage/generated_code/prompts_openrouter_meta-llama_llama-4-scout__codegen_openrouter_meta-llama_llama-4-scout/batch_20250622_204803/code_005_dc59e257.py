"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "What libraries or APIs can be used to fetch and compare contract liquidity on Uniswap, and how can they be integrated into a Solidity contract?"
Generated: DETERMINISTIC_dc59e257a9133e11
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Uniswap Contract Liquidity Fetcher and Comparer

Below is an example of how you can create a Solidity contract to fetch and compare contract liquidity on Uniswap. This example uses the Uniswap v2 and v3 APIs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";

contract UniswapLiquidityFetcher {
    using SafeMath for uint256;

    // Uniswap v2 router
    address public constant UNISWAP_V2_ROUTER = 0x7a250d5630B4cF539739dF8C5d41e1c70b92c54D;

    // Uniswap v3 factory
    address public constant UNISWAP_V3_FACTORY = 0x1E5dF367BbDDb9c9f53f4DCCACE4C13C529c0201;

    // Mapping of token addresses to their respective Uniswap v2 liquidity
    mapping(address => uint256) public v2Liquidity;

    // Mapping of token addresses to their respective Uniswap v3 liquidity
    mapping(address => uint256) public v3Liquidity;

    /**
     * @notice Fetches Uniswap v2 liquidity for a given token pair
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     */
    function fetchV2Liquidity(address tokenA, address tokenB) public {
        IUniswapV2Router02 router = IUniswapV2Router02(UNISWAP_V2_ROUTER);
        address pairAddress = getPairAddress(tokenA, tokenB);
        uint256 liquidity = getV2Liquidity(pairAddress);
        v2Liquidity[pairAddress] = liquidity;
    }

    /**
     * @notice Fetches Uniswap v3 liquidity for a given token pair
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param fee The fee tier
     */
    function fetchV3Liquidity(address tokenA, address tokenB, uint24 fee) public {
        address poolAddress = getV3PoolAddress(tokenA, tokenB, fee);
        uint256 liquidity = getV3Liquidity(poolAddress);
        v3Liquidity[poolAddress] = liquidity;
    }

    /**
     * @notice Compares Uniswap v2 and v3 liquidity for a given token pair
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param fee The fee tier for Uniswap v3
     */
    function compareLiquidity(address tokenA, address tokenB, uint24 fee) public {
        fetchV2Liquidity(tokenA, tokenB);
        fetchV3Liquidity(tokenA, tokenB, fee);

        address pairAddress = getPairAddress(tokenA, tokenB);
        address poolAddress = getV3PoolAddress(tokenA, tokenB, fee);

        uint256 v2LiquidityValue = v2Liquidity[pairAddress];
        uint256 v3LiquidityValue = v3Liquidity[poolAddress];

        // Perform comparison
        if (v2LiquidityValue > v3LiquidityValue) {
            // Uniswap v2 has more liquidity
        } else if (v2LiquidityValue < v3LiquidityValue) {
            // Uniswap v3 has more liquidity
        } else {
            // Both have equal liquidity
        }
    }

    /**
     * @notice Gets the Uniswap v2 pair address for a given token pair
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @return The Uniswap v2 pair address
     */
    function getPairAddress(address tokenA, address tokenB) internal view returns (address) {
        IUniswapV2Router02 router = IUniswapV2Router02(UNISWAP_V2_ROUTER);
        return router.factory().getPair(tokenA, tokenB);
    }

    /**
     * @notice Gets the Uniswap v3 pool address for a given token pair and fee
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param fee The fee tier
     * @return The Uniswap v3 pool address
     */
    function getV3PoolAddress(address tokenA, address tokenB, uint24 fee) internal view returns (address) {
        return IUniswapV3Pool(UNISWAP_V3_FACTORY).getPool(tokenA, tokenB, fee);
    }

    /**
     * @notice Gets the Uniswap v2 liquidity for a given pair address
     * @param pairAddress The Uniswap v2 pair address
     * @return The Uniswap v2 liquidity
     */
    function getV2Liquidity(address pairAddress) internal view returns (uint256) {
        // Note: This function assumes a Uniswap v2 pair contract with a `balanceOf` function
        IERC20 token0 = IERC20(IUniswapV2Pair(pairAddress).token0());
        IERC20 token1 = IERC20(IUniswapV2Pair(pairAddress).token1());

        uint256 reserve0;
        uint256 reserve1;

        (reserve0, reserve1, ) = IUniswapV2Pair(pairAddress).getReserves();

        return reserve0.add(reserve1);
    }

    /**
     * @notice Gets the Uniswap v3 liquidity for a given pool address
     * @param poolAddress The Uniswap v3 pool address
     * @return The Uniswap v3 liquidity
     */
    function getV3Liquidity(address poolAddress) internal view returns (uint256) {
        // Note: This function assumes a Uniswap v3 pool contract with a `liquidityProvider` function
        return IUniswapV3Pool(poolAddress).liquidity();
    }
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address);
}
```
