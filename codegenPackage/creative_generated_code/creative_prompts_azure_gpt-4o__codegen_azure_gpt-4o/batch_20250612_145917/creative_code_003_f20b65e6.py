"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoden.pages.dev
Prompt: Develop a Solidity contract that interacts with Uniswap's WETH contract (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`) and Uniswap Router contract (`0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`) to perform token swaps with slippage handling.
Generated: DETERMINISTIC_f20b65e69c19b995
Batch ID: 20250612_145917
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

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
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

contract TokenSwap {
    address public constant WETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public constant UNISWAP_ROUTER = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    IUniswapV2Router private uniswapRouter = IUniswapV2Router(UNISWAP_ROUTER);

    // Event to log swaps
    event SwapExecuted(
        address indexed sender,
        address inputToken,
        address outputToken,
        uint256 inputAmount,
        uint256 outputAmount
    );

    /**
     * @dev Swap ERC20 tokens for another ERC20 token.
     * @param amountIn Amount of input token to swap.
     * @param amountOutMin Minimum amount of output token to accept (slippage control).
     * @param path Array of token addresses (input -> intermediate(s) -> output).
     * @param deadline Timestamp until which the trade is valid.
     */
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external {
        require(path.length >= 2, "Invalid path");
        require(amountIn > 0, "Amount must be greater than 0");

        IERC20 inputToken = IERC20(path[0]);
        // Transfer tokens from sender to this contract
        require(inputToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        // Approve Uniswap Router to spend the input tokens
        require(inputToken.approve(UNISWAP_ROUTER, amountIn), "Approval failed");

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit SwapExecuted(msg.sender, path[0], path[path.length - 1], amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Swap ETH for ERC20 tokens.
     * @param amountOutMin Minimum amount of output tokens to accept (slippage control).
     * @param path Array of token addresses (WETH -> intermediate(s) -> output).
     * @param deadline Timestamp until which the trade is valid.
     */
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external payable {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(path[0] == WETH, "First token in path must be WETH");

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit SwapExecuted(msg.sender, WETH, path[path.length - 1], msg.value, amounts[amounts.length - 1]);
    }

    /**
     * @dev Swap ERC20 tokens for ETH.
     * @param amountIn Amount of input token to swap.
     * @param amountOutMin Minimum amount of ETH to accept (slippage control).
     * @param path Array of token addresses (input -> intermediate(s) -> WETH).
     * @param deadline Timestamp until which the trade is valid.
     */
    function swapExactTokensForETH(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external {
        require(path[path.length - 1] == WETH, "Last token in path must be WETH");

        IERC20 inputToken = IERC20(path[0]);
        // Transfer tokens from sender to this contract
        require(inputToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        // Approve Uniswap Router to spend the input tokens
        require(inputToken.approve(UNISWAP_ROUTER, amountIn), "Approval failed");

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit SwapExecuted(msg.sender, path[0], WETH, amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Fallback function to handle ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Withdraw accidentally sent funds from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function withdraw(address token, uint256 amount) external {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
