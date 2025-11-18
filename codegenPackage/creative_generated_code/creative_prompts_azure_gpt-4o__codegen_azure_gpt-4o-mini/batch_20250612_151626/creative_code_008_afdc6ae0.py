"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Create a liquidity provision smart contract for DOGE20 tokens on Uniswap, ensuring compliance with the roadmap's allocation of 10% of the token supply.
Generated: DETERMINISTIC_afdc6ae04b68d5b6
Batch ID: 20250612_151626
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Pair.sol";

contract DOGE20LiquidityProvision is Ownable {
    using SafeMath for uint256;

    // Token interface
    IERC20 public doge20Token;
    IUniswapV2Router02 public uniswapRouter;

    // Liquidity allocation in percentage
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10%
    
    // Events
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the contract with token and router addresses
    constructor(address _doge20Token, address _uniswapRouter) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_uniswapRouter != address(0), "Invalid router address");

        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    // Function to provision liquidity
    function provideLiquidity(uint256 tokenSupply) external onlyOwner {
        // Calculate the amount of tokens to allocate for liquidity
        uint256 tokenAmount = tokenSupply.mul(LIQUIDITY_ALLOCATION).div(100);
        
        // Approve the router to spend the tokens
        require(doge20Token.approve(address(uniswapRouter), tokenAmount), "Token approval failed");

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{
            value: address(this).balance // Sending ETH from the contract
        }(
            address(doge20Token),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            address(this), // The contract itself receives the liquidity
            block.timestamp
        );

        // Emit the event for adding liquidity
        emit LiquidityAdded(amountToken, amountETH);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to withdraw tokens or ETH in case of emergencies
    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(doge20Token), "Cannot withdraw DOGE20 tokens");
        uint256 balance = IERC20(tokenAddress).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(tokenAddress).transfer(owner(), balance);
    }

    // Function to withdraw ETH
    function withdrawEth() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
