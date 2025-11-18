"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfinty.github.io
Prompt: Develop a decentralized application (dApp) that integrates Axie Infinity's AMM model to enable users to trade ERC-20 tokens directly from their Ethereum wallets.
Generated: DETERMINISTIC_8814fbbe4650d5b9
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC20 interface and SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Axie Infinity AMM (Automated Market Maker) functionality
interface IAxieInfinityAMM {
    function trade(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient
    ) external returns (uint256 amountOut);
}

contract TokenTrader {
    using SafeMath for uint256;

    // Address of the Axie Infinity AMM contract
    IAxieInfinityAMM public amm;

    // Event emitted when a trade is executed
    event TradeExecuted(
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOut,
        address indexed recipient
    );

    // Constructor to set the AMM contract address
    constructor(address _ammAddress) {
        require(_ammAddress != address(0), "Invalid AMM address");
        amm = IAxieInfinityAMM(_ammAddress);
    }

    // Function to trade tokens through the Axie Infinity AMM
    function tradeTokens(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 minAmountOut
    ) external returns (uint256) {
        require(amountIn > 0, "Amount must be greater than zero");
        require(minAmountOut > 0, "Minimum output amount must be greater than zero");
        require(fromToken != toToken, "Cannot trade the same token");

        // Transfer tokens from the caller to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the AMM to spend the tokens
        IERC20(fromToken).approve(address(amm), amountIn);
        
        // Execute the trade
        uint256 amountOut = amm.trade(fromToken, toToken, amountIn, minAmountOut, msg.sender);

        // Emit the trade executed event
        emit TradeExecuted(fromToken, toToken, amountIn, amountOut, msg.sender);

        return amountOut;
    }
}
```
