"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "Write a Solidity code snippet that imports Uniswap V2 interfaces and sets up a contract to interact with Uniswap for trade execution."
Generated: DETERMINISTIC_767e71a2a16249f2
Batch ID: 20250622_204803
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

// Import Uniswap V2 interfaces
interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function swapTokensForExactTokens(
        uint amountOut,
        uint amountInMax,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
    function getAmountsIn(uint amountOut, address[] calldata path) external view returns (uint[] memory amounts);
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract UniswapV2Trader {
    address public immutable uniswapRouter;
    
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = _uniswapRouter;
    }
    
    /**
     * @dev Executes a token swap on Uniswap V2
     * @param amountIn Amount of input tokens to swap
     * @param amountOutMin Minimum amount of output tokens expected
     * @param path Array of token addresses representing the swap path
     * @param to Address to receive the output tokens
     * @param deadline Unix timestamp after which the transaction will revert
     */
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts) {
        require(path.length >= 2, "Invalid path length");
        require(deadline >= block.timestamp, "Expired deadline");
        
        IERC20 inputToken = IERC20(path[0]);
        require(inputToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        require(inputToken.approve(uniswapRouter, amountIn), "Approval failed");
        
        amounts = IUniswapV2Router(uniswapRouter).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );
    }
    
    /**
     * @dev Gets the estimated output amount for a given input
     * @param amountIn Amount of input tokens
     * @param path Array of token addresses representing the swap path
     */
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts) {
        return IUniswapV2Router(uniswapRouter).getAmountsOut(amountIn, path);
    }
    
    /**
     * @dev Gets the required input amount for a desired output
     * @param amountOut Desired amount of output tokens
     * @param path Array of token addresses representing the swap path
     */
    function getAmountsIn(uint amountOut, address[] calldata path) external view returns (uint[] memory amounts) {
        return IUniswapV2Router(uniswapRouter).getAmountsIn(amountOut, path);
    }
    
    /**
     * @dev Approves a token for spending by the Uniswap router
     * @param token Address of the token to approve
     * @param amount Amount to approve
     */
    function approveToken(address token, uint amount) external {
        require(token != address(0), "Invalid token address");
        require(IERC20(token).approve(uniswapRouter, amount), "Approval failed");
    }
}
```
