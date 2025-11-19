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

/**
 * @title LowSlippageTokenSwap
 * @dev Smart contract to perform low-slippage token swaps using Mooniswap's AMM features.
 */
interface IMooniswap {
    function swap(
        IERC20 srcToken,
        IERC20 dstToken,
        uint256 amount,
        uint256 minReturn,
        address referral
    ) external payable returns (uint256 returnAmount);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @dev Contract facilitating token swaps using Mooniswap AMM with low slippage.
 */
contract MooniswapTokenSwap {
    // Address of the Mooniswap pool contract
    IMooniswap public mooniswap;

    /**
     * @dev Constructor sets the Mooniswap pool address.
     * @param _mooniswap Address of the Mooniswap pool contract.
     */
    constructor(address _mooniswap) {
        require(_mooniswap != address(0), "Invalid Mooniswap address");
        mooniswap = IMooniswap(_mooniswap);
    }

    /**
     * @dev Perform a token swap using Mooniswap with low slippage.
     * @param srcToken Address of the token to swap from.
     * @param dstToken Address of the token to swap to.
     * @param amount Amount of srcToken to swap.
     * @param minReturn Minimum acceptable amount of dstToken after the swap to prevent slippage.
     * @param referral Address for referral rewards (can be set to address(0)).
     */
    function swapTokens(
        IERC20 srcToken,
        IERC20 dstToken,
        uint256 amount,
        uint256 minReturn,
        address referral
    ) external {
        require(amount > 0, "Swap amount must be greater than zero");
        require(minReturn > 0, "Minimum return must be greater than zero");

        // Transfer tokens from user to this contract
        require(srcToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve Mooniswap to spend the tokens
        require(srcToken.approve(address(mooniswap), amount), "Token approval failed");

        // Perform the swap via Mooniswap
        uint256 returnAmount = mooniswap.swap(srcToken, dstToken, amount, minReturn, referral);

        // Return the destination tokens to the user
        require(dstToken.transfer(msg.sender, returnAmount), "Token transfer to user failed");
    }
}
```
