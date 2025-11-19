"""
Generated Code Metadata:
========================
Original URL: https://claimalvara.pages.dev
Prompt: Implement a function in Solidity to integrate the Uniswap V2 Router for buying and selling underlying tokens during the creation and withdrawal of ERC-7621 Basket Tokens.
Generated: DETERMINISTIC_7098329d1e83eeaf
Batch ID: 20250612_154820
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract BasketTokenExchange {
    using SafeERC20 for IERC20;

    IUniswapV2Router02 public immutable uniswapRouter;

    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @notice Buy underlying tokens using ETH
     * @param tokenOut The token to receive
     * @param amountOutMin Minimum amount of tokens to receive
     * @param deadline Deadline for the transaction
     * @return amountOut Actual amount of tokens received
     */
    function buyUnderlyingWithETH(
        address tokenOut,
        uint amountOutMin,
        uint deadline
    ) external payable returns (uint amountOut) {
        require(tokenOut != address(0), "Invalid token address");
        require(deadline >= block.timestamp, "Expired deadline");

        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = tokenOut;

        uint[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        return amounts[amounts.length - 1];
    }

    /**
     * @notice Buy underlying tokens using another ERC20 token
     * @param tokenIn The token to spend
     * @param tokenOut The token to receive
     * @param amountIn Amount of tokens to spend
     * @param amountOutMin Minimum amount of tokens to receive
     * @param deadline Deadline for the transaction
     * @return amountOut Actual amount of tokens received
     */
    function buyUnderlyingWithToken(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external returns (uint amountOut) {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(deadline >= block.timestamp, "Expired deadline");

        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).safeApprove(address(uniswapRouter), amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        return amounts[amounts.length - 1];
    }

    /**
     * @notice Sell underlying tokens for ETH
     * @param tokenIn The token to sell
     * @param amountIn Amount of tokens to sell
     * @param amountOutMin Minimum amount of ETH to receive
     * @param deadline Deadline for the transaction
     * @return amountOut Actual amount of ETH received
     */
    function sellUnderlyingForETH(
        address tokenIn,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external returns (uint amountOut) {
        require(tokenIn != address(0), "Invalid token address");
        require(deadline >= block.timestamp, "Expired deadline");

        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).safeApprove(address(uniswapRouter), amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = uniswapRouter.WETH();

        uint[] memory amounts = uniswapRouter.swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        return amounts[amounts.length - 1];
    }

    /**
     * @notice Sell underlying tokens for another ERC20 token
     * @param tokenIn The token to sell
     * @param tokenOut The token to receive
     * @param amountIn Amount of tokens to sell
     * @param amountOutMin Minimum amount of tokens to receive
     * @param deadline Deadline for the transaction
     * @return amountOut Actual amount of tokens received
     */
    function sellUnderlyingForToken(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external returns (uint amountOut) {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(deadline >= block.timestamp, "Expired deadline");

        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).safeApprove(address(uniswapRouter), amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        return amounts[amounts.length - 1];
    }

    /**
     * @notice Emergency function to withdraw any ERC20 tokens sent to this contract
     * @param token The token to withdraw
     * @param amount The amount to withdraw
     */
    function emergencyWithdraw(address token, uint amount) external {
        require(token != address(0), "Invalid token address");
        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```
