"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Implement a function in Solidity to order contracts by their available liquidity, using a slice data structure and Uniswap V2.
Generated: DETERMINISTIC_6281e15c9b353fd1
Batch ID: 20250622_204938
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

/**
 * @title LiquiditySorter
 * @author [Your Name]
 * @notice Sorts Uniswap V2 contracts by their available liquidity.
 */
contract LiquiditySorter {
    // Uniswap V2 factory instance
    IUniswapV2Factory public immutable factory;

    /**
     * @param _factory Uniswap V2 factory address
     */
    constructor(address _factory) {
        require(_factory != address(0), "Invalid factory address");
        factory = IUniswapV2Factory(_factory);
    }

    /**
     * @dev Structure to hold pair information
     */
    struct PairInfo {
        address pairAddress;
        uint256 liquidity;
    }

    /**
     * @dev Sorts pairs by their liquidity in descending order
     * @param _pairs Array of pair addresses
     * @return sortedPairs Array of PairInfo sorted by liquidity
     */
    function sortPairsByLiquidity(address[] memory _pairs) public view returns (PairInfo[] memory) {
        // Initialize an empty array to store pair information
        PairInfo[] memory pairsInfo = new PairInfo[](_pairs.length);

        // Iterate over each pair address
        for (uint256 i = 0; i < _pairs.length; i++) {
            // Get the pair contract instance
            IUniswapV2Pair pair = IUniswapV2Pair(_pairs[i]);

            // Get the liquidity of the pair
            uint256 liquidity = pair.liquidity();

            // Store pair information
            pairsInfo[i] = PairInfo(_pairs[i], liquidity);
        }

        // Sort pairs by liquidity in descending order
        quickSort(pairsInfo, 0, pairsInfo.length - 1);

        return pairsInfo;
    }

    /**
     * @dev Quick sort implementation for PairInfo array
     * @param _pairs Array of PairInfo
     * @param _low Low index
     * @param _high High index
     */
    function quickSort(PairInfo[] memory _pairs, uint256 _low, uint256 _high) internal pure {
        if (_low < _high) {
            uint256 pivotIndex = partition(_pairs, _low, _high);

            quickSort(_pairs, _low, pivotIndex - 1);
            quickSort(_pairs, pivotIndex + 1, _high);
        }
    }

    /**
     * @dev Partitions the PairInfo array for quick sort
     * @param _pairs Array of PairInfo
     * @param _low Low index
     * @param _high High index
     * @return pivotIndex Pivot index
     */
    function partition(PairInfo[] memory _pairs, uint256 _low, uint256 _high) internal pure returns (uint256) {
        PairInfo pivot = _pairs[_high];
        uint256 i = _low - 1;

        for (uint256 j = _low; j < _high; j++) {
            if (_pairs[j].liquidity > pivot.liquidity) {
                i++;
                (_pairs[i], _pairs[j]) = (_pairs[j], _pairs[i]);
            }
        }

        (_pairs[i + 1], _pairs[_high]) = (_pairs[_high], _pairs[i + 1]);
        return i + 1;
    }

    /**
     * @dev Gets all pairs from Uniswap V2 factory
     * @return pairs Array of pair addresses
     */
    function getAllPairs() public view returns (address[] memory) {
        uint256 pairCount = factory.allPairsLength();
        address[] memory pairs = new address[](pairCount);

        for (uint256 i = 0; i < pairCount; i++) {
            pairs[i] = factory.allPairs(i);
        }

        return pairs;
    }
}
```
