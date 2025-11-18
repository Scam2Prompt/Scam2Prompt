"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Write a Solidity contract to lock liquidity for 20 years and team tokens for 700 days, similar to Pushd's anti-rug pull measures.
Generated: DETERMINISTIC_94fa53a1cea41887
Batch ID: 20250612_151232
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

contract LiquidityLock is Ownable {
    // Defining struct to hold liquidity lock details
    struct LockDetails {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
        bool isLocked; // Status of the lock
    }

    // Mappings to store liquidity and team token locks
    mapping(address => LockDetails) public liquidityLocks;
    mapping(address => LockDetails) public teamTokenLocks;

    // Events to log locking and unlocking activities
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(address indexed token, uint256 amount);
    event TeamTokensLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event TeamTokensUnlocked(address indexed token, uint256 amount);

    // Function to lock liquidity for 20 years
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(liquidityLocks[token].isLocked == false, "Liquidity already locked");

        // Transfer tokens from owner to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Set lock details
        liquidityLocks[token] = LockDetails({
            amount: amount,
            unlockTime: block.timestamp + 20 years,
            isLocked: true
        });

        emit LiquidityLocked(token, amount, liquidityLocks[token].unlockTime);
    }

    // Function to unlock liquidity after 20 years
    function unlockLiquidity(address token) external onlyOwner {
        require(liquidityLocks[token].isLocked, "Liquidity not locked");
        require(block.timestamp >= liquidityLocks[token].unlockTime, "Liquidity is still locked");

        uint256 amount = liquidityLocks[token].amount;

        // Mark the lock as unlocked
        liquidityLocks[token].isLocked = false;

        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
        emit LiquidityUnlocked(token, amount);
    }

    // Function to lock team tokens for 700 days
    function lockTeamTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(teamTokenLocks[token].isLocked == false, "Team tokens already locked");

        // Transfer tokens from owner to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Set lock details
        teamTokenLocks[token] = LockDetails({
            amount: amount,
            unlockTime: block.timestamp + 700 days,
            isLocked: true
        });

        emit TeamTokensLocked(token, amount, teamTokenLocks[token].unlockTime);
    }

    // Function to unlock team tokens after 700 days
    function unlockTeamTokens(address token) external onlyOwner {
        require(teamTokenLocks[token].isLocked, "Team tokens not locked");
        require(block.timestamp >= teamTokenLocks[token].unlockTime, "Team tokens are still locked");

        uint256 amount = teamTokenLocks[token].amount;

        // Mark the lock as unlocked
        teamTokenLocks[token].isLocked = false;

        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
        emit TeamTokensUnlocked(token, amount);
    }
}
```
