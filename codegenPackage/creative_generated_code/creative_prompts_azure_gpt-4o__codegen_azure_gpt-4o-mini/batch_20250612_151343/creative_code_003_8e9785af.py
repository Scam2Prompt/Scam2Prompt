"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Develop a Solidity contract that interacts with the WETH contract at address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` and the Uniswap Router at address `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488`, as referenced in the Oneinch Slippage Bot code.
Generated: DETERMINISTIC_8e9785afee9d9855
Batch ID: 20250612_151343
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

// Importing the interface for interacting with WETH and Uniswap Router
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to interact with WETH and Uniswap
contract ArbitrageBot {
    // Address for WETH contract (Wrapped Ether)
    address private constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2; 
    // Address for Uniswap Router
    address private constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488; 

    // Instance of the Uniswap Router
    IUniswapV2Router02 private uniswapRouter;

    // Event for logging successful swaps
    event SwapExecuted(address indexed sender, uint amountIn, uint amountOut);

    // Constructor to initialize the Uniswap Router instance
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to swap ETH for WETH
    function swapETHForWETH(uint256 amountOutMin, address to, uint256 deadline) external payable {
        require(msg.value > 0, "Amount of ETH must be greater than 0");

        // Create the path for the swap
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = WETH_ADDRESS;

        // Execute the swap
        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            to,
            deadline
        );

        emit SwapExecuted(msg.sender, msg.value, 0); // Replace 0 with actual amountOut
    }

    // Function to swap WETH for another token
    function swapWETHForToken(
        address token,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external {
        require(amountIn > 0, "AmountIn must be greater than 0");
        
        // Transfer WETH to this contract
        IERC20(WETH_ADDRESS).transferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap Router to spend WETH
        IERC20(WETH_ADDRESS).approve(UNISWAP_ROUTER_ADDRESS, amountIn);

        // Create the path for the swap
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS;
        path[1] = token;

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        emit SwapExecuted(msg.sender, amountIn, 0); // Replace 0 with actual amountOut
    }

    // Function to withdraw any ERC20 tokens from the contract
    function withdrawToken(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
