"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Create a Solidity smart contract snippet that locks liquidity for one year, similar to Mello Token's locked liquidity pool on PancakeSwap.
Generated: DETERMINISTIC_3c7ff4deb57acaca
Batch ID: 20250612_154949
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// LiquidityLocker contract for locking liquidity in a PancakeSwap pool
contract LiquidityLocker is Ownable {
    // Token that is being locked
    IERC20 public token;
    
    // Address of the liquidity pool
    address public liquidityPool;
    
    // Timestamp until which the liquidity is locked
    uint256 public unlockTimestamp;

    // Event to emit when liquidity is locked
    event LiquidityLocked(address indexed token, address indexed liquidityPool, uint256 amount, uint256 unlockTime);
    
    // Event to emit when liquidity is unlocked
    event LiquidityUnlocked(address indexed token, address indexed liquidityPool, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _token, address _liquidityPool) {
        require(_token != address(0), "Token address cannot be zero");
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        
        token = IERC20(_token);
        liquidityPool = _liquidityPool;
    }

    // Function to lock liquidity for one year
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens from the owner to the liquidity pool
        token.transferFrom(msg.sender, liquidityPool, amount);

        // Set the unlock timestamp to one year from now
        unlockTimestamp = block.timestamp + 365 days;

        emit LiquidityLocked(address(token), liquidityPool, amount, unlockTimestamp);
    }

    // Function to unlock liquidity after the lock period
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTimestamp, "Liquidity is still locked");
        
        // Logic for unlocking liquidity would go here
        // For simplicity, this example assumes manual withdrawal
        // In a real scenario, you may want to automatically handle it

        emit LiquidityUnlocked(address(token), liquidityPool, token.balanceOf(liquidityPool));
    }

    // Function to check if liquidity is still locked
    function isLocked() external view returns (bool) {
        return block.timestamp < unlockTimestamp;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
