"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate Solidity code for deploying a smart contract that integrates zkSwap Finance's Universal Router to facilitate token swaps across multiple chains.
Generated: DETERMINISTIC_130b0b19d0441812
Batch ID: 20250612_154728
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

/**
 * @title CrossChainTokenSwap
 * @dev A smart contract integrating zkSwap Finance's Universal Router for token swaps across multiple chains
 */
contract CrossChainTokenSwap {
    // Address of zkSwap Universal Router
    address public immutable universalRouter;

    // Event emitted after a successful token swap
    event TokenSwap(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Constructor to initialize the contract with the zkSwap Universal Router address
     * @param _universalRouter Address of the zkSwap Universal Router contract
     */
    constructor(address _universalRouter) {
        require(_universalRouter != address(0), "Invalid router address");
        universalRouter = _universalRouter;
    }

    /**
     * @dev Swap tokens using zkSwap Universal Router
     * @param tokenIn Address of the token to swap from
     * @param tokenOut Address of the token to swap to
     * @param amountIn Amount of tokens to swap
     * @param minAmountOut Minimum amount of tokens to receive (slippage tolerance)
     * @param swapData Encoded data for the swap (specific to zkSwap Universal Router)
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes calldata swapData
    ) external payable {
        require(amountIn > 0, "Amount must be greater than 0");
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token addresses");

        // Transfer input tokens from the user to this contract
        require(
            IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn),
            "Token transfer failed"
        );

        // Approve the router contract to spend the tokens
        require(
            IERC20(tokenIn).approve(universalRouter, amountIn),
            "Approval failed"
        );

        // Perform the swap using the Universal Router
        (bool success, ) = universalRouter.call{value: msg.value}(swapData);
        require(success, "Swap failed");

        // Emit event after successful swap
        emit TokenSwap(msg.sender, tokenIn, tokenOut, amountIn, minAmountOut);
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
