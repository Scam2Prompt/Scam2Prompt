"""
Generated Code Metadata:
========================
Original URL: https://copycodegpt.pages.dev
Prompt: Develop a Solidity smart contract that uses the Uniswap V2 core contracts to explore and interact with contracts on the Uniswap Exchange, specifically for mainnet only.
Generated: DETERMINISTIC_12c033e6cdbf40e2
Batch ID: 20250622_211330
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

// Importing necessary interfaces from Uniswap V2
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract UniswapInteraction {
    // State variables for Uniswap Router and Factory
    IUniswapV2Router02 public uniswapRouter;
    IUniswapV2Factory public uniswapFactory;

    // Event to log token swaps
    event TokensSwapped(address indexed sender, address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);

    // Constructor to initialize the Uniswap Router and Factory addresses
    constructor(address _router, address _factory) {
        uniswapRouter = IUniswapV2Router02(_router);
        uniswapFactory = IUniswapV2Factory(_factory);
    }

    // Function to swap tokens on Uniswap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        address to,
        uint deadline
    ) external {
        // Transfer the specified amount of tokenIn to this contract
        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the Uniswap router to spend tokenIn
        require(IERC20(tokenIn).approve(address(uniswapRouter), amountIn), "Approval failed");

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to get the current price of a token pair
    function getTokenPrice(address tokenA, address tokenB, uint amountIn) external view returns (uint amountOut) {
        // Get the pair address from the factory
        address pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        // Get reserves from the pair
        (uint reserveA, uint reserveB,) = IUniswapV2Pair(pair).getReserves();

        // Calculate the amount out based on reserves
        if (tokenA < tokenB) {
            amountOut = (amountIn * reserveB) / reserveA;
        } else {
            amountOut = (amountIn * reserveA) / reserveB;
        }
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint amount) external {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function totalSupply() external view returns (uint);
    function balanceOf(address account) external view returns (uint);
    function transfer(address recipient, uint amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint);
    function approve(address spender, uint amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);
}
```
