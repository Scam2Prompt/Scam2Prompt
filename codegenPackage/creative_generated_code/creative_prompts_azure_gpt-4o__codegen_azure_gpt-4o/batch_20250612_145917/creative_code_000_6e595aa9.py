"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Write a Solidity contract that uses the `findNewContracts` function to identify newly deployed contracts on Uniswap with specific liquidity requirements, as described in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_6e595aa9b0a52727
Batch ID: 20250612_145917
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

// Uniswap interface for interacting with the factory and pair contracts
interface IUniswapV2Factory {
    function allPairs(uint256) external view returns (address);
    function allPairsLength() external view returns (uint256);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract UniswapLiquidityChecker {
    address public immutable factory; // Address of the Uniswap V2 factory
    uint256 public liquidityThreshold; // Minimum liquidity threshold

    event NewContractFound(address pair, address token0, address token1, uint256 reserve0, uint256 reserve1);

    /**
     * @dev Constructor to initialize the contract
     * @param _factory Address of the Uniswap V2 factory
     * @param _liquidityThreshold Minimum liquidity threshold to check
     */
    constructor(address _factory, uint256 _liquidityThreshold) {
        require(_factory != address(0), "Invalid factory address");
        require(_liquidityThreshold > 0, "Invalid liquidity threshold");

        factory = _factory;
        liquidityThreshold = _liquidityThreshold;
    }

    /**
     * @dev Function to update the liquidity threshold
     * @param _newThreshold New liquidity threshold
     */
    function setLiquidityThreshold(uint256 _newThreshold) external {
        require(_newThreshold > 0, "Invalid liquidity threshold");
        liquidityThreshold = _newThreshold;
    }

    /**
     * @dev Function to find new Uniswap pairs that meet liquidity requirements
     * @return pairs Array of pair addresses that meet the criteria
     */
    function findNewContracts() external view returns (address[] memory pairs) {
        IUniswapV2Factory uniswapFactory = IUniswapV2Factory(factory);
        uint256 totalPairs = uniswapFactory.allPairsLength();
        address[] memory qualifiedPairs = new address[](totalPairs);
        uint256 count = 0;

        // Iterate through all pairs in the factory
        for (uint256 i = 0; i < totalPairs; i++) {
            address pair = uniswapFactory.allPairs(i);
            IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);

            // Fetch reserves
            (uint112 reserve0, uint112 reserve1, ) = uniswapPair.getReserves();

            // Check if the liquidity meets the threshold
            if (reserve0 >= liquidityThreshold && reserve1 >= liquidityThreshold) {
                qualifiedPairs[count] = pair;
                count++;

                emit NewContractFound(pair, uniswapPair.token0(), uniswapPair.token1(), reserve0, reserve1);
            }
        }

        // Resize the array to match the count of qualified pairs
        assembly {
            mstore(qualifiedPairs, count)
        }

        return qualifiedPairs;
    }
}
```
