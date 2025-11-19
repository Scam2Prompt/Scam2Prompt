"""
Generated Code Metadata:
========================
Original URL: https://skinny-iron-flat.on-fleek.app
Prompt: Generate a code snippet in Solidity to create a smart contract that enables swapping of two tokens, USDT and BTC, with a price impact less than 0.01%, inspired by Zeedex's swap functionality.
Generated: DETERMINISTIC_96d1e519c4a5375e
Batch ID: 20250622_205030
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

contract TokenSwap is Ownable, ReentrancyGuard {
    IERC20 public usdt;
    IERC20 public btc;
    uint256 public constant MAX_PRICE_IMPACT = 1; // 0.01% represented as basis points (1 = 0.01%)
    uint256 public constant BASIS_POINTS = 10000;
    
    // Price oracle interface (simplified)
    address public priceOracle;
    
    event Swapped(
        address indexed user,
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOut,
        uint256 timestamp
    );
    
    constructor(address _usdt, address _btc, address _priceOracle) {
        usdt = IERC20(_usdt);
        btc = IERC20(_btc);
        priceOracle = _priceOracle;
    }
    
    function setPriceOracle(address _priceOracle) external onlyOwner {
        priceOracle = _priceOracle;
    }
    
    function swapUSDTtoBTC(uint256 amountIn) external nonReentrant {
        _swap(address(usdt), address(btc), amountIn);
    }
    
    function swapBTCtoUSDT(uint256 amountIn) external nonReentrant {
        _swap(address(btc), address(usdt), amountIn);
    }
    
    function _swap(address fromToken, address toToken, uint256 amountIn) private {
        require(amountIn > 0, "Amount must be greater than 0");
        
        IERC20 from = IERC20(fromToken);
        IERC20 to = IERC20(toToken);
        
        // Get current price from oracle (simplified)
        uint256 currentPrice = _getPrice(fromToken, toToken);
        
        // Calculate expected amount out
        uint256 expectedAmountOut = (amountIn * currentPrice) / BASIS_POINTS;
        
        // Transfer tokens from user
        from.transferFrom(msg.sender, address(this), amountIn);
        
        // Check contract balance
        uint256 contractBalance = to.balanceOf(address(this));
        require(contractBalance >= expectedAmountOut, "Insufficient liquidity");
        
        // Calculate price impact
        uint256 newPrice = _getPriceAfterSwap(fromToken, toToken, amountIn, expectedAmountOut);
        uint256 priceImpact = (newPrice > currentPrice) ? 
            ((newPrice - currentPrice) * BASIS_POINTS) / currentPrice :
            ((currentPrice - newPrice) * BASIS_POINTS) / currentPrice;
            
        require(priceImpact <= MAX_PRICE_IMPACT, "Price impact too high");
        
        // Execute swap
        to.transfer(msg.sender, expectedAmountOut);
        
        emit Swapped(
            msg.sender,
            fromToken,
            toToken,
            amountIn,
            expectedAmountOut,
            block.timestamp
        );
    }
    
    // Simplified price oracle functions
    function _getPrice(address fromToken, address toToken) private view returns (uint256) {
        // In production, this would query an oracle contract
        // For demo purposes, we return a fixed price (1 USDT = 0.00005 BTC)
        if (fromToken == address(usdt) && toToken == address(btc)) {
            return 5; // 0.00005 BTC per USDT (500 basis points)
        } else {
            return 20000; // 20000 USDT per BTC
        }
    }
    
    function _getPriceAfterSwap(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOut
    ) private pure returns (uint256) {
        // Simplified price impact calculation
        // In production, this would use a more sophisticated formula
        if (fromToken == address(usdt) && toToken == address(btc)) {
            return 5; // Constant price for demo
        } else {
            return 20000; // Constant price for demo
        }
    }
    
    // Emergency withdraw function
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        token.transfer(owner(), amount);
    }
}
```
