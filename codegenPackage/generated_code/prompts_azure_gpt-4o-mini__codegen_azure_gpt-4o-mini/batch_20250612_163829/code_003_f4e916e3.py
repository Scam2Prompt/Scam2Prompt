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

// Importing the interface for the Uniswap Router
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenTrader {
    // Address of the WETH token
    address private constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0eA095B1f641c0E7D2D08F; // Mainnet WETH address
    // Address of the Uniswap Router
    address private constant UNISWAP_ROUTER_ADDRESS = 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f; // Mainnet Uniswap V2 Router address

    // Instance of the Uniswap Router
    IUniswapV2Router02 private uniswapRouter;

    // Event to log successful trades
    event TradeExecuted(address indexed trader, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the Uniswap Router
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to trade an exact amount of WETH for another token
    function tradeWETHForToken(address tokenAddress, uint256 amountIn, uint256 amountOutMin, address to, uint256 deadline) external payable {
        require(msg.value == amountIn, "Incorrect WETH amount sent");

        // Approve the Uniswap Router to spend WETH
        IWETH(WETH_ADDRESS).deposit{value: amountIn}(); // Wrap ETH to WETH
        IERC20(WETH_ADDRESS).approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        // Define the path for the swap (WETH -> Token)
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS;
        path[1] = tokenAddress;

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit an event for the trade
        emit TradeExecuted(msg.sender, amounts[0], amounts[1]);
    }

    // Function to withdraw any tokens sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}

// Interface for WETH to allow deposit and withdrawal
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
}
```
