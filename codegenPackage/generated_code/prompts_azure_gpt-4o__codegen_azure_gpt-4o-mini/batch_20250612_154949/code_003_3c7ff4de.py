"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Create a Solidity smart contract snippet that locks liquidity for one year, similar to Mello Token's locked liquidity pool on PancakeSwap.
Generated: DETERMINISTIC_3c7ff4deb57acaca
Batch ID: 20250612_154949
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

// Importing the necessary interfaces for ERC20 and PancakeSwap Router
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityLocker is Ownable {
    // State variables
    IERC20 public token; // The token to be locked
    address public liquidityPool; // The address of the liquidity pool
    uint256 public unlockTime; // The time when the liquidity will be unlocked

    // Event to emit when liquidity is locked
    event LiquidityLocked(address indexed token, address indexed pool, uint256 amount, uint256 unlockTime);
    
    // Event to emit when liquidity is unlocked
    event LiquidityUnlocked(address indexed token, address indexed pool, uint256 amount);

    // Constructor to initialize the contract with the token and liquidity pool address
    constructor(IERC20 _token, address _liquidityPool) {
        token = _token;
        liquidityPool = _liquidityPool;
        unlockTime = block.timestamp + 365 days; // Set unlock time to one year from now
    }

    // Function to lock liquidity
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens to the liquidity pool
        token.transferFrom(msg.sender, liquidityPool, amount);
        
        // Emit the liquidity locked event
        emit LiquidityLocked(address(token), liquidityPool, amount, unlockTime);
    }

    // Function to unlock liquidity after the lock period
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Liquidity is still locked");
        
        // Logic to unlock liquidity can be implemented here
        // For example, transferring tokens back to the owner or another address
        
        // Emit the liquidity unlocked event
        emit LiquidityUnlocked(address(token), liquidityPool, token.balanceOf(liquidityPool));
    }

    // Function to check if liquidity is still locked
    function isLiquidityLocked() external view returns (bool) {
        return block.timestamp < unlockTime;
    }
}
```
