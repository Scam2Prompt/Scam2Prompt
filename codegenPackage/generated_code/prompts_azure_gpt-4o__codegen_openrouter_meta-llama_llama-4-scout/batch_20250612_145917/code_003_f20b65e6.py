"""
Generated Code Metadata:
========================
Original URL: https://copycoden.pages.dev
Prompt: Develop a Solidity contract that interacts with Uniswap's WETH contract (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`) and Uniswap Router contract (`0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`) to perform token swaps with slippage handling.
Generated: DETERMINISTIC_f20b65e69c19b995
Batch ID: 20250612_145917
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title UniswapSwapper
 * @author [Your Name]
 * @notice This contract facilitates token swaps using Uniswap's WETH and Router contracts.
 */
contract UniswapSwapper {
    using SafeMath for uint256;

    // Uniswap WETH contract address
    address public constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;

    // Uniswap Router contract address
    address public constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    // Mapping of token addresses to their decimals
    mapping(address => uint8) public tokenDecimals;

    /**
     * @dev Constructor
     */
    constructor() public {}

    /**
     * @dev Swap tokens using Uniswap Router
     * @param tokenIn Address of token to swap from
     * @param tokenOut Address of token to swap to
     * @param amountIn Amount of token to swap
     * @param slippage Maximum slippage (in %) for the swap
     * @param to Address to send the swapped tokens to
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 slippage,
        address to
    ) external {
        require(tokenIn != tokenOut, "Token in and out must be different");

        // Get token decimals
        uint8 decimalsIn = getTokenDecimals(tokenIn);
        uint8 decimalsOut = getTokenDecimals(tokenOut);

        // Approve Uniswap Router to spend tokens
        IERC20(tokenIn).approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        // Calculate minimum amount out with slippage
        uint256 amountOutMin = calculateAmountOutMin(
            amountIn,
            decimalsIn,
            decimalsOut,
            slippage
        );

        // Perform swap
        _swapTokens(
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            to
        );
    }

    /**
     * @dev Get token decimals
     * @param token Address of token
     * @return uint8 Token decimals
     */
    function getTokenDecimals(address token) public view returns (uint8) {
        if (tokenDecimals[token] == 0) {
            // If not cached, get from token contract
            uint8 decimals = IERC20(token).decimals();
            tokenDecimals[token] = decimals;
            return decimals;
        }
        return tokenDecimals[token];
    }

    /**
     * @dev Calculate minimum amount out with slippage
     * @param amountIn Amount of token to swap
     * @param decimalsIn Decimals of token in
     * @param decimalsOut Decimals of token out
     * @param slippage Maximum slippage (in %)
     * @return uint256 Minimum amount out
     */
    function calculateAmountOutMin(
        uint256 amountIn,
        uint8 decimalsIn,
        uint8 decimalsOut,
        uint256 slippage
    ) internal pure returns (uint256) {
        // Calculate amount out with slippage
        uint256 amountOutMin = amountIn.mul(100 - slippage).div(100);

        // Adjust for decimals
        if (decimalsIn > decimalsOut) {
            amountOutMin = amountOutMin.div(10**(decimalsIn - decimalsOut));
        } else if (decimalsIn < decimalsOut) {
            amountOutMin = amountOutMin.mul(10**(decimalsOut - decimalsIn));
        }

        return amountOutMin;
    }

    /**
     * @dev Perform token swap using Uniswap Router
     * @param tokenIn Address of token to swap from
     * @param tokenOut Address of token to swap to
     * @param amountIn Amount of token to swap
     * @param amountOutMin Minimum amount of token out
     * @param to Address to send the swapped tokens to
     */
    function _swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) internal {
        // WETH address is used for ETH swaps
        address[] memory path;
        if (tokenIn == WETH_ADDRESS || tokenOut == WETH_ADDRESS) {
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // Use WETH as intermediate for non-ETH swaps
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH_ADDRESS;
            path[2] = tokenOut;
        }

        // Perform swap
        uint256[] memory amounts = IUniswapRouter(UNISWAP_ROUTER_ADDRESS).getAmountsOut(
            amountIn,
            path
        );
        require(amounts[1] >= amountOutMin, "Insufficient amount out");

        IUniswapRouter(UNISWAP_ROUTER_ADDRESS).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            block.timestamp
        );
    }
}

interface IUniswapRouter {
    function getAmountsOut(uint amountIn, address[] memory path) external view returns (uint[] memory amounts);
    function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] memory path, address to, uint deadline) external;
}
```
