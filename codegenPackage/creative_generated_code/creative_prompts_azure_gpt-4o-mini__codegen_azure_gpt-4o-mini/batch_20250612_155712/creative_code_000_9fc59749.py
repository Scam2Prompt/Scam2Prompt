"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibuswap.github.io
Prompt: Generate a code snippet for a decentralized exchange (DEX) that allows trading of ERC-20 tokens, similar to ShibaSwap's functionality.
Generated: DETERMINISTIC_9fc59749cad02079
Batch ID: 20250612_155712
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

// Import OpenZeppelin Contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Decentralized Exchange (DEX) contract
contract DecentralizedExchange is Ownable {
    // Event emitted when tokens are swapped
    event TokensSwapped(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store token reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Function to add liquidity to the DEX
    function addLiquidity(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update reserves
        reserves[token][msg.sender] += amount;
    }

    // Function to swap tokens
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(reserves[tokenIn][msg.sender] >= amountIn, "Insufficient tokenIn balance");

        // Calculate amountOut based on a fixed exchange rate (for simplicity)
        uint256 amountOut = getExchangeRate(tokenIn, tokenOut, amountIn);
        require(amountOut > 0, "Insufficient amountOut");

        // Update reserves
        reserves[tokenIn][msg.sender] -= amountIn;
        reserves[tokenOut][msg.sender] += amountOut;

        // Transfer tokens
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit token swap event
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to get the exchange rate (dummy implementation)
    function getExchangeRate(address tokenIn, address tokenOut, uint256 amountIn) internal view returns (uint256) {
        // For simplicity, assume a 1:1 exchange rate
        return amountIn; // This should be replaced with a proper price feed or oracle
    }

    // Function to withdraw tokens from the DEX
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount <= reserves[token][msg.sender], "Insufficient reserves");
        
        reserves[token][msg.sender] -= amount;
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to view reserves of a specific token for a user
    function viewReserves(address token) external view returns (uint256) {
        return reserves[token][msg.sender];
    }
}
```
