"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Write a Solidity function that identifies and returns newly deployed contracts on Uniswap with specific liquidity requirements, inspired by the `findNewContracts` function on https://codesrc.pages.dev.
Generated: DETERMINISTIC_8ac43defd849b705
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

interface IUniswapV2Factory {
    function allPairsLength() external view returns (uint);
    function allPairs(uint index) external view returns (address);
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

contract UniswapPairScanner {
    // Address of the Uniswap V2 factory
    address public immutable uniswapV2Factory;

    // Minimum required liquidity in the pair (both tokens combined)
    uint256 public immutable minLiquidity;

    /**
     * @dev Constructor sets the Uniswap V2 factory address and liquidity threshold.
     * @param _uniswapV2Factory The address of the Uniswap V2 factory.
     * @param _minLiquidity Minimum liquidity threshold.
     */
    constructor(address _uniswapV2Factory, uint256 _minLiquidity) {
        require(_uniswapV2Factory != address(0), "Invalid factory address");
        require(_minLiquidity > 0, "Minimum liquidity must be greater than zero");
        uniswapV2Factory = _uniswapV2Factory;
        minLiquidity = _minLiquidity;
    }

    /**
     * @dev Finds and returns newly deployed Uniswap pairs with liquidity exceeding the threshold.
     * @param startIndex The index to start scanning from (to avoid rescanning old pairs).
     * @param endIndex The index to stop scanning at.
     * @return newPairs An array of addresses of pairs meeting the criteria.
     */
    function findNewPairs(uint startIndex, uint endIndex) external view returns (address[] memory newPairs) {
        IUniswapV2Factory factory = IUniswapV2Factory(uniswapV2Factory);
        uint totalPairs = factory.allPairsLength();

        // Ensure indices are valid
        require(startIndex < endIndex, "Invalid index range");
        require(endIndex <= totalPairs, "End index exceeds total pairs");

        // Temporary array to store matching pairs
        address[] memory tempPairs = new address[](endIndex - startIndex);
        uint count = 0;

        for (uint i = startIndex; i < endIndex; i++) {
            address pairAddress = factory.allPairs(i);
            IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

            // Fetch reserves of the pair
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

            // Check if combined liquidity meets the threshold
            uint256 totalLiquidity = uint256(reserve0) + uint256(reserve1);
            if (totalLiquidity >= minLiquidity) {
                tempPairs[count] = pairAddress;
                count++;
            }
        }

        // Copy matching pairs into a properly sized array
        newPairs = new address[](count);
        for (uint i = 0; i < count; i++) {
            newPairs[i] = tempPairs[i];
        }

        return newPairs;
    }
}
```
