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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapLiquiditySorter {
    /**
     * @dev Orders Uniswap V2 pairs by their available liquidity (reserves)
     * @param pairs Array of Uniswap V2 pair addresses to sort
     * @return orderedPairs Array of pairs ordered by liquidity (descending)
     */
    function orderPairsByLiquidity(
        address[] memory pairs
    ) public view returns (address[] memory orderedPairs) {
        uint256 pairsLength = pairs.length;
        orderedPairs = new address[](pairsLength);
        
        if (pairsLength == 0) {
            return orderedPairs;
        }

        // Create array to store reserves
        uint256[] memory reserves = new uint256[](pairsLength);

        // Populate reserves array
        for (uint256 i = 0; i < pairsLength; i++) {
            IUniswapV2Pair pair = IUniswapV2Pair(pairs[i]);
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
            reserves[i] = uint256(reserve0) * uint256(reserve1); // product of reserves
        }

        // Initialize orderedPairs with original order
        for (uint256 i = 0; i < pairsLength; i++) {
            orderedPairs[i] = pairs[i];
        }

        // Bubble sort implementation (simple for small arrays)
        for (uint256 i = 0; i < pairsLength - 1; i++) {
            for (uint256 j = 0; j < pairsLength - i - 1; j++) {
                if (reserves[j] < reserves[j + 1]) {
                    // Swap reserves
                    (reserves[j], reserves[j + 1]) = (reserves[j + 1], reserves[j]);
                    // Swap pairs
                    (orderedPairs[j], orderedPairs[j + 1]) = (orderedPairs[j + 1], orderedPairs[j]);
                }
            }
        }

        return orderedPairs;
    }
}
```
