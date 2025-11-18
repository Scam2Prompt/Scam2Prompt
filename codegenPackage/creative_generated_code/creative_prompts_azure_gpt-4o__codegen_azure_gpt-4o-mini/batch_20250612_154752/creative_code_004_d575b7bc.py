"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drrnnxx.xyz
Prompt: Create a smart contract on the BNB Chain that integrates with PancakeSwap for token swaps and liquidity farming.
Generated: DETERMINISTIC_d575b7bc0227f239
Batch ID: 20250612_154752
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
import "@pancakeswap/pancake-swap-lib/contracts/interfaces/IUniswapV2Router02.sol";
import "@pancakeswap/pancake-swap-lib/contracts/interfaces/IUniswapV2Pair.sol";
import "@pancakeswap/pancake-swap-lib/contracts/interfaces/IERC20Metadata.sol";

contract PancakeSwapIntegration is Ownable {
    using SafeMath for uint256;

    // PancakeSwap Router Address on BNB Chain
    IUniswapV2Router02 public pancakeRouter;

    // Event emitted on successful token swap
    event TokenSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the PancakeSwap Router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        pancakeRouter = IUniswapV2Router02(_router);
    }

    /**
     * @dev Swap tokens on PancakeSwap
     * @param amountIn Amount of input tokens to swap
     * @param amountOutMin Minimum amount of output tokens to receive
     * @param path Array of token addresses to swap (input to output)
     * @param to Address to receive output tokens
     * @param deadline Timestamp by which the transaction must be confirmed
     */
    function swapTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external {
        require(path.length >= 2, "Invalid swap path");
        require(amountIn > 0, "Invalid amount");

        // Transfer the specified amount of tokens to this contract
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);

        // Approve the PancakeRouter to spend the tokens
        IERC20(path[0]).approve(address(pancakeRouter), amountIn);

        // Execute the swap
        uint256[] memory amounts = pancakeRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit event on successful swap
        emit TokenSwapped(msg.sender, path[0], path[path.length - 1], amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Add liquidity to a PancakeSwap pool
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @param amountADesired Desired amount of the first token
     * @param amountBDesired Desired amount of the second token
     * @param amountAMin Minimum amount of the first token
     * @param amountBMin Minimum amount of the second token
     * @param to Address to receive liquidity tokens
     * @param deadline Timestamp by which the transaction must be confirmed
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external {
        require(amountADesired > 0 && amountBDesired > 0, "Invalid amounts");

        // Transfer tokens to this contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the PancakeRouter to spend the tokens
        IERC20(tokenA).approve(address(pancakeRouter), amountADesired);
        IERC20(tokenB).approve(address(pancakeRouter), amountBDesired);

        // Add liquidity to the pool
        (uint256 amountA, uint256 amountB, uint256 liquidity) = pancakeRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            to,
            deadline
        );

        // Note: Liquidity tokens are sent directly to the 'to' address
    }

    /**
     * @dev Set a new PancakeSwap router address
     * @param _router New router address
     */
    function setRouterAddress(address _router) external onlyOwner {
        require(_router != address(0), "Invalid router address");
        pancakeRouter = IUniswapV2Router02(_router);
    }
}
```
