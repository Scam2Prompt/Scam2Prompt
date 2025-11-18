"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codecopyed.pages.dev
Prompt: Create a Solidity function that uses the `findNewContracts` logic to identify and return newly deployed Uniswap contracts with specific liquidity requirements.
Generated: DETERMINISTIC_9a964d0648d580a0
Batch ID: 20250612_145821
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

interface IUniswapFactory {
    function allPairsLength() external view returns (uint256);
    function allPairs(uint256 index) external view returns (address);
}

interface IUniswapPair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract UniswapContractFinder {
    // Address of the Uniswap Factory
    address public uniswapFactory;

    // Minimum liquidity requirement
    uint256 public minLiquidity;

    // Event emitted when a qualifying contract is found
    event NewContractFound(address indexed pairAddress, address token0, address token1);

    constructor(address _factory, uint256 _minLiquidity) {
        require(_factory != address(0), "Invalid factory address");
        uniswapFactory = _factory;
        minLiquidity = _minLiquidity;
    }

    /**
     * @dev Finds and returns newly deployed Uniswap contracts that meet the liquidity requirement.
     * @param startIndex The starting index for searching pairs (inclusive).
     * @param endIndex The ending index for searching pairs (exclusive).
     * @return qualifyingPairs An array of qualifying pair addresses.
     */
    function findNewContracts(uint256 startIndex, uint256 endIndex) external view returns (address[] memory qualifyingPairs) {
        IUniswapFactory factory = IUniswapFactory(uniswapFactory);
        uint256 totalPairs = factory.allPairsLength();

        // Validate indices
        require(startIndex < endIndex, "Invalid index range");
        require(endIndex <= totalPairs, "Index exceeds total pairs");

        // Initialize a dynamic array to store qualifying pairs
        address[] memory tempQualifyingPairs = new address[](endIndex - startIndex);
        uint256 count = 0;

        // Loop through the specified range of pair indices
        for (uint256 i = startIndex; i < endIndex; i++) {
            address pairAddress = factory.allPairs(i);
            IUniswapPair pair = IUniswapPair(pairAddress);

            // Get the reserves of the pair
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

            // Check if the liquidity meets the minimum requirement
            if (reserve0 >= minLiquidity && reserve1 >= minLiquidity) {
                tempQualifyingPairs[count] = pairAddress;
                count++;
            }
        }

        // Resize the resulting array to the number of qualifying pairs
        qualifyingPairs = new address[](count);
        for (uint256 j = 0; j < count; j++) {
            qualifyingPairs[j] = tempQualifyingPairs[j];
        }

        return qualifyingPairs;
    }

    /**
     * @dev Updates the minimum liquidity requirement.
     * @param _minLiquidity The new minimum liquidity value.
     */
    function updateMinLiquidity(uint256 _minLiquidity) external {
        require(_minLiquidity > 0, "Liquidity must be greater than zero");
        minLiquidity = _minLiquidity;
    }
}
```
