"""
Generated Code Metadata:
========================
Original URL: https://revoke.bouncebit-7g1.pages.dev
Prompt: Create a Solidity smart contract for managing liquidity pools on the Bitleverage app, specifically for "FDUSD" and "BOUNCEBIT."
Generated: DETERMINISTIC_c970442a4b02a5a8
Batch ID: 20250612_152321
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

contract BitleverageLiquidityPool is Ownable, ReentrancyGuard {
    IERC20 public fdusdToken;
    IERC20 public bouncebitToken;
    
    uint256 public totalFdusdLiquidity;
    uint256 public totalBouncebitLiquidity;
    
    mapping(address => uint256) public userFdusdLiquidity;
    mapping(address => uint256) public userBouncebitLiquidity;
    
    event LiquidityAdded(address indexed provider, uint256 fdusdAmount, uint256 bouncebitAmount);
    event LiquidityRemoved(address indexed provider, uint256 fdusdAmount, uint256 bouncebitAmount);
    event TokensSwapped(address indexed user, bool fdusdToBouncebit, uint256 amountIn, uint256 amountOut);

    constructor(address _fdusdToken, address _bouncebitToken) {
        require(_fdusdToken != address(0), "FDUSD token address cannot be zero");
        require(_bouncebitToken != address(0), "BounceBit token address cannot be zero");
        
        fdusdToken = IERC20(_fdusdToken);
        bouncebitToken = IERC20(_bouncebitToken);
    }

    function addLiquidity(uint256 fdusdAmount, uint256 bouncebitAmount) external nonReentrant {
        require(fdusdAmount > 0, "FDUSD amount must be greater than zero");
        require(bouncebitAmount > 0, "BounceBit amount must be greater than zero");
        
        // Transfer tokens from user to contract
        require(fdusdToken.transferFrom(msg.sender, address(this), fdusdAmount), "FDUSD transfer failed");
        require(bouncebitToken.transferFrom(msg.sender, address(this), bouncebitAmount), "BounceBit transfer failed");
        
        // Update liquidity
        userFdusdLiquidity[msg.sender] += fdusdAmount;
        userBouncebitLiquidity[msg.sender] += bouncebitAmount;
        totalFdusdLiquidity += fdusdAmount;
        totalBouncebitLiquidity += bouncebitAmount;
        
        emit LiquidityAdded(msg.sender, fdusdAmount, bouncebitAmount);
    }

    function removeLiquidity(uint256 fdusdAmount, uint256 bouncebitAmount) external nonReentrant {
        require(fdusdAmount > 0, "FDUSD amount must be greater than zero");
        require(bouncebitAmount > 0, "BounceBit amount must be greater than zero");
        require(userFdusdLiquidity[msg.sender] >= fdusdAmount, "Insufficient FDUSD liquidity");
        require(userBouncebitLiquidity[msg.sender] >= bouncebitAmount, "Insufficient BounceBit liquidity");
        
        // Update liquidity
        userFdusdLiquidity[msg.sender] -= fdusdAmount;
        userBouncebitLiquidity[msg.sender] -= bouncebitAmount;
        totalFdusdLiquidity -= fdusdAmount;
        totalBouncebitLiquidity -= bouncebitAmount;
        
        // Transfer tokens back to user
        require(fdusdToken.transfer(msg.sender, fdusdAmount), "FDUSD transfer failed");
        require(bouncebitToken.transfer(msg.sender, bouncebitAmount), "BounceBit transfer failed");
        
        emit LiquidityRemoved(msg.sender, fdusdAmount, bouncebitAmount);
    }

    function swapFdusdToBouncebit(uint256 fdusdAmount) external nonReentrant {
        require(fdusdAmount > 0, "FDUSD amount must be greater than zero");
        require(totalFdusdLiquidity > 0 && totalBouncebitLiquidity > 0, "Insufficient liquidity");
        
        uint256 bouncebitAmount = (fdusdAmount * totalBouncebitLiquidity) / totalFdusdLiquidity;
        require(bouncebitAmount > 0, "Insufficient output amount");
        
        // Transfer FDUSD from user to contract
        require(fdusdToken.transferFrom(msg.sender, address(this), fdusdAmount), "FDUSD transfer failed");
        
        // Update liquidity
        totalFdusdLiquidity += fdusdAmount;
        totalBouncebitLiquidity -= bouncebitAmount;
        
        // Transfer BounceBit to user
        require(bouncebitToken.transfer(msg.sender, bouncebitAmount), "BounceBit transfer failed");
        
        emit TokensSwapped(msg.sender, true, fdusdAmount, bouncebitAmount);
    }

    function swapBouncebitToFdusd(uint256 bouncebitAmount) external nonReentrant {
        require(bouncebitAmount > 0, "BounceBit amount must be greater than zero");
        require(totalFdusdLiquidity > 0 && totalBouncebitLiquidity > 0, "Insufficient liquidity");
        
        uint256 fdusdAmount = (bouncebitAmount * totalFdusdLiquidity) / totalBouncebitLiquidity;
        require(fdusdAmount > 0, "Insufficient output amount");
        
        // Transfer BounceBit from user to contract
        require(bouncebitToken.transferFrom(msg.sender, address(this), bouncebitAmount), "BounceBit transfer failed");
        
        // Update liquidity
        totalBouncebitLiquidity += bouncebitAmount;
        totalFdusdLiquidity -= fdusdAmount;
        
        // Transfer FDUSD to user
        require(fdusdToken.transfer(msg.sender, fdusdAmount), "FDUSD transfer failed");
        
        emit TokensSwapped(msg.sender, false, bouncebitAmount, fdusdAmount);
    }

    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }
}
```
