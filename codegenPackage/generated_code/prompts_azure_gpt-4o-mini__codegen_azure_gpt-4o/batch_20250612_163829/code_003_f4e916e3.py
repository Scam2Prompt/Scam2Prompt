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

/**
 * @title UniswapTrading
 * @dev A contract for trading tokens using Uniswap and WETH.
 * This contract demonstrates how to interact with WETH and Uniswap contracts.
 */
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory amounts);
}

contract UniswapTrading {
    address public immutable WETH; // Address of the WETH contract
    address public immutable UNISWAP_ROUTER; // Address of the Uniswap V2 Router

    constructor(address _weth, address _uniswapRouter) {
        require(_weth != address(0), "Invalid WETH address");
        require(_uniswapRouter != address(0), "Invalid Uniswap Router address");

        WETH = _weth;
        UNISWAP_ROUTER = _uniswapRouter;
    }

    /**
     * @dev Converts ETH to WETH.
     */
    function convertEthToWeth() external payable {
        require(msg.value > 0, "Must send ETH to convert to WETH");

        IWETH(WETH).deposit{value: msg.value}();
    }

    /**
     * @dev Converts WETH back to ETH.
     * @param amount The amount of WETH to convert.
     */
    function convertWethToEth(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IWETH(WETH).balanceOf(address(this)) >= amount, "Insufficient WETH balance");

        IWETH(WETH).withdraw(amount);
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Trades WETH for another token using Uniswap.
     * @param tokenOut The address of the token to receive.
     * @param amountIn The amount of WETH to trade.
     * @param amountOutMin The minimum amount of tokenOut to receive.
     * @param deadline The deadline for the trade.
     */
    function tradeWethForToken(
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Approve Uniswap Router to spend WETH
        IWETH(WETH).transfer(UNISWAP_ROUTER, amountIn);

        // Define the trading path: WETH -> tokenOut
        address[] memory path = new address[](2);
        path[0] = WETH;
        path[1] = tokenOut;

        // Execute the trade
        IUniswapV2Router(UNISWAP_ROUTER).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {
        // Allow the contract to receive ETH
    }
}
```
