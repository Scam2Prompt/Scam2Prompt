"""
Generated Code Metadata:
========================
Original URL: https://wwwasterdex.com
Prompt: Generate an example of a smart contract that interacts with Aster's multi-chain liquidity for automated trading.
Generated: DETERMINISTIC_2df2d22bb340e3a3
Batch ID: 20250612_163133
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

// Import OpenZeppelin contracts for safe math and ownership
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Aster's liquidity pool
interface IAsterLiquidityPool {
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 chainId
    ) external returns (uint256 amountOut);
    
    function getExpectedAmountOut(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 chainId
    ) external view returns (uint256);
}

contract AsterAutoTrader is Ownable {
    using SafeMath for uint256;
    
    IAsterLiquidityPool public asterPool;
    address public feeReceiver;
    uint256 public feePercentage; // Basis points (e.g., 100 = 1%)
    
    event SwapExecuted(
        address indexed user,
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOut,
        uint256 chainId
    );
    
    event FeeCollected(
        address indexed user,
        address token,
        uint256 amount
    );
    
    constructor(
        address _asterPoolAddress,
        address _feeReceiver,
        uint256 _feePercentage
    ) {
        require(_asterPoolAddress != address(0), "Invalid pool address");
        require(_feeReceiver != address(0), "Invalid fee receiver");
        require(_feePercentage <= 1000, "Fee too high"); // Max 10%
        
        asterPool = IAsterLiquidityPool(_asterPoolAddress);
        feeReceiver = _feeReceiver;
        feePercentage = _feePercentage;
    }
    
    function executeSwap(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 chainId
    ) external returns (uint256) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(fromToken != toToken, "Tokens must be different");
        
        // Calculate fee
        uint256 feeAmount = amountIn.mul(feePercentage).div(10000);
        uint256 swapAmount = amountIn.sub(feeAmount);
        
        // Transfer tokens from user
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);
        
        // Collect fee
        if (feeAmount > 0) {
            IERC20(fromToken).transfer(feeReceiver, feeAmount);
            emit FeeCollected(msg.sender, fromToken, feeAmount);
        }
        
        // Approve Aster pool to spend tokens
        IERC20(fromToken).approve(address(asterPool), swapAmount);
        
        // Execute swap
        uint256 amountOut = asterPool.swapTokens(
            fromToken,
            toToken,
            swapAmount,
            minAmountOut,
            chainId
        );
        
        require(amountOut >= minAmountOut, "Insufficient output amount");
        
        // Transfer output tokens to user
        IERC20(toToken).transfer(msg.sender, amountOut);
        
        emit SwapExecuted(
            msg.sender,
            fromToken,
            toToken,
            swapAmount,
            amountOut,
            chainId
        );
        
        return amountOut;
    }
    
    function getExpectedAmountOut(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 chainId
    ) external view returns (uint256) {
        uint256 swapAmount = amountIn.sub(amountIn.mul(feePercentage).div(10000));
        return asterPool.getExpectedAmountOut(
            fromToken,
            toToken,
            swapAmount,
            chainId
        );
    }
    
    function updateFeeReceiver(address newFeeReceiver) external onlyOwner {
        require(newFeeReceiver != address(0), "Invalid fee receiver");
        feeReceiver = newFeeReceiver;
    }
    
    function updateFeePercentage(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 1000, "Fee too high");
        feePercentage = newFeePercentage;
    }
    
    // Emergency function to recover ERC20 tokens
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
