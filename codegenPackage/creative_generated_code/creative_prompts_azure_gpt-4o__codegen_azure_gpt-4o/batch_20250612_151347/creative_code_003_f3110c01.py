"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Develop a Solidity contract that interacts with both the WETH contract (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`) and the Uniswap Router contract (`0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`) to perform token swaps with slippage control.
Generated: DETERMINISTIC_f3110c01e88cd4a6
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

/**
 * @title TokenSwap
 * @dev A contract that interacts with the WETH contract and Uniswap Router to swap tokens with slippage control.
 */
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

interface IUniswapRouter {
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

    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory amounts);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenSwap {
    address public constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    IWETH private immutable weth = IWETH(WETH_ADDRESS);
    IUniswapRouter private immutable uniswapRouter = IUniswapRouter(UNISWAP_ROUTER_ADDRESS);

    /**
     * @notice Swaps ETH for tokens on Uniswap with slippage control.
     * @param tokenOut The address of the token to receive.
     * @param amountOutMin Minimum amount of tokens to receive (slippage control).
     * @param deadline Unix timestamp after which the transaction reverts.
     */
    function swapETHForTokens(
        address tokenOut,
        uint256 amountOutMin,
        uint256 deadline
    ) external payable {
        require(msg.value > 0, "Insufficient ETH sent");

        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS;
        path[1] = tokenOut;

        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @notice Swaps tokens for ETH on Uniswap with slippage control.
     * @param tokenIn The address of the token to swap.
     * @param amountIn The amount of tokens to swap.
     * @param amountOutMin Minimum amount of ETH to receive (slippage control).
     * @param deadline Unix timestamp after which the transaction reverts.
     */
    function swapTokensForETH(
        address tokenIn,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Insufficient token amount");

        IERC20(tokenIn).approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = WETH_ADDRESS;

        uniswapRouter.swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @notice Swaps tokens for another token on Uniswap with slippage control.
     * @param tokenIn The address of the token to swap.
     * @param tokenOut The address of the token to receive.
     * @param amountIn The amount of tokens to swap.
     * @param amountOutMin Minimum amount of tokens to receive (slippage control).
     * @param deadline Unix timestamp after which the transaction reverts.
     */
    function swapTokensForTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Insufficient token amount");

        IERC20(tokenIn).approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @notice Gets the estimated output amount for a token swap.
     * @param amountIn Amount of the input token.
     * @param path Array of token addresses representing the swap path.
     * @return amounts Array containing estimated amounts along the swap path.
     */
    function getEstimatedSwapAmount(uint256 amountIn, address[] memory path) external view returns (uint256[] memory amounts) {
        return uniswapRouter.getAmountsOut(amountIn, path);
    }

    /**
     * @notice Withdraws ETH from the contract balance (owner only).
     */
    function withdrawETH() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }

    /**
     * @notice Fallback function to accept ETH.
     */
    receive() external payable {}
}
```
