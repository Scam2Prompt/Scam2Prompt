"""
Generated Code Metadata:
========================
Original URL: https://botcodesrc.pages.dev
Prompt: Develop a Solidity contract that interacts with the WETH contract at address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` and the Uniswap Router at address `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488`, as referenced in the Oneinch Slippage Bot code.
Generated: DETERMINISTIC_8e9785afee9d9855
Batch ID: 20250612_151343
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

// Importing the necessary interfaces for WETH and Uniswap Router
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract WETHUniswapInteraction {
    // Address of the WETH contract
    address constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    // Address of the Uniswap Router
    address constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488;

    // Instance of the Uniswap Router
    IUniswapV2Router02 public uniswapRouter;

    // Event to log successful swaps
    event SwapExecuted(address indexed user, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the Uniswap Router
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);
    }

    // Function to swap ETH for tokens
    function swapETHForTokens(address tokenOut, uint256 minAmountOut) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the path for the swap (ETH -> Token)
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS; // WETH address
        path[1] = tokenOut;     // Token address

        // Approve the router to spend WETH
        IWETH(WETH_ADDRESS).deposit{value: msg.value}(); // Wrap ETH to WETH
        IERC20(WETH_ADDRESS).approve(UNISWAP_ROUTER_ADDRESS, msg.value);

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            msg.value,
            minAmountOut,
            path,
            address(this), // Send tokens to this contract
            block.timestamp
        );

        // Emit event for successful swap
        emit SwapExecuted(msg.sender, msg.value, amounts[1]);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(address(this).balance >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}

// Interface for WETH to allow deposit function
interface IWETH {
    function deposit() external payable;
}
```
