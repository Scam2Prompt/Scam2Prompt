"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-is.pages.dev
Prompt: Develop a liquidity provision smart contract for DOGE20 tokens on Uniswap, ensuring 10% of the total token supply is allocated as described in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_b384d5cddbd7cb08
Batch ID: 20250612_153606
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

// Import the Uniswap interfaces for adding liquidity
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20LiquidityProvision is Ownable {
    // Uniswap router address (mainnet)
    IUniswapV2Router02 public uniswapRouter;
    
    // Address of the DOGE20 token
    IERC20 public doge20Token;

    // Amount of tokens to be allocated for liquidity
    uint256 public liquidityTokens;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to set the router and token addresses
    constructor(address _router, address _token, uint256 _totalSupply) {
        uniswapRouter = IUniswapV2Router02(_router);
        doge20Token = IERC20(_token);
        
        // Calculate 10% of the total supply
        liquidityTokens = _totalSupply * 10 / 100;
        
        // Approve the Uniswap router to spend the tokens
        doge20Token.approve(address(uniswapRouter), liquidityTokens);
    }

    // Function to add liquidity to the Uniswap pool
    function addLiquidity(uint256 ethAmount) external onlyOwner {
        require(liquidityTokens > 0, "No liquidity tokens available");
        
        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = 
            uniswapRouter.addLiquidityETH{value: ethAmount}(
                address(doge20Token),
                liquidityTokens,
                0, // Accept any amount of tokens
                0, // Accept any amount of ETH
                owner(),
                block.timestamp
            );

        // Emit the event
        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to withdraw stuck tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(tokenAddress).transfer(owner(), amount), "Transfer failed");
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    // Allow contract to receive ETH
    receive() external payable {}
}
```
