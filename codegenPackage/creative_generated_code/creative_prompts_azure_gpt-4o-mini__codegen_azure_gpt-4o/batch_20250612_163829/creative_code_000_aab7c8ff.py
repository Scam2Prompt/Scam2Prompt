"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, utilizing the Uniswap V2 interfaces as shown in the provided example.
Generated: DETERMINISTIC_aab7c8ffb543a674
Batch ID: 20250612_163829
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

// Interface for Uniswap V2 Router
interface IUniswapV2Router {
    function getAmountsOut(uint amountIn, address[] memory path) external view returns (uint[] memory amounts);
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// Interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint);
    function transfer(address recipient, uint amount) external returns (bool);
    function approve(address spender, uint amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint);
}

contract SlippageBot {
    address public owner;
    IUniswapV2Router public uniswapRouter;
    uint public slippageTolerance; // Slippage tolerance in percentage (e.g., 5 for 5%)

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    event SwapExecuted(address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);

    constructor(address _uniswapRouter, uint _slippageTolerance) {
        require(_slippageTolerance <= 100, "Slippage tolerance must be between 0 and 100");
        owner = msg.sender;
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
        slippageTolerance = _slippageTolerance;
    }

    // Set a new slippage tolerance
    function setSlippageTolerance(uint _slippageTolerance) external onlyOwner {
        require(_slippageTolerance <= 100, "Slippage tolerance must be between 0 and 100");
        slippageTolerance = _slippageTolerance;
    }

    // Execute a token swap with slippage tolerance check
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint deadline
    ) external onlyOwner {
        require(IERC20(tokenIn).balanceOf(address(this)) >= amountIn, "Insufficient balance");

        // Define the swap path (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Get expected amounts out
        uint[] memory amountsOut = uniswapRouter.getAmountsOut(amountIn, path);
        uint expectedAmountOut = amountsOut[1];

        // Calculate minimum amountOut based on slippage tolerance
        uint amountOutMin = (expectedAmountOut * (100 - slippageTolerance)) / 100;

        // Approve Uniswap router to spend tokenIn
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Perform the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            deadline
        );

        // Emit event for successful swap
        emit SwapExecuted(tokenIn, tokenOut, amountIn, amounts[1]);
    }

    // Withdraw tokens from the contract
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        IERC20(token).transfer(owner, amount);
    }

    // Emergency owner transfer of Ether (if any sent to contract accidentally)
    function withdrawEther(uint amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
