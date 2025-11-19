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

import "@mooniswap/contracts/IMooniswap.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract MooniswapSwapper {
    using SafeERC20 for IERC20;

    /**
     * @dev Performs a token swap with low slippage using Mooniswap
     * @param mooniswapPool The Mooniswap pool contract address
     * @param srcToken The token to swap from
     * @param dstToken The token to swap to
     * @param amount The amount of srcToken to swap
     * @param minReturn The minimum amount of dstToken to receive (slippage protection)
     * @param deadline The timestamp after which the transaction will revert
     * @param referral The referral address (can be address(0))
     */
    function swapWithLowSlippage(
        IMooniswap mooniswapPool,
        IERC20 srcToken,
        IERC20 dstToken,
        uint256 amount,
        uint256 minReturn,
        uint256 deadline,
        address payable referral
    ) external {
        // Verify deadline hasn't passed
        require(block.timestamp <= deadline, "MooniswapSwapper: Deadline expired");

        // Transfer tokens from sender to this contract
        srcToken.safeTransferFrom(msg.sender, address(this), amount);

        // Approve Mooniswap to spend srcToken
        srcToken.safeIncreaseAllowance(address(mooniswapPool), amount);

        // Get expected return amount for better slippage estimation
        uint256 expectedReturn = mooniswapPool.getReturn(
            srcToken,
            dstToken,
            amount
        );

        // Verify expected return meets minimum requirements
        require(
            expectedReturn >= minReturn,
            "MooniswapSwapper: Expected return too low"
        );

        // Perform the swap
        uint256 receivedAmount = mooniswapPool.swap{value: 0}(
            srcToken,
            dstToken,
            amount,
            minReturn,
            referral,
            new bytes(0)
        );

        // Transfer received tokens to sender
        dstToken.safeTransfer(msg.sender, receivedAmount);
    }

    /**
     * @dev Estimates the return amount for a potential swap
     * @param mooniswapPool The Mooniswap pool contract address
     * @param srcToken The token to swap from
     * @param dstToken The token to swap to
     * @param amount The amount of srcToken to swap
     * @return The estimated amount of dstToken to receive
     */
    function estimateSwap(
        IMooniswap mooniswapPool,
        IERC20 srcToken,
        IERC20 dstToken,
        uint256 amount
    ) external view returns (uint256) {
        return mooniswapPool.getReturn(srcToken, dstToken, amount);
    }
}
```
