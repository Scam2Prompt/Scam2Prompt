"""
Generated Code Metadata:
========================
Original URL: https://solanche-token.blogspot.com
Prompt: Write a code example that demonstrates how to build a liquidity pool for $SAVAX tokens using the funds from the presale as detailed in the Solanche content.
Generated: DETERMINISTIC_739e4066c5b8b07e
Batch ID: 20250612_160940
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract SAVAXLiquidityPool is Ownable, ReentrancyGuard {
    IERC20 public sAVAX;
    IERC20 public pairedToken;
    IUniswapV2Router02 public uniswapRouter;
    address public liquidityPoolAddress;
    
    bool public liquidityAdded;
    uint256 public presaleFunds;
    uint256 public tokenAmountForLiquidity;
    
    event LiquidityAdded(
        uint256 tokenAmount,
        uint256 pairedTokenAmount,
        uint256 liquidity
    );
    
    constructor(
        address _sAVAX,
        address _pairedToken,
        address _uniswapRouter
    ) {
        require(_sAVAX != address(0), "Invalid sAVAX address");
        require(_pairedToken != address(0), "Invalid paired token address");
        require(_uniswapRouter != address(0), "Invalid router address");
        
        sAVAX = IERC20(_sAVAX);
        pairedToken = IERC20(_pairedToken);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }
    
    function setPresaleFunds(uint256 _presaleFunds) external onlyOwner {
        require(_presaleFunds > 0, "Funds must be greater than 0");
        presaleFunds = _presaleFunds;
    }
    
    function setTokenAmountForLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        tokenAmountForLiquidity = _amount;
    }
    
    function addLiquidity() external onlyOwner nonReentrant {
        require(!liquidityAdded, "Liquidity already added");
        require(presaleFunds > 0, "No presale funds available");
        require(tokenAmountForLiquidity > 0, "No tokens allocated for liquidity");
        
        // Approve token transfers
        sAVAX.approve(address(uniswapRouter), tokenAmountForLiquidity);
        pairedToken.approve(address(uniswapRouter), presaleFunds);
        
        // Add liquidity
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = 
            uniswapRouter.addLiquidity(
                address(sAVAX),
                address(pairedToken),
                tokenAmountForLiquidity,
                presaleFunds,
                0, // slippage is unavoidable
                0, // slippage is unavoidable
                address(this),
                block.timestamp + 3600
            );
        
        liquidityPoolAddress = IUniswapV2Factory(uniswapRouter.factory()).getPair(
            address(sAVAX),
            address(pairedToken)
        );
        
        liquidityAdded = true;
        
        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }
    
    function withdrawRemainingTokens() external onlyOwner {
        require(liquidityAdded, "Liquidity not yet added");
        
        uint256 remainingSAVAX = sAVAX.balanceOf(address(this));
        uint256 remainingPairedToken = pairedToken.balanceOf(address(this));
        
        if (remainingSAVAX > 0) {
            sAVAX.transfer(owner(), remainingSAVAX);
        }
        
        if (remainingPairedToken > 0) {
            pairedToken.transfer(owner(), remainingPairedToken);
        }
    }
    
    function emergencyWithdraw(address _token) external onlyOwner {
        require(_token != address(sAVAX) && _token != address(pairedToken), 
            "Cannot withdraw pool tokens");
        
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        token.transfer(owner(), balance);
    }
}
```
