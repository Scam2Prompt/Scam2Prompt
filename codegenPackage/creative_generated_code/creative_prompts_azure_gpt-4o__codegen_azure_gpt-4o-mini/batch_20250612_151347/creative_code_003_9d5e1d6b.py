"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH contract at address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` and the Uniswap V2 router at address `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`, as shown in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_9d5e1d6bfa9dcad4
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

// Importing Interfaces for WETH and Uniswap Router
interface IWETH {
    function deposit() external payable;
    function withdraw(uint wad) external;
}

interface IUniswapV2Router {
    function swapExactTokensForETH(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract SlippageBot {
    // Address of the WETH contract
    address constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    // Address of the Uniswap V2 router
    address constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;
    
    IWETH private weth;
    IUniswapV2Router private uniswapRouter;

    // Event for logging swaps
    event SwapExecuted(address indexed user, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize contract with WETH and Uniswap Router instances
    constructor() {
        weth = IWETH(WETH_ADDRESS);
        uniswapRouter = IUniswapV2Router(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to deposit ETH into WETH and perform a swap on Uniswap
    function swapETHForToken(address token, uint amountOutMin, uint deadline) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Deposit ETH to get WETH
        weth.deposit{value: msg.value}();

        // Create an array for the token path
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS; // WETH address
        path[1] = token;        // Token address

        // Approve the Uniswap Router to spend WETH
        // Note: This assumes the contract has WETH balance after deposit
        require(IERC20(WETH_ADDRESS).approve(UNISWAP_ROUTER_ADDRESS, msg.value), "Approve failed");

        // Perform the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForETH(
            msg.value,
            amountOutMin,
            path,
            msg.sender, // Send output to the user
            deadline
        );

        // Emit an event with the swap details
        emit SwapExecuted(msg.sender, amounts[0], amounts[1]);
    }

    // Function to withdraw WETH back to ETH
    function withdrawWETH(uint wad) external {
        require(wad > 0, "Withdraw amount must be greater than zero");

        // Withdraw WETH to ETH
        weth.withdraw(wad);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
