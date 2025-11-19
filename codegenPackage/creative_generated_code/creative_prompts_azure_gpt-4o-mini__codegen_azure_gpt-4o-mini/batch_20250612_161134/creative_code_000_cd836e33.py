"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity function for a Uniswap slippage bot that can handle mainnet transactions, referencing the contract structure provided in the UniswapSlippageBot example.
Generated: DETERMINISTIC_cd836e33226a3b63
Batch ID: 20250612_161134
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

// Import necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UniswapSlippageBot {
    // State variables
    address private owner;
    IUniswapV2Router02 public uniswapRouter;

    // Events for logging
    event Swapped(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOutMin, address indexed recipient);

    // Constructor to set the Uniswap router address and owner
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        uniswapRouter = IUniswapV2Router02(_router);
        owner = msg.sender;
    }

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to swap tokens with slippage control
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 slippage,
        address to
    ) external onlyOwner {
        require(slippage >= 0 && slippage <= 100, "Slippage must be between 0 and 100");
        
        // Transfer the specified amount of input tokens to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the input tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Calculate the minimum amount out based on slippage
        uint256 amountOutMin = getAmountOutMin(amountIn, slippage);

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            block.timestamp
        );

        emit Swapped(tokenIn, tokenOut, amountIn, amountOutMin, to);
    }

    // Internal function to calculate minimum amount out based on slippage
    function getAmountOutMin(uint256 amountIn, uint256 slippage) internal view returns (uint256) {
        // Get the token price from Uniswap's pair
        uint256[] memory amountsOut = uniswapRouter.getAmountsOut(amountIn, new address[](2){path[0], path[1]});
        uint256 amountOut = amountsOut[1];

        // Calculate the minimum amount out based on slippage
        return amountOut - (amountOut * slippage / 100);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
