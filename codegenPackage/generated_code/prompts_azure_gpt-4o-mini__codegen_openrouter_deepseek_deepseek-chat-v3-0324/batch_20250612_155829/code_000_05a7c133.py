"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, referencing the Uniswap V2 interfaces as shown in the provided code.
Generated: DETERMINISTIC_05a7c1333f89c984
Batch ID: 20250612_155829
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

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

interface I1inchAggregationRouter {
    function swap(
        address caller,
        address tokenIn,
        address tokenOut,
        uint256 amount,
        uint256 minReturn,
        address[] calldata pools
    ) external payable returns (uint256 returnAmount);
}

contract SlippageBot {
    address public owner;
    IUniswapV2Router public uniswapRouter;
    I1inchAggregationRouter public oneInchRouter;
    
    event SwapExecuted(
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 expectedAmountOut,
        uint256 slippage
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    constructor(address _uniswapRouter, address _oneInchRouter) {
        owner = msg.sender;
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
        oneInchRouter = I1inchAggregationRouter(_oneInchRouter);
    }
    
    /**
     * @dev Executes a swap with slippage protection using 1inch
     * @param tokenIn Address of the input token
     * @param tokenOut Address of the output token
     * @param amount Amount of input tokens to swap
     * @param maxSlippage Maximum allowed slippage percentage (e.g., 1 for 1%)
     * @param pools Array of pool addresses to use for the swap
     */
    function executeSwapWithSlippageProtection(
        address tokenIn,
        address tokenOut,
        uint256 amount,
        uint256 maxSlippage,
        address[] calldata pools
    ) external onlyOwner returns (uint256) {
        require(maxSlippage <= 100, "Slippage too high");
        
        // Get expected amount out from Uniswap as reference price
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;
        
        uint256[] memory amounts = uniswapRouter.getAmountsOut(amount, path);
        uint256 expectedAmountOut = amounts[1];
        
        // Calculate minimum return based on max slippage
        uint256 minReturn = expectedAmountOut * (100 - maxSlippage) / 100;
        
        // Approve 1inch router to spend tokens
        IERC20(tokenIn).approve(address(oneInchRouter), amount);
        
        // Execute swap on 1inch
        uint256 returnAmount = oneInchRouter.swap(
            address(this),
            tokenIn,
            tokenOut,
            amount,
            minReturn,
            pools
        );
        
        // Calculate actual slippage
        uint256 slippage = 0;
        if (expectedAmountOut > returnAmount) {
            slippage = (expectedAmountOut - returnAmount) * 100 / expectedAmountOut;
        }
        
        emit SwapExecuted(
            tokenIn,
            tokenOut,
            amount,
            returnAmount,
            expectedAmountOut,
            slippage
        );
        
        return returnAmount;
    }
    
    /**
     * @dev Withdraws tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
    
    /**
     * @dev Changes the owner of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
