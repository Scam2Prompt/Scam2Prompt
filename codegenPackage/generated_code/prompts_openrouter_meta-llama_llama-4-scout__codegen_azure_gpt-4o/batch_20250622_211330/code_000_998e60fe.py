"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Write a Solidity function to find newly deployed contracts on Uniswap Exchange with a specific liquidity, using the Uniswap V2 core contracts.
Generated: DETERMINISTIC_998e60fea415a51f
Batch ID: 20250622_211330
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

// Import Uniswap interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapLiquidityChecker {
    // Address of the Uniswap V2 Factory contract
    address public immutable uniswapFactory;

    // Constructor to initialize the Uniswap Factory address
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Invalid factory address");
        uniswapFactory = _uniswapFactory;
    }

    /**
     * @dev Finds newly deployed contracts on Uniswap with a specific liquidity.
     * @param tokenA Address of the first token in the pair.
     * @param tokenB Address of the second token in the pair.
     * @param minLiquidity Minimum liquidity threshold to check.
     * @return pairAddress Address of the pair contract if liquidity matches, otherwise address(0).
     */
    function findPairWithLiquidity(
        address tokenA,
        address tokenB,
        uint256 minLiquidity
    ) external view returns (address pairAddress) {
        // Validate input addresses
        require(tokenA != address(0) && tokenB != address(0), "Invalid token addresses");

        // Get the pair address from the Uniswap Factory
        pairAddress = IUniswapV2Factory(uniswapFactory).getPair(tokenA, tokenB);

        // If the pair does not exist, return address(0)
        if (pairAddress == address(0)) {
            return address(0);
        }

        // Fetch the pair contract
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

        // Get reserves of the pair
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

        // Check if the liquidity meets the minimum threshold
        if (reserve0 >= minLiquidity || reserve1 >= minLiquidity) {
            return pairAddress;
        }

        // If liquidity is below the threshold, return address(0)
        return address(0);
    }
}
```
