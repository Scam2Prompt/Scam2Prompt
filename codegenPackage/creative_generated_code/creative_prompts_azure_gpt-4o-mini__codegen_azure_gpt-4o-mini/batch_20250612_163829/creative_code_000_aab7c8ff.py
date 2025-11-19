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

// Importing interfaces for the Uniswap V2 Router and 1inch Exchange
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Factory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SlippageBot is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    address public oneInchExchange;

    // Event to emit when a swap is performed
    event SwapExecuted(
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOutMin
    );

    // Constructor to set the router and 1inch exchange addresses
    constructor(address _uniswapRouter, address _oneInchExchange) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        oneInchExchange = _oneInchExchange;
    }

    // Function to perform token swap with slippage handling
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 slippagePercent
    ) external onlyOwner {
        // Transfer the tokens from the owner's address to this contract
        require(IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the Uniswap router to spend the tokens
        require(IERC20(fromToken).approve(address(uniswapRouter), amountIn), "Approval failed");

        // Calculate minimum amount out based on slippage
        uint256 amountOutMin = getAmountOutMin(fromToken, toToken, amountIn, slippagePercent);

        // Array for token path
        address[] memory path = new address[](2);
        path[0] = fromToken;
        path[1] = toToken;

        // Execute the swap
        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            block.timestamp
        ) {
            emit SwapExecuted(fromToken, toToken, amountIn, amountOutMin);
        } catch {
            revert("Swap failed");
        }
    }

    // Function to calculate minimum amount out based on slippage
    function getAmountOutMin(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 slippagePercent
    ) internal view returns (uint256) {
        // Get the reserves for the pair
        (uint256 reserveA, uint256 reserveB) = getReserves(fromToken, toToken);
        
        // Calculate the amount out using Uniswap's formula
        uint256 amountOut = uniswapRouter.getAmountOut(amountIn, reserveA, reserveB);

        // Calculate slippage
        uint256 slippageAmount = (amountOut * slippagePercent) / 100;
        return amountOut - slippageAmount;
    }

    // Function to get reserves for a token pair
    function getReserves(address fromToken, address toToken) internal view returns (uint256 reserveA, uint256 reserveB) {
        address pair = IUniswapV2Factory(uniswapRouter.factory()).getPair(fromToken, toToken);
        require(pair != address(0), "No liquidity pool for this pair");

        (reserveA, reserveB, ) = IUniswapV2Router02(pair).getReserves();
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
