"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Provide code examples for creating liquidity pools on decentralized exchanges (DEXs) for $STARS tokens, as outlined in the Crypto All-Stars tokenomics.
Generated: DETERMINISTIC_72513b75152940a0
Batch ID: 20250612_153722
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LiquidityPoolManager is Ownable {
    // State variables
    IUniswapV2Router02 public uniswapRouter;
    IUniswapV2Factory public uniswapFactory;
    address public starsTokenAddress;
    address public liquidityPair;

    // Events
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);
    event LiquidityRemoved(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the contract with necessary parameters
    constructor(address _router, address _factory, address _starsToken) {
        uniswapRouter = IUniswapV2Router02(_router);
        uniswapFactory = IUniswapV2Factory(_factory);
        starsTokenAddress = _starsToken;
    }

    // Function to create a liquidity pool for $STARS tokens
    function createLiquidityPool(uint256 tokenAmount) external onlyOwner {
        // Approve the router to spend the specified amount of $STARS tokens
        IERC20(starsTokenAddress).approve(address(uniswapRouter), tokenAmount);

        // Create the liquidity pair if it doesn't exist
        liquidityPair = uniswapFactory.getPair(starsTokenAddress, uniswapRouter.WETH());
        if (liquidityPair == address(0)) {
            liquidityPair = uniswapFactory.createPair(starsTokenAddress, uniswapRouter.WETH());
        }

        // Add liquidity to the pool
        (uint256 amountToken, uint256 amountETH, ) = uniswapRouter.addLiquidityETH{value: msg.value}(
            starsTokenAddress,
            tokenAmount,
            0, // Slippage is unavoidable
            0, // Slippage is unavoidable
            address(this),
            block.timestamp
        );

        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to remove liquidity from the pool
    function removeLiquidity(uint256 liquidity) external onlyOwner {
        // Approve the router to spend the liquidity tokens
        IERC20(liquidityPair).approve(address(uniswapRouter), liquidity);

        // Remove liquidity from the pool
        (uint256 amountToken, uint256 amountETH) = uniswapRouter.removeLiquidityETH(
            starsTokenAddress,
            liquidity,
            0, // Slippage is unavoidable
            0, // Slippage is unavoidable
            address(this),
            block.timestamp
        );

        emit LiquidityRemoved(amountToken, amountETH);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw $STARS tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        IERC20(starsTokenAddress).transfer(owner(), amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
