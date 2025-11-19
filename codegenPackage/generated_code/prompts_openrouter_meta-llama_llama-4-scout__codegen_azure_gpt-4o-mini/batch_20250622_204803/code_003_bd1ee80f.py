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

// Importing the necessary interfaces from the Uniswap V2 core library
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapInteraction {
    IUniswapV2Factory public uniswapFactory;
    IUniswapV2Pair public uniswapPair;
    address public tokenA;
    address public tokenB;

    // Event to log swap actions
    event Swapped(address indexed sender, uint amountIn, uint amountOut);

    // Constructor to initialize the Uniswap factory and token addresses
    constructor(address _factory, address _tokenA, address _tokenB) {
        uniswapFactory = IUniswapV2Factory(_factory);
        tokenA = _tokenA;
        tokenB = _tokenB;

        // Create a pair for the two tokens if it doesn't exist
        uniswapPair = IUniswapV2Pair(uniswapFactory.getPair(tokenA, tokenB));
        require(address(uniswapPair) != address(0), "Pair does not exist");
    }

    // Function to swap tokens on Uniswap
    function swapTokens(uint amountIn, uint amountOutMin, address to, uint deadline) external {
        // Transfer the specified amount of tokenA from the sender to this contract
        require(IUniswapV2ERC20(tokenA).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the Uniswap pair to spend tokenA
        require(IUniswapV2ERC20(tokenA).approve(address(uniswapPair), amountIn), "Approval failed");

        // Execute the swap
        (uint amountOut) = uniswapPair.swap(amountIn, amountOutMin, to, new bytes(0));

        // Emit an event for the swap
        emit Swapped(msg.sender, amountIn, amountOut);
    }

    // Function to get the reserves of the token pair
    function getReserves() external view returns (uint reserveA, uint reserveB) {
        (reserveA, reserveB, ) = uniswapPair.getReserves();
    }
}
```
