"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdogecoin20-portal.pages.dev
Prompt: Create code to add liquidity for DOGE20 tokens on Uniswap, ensuring compliance with the allocation of 10% of the total token supply for liquidity provision.
Generated: DETERMINISTIC_622eb6592ab01a92
Batch ID: 20250612_153526
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

// Import Uniswap interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20LiquidityManager is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;
    IERC20 public doge20Token;

    // Event for logging liquidity adds
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the contract with the router and token address
    constructor(address _router, address _token) {
        uniswapRouter = IUniswapV2Router02(_router);
        doge20Token = IERC20(_token);
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(address(doge20Token), uniswapRouter.WETH());
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        
        // Ensure that the token amount does not exceed 10% of the total supply
        uint256 totalSupply = doge20Token.totalSupply();
        uint256 maxLiquidityAmount = (totalSupply * 10) / 100; // 10% of total supply
        require(tokenAmount <= maxLiquidityAmount, "Exceeds 10% of total supply for liquidity");

        // Transfer the token from the owner to this contract
        require(doge20Token.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        // Approve the Uniswap router to spend the tokens
        doge20Token.approve(address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            address(doge20Token),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            address(this), // liquidity will go to this contract
            block.timestamp // transaction deadline
        );

        // Emit liquidity addition event
        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Function to withdraw ERC20 tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(doge20Token), "Cannot withdraw DOGE20 tokens");
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Token withdrawal failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
