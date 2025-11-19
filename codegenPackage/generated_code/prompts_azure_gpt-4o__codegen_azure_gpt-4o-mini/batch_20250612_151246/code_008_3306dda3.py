"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Generate a Solidity function to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's anti-rug pull measures.
Generated: DETERMINISTIC_3306dda3b478ee44
Batch ID: 20250612_151246
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

contract LiquidityLocker is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
        bool isLocked;         // Status of the lock
    }

    // Mappings to store liquidity and team token locks
    mapping(address => Lock) public liquidityLocks;
    mapping(address => Lock) public teamTokenLocks;

    // Events for logging
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event TeamTokensLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(address indexed token, uint256 amount);
    event TeamTokensUnlocked(address indexed token, uint256 amount);

    // Function to lock liquidity for 20 years
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set lock details
        liquidityLocks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 20 * 365 days, // 20 years
            isLocked: true
        });

        emit LiquidityLocked(token, amount, liquidityLocks[token].unlockTime);
    }

    // Function to lock team tokens for 700 days
    function lockTeamTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set lock details
        teamTokenLocks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 700 days, // 700 days
            isLocked: true
        });

        emit TeamTokensLocked(token, amount, teamTokenLocks[token].unlockTime);
    }

    // Function to unlock liquidity after the lock period
    function unlockLiquidity(address token) external onlyOwner {
        Lock storage lock = liquidityLocks[token];
        require(lock.isLocked, "Liquidity is not locked");
        require(block.timestamp >= lock.unlockTime, "Unlock time has not yet arrived");

        uint256 amount = lock.amount;
        lock.isLocked = false; // Mark as unlocked

        // Transfer tokens back to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit LiquidityUnlocked(token, amount);
    }

    // Function to unlock team tokens after the lock period
    function unlockTeamTokens(address token) external onlyOwner {
        Lock storage lock = teamTokenLocks[token];
        require(lock.isLocked, "Team tokens are not locked");
        require(block.timestamp >= lock.unlockTime, "Unlock time has not yet arrived");

        uint256 amount = lock.amount;
        lock.isLocked = false; // Mark as unlocked

        // Transfer tokens back to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit TeamTokensUnlocked(token, amount);
    }
}
```
