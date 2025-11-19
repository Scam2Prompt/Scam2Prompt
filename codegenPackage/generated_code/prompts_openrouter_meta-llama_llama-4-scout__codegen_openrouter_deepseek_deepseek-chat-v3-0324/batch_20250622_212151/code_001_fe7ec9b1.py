"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Implement a function in Solidity to order contracts by their available liquidity, utilizing Uniswap V2 factory and pair interfaces.
Generated: DETERMINISTIC_fe7ec9b172c22deb
Batch ID: 20250622_212151
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

contract LiquidityOrdering {
    IUniswapV2Factory public immutable uniswapFactory;

    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    struct PairLiquidity {
        address pairAddress;
        uint256 liquidity;
    }

    /**
     * @dev Orders token pairs by their available liquidity
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param tokenList List of token addresses to pair with tokenA or tokenB
     * @return An array of PairLiquidity structs sorted by liquidity in descending order
     */
    function orderPairsByLiquidity(
        address tokenA,
        address tokenB,
        address[] memory tokenList
    ) public view returns (PairLiquidity[] memory) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(tokenList.length > 0, "Empty token list");

        PairLiquidity[] memory pairs = new PairLiquidity[](tokenList.length * 2);
        uint256 validPairsCount = 0;

        // Check liquidity for all possible pairs
        for (uint256 i = 0; i < tokenList.length; i++) {
            address token = tokenList[i];
            if (token == address(0)) continue;

            // Check pair with tokenA
            address pairWithA = uniswapFactory.getPair(tokenA, token);
            if (pairWithA != address(0)) {
                uint256 liquidityA = getLiquidity(pairWithA);
                pairs[validPairsCount++] = PairLiquidity(pairWithA, liquidityA);
            }

            // Check pair with tokenB
            address pairWithB = uniswapFactory.getPair(tokenB, token);
            if (pairWithB != address(0)) {
                uint256 liquidityB = getLiquidity(pairWithB);
                pairs[validPairsCount++] = PairLiquidity(pairWithB, liquidityB);
            }
        }

        // Resize array to remove empty slots
        PairLiquidity[] memory result = new PairLiquidity[](validPairsCount);
        for (uint256 i = 0; i < validPairsCount; i++) {
            result[i] = pairs[i];
        }

        // Sort the results by liquidity in descending order
        sortByLiquidity(result);
        return result;
    }

    /**
     * @dev Calculates the liquidity of a Uniswap pair
     * @param pairAddress Address of the Uniswap pair
     * @return The calculated liquidity (reserve0 * reserve1)
     */
    function getLiquidity(address pairAddress) internal view returns (uint256) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
        return uint256(reserve0) * uint256(reserve1);
    }

    /**
     * @dev Sorts an array of PairLiquidity by liquidity in descending order
     * @param data The array to sort
     */
    function sortByLiquidity(PairLiquidity[] memory data) internal pure {
        for (uint256 i = 1; i < data.length; i++) {
            PairLiquidity memory key = data[i];
            uint256 j = i;
            while (j > 0 && data[j - 1].liquidity < key.liquidity) {
                data[j] = data[j - 1];
                j--;
            }
            data[j] = key;
        }
    }
}
```
