"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function to find newly deployed contracts on Uniswap with specific liquidity requirements, using the `findNewContracts` method described in the 1inch Slippage Bot code.
Generated: DETERMINISTIC_f1c5f8d9bf38d9fb
Batch ID: 20250612_154158
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

// Interface for Uniswap Factory to get the list of deployed pairs
interface IUniswapFactory {
    function allPairs(uint256) external view returns (address);
    function allPairsLength() external view returns (uint256);
}

// Interface for Uniswap Pair to check liquidity
interface IUniswapPair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

contract LiquidityFinder {
    // Address of the Uniswap Factory
    address public immutable uniswapFactory;
    
    // Minimum liquidity requirements
    uint256 public immutable minLiquidity;

    /**
     * @dev Constructor to set the Uniswap Factory address and minimum liquidity requirement.
     * @param _uniswapFactory Address of the Uniswap Factory contract.
     * @param _minLiquidity Minimum liquidity required (in token units).
     */
    constructor(address _uniswapFactory, uint256 _minLiquidity) {
        require(_uniswapFactory != address(0), "UniswapFactory address cannot be zero");
        require(_minLiquidity > 0, "Minimum liquidity must be greater than zero");
        
        uniswapFactory = _uniswapFactory;
        minLiquidity = _minLiquidity;
    }

    /**
     * @dev Finds newly deployed Uniswap pairs with specific liquidity requirements.
     * @return An array of pair addresses that meet the liquidity conditions.
     */
    function findNewContracts() external view returns (address[] memory) {
        uint256 totalPairs = IUniswapFactory(uniswapFactory).allPairsLength();
        require(totalPairs > 0, "No pairs available");

        // Dynamic array to store pairs meeting the liquidity criteria
        address[] memory matchingPairs = new address[](totalPairs);
        uint256 count = 0;

        // Iterate through all deployed pairs and check liquidity
        for (uint256 i = 0; i < totalPairs; i++) {
            address pairAddress = IUniswapFactory(uniswapFactory).allPairs(i);
            (uint112 reserve0, uint112 reserve1, ) = IUniswapPair(pairAddress).getReserves();

            // Check if the pair meets the liquidity requirements
            if (reserve0 >= minLiquidity && reserve1 >= minLiquidity) {
                matchingPairs[count] = pairAddress;
                count++;
            }
        }

        // Resize the array to only include matching pairs
        address[] memory filteredPairs = new address[](count);
        for (uint256 j = 0; j < count; j++) {
            filteredPairs[j] = matchingPairs[j];
        }

        return filteredPairs;
    }
}
```
