"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Write a Solidity contract that uses the `receive()` function to accept Ether payments and integrates with Uniswap for liquidity operations, as described in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_d9f2f360cb381277
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

// Importing necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SlippageBot {
    // State variables
    address private owner;
    IUniswapV2Router02 public uniswapRouter;
    
    // Events
    event PaymentReceived(address sender, uint256 amount);
    event TokensSwapped(address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);
    
    // Constructor to initialize the Uniswap router address
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        owner = msg.sender;
    }

    // Fallback function to receive Ether
    receive() external payable {
        emit PaymentReceived(msg.sender, msg.value);
    }

    // Function to swap ETH for a specific token
    function swapEthForToken(address tokenOut, uint256 minTokensOut) external {
        require(msg.value > 0, "Must send Ether to swap");

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = tokenOut;

        // Approve the router to spend tokens
        // Note: This is not necessary for ETH, included for completeness if calling from tokens
        // IERC20(tokenOut).approve(address(uniswapRouter), minTokensOut);

        // Set the swap parameters
        uint256 deadline = block.timestamp + 300; // 5 minutes
        uint256[] memory amountsOut = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minTokensOut,
            path,
            address(this),
            deadline
        );

        emit TokensSwapped(uniswapRouter.WETH(), tokenOut, msg.value, amountsOut[1]);
    }

    // Function to withdraw Ether from the contract, callable only by the owner
    function withdrawEther() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        payable(owner).transfer(address(this).balance);
    }

    // Function to withdraw tokens from the contract, callable only by the owner
    function withdrawTokens(address token) external {
        require(msg.sender == owner, "Only the owner can withdraw tokens");
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(owner, balance);
    }
}
```
