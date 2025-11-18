"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: Create a smart contract for handling ETH to USDC swaps in a Uniswap clone platform.
Generated: DETERMINISTIC_8da14d97fb197e11
Batch ID: 20250612_155006
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

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Interface for Uniswap-like router
interface IUniswapV2Router {
    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory);
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256[] memory);
}

contract ETHtoUSDC {
    // State variables
    address private immutable usdcToken; // USDC token address
    IUniswapV2Router private immutable uniswapRouter; // Router interface

    // Events
    event SwapCompleted(address indexed user, uint256 ethAmount, uint256 usdcReceived);

    // Constructor to initialize router and USDC token address
    constructor(address _router, address _usdcToken) {
        require(_router != address(0), "Router address cannot be zero");
        require(_usdcToken != address(0), "USDC address cannot be zero");
        uniswapRouter = IUniswapV2Router(_router);
        usdcToken = _usdcToken;
    }

    // Function to handle ETH to USDC swaps
    function swapETHForUSDC(uint256 minUSDCOut) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the swap path: ETH -> USDC
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // WETH represents wrapped ETH
        path[1] = usdcToken;

        // Perform the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minUSDCOut,
            path,
            msg.sender, // Send USDC directly to the sender
            block.timestamp + 300 // Deadline: current time + 5 minutes
        );

        // Emit event with swap details
        emit SwapCompleted(msg.sender, msg.value, amounts[1]);
    }

    // Helper function to check USDC balance of the contract
    function getContractUSDCBalance() external view returns (uint256) {
        return IERC20(usdcToken).balanceOf(address(this));
    }

    // Fallback function to handle ETH sent directly to contract
    receive() external payable {
        revert("Direct ETH deposits not allowed");
    }

    fallback() external payable {
        revert("Function does not exist");
    }
}
```
