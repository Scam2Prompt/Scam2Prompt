"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Write a Solidity contract that uses the Uniswap V2 Factory and Pair interfaces to find newly deployed contracts with specific liquidity requirements, similar to the functionality described in the UniswapSlippageBot contract.
Generated: DETERMINISTIC_9c0b1a13a3a55f17
Batch ID: 20250612_154741
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

// Import the necessary Uniswap V2 interfaces
interface IUniswapV2Factory {
    function allPairs(uint256) external view returns (address);
    function allPairsLength() external view returns (uint256);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract LiquidityTracker {
    // Address of the Uniswap V2 Factory contract
    address public uniswapV2Factory;

    // Event emitted for newly found pair contracts with specific liquidity requirements
    event NewPairFound(address indexed pair, address token0, address token1, uint256 reserve0, uint256 reserve1);

    // Constructor to initialize the factory address
    constructor(address _uniswapV2Factory) {
        require(_uniswapV2Factory != address(0), "Invalid factory address");
        uniswapV2Factory = _uniswapV2Factory;
    }

    /**
     * @notice Check all pairs in the Uniswap V2 Factory for specified liquidity requirements.
     * @param minReserve0 Minimum reserve for token0
     * @param minReserve1 Minimum reserve for token1
     */
    function checkPairs(uint256 minReserve0, uint256 minReserve1) external {
        IUniswapV2Factory factory = IUniswapV2Factory(uniswapV2Factory);

        // Get the total number of pairs in the factory
        uint256 pairCount = factory.allPairsLength();

        // Iterate through all pairs
        for (uint256 i = 0; i < pairCount; i++) {
            address pairAddress = factory.allPairs(i);

            // Interface with the pair contract
            IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

            // Fetch reserve values
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

            // Fetch token addresses
            address token0 = pair.token0();
            address token1 = pair.token1();

            // Check if the reserves meet the criteria
            if (reserve0 >= minReserve0 && reserve1 >= minReserve1) {
                emit NewPairFound(pairAddress, token0, token1, reserve0, reserve1);
            }
        }
    }
}
```
