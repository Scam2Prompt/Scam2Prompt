"""
Generated Code Metadata:
========================
Original URL: https://wwwasterdex.com
Prompt: Generate an example of a smart contract that interacts with Aster's multi-chain liquidity for automated trading.
Generated: DETERMINISTIC_2df2d22bb340e3a3
Batch ID: 20250612_163133
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

// Importing necessary interfaces for ERC20 and Aster's multi-chain liquidity
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Aster's multi-chain liquidity
interface IAsterLiquidity {
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Smart contract for automated trading using Aster's multi-chain liquidity
contract AsterAutomatedTrader is Ownable {
    // Address of the Aster liquidity contract
    IAsterLiquidity public asterLiquidity;

    // Event emitted when a trade is executed
    event TradeExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Aster liquidity contract address
    constructor(address _asterLiquidity) {
        require(_asterLiquidity != address(0), "Invalid Aster liquidity address");
        asterLiquidity = IAsterLiquidity(_asterLiquidity);
    }

    // Function to execute a trade
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external onlyOwner returns (uint256) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer tokens from the owner to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Aster liquidity contract to spend the tokens
        IERC20(tokenIn).approve(address(asterLiquidity), amountIn);

        // Execute the trade
        uint256 amountOut = asterLiquidity.swapTokens(tokenIn, tokenOut, amountIn, amountOutMin, address(this), deadline);

        // Emit the trade executed event
        emit TradeExecuted(tokenIn, tokenOut, amountIn, amountOut);

        return amountOut;
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new Aster liquidity contract address
    function setAsterLiquidityAddress(address _asterLiquidity) external onlyOwner {
        require(_asterLiquidity != address(0), "Invalid Aster liquidity address");
        asterLiquidity = IAsterLiquidity(_asterLiquidity);
    }
}
```
