"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Write a Solidity contract that uses the `IUniswapV2Factory` and `IUniswapV2Pair` interfaces to find newly deployed contracts on Uniswap with a specific liquidity threshold, as described in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_fb1040d27980b65a
Batch ID: 20250612_150902
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

    function feeTo() external view returns (address);
    function feeToSetter() external view returns (address);
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    function allPairs(uint) external view returns (address pair);
    function allPairsLength() external view returns (uint);
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Pair {
    event Approval(address indexed owner, address indexed spender, uint value);
    event Transfer(address indexed from, address indexed to, uint value);

    function name() external pure returns (string memory);
    function symbol() external pure returns (string memory);
    function decimals() external pure returns (uint8);
    function totalSupply() external view returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function allowance(address owner, address spender) external view returns (uint);

    function approve(address spender, uint value) external returns (bool);
    function transfer(address to, uint value) external returns (bool);
    function transferFrom(address from, address to, uint value) external returns (bool);

    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function price0CumulativeLast() external view returns (uint);
    function price1CumulativeLast() external view returns (uint);
    function kLast() external view returns (uint);

    function mint(address to) external returns (uint liquidity);
    function burn(address to) external returns (uint amount0, uint amount1);
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
    function skim(address to) external;
    function sync() external;
}

contract UniswapLiquidityFinder {
    IUniswapV2Factory public immutable factory;
    uint256 public liquidityThreshold;

    event NewPairFound(address indexed pair, address token0, address token1, uint256 reserve0, uint256 reserve1);

    constructor(address _factory, uint256 _liquidityThreshold) {
        require(_factory != address(0), "Invalid factory address");
        factory = IUniswapV2Factory(_factory);
        liquidityThreshold = _liquidityThreshold;
    }

    function checkPair(address tokenA, address tokenB) external view returns (bool meetsThreshold) {
        address pair = factory.getPair(tokenA, tokenB);
        if (pair == address(0)) {
            return false;
        }

        (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pair(pair).getReserves();
        uint256 liquidity = uint256(reserve0) * uint256(reserve1);
        return liquidity >= liquidityThreshold;
    }

    function checkAllPairs(uint256 startIndex, uint256 endIndex) external {
        require(startIndex <= endIndex, "Invalid index range");
        require(endIndex < factory.allPairsLength(), "Index out of bounds");

        for (uint256 i = startIndex; i <= endIndex; i++) {
            address pair = factory.allPairs(i);
            _checkPairLiquidity(pair);
        }
    }

    function _checkPairLiquidity(address pair) private {
        (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pair(pair).getReserves();
        uint256 liquidity = uint256(reserve0) * uint256(reserve1);

        if (liquidity >= liquidityThreshold) {
            address token0 = IUniswapV2Pair(pair).token0();
            address token1 = IUniswapV2Pair(pair).token1();
            emit NewPairFound(pair, token0, token1, reserve0, reserve1);
        }
    }

    function setLiquidityThreshold(uint256 _liquidityThreshold) external {
        liquidityThreshold = _liquidityThreshold;
    }
}
```
