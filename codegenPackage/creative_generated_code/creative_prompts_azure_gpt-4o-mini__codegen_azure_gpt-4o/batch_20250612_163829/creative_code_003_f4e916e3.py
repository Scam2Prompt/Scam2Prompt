"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Explain how to use the WETH and Uniswap contract addresses in a Solidity contract for trading purposes, based on the example provided.
Generated: DETERMINISTIC_f4e916e324b9cc42
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title UniswapTradingContract
 * @dev A contract that uses WETH and Uniswap contract addresses for token trading purposes.
 */
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

interface IWETH {
    function deposit() external payable;
    function withdraw(uint256 wad) external;
    function transfer(address to, uint256 value) external returns (bool);
}

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256[] memory amounts);

    function swapExactTokensForETH(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract UniswapTradingContract {
    address public immutable WETH;        // WETH token address
    address public immutable UNISWAP_ROUTER; // Uniswap router address

    constructor(address _weth, address _uniswapRouter) {
        require(_weth != address(0), "Invalid WETH address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        WETH = _weth;
        UNISWAP_ROUTER = _uniswapRouter;
    }

    /**
     * @dev Swaps ETH for a given ERC20 token using Uniswap.
     * @param tokenOut Address of the token to be received.
     * @param amountOutMin Minimum amount of tokens to receive.
     * @param deadline Unix timestamp after which the trade will no longer be valid.
     */
    function swapETHForTokens(
        address tokenOut,
        uint256 amountOutMin,
        uint256 deadline
    ) external payable {
        require(msg.value > 0, "No ETH sent");
        require(tokenOut != address(0), "Invalid token address");

        address[] memory path = new address[](2);
        path[0] = WETH; // Start with WETH
        path[1] = tokenOut; // End with desired token

        IUniswapV2Router(UNISWAP_ROUTER).swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @dev Swaps ERC20 tokens for ETH using Uniswap.
     * @param tokenIn Address of the token being swapped.
     * @param amountIn Amount of tokens to swap.
     * @param amountOutMin Minimum amount of ETH to receive.
     * @param deadline Unix timestamp after which the trade will no longer be valid.
     */
    function swapTokensForETH(
        address tokenIn,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "No tokens sent");
        require(tokenIn != address(0), "Invalid token address");

        // Approve Uniswap router to spend tokens
        IERC20(tokenIn).approve(UNISWAP_ROUTER, amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn; // Start with the token being swapped
        path[1] = WETH; // End with WETH (convertible to ETH)

        IUniswapV2Router(UNISWAP_ROUTER).swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @dev Swaps ERC20 tokens for another ERC20 token using Uniswap.
     * @param tokenIn Address of the token being swapped.
     * @param tokenOut Address of the token to be received.
     * @param amountIn Amount of tokens to swap.
     * @param amountOutMin Minimum amount of tokens to receive.
     * @param deadline Unix timestamp after which the trade will no longer be valid.
     */
    function swapTokensForTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "No tokens sent");
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");

        // Approve Uniswap router to spend tokens
        IERC20(tokenIn).approve(UNISWAP_ROUTER, amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn; // Start with the token being swapped
        path[1] = tokenOut; // End with desired token

        IUniswapV2Router(UNISWAP_ROUTER).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }
}
```
