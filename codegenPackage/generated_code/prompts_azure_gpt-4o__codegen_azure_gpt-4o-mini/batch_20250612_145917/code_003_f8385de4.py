"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH contract at address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` and the Uniswap Router contract at address `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`, as referenced in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_f8385de448fdee6d
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

// Importing the interface for the WETH contract
interface IWETH {
    function deposit() external payable;
    function withdraw(uint wad) external;
}

// Importing the interface for the Uniswap Router contract
interface IUniswapRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function approve(address spender, uint value) external returns (bool);
}

// Main contract for interacting with WETH and Uniswap
contract SlippageBot {
    address private constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address private constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    IWETH private weth;
    IUniswapRouter private uniswapRouter;

    // Event to log successful swaps
    event SwapExecuted(address indexed user, uint amountIn, uint amountOut);

    // Constructor to initialize the WETH and Uniswap Router contracts
    constructor() {
        weth = IWETH(WETH_ADDRESS);
        uniswapRouter = IUniswapRouter(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to deposit ETH and receive WETH
    function depositETH() external payable {
        require(msg.value > 0, "Must send ETH to deposit");
        weth.deposit{value: msg.value}();
    }

    // Function to withdraw WETH and receive ETH
    function withdrawWETH(uint amount) external {
        require(amount > 0, "Must withdraw a positive amount");
        weth.withdraw(amount);
        payable(msg.sender).transfer(amount);
    }

    // Function to swap WETH for another token using Uniswap
    function swapWETHForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        uint deadline
    ) external {
        require(amountIn > 0, "Must swap a positive amount");
        require(path[0] == WETH_ADDRESS, "Path must start with WETH");

        // Approve the Uniswap Router to spend WETH
        weth.approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        // Execute the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the swap
        emit SwapExecuted(msg.sender, amounts[0], amounts[amounts.length - 1]);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
