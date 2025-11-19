"""
Generated Code Metadata:
========================
Original URL: https://dogee1.pages.dev
Prompt: Create a liquidity provision smart contract for DOGE20 tokens on Uniswap, ensuring compliance with the roadmap's allocation of 10% of the token supply.
Generated: DETERMINISTIC_afdc6ae04b68d5b6
Batch ID: 20250612_151626
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LiquidityProvision contract for DOGE20 tokens on Uniswap
contract LiquidityProvision is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public doge20Token; // DOGE20 token contract
    address public uniswapRouter; // Uniswap router address
    uint256 public totalSupply; // Total supply of DOGE20 tokens
    uint256 public liquidityAllocation; // Amount allocated for liquidity provision

    // Event to log liquidity provision
    event LiquidityProvided(address indexed provider, uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the contract
    constructor(address _doge20Token, address _uniswapRouter, uint256 _totalSupply) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        doge20Token = IERC20(_doge20Token);
        uniswapRouter = _uniswapRouter;
        totalSupply = _totalSupply;
        liquidityAllocation = totalSupply.mul(10).div(100); // 10% of total supply
    }

    // Function to provide liquidity to Uniswap
    function provideLiquidity(uint256 tokenAmount, uint256 ethAmount) external onlyOwner {
        require(tokenAmount <= liquidityAllocation, "Exceeds liquidity allocation");
        require(doge20Token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance");

        // Approve the Uniswap router to spend the DOGE20 tokens
        doge20Token.approve(uniswapRouter, tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = IUniswapV2Router(uniswapRouter).addLiquidityETH{value: ethAmount}(
            address(doge20Token),
            tokenAmount,
            0, // Slippage is unavoidable
            0, // Slippage is unavoidable
            address(this),
            block.timestamp
        );

        // Emit event for liquidity provision
        emit LiquidityProvided(msg.sender, amountToken, amountETH);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient token balance");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to get the current balance of DOGE20 tokens
    function getDoge20Balance() external view returns (uint256) {
        return doge20Token.balanceOf(address(this));
    }

    // Function to get the current ETH balance
    function getEthBalance() external view returns (uint256) {
        return address(this).balance;
    }
}

// Interface for Uniswap V2 Router
interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint256 tokenAmount,
        uint256 minTokenAmount,
        uint256 minETHAmount,
        address to,
        uint256 deadline
    ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
}
```
