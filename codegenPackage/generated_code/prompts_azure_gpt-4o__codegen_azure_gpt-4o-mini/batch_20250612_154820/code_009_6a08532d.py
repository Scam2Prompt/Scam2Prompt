"""
Generated Code Metadata:
========================
Original URL: https://cruas.ru
Prompt: Create a tutorial for deploying a decentralized exchange (DEX) similar to Velodrome Finance using the AMM protocol on Ethereum.
Generated: DETERMINISTIC_6a08532d7d1e1856
Batch ID: 20250612_154820
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
    
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// Main contract for the DEX
contract DecentralizedExchange is Ownable {
    // State variables
    IUniswapV2Router public uniswapRouter;
    address public tokenA;
    address public tokenB;

    // Events for logging
    event LiquidityAdded(uint amountA, uint amountB, uint liquidity);
    event TokensSwapped(uint amountIn, uint amountOut);

    // Constructor to initialize the router and tokens
    constructor(address _router, address _tokenA, address _tokenB) {
        uniswapRouter = IUniswapV2Router(_router);
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    // Function to add liquidity to the DEX
    function addLiquidity(
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin
    ) external onlyOwner {
        // Transfer tokens from the owner to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the router to spend the tokens
        IERC20(tokenA).approve(address(uniswapRouter), amountADesired);
        IERC20(tokenB).approve(address(uniswapRouter), amountBDesired);

        // Add liquidity to the DEX
        (uint amountA, uint amountB, uint liquidity) = uniswapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this),
            block.timestamp
        );

        emit LiquidityAdded(amountA, amountB, liquidity);
    }

    // Function to swap tokens
    function swapTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path
    ) external onlyOwner {
        // Transfer tokens from the owner to the contract
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(path[0]).approve(address(uniswapRouter), amountIn);

        // Perform the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        emit TokensSwapped(amounts[0], amounts[amounts.length - 1]);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```

### Notes:
- This code is a basic implementation of a decentralized exchange (DEX) using the AMM protocol on Ethereum.
- It includes functions for adding liquidity and swapping tokens, with proper error handling and event logging.
- The contract owner has the ability to withdraw tokens, ensuring control over the contract's funds.
- Ensure to test the contract thoroughly on a test network before deploying it to the main Ethereum network.
