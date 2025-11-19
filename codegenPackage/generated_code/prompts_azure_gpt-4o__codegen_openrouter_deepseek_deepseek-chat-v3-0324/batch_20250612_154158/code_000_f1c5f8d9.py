"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function to find newly deployed contracts on Uniswap with specific liquidity requirements, using the `findNewContracts` method described in the 1inch Slippage Bot code.
Generated: DETERMINISTIC_f1c5f8d9bf38d9fb
Batch ID: 20250612_154158
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapLiquidityFinder {
    IUniswapV2Factory public immutable uniswapFactory;
    uint256 public constant MIN_LIQUIDITY_ETH = 1 ether; // Minimum liquidity threshold in ETH

    event NewPairFound(address indexed pair, address token0, address token1, uint256 reserve0, uint256 reserve1);

    constructor(address _factory) {
        uniswapFactory = IUniswapV2Factory(_factory);
    }

    /**
     * @dev Finds newly deployed Uniswap pairs with minimum liquidity requirements
     * @param tokenAddresses Array of token addresses to check for new pairs
     * @param maxPairsToCheck Maximum number of pairs to check in a single call
     * @return foundPairs Array of addresses of pairs that meet liquidity requirements
     */
    function findNewContracts(
        address[] memory tokenAddresses,
        uint256 maxPairsToCheck
    ) external returns (address[] memory foundPairs) {
        require(tokenAddresses.length > 0, "No tokens provided");
        require(maxPairsToCheck > 0, "Must check at least one pair");

        address[] memory tempFoundPairs = new address[](maxPairsToCheck);
        uint256 foundCount = 0;

        for (uint256 i = 0; i < tokenAddresses.length && foundCount < maxPairsToCheck; i++) {
            for (uint256 j = i + 1; j < tokenAddresses.length && foundCount < maxPairsToCheck; j++) {
                address tokenA = tokenAddresses[i];
                address tokenB = tokenAddresses[j];
                address pair = uniswapFactory.getPair(tokenA, tokenB);

                if (pair != address(0) && meetsLiquidityRequirements(pair)) {
                    tempFoundPairs[foundCount] = pair;
                    foundCount++;
                }
            }
        }

        foundPairs = new address[](foundCount);
        for (uint256 i = 0; i < foundCount; i++) {
            foundPairs[i] = tempFoundPairs[i];
        }

        return foundPairs;
    }

    /**
     * @dev Checks if a pair meets minimum liquidity requirements
     * @param pair Address of the Uniswap pair
     * @return bool True if liquidity requirements are met
     */
    function meetsLiquidityRequirements(address pair) internal view returns (bool) {
        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        
        try uniswapPair.getReserves() returns (uint112 reserve0, uint112 reserve1, uint32) {
            address token0 = uniswapPair.token0();
            address token1 = uniswapPair.token1();
            
            // Skip pairs with WETH as one of the tokens (already denominated in ETH)
            if (token0 == address(0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2) || 
                token1 == address(0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2)) {
                return (reserve0 > MIN_LIQUIDITY_ETH || reserve1 > MIN_LIQUIDITY_ETH);
            }
            
            // For non-WETH pairs, we'd need an oracle to check USD value
            // This is simplified to just check raw reserves
            return (reserve0 > 0 && reserve1 > 0);
        } catch {
            return false;
        }
    }
}
```
