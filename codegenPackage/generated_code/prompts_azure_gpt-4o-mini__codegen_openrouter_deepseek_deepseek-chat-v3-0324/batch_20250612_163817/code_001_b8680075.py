"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: How can I implement a function in Solidity to find newly deployed contracts on Uniswap Exchange using the provided contract structure?
Generated: DETERMINISTIC_b8680075e0a44a29
Batch ID: 20250612_163817
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

interface IUniswapV2Factory {
    event PairCreated(address indexed token0, address indexed token1, address pair, uint);
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    function allPairs(uint) external view returns (address pair);
    function allPairsLength() external view returns (uint);
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

contract UniswapPairFinder {
    IUniswapV2Factory public uniswapFactory;
    
    // Event to log newly detected pairs
    event NewPairDetected(address indexed token0, address indexed token1, address pairAddress);
    
    /**
     * @dev Initialize with Uniswap V2 Factory address
     * @param _factoryAddress Address of the Uniswap V2 Factory contract
     */
    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Invalid factory address");
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }
    
    /**
     * @dev Check for new pairs created since last check
     * @param lastKnownPairCount The number of pairs known from previous check
     * @return newPairs Array of newly created pair addresses
     */
    function findNewPairs(uint lastKnownPairCount) external returns (address[] memory newPairs) {
        uint currentPairCount = uniswapFactory.allPairsLength();
        
        require(currentPairCount >= lastKnownPairCount, "Pair count cannot decrease");
        
        uint newPairCount = currentPairCount - lastKnownPairCount;
        newPairs = new address[](newPairCount);
        
        for (uint i = 0; i < newPairCount; i++) {
            address pairAddress = uniswapFactory.allPairs(lastKnownPairCount + i);
            newPairs[i] = pairAddress;
            
            // Emit event for each new pair
            emit NewPairDetected(
                IUniswapV2Pair(pairAddress).token0(),
                IUniswapV2Pair(pairAddress).token1(),
                pairAddress
            );
        }
        
        return newPairs;
    }
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}
```
