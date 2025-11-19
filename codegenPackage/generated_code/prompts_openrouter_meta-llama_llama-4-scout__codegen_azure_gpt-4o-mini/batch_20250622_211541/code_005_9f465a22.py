"""
Generated Code Metadata:
========================
Original URL: https://cowswap.io
Prompt: "Design a smart contract for a cryptocurrency swap platform inspired by CowSwap's architecture on Ethereum blockchain."
Generated: DETERMINISTIC_9f465a22795a1cdb
Batch ID: 20250622_211541
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for a cryptocurrency swap platform
contract CryptoSwap is Ownable, ReentrancyGuard {
    // Event emitted when a swap occurs
    event Swap(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Mapping to store token reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Function to add liquidity to the swap platform
    function addLiquidity(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update reserves
        reserves[token][msg.sender] += amount;
    }

    // Function to swap tokens
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) external nonReentrant {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(amountOutMin > 0, "Amount out minimum must be greater than zero");
        require(reserves[tokenIn][msg.sender] >= amountIn, "Insufficient tokenIn balance");

        // Calculate the amount of tokenOut to send
        uint256 amountOut = getAmountOut(tokenIn, tokenOut, amountIn);
        require(amountOut >= amountOutMin, "Insufficient output amount");

        // Update reserves
        reserves[tokenIn][msg.sender] -= amountIn;
        reserves[tokenOut][msg.sender] += amountOut;

        // Transfer tokens
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit swap event
        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to get the amount of tokenOut for a given amount of tokenIn
    function getAmountOut(address tokenIn, address tokenOut, uint256 amountIn) public view returns (uint256) {
        // Placeholder for actual pricing logic (e.g., using an oracle or liquidity pool)
        // For simplicity, we assume a 1:1 swap rate
        return amountIn; // This should be replaced with actual logic
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(reserves[token][msg.sender] >= amount, "Insufficient balance");

        // Update reserves
        reserves[token][msg.sender] -= amount;

        // Transfer tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
