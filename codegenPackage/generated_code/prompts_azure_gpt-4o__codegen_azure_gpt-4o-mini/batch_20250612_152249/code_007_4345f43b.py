"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Write a function in Solidity to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's security measures to prevent rug pulls.
Generated: DETERMINISTIC_4345f43b9fe35cf2
Batch ID: 20250612_152249
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

/**
 * @title LiquidityLocker
 * @dev This contract locks liquidity and team tokens for specified durations to prevent rug pulls.
 */
contract LiquidityLocker is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
    }

    // Mappings to store locked liquidity and team tokens
    mapping(address => Lock) public liquidityLocks;
    mapping(address => Lock) public teamTokenLocks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    
    // Event emitted when team tokens are locked
    event TeamTokensLocked(address indexed token, uint256 amount, uint256 unlockTime);

    /**
     * @dev Locks liquidity for 20 years.
     * @param token The address of the ERC20 token to lock.
     * @param amount The amount of tokens to lock.
     */
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set the lock details
        liquidityLocks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 20 * 365 days // 20 years
        });

        emit LiquidityLocked(token, amount, liquidityLocks[token].unlockTime);
    }

    /**
     * @dev Locks team tokens for 700 days.
     * @param token The address of the ERC20 token to lock.
     * @param amount The amount of tokens to lock.
     */
    function lockTeamTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Set the lock details
        teamTokenLocks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 700 days // 700 days
        });

        emit TeamTokensLocked(token, amount, teamTokenLocks[token].unlockTime);
    }

    /**
     * @dev Allows the owner to withdraw tokens after the lock period has expired.
     * @param token The address of the ERC20 token to withdraw.
     */
    function withdrawLockedTokens(address token) external onlyOwner {
        Lock storage liquidityLock = liquidityLocks[token];
        Lock storage teamTokenLock = teamTokenLocks[token];

        // Check if liquidity lock has expired
        if (liquidityLock.unlockTime <= block.timestamp) {
            uint256 amount = liquidityLock.amount;
            liquidityLock.amount = 0; // Prevent re-entrancy
            require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
        }

        // Check if team token lock has expired
        if (teamTokenLock.unlockTime <= block.timestamp) {
            uint256 amount = teamTokenLock.amount;
            teamTokenLock.amount = 0; // Prevent re-entrancy
            require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
        }
    }
}
```
