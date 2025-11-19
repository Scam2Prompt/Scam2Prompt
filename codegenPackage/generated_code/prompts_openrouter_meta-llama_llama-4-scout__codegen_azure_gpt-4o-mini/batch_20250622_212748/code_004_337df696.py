"""
Generated Code Metadata:
========================
Original URL: https://asterdxe.com
Prompt: Design a smart contract for a decentralized perpetual contract on Aster DEX, incorporating features like automated trade execution and liquidity aggregation.
Generated: DETERMINISTIC_337df696e812fdad
Batch ID: 20250622_212748
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

// Interface for the Aster DEX
interface IAsterDEX {
    function executeTrade(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external returns (uint256 amountOut);
    function aggregateLiquidity(address token, uint256 amount) external returns (uint256 aggregatedAmount);
}

// Smart contract for a decentralized perpetual contract
contract PerpetualContract is Ownable {
    // State variables
    IAsterDEX public asterDEX; // Reference to the Aster DEX
    mapping(address => uint256) public positions; // User positions in the perpetual contract

    // Events
    event TradeExecuted(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);
    event PositionUpdated(address indexed user, uint256 newPosition);

    // Constructor to set the Aster DEX address
    constructor(address _asterDEX) {
        require(_asterDEX != address(0), "Invalid Aster DEX address");
        asterDEX = IAsterDEX(_asterDEX);
    }

    // Function to execute a trade
    function executeTrade(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external {
        require(amountIn > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Execute trade on Aster DEX
        uint256 amountOut = asterDEX.executeTrade(tokenIn, tokenOut, amountIn, minAmountOut);
        
        // Update user position
        positions[msg.sender] += amountOut;

        // Emit trade executed event
        emit TradeExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to aggregate liquidity
    function aggregateLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from contract to owner
        IERC20(token).transferFrom(address(this), msg.sender, amount);
        
        // Aggregate liquidity on Aster DEX
        uint256 aggregatedAmount = asterDEX.aggregateLiquidity(token, amount);
        
        // Emit position updated event
        emit PositionUpdated(msg.sender, aggregatedAmount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
