"""
Generated Code Metadata:
========================
Original URL: https://web-frax-finance.github.io
Prompt: Design a simple decentralized exchange (DEX) protocol using Frax Finance's AMM model, including a basic smart contract in Solidity for liquidity provision and token swapping.
Generated: DETERMINISTIC_45faf81c97ff3deb
Batch ID: 20250622_210821
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Simple Decentralized Exchange (DEX) contract
contract SimpleDEX is Ownable {
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    // Event emitted when a swap occurs
    event Swapped(address indexed trader, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Struct to hold liquidity information
    struct Liquidity {
        uint256 amountA;
        uint256 amountB;
    }

    // Mapping to track liquidity for each provider
    mapping(address => Liquidity) public liquidityProviders;

    // Function to add liquidity to the DEX
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens from the provider to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);

        // Update the liquidity provider's balance
        liquidityProviders[msg.sender].amountA += amountA;
        liquidityProviders[msg.sender].amountB += amountB;

        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    // Function to swap tokens
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than zero");

        // Calculate the amount of tokenOut to be received (simple 1:1 for demonstration)
        uint256 amountOut = amountIn; // In a real DEX, this would involve a pricing algorithm

        // Transfer tokenIn from the trader to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        // Transfer tokenOut from the contract to the trader
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw liquidity
    function withdrawLiquidity(address tokenA, address tokenB) external onlyOwner {
        uint256 amountA = liquidityProviders[msg.sender].amountA;
        uint256 amountB = liquidityProviders[msg.sender].amountB;

        require(amountA > 0 || amountB > 0, "No liquidity to withdraw");

        // Reset the provider's liquidity
        liquidityProviders[msg.sender].amountA = 0;
        liquidityProviders[msg.sender].amountB = 0;

        // Transfer tokens back to the provider
        if (amountA > 0) {
            IERC20(tokenA).transfer(msg.sender, amountA);
        }
        if (amountB > 0) {
            IERC20(tokenB).transfer(msg.sender, amountB);
        }
    }
}
```
