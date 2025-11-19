"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismm.github.io
Prompt: Explain how to use Mooniswap's AMM features to achieve low-slippage token swaps in a smart contract.
Generated: DETERMINISTIC_c8ac66833102fbae
Batch ID: 20250612_155727
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Mooniswap contract
interface IMooniswap {
    function swap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address recipient
    ) external returns (uint256 returnAmount);
}

// Smart contract to facilitate low-slippage token swaps using Mooniswap
contract LowSlippageTokenSwap is Ownable {
    using SafeMath for uint256;

    // Address of the Mooniswap contract
    IMooniswap public mooniswap;

    // Event to log successful swaps
    event SwapExecuted(address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Mooniswap contract address
    constructor(address _mooniswapAddress) {
        require(_mooniswapAddress != address(0), "Invalid Mooniswap address");
        mooniswap = IMooniswap(_mooniswapAddress);
    }

    // Function to swap tokens with low slippage
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount
    ) external {
        require(fromToken != address(0), "Invalid fromToken address");
        require(toToken != address(0), "Invalid toToken address");
        require(fromAmount > 0, "Amount must be greater than zero");
        require(minReturnAmount > 0, "Minimum return amount must be greater than zero");

        // Transfer tokens from user to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), fromAmount);

        // Approve Mooniswap to spend the tokens
        IERC20(fromToken).approve(address(mooniswap), fromAmount);

        // Execute the token swap
        uint256 returnAmount = mooniswap.swap(fromToken, toToken, fromAmount, minReturnAmount, msg.sender);

        // Emit event for the swap
        emit SwapExecuted(fromToken, toToken, fromAmount, returnAmount);
    }

    // Function to withdraw tokens from the contract (owner only)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
