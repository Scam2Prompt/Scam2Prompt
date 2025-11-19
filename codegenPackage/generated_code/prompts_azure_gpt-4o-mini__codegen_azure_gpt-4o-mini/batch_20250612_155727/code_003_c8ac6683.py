"""
Generated Code Metadata:
========================
Original URL: https://optimismm.github.io
Prompt: Explain how to use Mooniswap's AMM features to achieve low-slippage token swaps in a smart contract.
Generated: DETERMINISTIC_c8ac66833102fbae
Batch ID: 20250612_155727
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

// Interface for Mooniswap's AMM
interface IMooniswap {
    function swap(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 fromAmount,
        uint256 minReturn,
        address recipient
    ) external returns (uint256);
}

// Smart contract to interact with Mooniswap's AMM
contract MooniswapSwapper is Ownable {
    // Address of the Mooniswap contract
    IMooniswap public mooniswap;

    // Event to log successful swaps
    event SwapExecuted(address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Mooniswap contract address
    constructor(address _mooniswap) {
        require(_mooniswap != address(0), "Invalid Mooniswap address");
        mooniswap = IMooniswap(_mooniswap);
    }

    // Function to swap tokens using Mooniswap's AMM
    function swapTokens(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 fromAmount,
        uint256 minReturn
    ) external {
        // Validate input parameters
        require(fromAmount > 0, "Amount must be greater than zero");
        require(minReturn > 0, "Minimum return must be greater than zero");

        // Transfer tokens from the user to this contract
        require(fromToken.transferFrom(msg.sender, address(this), fromAmount), "Transfer failed");

        // Approve the Mooniswap contract to spend the tokens
        require(fromToken.approve(address(mooniswap), fromAmount), "Approval failed");

        // Execute the swap
        uint256 amountOut = mooniswap.swap(fromToken, toToken, fromAmount, minReturn, msg.sender);

        // Emit an event for the swap
        emit SwapExecuted(address(fromToken), address(toToken), fromAmount, amountOut);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
