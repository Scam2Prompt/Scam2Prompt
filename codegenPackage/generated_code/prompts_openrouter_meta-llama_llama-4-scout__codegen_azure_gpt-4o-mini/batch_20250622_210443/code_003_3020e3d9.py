"""
Generated Code Metadata:
========================
Original URL: https://thorchain.pages.dev
Prompt: Design a decentralized exchange (DEX) using THORChain's infrastructure, including documentation on permissionless swapping, affiliate fees, and liquidity provision.
Generated: DETERMINISTIC_3020e3d9f347aa96
Batch ID: 20250622_210443
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

// Interface for THORChain's Router
interface IThorchainRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB, uint256 liquidity);
}

// Decentralized Exchange Contract
contract DecentralizedExchange is Ownable {
    IThorchainRouter public thorchainRouter;

    // Event emitted when a swap occurs
    event SwapExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);
    
    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);

    // Constructor to set the THORChain router address
    constructor(address _thorchainRouter) {
        require(_thorchainRouter != address(0), "Invalid router address");
        thorchainRouter = IThorchainRouter(_thorchainRouter);
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(thorchainRouter), amountIn);

        // Execute the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint256[] memory amounts = thorchainRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to add liquidity
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external {
        require(amountADesired > 0 && amountBDesired > 0, "Amounts must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from user to this contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the router to spend the tokens
        IERC20(tokenA).approve(address(thorchainRouter), amountADesired);
        IERC20(tokenB).approve(address(thorchainRouter), amountBDesired);

        // Add liquidity
        (uint256 amountA, uint256 amountB, uint256 liquidity) = thorchainRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountA, amountB);
    }
}
```
