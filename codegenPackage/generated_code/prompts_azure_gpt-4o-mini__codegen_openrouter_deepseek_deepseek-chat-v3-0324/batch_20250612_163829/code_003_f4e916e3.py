"""
Generated Code Metadata:
========================
Original URL: https://codesrc.pages.dev
Prompt: Explain how to use the WETH and Uniswap contract addresses in a Solidity contract for trading purposes, based on the example provided.
Generated: DETERMINISTIC_f4e916e324b9cc42
Batch ID: 20250612_163829
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract UniswapTrader {
    // Mainnet addresses - replace with appropriate addresses for other networks
    address public constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    IERC20 private weth;
    IUniswapV2Router02 private uniswapRouter;

    constructor() {
        weth = IERC20(WETH_ADDRESS);
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    /**
     * @notice Swap ETH for tokens
     * @param tokenAddress The address of the token to receive
     * @param amountOutMin Minimum amount of tokens expected in return
     * @param deadline Deadline for the swap transaction
     * @param recipient Address to receive the output tokens
     */
    function swapETHForTokens(
        address tokenAddress,
        uint256 amountOutMin,
        uint256 deadline,
        address recipient
    ) external payable {
        require(msg.value > 0, "Must send ETH to swap");
        require(tokenAddress != address(0), "Invalid token address");
        require(deadline > block.timestamp, "Deadline has passed");

        // Define the swap path (ETH -> WETH -> target token)
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS;
        path[1] = tokenAddress;

        // Execute the swap
        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            recipient,
            deadline
        );
    }

    /**
     * @notice Swap tokens for ETH
     * @param tokenAddress The address of the token to swap
     * @param tokenAmount The amount of tokens to swap
     * @param amountOutMin Minimum amount of ETH expected in return
     * @param deadline Deadline for the swap transaction
     * @param recipient Address to receive the ETH
     */
    function swapTokensForETH(
        address tokenAddress,
        uint256 tokenAmount,
        uint256 amountOutMin,
        uint256 deadline,
        address recipient
    ) external {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(tokenAddress != address(0), "Invalid token address");
        require(deadline > block.timestamp, "Deadline has passed");

        // Define the swap path (token -> WETH -> ETH)
        address[] memory path = new address[](2);
        path[0] = tokenAddress;
        path[1] = WETH_ADDRESS;

        // Transfer tokens to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve Uniswap Router to spend tokens
        IERC20(tokenAddress).approve(UNISWAP_ROUTER_ADDRESS, tokenAmount);

        // Execute the swap
        uniswapRouter.swapExactTokensForETH(
            tokenAmount,
            amountOutMin,
            path,
            recipient,
            deadline
        );
    }

    /**
     * @notice Swap tokens for tokens
     * @param tokenIn The address of the input token
     * @param tokenOut The address of the output token
     * @param tokenAmount The amount of input tokens to swap
     * @param amountOutMin Minimum amount of output tokens expected
     * @param deadline Deadline for the swap transaction
     * @param recipient Address to receive the output tokens
     */
    function swapTokensForTokens(
        address tokenIn,
        address tokenOut,
        uint256 tokenAmount,
        uint256 amountOutMin,
        uint256 deadline,
        address recipient
    ) external {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer tokens to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve Uniswap Router to spend tokens
        IERC20(tokenIn).approve(UNISWAP_ROUTER_ADDRESS, tokenAmount);

        // Define swap path (may need more hops depending on liquidity)
        address[] memory path;
        if (tokenIn == WETH_ADDRESS || tokenOut == WETH_ADDRESS) {
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH_ADDRESS;
            path[2] = tokenOut;
        }

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            tokenAmount,
            amountOutMin,
            path,
            recipient,
            deadline
        );
    }

    /**
     * @notice Get price quote for a token swap
     * @param amountIn The input amount
     * @param path The swap path (array of token addresses)
     * @return amounts The output amounts at each step of the path
     */
    function getAmountsOut(uint256 amountIn, address[] memory path) external view returns (uint256[] memory) {
        return uniswapRouter.getAmountsOut(amountIn, path);
    }

    // Emergency function to withdraw accidentally sent ERC20 tokens
    function withdrawERC20(address tokenAddress, uint256 amount) external {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
