"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botgptcode.pages.dev
Prompt: Write a Solidity smart contract that integrates Uniswap V2 ERC20, Factory, and Pair interfaces, replicating the structure of the OneinchSlippageBot from https://botgptcode.pages.dev.
Generated: DETERMINISTIC_83cf6427bdb94a18
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

// Importing interfaces for Uniswap V2
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function decimals() external view returns (uint8);
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract UniswapV2IntegrationBot {
    address public owner;
    IUniswapV2Factory public uniswapFactory;

    // Events for logging key actions
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event SwapExecuted(address tokenA, address tokenB, uint256 amountIn, uint256 amountOut);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _factoryAddress) {
        owner = msg.sender;
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    // Transfer ownership for contract management
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address is invalid");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fetches pair reserves for slippage calculation
    function getReserves(address tokenA, address tokenB) external view returns (uint112 reserveA, uint112 reserveB) {
        address pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        (uint112 reserve0, uint112 reserve1, ) = uniswapPair.getReserves();

        if (uniswapPair.token0() == tokenA) {
            reserveA = reserve0;
            reserveB = reserve1;
        } else {
            reserveA = reserve1;
            reserveB = reserve0;
        }
    }

    // Executes a swap with slippage protection
    function executeSwap(
        address tokenA,
        address tokenB,
        uint256 amountIn,
        uint256 minAmountOut
    ) external onlyOwner {
        address pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        IERC20(tokenA).transferFrom(msg.sender, pair, amountIn);

        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);

        (uint112 reserve0, uint112 reserve1, ) = uniswapPair.getReserves();

        uint256 amountOut;
        if (uniswapPair.token0() == tokenA) {
            amountOut = getAmountOut(amountIn, reserve0, reserve1);
        } else {
            amountOut = getAmountOut(amountIn, reserve1, reserve0);
        }

        require(amountOut >= minAmountOut, "Slippage exceeded");

        IERC20(tokenB).transferFrom(pair, msg.sender, amountOut);

        emit SwapExecuted(tokenA, tokenB, amountIn, amountOut);
    }

    // Helper function to calculate output amount based on Uniswap formula
    function getAmountOut(
        uint256 amountIn,
        uint112 reserveIn,
        uint112 reserveOut
    ) public pure returns (uint256) {
        require(amountIn > 0, "Invalid input amount");
        require(reserveIn > 0 && reserveOut > 0, "Invalid reserves");

        uint256 amountInWithFee = amountIn * 997; // Uniswap charges 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = reserveIn * 1000 + amountInWithFee;

        return numerator / denominator;
    }

    // Recover tokens mistakenly sent to the contract
    function recoverTokens(address tokenAddress) external onlyOwner {
        uint256 balance = IERC20(tokenAddress).balanceOf(address(this));
        require(balance > 0, "No tokens to recover");

        IERC20(tokenAddress).transfer(owner, balance);
    }
}
```
