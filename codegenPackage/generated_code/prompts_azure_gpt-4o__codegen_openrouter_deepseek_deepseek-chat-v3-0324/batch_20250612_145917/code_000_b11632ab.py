"""
Generated Code Metadata:
========================
Original URL: https://copycoden.pages.dev
Prompt: Write a Solidity contract that uses Uniswap V2 interfaces (`IUniswapV2ERC20`, `IUniswapV2Factory`, `IUniswapV2Pair`) to find newly deployed contracts with specific liquidity requirements, similar to the functionality described in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_b11632ab88a64a7a
Batch ID: 20250612_145917
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
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    function allPairs(uint) external view returns (address pair);
    function allPairsLength() external view returns (uint);
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

interface IUniswapV2ERC20 {
    function totalSupply() external view returns (uint);
}

contract LiquidityFinder {
    IUniswapV2Factory public immutable factory;
    address public immutable WETH;
    
    struct PairInfo {
        address pairAddress;
        address token0;
        address token1;
        uint reserve0;
        uint reserve1;
        uint liquidity;
    }

    constructor(address _factory, address _WETH) {
        factory = IUniswapV2Factory(_factory);
        WETH = _WETH;
    }

    function checkNewPairs(uint minLiquidityETH) external view returns (PairInfo[] memory) {
        uint pairCount = factory.allPairsLength();
        PairInfo[] memory pairs = new PairInfo[](pairCount);
        uint validPairsCount = 0;

        for (uint i = 0; i < pairCount; i++) {
            address pairAddress = factory.allPairs(i);
            IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
            
            address token0 = pair.token0();
            address token1 = pair.token1();
            
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
            uint liquidity = IUniswapV2ERC20(pairAddress).totalSupply();

            bool isWETHPair = (token0 == WETH || token1 == WETH);
            uint ethReserve = token0 == WETH ? reserve0 : reserve1;
            
            if (isWETHPair && ethReserve >= minLiquidityETH) {
                pairs[validPairsCount] = PairInfo({
                    pairAddress: pairAddress,
                    token0: token0,
                    token1: token1,
                    reserve0: reserve0,
                    reserve1: reserve1,
                    liquidity: liquidity
                });
                validPairsCount++;
            }
        }

        // Resize the array to remove empty slots
        PairInfo[] memory filteredPairs = new PairInfo[](validPairsCount);
        for (uint i = 0; i < validPairsCount; i++) {
            filteredPairs[i] = pairs[i];
        }

        return filteredPairs;
    }

    function getPairInfo(address pairAddress) external view returns (PairInfo memory) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        address token0 = pair.token0();
        address token1 = pair.token1();
        
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
        uint liquidity = IUniswapV2ERC20(pairAddress).totalSupply();

        return PairInfo({
            pairAddress: pairAddress,
            token0: token0,
            token1: token1,
            reserve0: reserve0,
            reserve1: reserve1,
            liquidity: liquidity
        });
    }
}
```
