"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswaparbitrum.github.io
Prompt: Create a smart contract in Solidity that utilizes Sushiswap Arbitrum for batch token swaps, optimizing for low transaction fees and high throughput.
Generated: DETERMINISTIC_97e6e492708e7b11
Batch ID: 20250612_150440
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

import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SushiSwapBatchSwap {
    // The router for Sushiswap on Arbitrum
    IUniswapV2Router02 public sushiRouter;

    // Event emitted when a batch swap is executed
    event BatchSwapExecuted(address indexed user, address[] tokens, uint256[] amountsIn, uint256[] amountsOut);

    // Constructor to set the router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        sushiRouter = IUniswapV2Router02(_router);
    }

    /**
     * @notice Executes a batch token swap on Sushiswap
     * @param tokens The addresses of the tokens to be swapped
     * @param amountsIn The amounts of tokens to swap
     * @param amountsOutMin The minimum amounts of tokens expected to receive
     * @param to The address to receive the output tokens
     * @param deadline The timestamp by which the swap must be completed
     */
    function batchSwap(
        address[] calldata tokens,
        uint256[] calldata amountsIn,
        uint256[] calldata amountsOutMin,
        address to,
        uint256 deadline
    ) external {
        require(tokens.length == amountsIn.length, "Tokens and amountsIn length mismatch");
        require(tokens.length == amountsOutMin.length, "Tokens and amountsOutMin length mismatch");

        // Transfer the input tokens from the user to the contract
        for (uint256 i = 0; i < tokens.length; i++) {
            IERC20(tokens[i]).transferFrom(msg.sender, address(this), amountsIn[i]);
        }

        // Approve the router to spend tokens
        for (uint256 i = 0; i < tokens.length; i++) {
            IERC20(tokens[i]).approve(address(sushiRouter), amountsIn[i]);
        }

        // Perform the swaps
        for (uint256 i = 0; i < tokens.length; i++) {
            address[] memory path = new address[](2);
            path[0] = tokens[i];  // Input token
            path[1] = sushiRouter.WETH(); // Assuming output token is WETH; can be modified based on use case

            // Execute the swap
            sushiRouter.swapExactTokensForTokens(
                amountsIn[i],
                amountsOutMin[i],
                path,
                to,
                deadline
            );
        }

        emit BatchSwapExecuted(msg.sender, tokens, amountsIn, amountsOutMin);
    }

    /**
     * @notice Allows the contract to receive ETH from swaps
     */
    receive() external payable {}

    /**
     * @notice Withdraw tokens from the contract in case of an emergency
     * @param token The address of the ERC20 token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @notice Withdraw ETH from the contract
     * @param amount The amount of ETH to withdraw
     */
    function withdrawETH(uint256 amount) external {
        require(amount > 0 && amount <= address(this).balance, "Invalid amount");
        payable(msg.sender).transfer(amount);
    }
}
```
