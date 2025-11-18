"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Write a Solidity function that interacts with Uniswap V2 and WETH contracts to perform token swaps with slippage control, leveraging the addresses and logic provided in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_2eb146e5fb4de151
Batch ID: 20250612_151347
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract TokenSwapWithSlippage {
    address public immutable WETH; // Address of the WETH contract
    IUniswapV2Router02 public immutable uniswapRouter; // Uniswap V2 Router address

    constructor(address _weth, address _uniswapRouter) {
        require(_weth != address(0), "Invalid WETH address");
        require(_uniswapRouter != address(0), "Invalid Uniswap Router address");
        WETH = _weth;
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @dev Performs a token swap with slippage control.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of `tokenIn` to swap.
     * @param amountOutMin Minimum acceptable amount of `tokenOut` after the swap (slippage control).
     * @param to Address to receive the swapped tokens.
     * @param deadline Unix timestamp by which the transaction must be mined.
     */
    function swapTokensWithSlippage(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(to != address(0), "Invalid recipient address");
        require(amountIn > 0, "Amount in must be greater than 0");
        require(amountOutMin > 0, "Amount out min must be greater than 0");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer the input tokens from the sender to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap router to spend the input tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        address[] memory path;
        if (tokenIn == WETH || tokenOut == WETH) {
            // Direct swap between WETH and another token
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // Indirect swap via WETH as the intermediary
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH;
            path[2] = tokenOut;
        }

        // Perform the token swap with slippage control
        try
            uniswapRouter.swapExactTokensForTokens(
                amountIn,
                amountOutMin,
                path,
                to,
                deadline
            )
        {
            // Successful swap
        } catch {
            revert("Token swap failed");
        }
    }
}
```
