"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Write a Solidity smart contract that uses Uniswap V2 interfaces (`IUniswapV2ERC20`, `IUniswapV2Factory`, and `IUniswapV2Pair`) to find newly deployed contracts with specific liquidity requirements, similar to the functionality described in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_55a8d18e36ae3724
Batch ID: 20250612_151347
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

// Import required Uniswap V2 interfaces
interface IUniswapV2Factory {
    function allPairs(uint) external view returns (address);
    function allPairsLength() external view returns (uint);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

interface IUniswapV2ERC20 {
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
}

contract LiquidityScanner {

    // Address of the Uniswap V2 factory contract
    address public immutable uniswapV2Factory;
    
    // Minimum liquidity requirement threshold
    uint256 public immutable minLiquidityThreshold;

    // Event emitted when a pair with sufficient liquidity is found
    event PairWithSufficientLiquidity(address indexed pair, address indexed token0, address indexed token1, uint112 reserve0, uint112 reserve1);

    /**
     * @dev Constructor to set the Uniswap V2 factory address and liquidity threshold.
     * @param _uniswapV2Factory Address of the Uniswap V2 factory contract.
     * @param _minLiquidityThreshold Minimum liquidity threshold to filter pairs.
     */
    constructor(address _uniswapV2Factory, uint256 _minLiquidityThreshold) {
        require(_uniswapV2Factory != address(0), "Invalid Uniswap V2 Factory address");
        require(_minLiquidityThreshold > 0, "Liquidity threshold must be greater than zero");
        
        uniswapV2Factory = _uniswapV2Factory;
        minLiquidityThreshold = _minLiquidityThreshold;
    }

    /**
     * @dev Function to scan all pairs in the Uniswap V2 factory and find those with sufficient liquidity.
     * Emits an event for each pair that meets the liquidity requirements.
     */
    function scanPairs() external {
        // Get the total number of pairs in the factory
        uint256 totalPairs = IUniswapV2Factory(uniswapV2Factory).allPairsLength();
        
        for (uint256 i = 0; i < totalPairs; i++) {
            // Get the pair address
            address pairAddress = IUniswapV2Factory(uniswapV2Factory).allPairs(i);
            
            // Get the reserves of the pair
            (uint112 reserve0, uint112 reserve1, ) = IUniswapV2Pair(pairAddress).getReserves();
            
            // Get the tokens in the pair
            address token0 = IUniswapV2Pair(pairAddress).token0();
            address token1 = IUniswapV2Pair(pairAddress).token1();
            
            // Check if the reserves meet the minimum liquidity threshold
            if (reserve0 >= minLiquidityThreshold && reserve1 >= minLiquidityThreshold) {
                emit PairWithSufficientLiquidity(pairAddress, token0, token1, reserve0, reserve1);
            }
        }
    }

    /**
     * @dev Utility function to get the metadata of a token.
     * @param token Address of the token.
     * @return symbol Symbol of the token.
     * @return decimals Decimals of the token.
     */
    function getTokenMetadata(address token) external view returns (string memory symbol, uint8 decimals) {
        symbol = IUniswapV2ERC20(token).symbol();
        decimals = IUniswapV2ERC20(token).decimals();
    }
}
```

This Solidity code defines a `LiquidityScanner` contract that interacts with Uniswap V2 factory and pair interfaces. It scans for pairs with liquidity reserves meeting a given threshold, emitting an event for each qualified pair. The code is well-documented and follows best practices, including error handling and proper comments.
