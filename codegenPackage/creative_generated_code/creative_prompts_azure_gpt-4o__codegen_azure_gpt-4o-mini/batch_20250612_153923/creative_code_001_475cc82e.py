"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismm.github.io
Prompt: Generate Solidity code for an Optimism-based smart contract that bundles multiple token swaps into a single transaction to optimize gas costs.
Generated: DETERMINISTIC_475cc82eda23f490
Batch ID: 20250612_153923
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

// Interface for the token swaps (could be Uniswap or any other DEX)
interface ITokenSwap {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Main contract for bundling token swaps
contract TokenSwapper {
    // State variable to hold the address of the token swap contract
    ITokenSwap public tokenSwap;

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the token swap contract address
    constructor(address _tokenSwap) {
        require(_tokenSwap != address(0), "Invalid token swap address");
        tokenSwap = ITokenSwap(_tokenSwap);
    }

    // Function to execute multiple token swaps in a single transaction
    function bundleSwaps(
        address[] calldata tokenIns,
        address[] calldata tokenOuts,
        uint256[] calldata amountsIn,
        uint256[] calldata amountsOutMin,
        uint256 deadline
    ) external {
        require(tokenIns.length == tokenOuts.length, "Input and output token arrays must match");
        require(tokenIns.length == amountsIn.length, "Input token array and amounts must match");
        require(tokenIns.length == amountsOutMin.length, "Output token array and amounts must match");

        for (uint256 i = 0; i < tokenIns.length; i++) {
            // Ensure that the amountIn is greater than 0
            require(amountsIn[i] > 0, "Amount in must be greater than zero");
            
            // Transfer the input tokens from the user to this contract
            IERC20(tokenIns[i]).transferFrom(msg.sender, address(this), amountsIn[i]);

            // Approve the token swap contract to spend the tokens
            IERC20(tokenIns[i]).approve(address(tokenSwap), amountsIn[i]);

            // Execute the swap
            uint256 amountOut = tokenSwap.swap(
                tokenIns[i],
                tokenOuts[i],
                amountsIn[i],
                amountsOutMin[i],
                msg.sender,
                deadline
            );

            // Emit an event for the executed swap
            emit SwapExecuted(tokenIns[i], tokenOuts[i], amountsIn[i], amountOut);
        }
    }
}

// Minimal ERC20 interface for token transfers
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
