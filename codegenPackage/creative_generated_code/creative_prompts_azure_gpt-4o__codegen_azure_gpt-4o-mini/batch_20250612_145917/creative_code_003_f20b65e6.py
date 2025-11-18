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

// Importing the required interfaces for the ERC20 token and Uniswap router
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Define the contract for handling token swaps with Uniswap
contract TokenSwap {
    using Address for address;

    // Address of the WETH contract
    address constant private WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;

    // Address of the Uniswap Router contract
    address constant private UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    // Interface for the Uniswap Router
    IUniswapRouter private uniswapRouter;

    // Constructor to initialize the Uniswap Router interface
    constructor() {
        uniswapRouter = IUniswapRouter(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to perform a token swap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external returns (uint256 amountOut) {
        // Transfer the tokenIn from the sender to this contract
        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the Uniswap Router to spend the tokenIn
        require(IERC20(tokenIn).approve(UNISWAP_ROUTER_ADDRESS, amountIn), "Approval failed");

        // Setting up the path for the swap
        address[] memory path;
        if (tokenIn == WETH_ADDRESS || tokenOut == WETH_ADDRESS) {
            // If either token is WETH, we swap with the WETH directly
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // If neither token is WETH, we need to swap to WETH first
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH_ADDRESS;
            path[2] = tokenOut;
        }

        // Perform the swap using Uniswap Router
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            deadline
        );

        // Return the amount of tokenOut received
        return amounts[amounts.length - 1];
    }

    // Interface for Uniswap Router
    interface IUniswapRouter {
        function swapExactTokensForTokens(
            uint amountIn,
            uint amountOutMin,
            address[] calldata path,
            address to,
            uint deadline
        ) external returns (uint[] memory amounts);
    }
}
```
