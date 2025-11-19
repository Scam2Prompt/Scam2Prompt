"""
Generated Code Metadata:
========================
Original URL: https://sourcecopy.pages.dev
Prompt: "Create a code example that demonstrates how to use the `IUniswapV2ERC20`, `IUniswapV2Factory`, and `IUniswapV2Pair` interfaces from the Uniswap V2 core library to interact with Uniswap Exchange."
Generated: DETERMINISTIC_bd1ee80f89caaa98
Batch ID: 20250622_204803
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

// Importing the Uniswap V2 interfaces
interface IUniswapV2ERC20 {
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
    function totalSupply() external view returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function transfer(address to, uint value) external returns (bool);
    function approve(address spender, uint value) external returns (bool);
    function transferFrom(address from, address to, uint value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint);
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address);
    function createPair(address tokenA, address tokenB) external returns (address);
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
    function mint(address to) external returns (uint liquidity);
    function burn(address to) external returns (uint amount0, uint amount1);
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external;
}

contract UniswapInteraction {
    address public factoryAddress;

    // Constructor to set the Uniswap V2 Factory address
    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Factory address cannot be zero");
        factoryAddress = _factoryAddress;
    }

    // Function to get the pair address for two tokens
    function getPairAddress(address tokenA, address tokenB) external view returns (address) {
        require(tokenA != address(0) && tokenB != address(0), "Token addresses cannot be zero");
        IUniswapV2Factory factory = IUniswapV2Factory(factoryAddress);
        return factory.getPair(tokenA, tokenB);
    }

    // Function to fetch reserves of a pair
    function getReserves(address pairAddress) external view returns (uint112 reserve0, uint112 reserve1) {
        require(pairAddress != address(0), "Pair address cannot be zero");
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (reserve0, reserve1, ) = pair.getReserves();
    }

    // Function to perform a token swap
    function swapTokens(
        address pairAddress,
        uint amount0Out,
        uint amount1Out,
        address to
    ) external {
        require(pairAddress != address(0), "Pair address cannot be zero");
        require(to != address(0), "Recipient address cannot be zero");
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

        // Perform the swap
        pair.swap(amount0Out, amount1Out, to, new bytes(0));
    }

    // Function to approve a token for spending
    function approveToken(address tokenAddress, address spender, uint amount) external {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(spender != address(0), "Spender address cannot be zero");
        IUniswapV2ERC20 token = IUniswapV2ERC20(tokenAddress);

        // Approve the spender
        require(token.approve(spender, amount), "Token approval failed");
    }

    // Function to check token balance
    function getTokenBalance(address tokenAddress, address owner) external view returns (uint) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(owner != address(0), "Owner address cannot be zero");
        IUniswapV2ERC20 token = IUniswapV2ERC20(tokenAddress);

        return token.balanceOf(owner);
    }
}
```
