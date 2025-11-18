"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity contract that includes a `receive()` function for handling Ether and integrates Uniswap V2 core libraries, as outlined in the Uniswap Slippage Bot.
Generated: DETERMINISTIC_573114b93ba43ace
Batch ID: 20250612_154809
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

// Importing the necessary Uniswap V2 interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract SlippageBot {
    // The address of the Uniswap V2 Factory contract
    address public immutable uniswapV2Factory;

    // Event to log received Ether
    event EtherReceived(address indexed sender, uint256 value);

    // Constructor to initialize the Uniswap V2 Factory address
    constructor(address _uniswapV2Factory) {
        require(_uniswapV2Factory != address(0), "Invalid factory address");
        uniswapV2Factory = _uniswapV2Factory;
    }

    // `receive()` function to handle incoming Ether
    receive() external payable {
        require(msg.value > 0, "No Ether sent");
        emit EtherReceived(msg.sender, msg.value);
    }

    // Function to fetch reserves from a Uniswap V2 pair
    function getReserves(address tokenA, address tokenB)
        external
        view
        returns (uint256 reserveA, uint256 reserveB)
    {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token addresses");

        // Sort token addresses to match the Uniswap V2 pair logic
        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);

        // Fetch the pair address from the factory
        address pairAddress = IUniswapV2Factory(uniswapV2Factory).getPair(token0, token1);
        require(pairAddress != address(0), "Pair does not exist");

        // Fetch reserves from the pair contract
        (uint256 reserve0, uint256 reserve1, ) = IUniswapV2Pair(pairAddress).getReserves();

        // Assign reserves based on token order
        (reserveA, reserveB) = tokenA == token0 ? (reserve0, reserve1) : (reserve1, reserve0);
    }

    // Function to calculate the price of tokenA in terms of tokenB
    function calculatePrice(address tokenA, address tokenB)
        external
        view
        returns (uint256 price)
    {
        (uint256 reserveA, uint256 reserveB) = getReserves(tokenA, tokenB);

        // Ensure reserves are non-zero
        require(reserveA > 0 && reserveB > 0, "Insufficient liquidity");

        // Price calculation: reserveB / reserveA
        price = (reserveB * 1e18) / reserveA; // Scale price to 18 decimals
    }
}
```
