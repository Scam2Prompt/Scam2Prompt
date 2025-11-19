"""
Generated Code Metadata:
========================
Original URL: https://codesrc.pages.dev
Prompt: "Generate Solidity code for a smart contract that orders Uniswap contracts by their available liquidity, inspired by the `orderContractsByLiquidity` function in the provided 1inch Slippage bot contract."
Generated: DETERMINISTIC_2ffd3e478023f103
Batch ID: 20250622_204816
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapLiquidityOrderer {
    // Uniswap router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Constructor
    constructor(address _uniswapRouter) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * Orders Uniswap contracts by their available liquidity.
     * 
     * @param _pairs Array of Uniswap pair addresses.
     * @return An array of pairs ordered by their liquidity in descending order.
     */
    function orderContractsByLiquidity(address[] memory _pairs) public view returns (address[] memory) {
        // Initialize an array to store pairs with their liquidity
        PairLiquidity[] memory pairsWithLiquidity = new PairLiquidity[](_pairs.length);

        // Iterate over pairs to fetch their liquidity
        for (uint256 i = 0; i < _pairs.length; i++) {
            // Get the Uniswap pair
            IUniswapV2Pair pair = IUniswapV2Pair(_pairs[i]);

            // Get the reserves of the pair
            (uint256 reserve0, uint256 reserve1, ) = pair.getReserves();

            // Calculate the liquidity (using the Uniswap v2 formula)
            uint256 liquidity = sqrt(reserve0 * reserve1);

            // Store the pair with its liquidity
            pairsWithLiquidity[i] = PairLiquidity(_pairs[i], liquidity);
        }

        // Sort pairs by liquidity in descending order
        pairsWithLiquidity = sortByLiquidity(pairsWithLiquidity);

        // Extract and return the sorted pair addresses
        address[] memory sortedPairs = new address[](pairsWithLiquidity.length);
        for (uint256 i = 0; i < pairsWithLiquidity.length; i++) {
            sortedPairs[i] = pairsWithLiquidity[i].pair;
        }

        return sortedPairs;
    }

    /**
     * Sorts an array of pairs by their liquidity in descending order.
     * 
     * @param _pairs Array of pairs with their liquidity.
     * @return The sorted array of pairs.
     */
    function sortByLiquidity(PairLiquidity[] memory _pairs) internal pure returns (PairLiquidity[] memory) {
        // Implement a sorting algorithm (e.g., bubble sort, quicksort)
        // For simplicity, we use a basic bubble sort here
        for (uint256 i = 0; i < _pairs.length; i++) {
            for (uint256 j = i + 1; j < _pairs.length; j++) {
                if (_pairs[i].liquidity < _pairs[j].liquidity) {
                    // Swap pairs
                    PairLiquidity temp = _pairs[i];
                    _pairs[i] = _pairs[j];
                    _pairs[j] = temp;
                }
            }
        }
        return _pairs;
    }

    /**
     * Calculates the square root of a number.
     * 
     * @param _num The number.
     * @return The square root of the number.
     */
    function sqrt(uint256 _num) internal pure returns (uint256) {
        uint256 x = _num;
        uint256 y = (x + 1) / 2;
        while (y < x) {
            x = y;
            y = (x + _num / x) / 2;
        }
        return x;
    }

    // Struct to represent a pair with its liquidity
    struct PairLiquidity {
        address pair;
        uint256 liquidity;
    }
}
```
