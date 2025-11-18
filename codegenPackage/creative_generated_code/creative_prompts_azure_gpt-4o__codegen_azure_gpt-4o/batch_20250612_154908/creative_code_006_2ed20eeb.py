"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap3.vercel.app
Prompt: Write Solidity code to interact with Uniswap v3's router contract for executing multi-hop swaps.
Generated: DETERMINISTIC_2ed20eeb15d5e4dd
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Interface for Uniswap V3's router contract
interface ISwapRouter {
    struct ExactInputParams {
        bytes path; // Encodes the path to follow for the swap (token1 -> token2 -> token3)
        address recipient; // Address that will receive the output token
        uint256 deadline; // Timestamp after which the trade is invalid
        uint256 amountIn; // The amount of input token to swap
        uint256 amountOutMinimum; // Minimum amount of output token to receive
    }

    function exactInput(ExactInputParams calldata params) external payable returns (uint256);
}

contract MultiHopSwap {
    address public immutable swapRouter; // Address of the Uniswap V3 router contract

    constructor(address _swapRouter) {
        require(_swapRouter != address(0), "Invalid swap router address");
        swapRouter = _swapRouter;
    }

    // Approve tokens for swapping
    function approveToken(
        address token,
        uint256 amount
    ) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        (bool success, bytes memory data) = token.call(
            abi.encodeWithSignature("approve(address,uint256)", swapRouter, amount)
        );

        require(
          succwss
