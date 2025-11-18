"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Write a Solidity contract for tokenomics similar to GrowBTC, including features like capped supply, locked tokens for a specific duration, and transparent allocation.
Generated: DETERMINISTIC_9804816a794b483a
Batch ID: 20250612_154452
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GrowBTC Token
 * @dev ERC20 Token with capped supply, locked tokens, and transparent allocation
 */
contract GrowBTC is ERC20, Ownable, ReentrancyGuard {
    // Maximum supply of the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** decimals();
    
    // Total locked tokens
    uint256 public lockedTokens;

    // Structure to hold information about locked tokens
    struct Lock {
        uint256 amount;
        uint256 unlockTime;
    }

    // Mapping of addresses to their locked tokens
    mapping(address => Lock) public locks;

    // Events for logging
    event TokensLocked(address indexed account, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed account, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol
     */
    constructor() ERC20("GrowBTC", "GBTC") {
        // Mint initial supply to the owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Lock tokens for a specified duration
     * @param amount Amount of tokens to lock
     * @param duration Duration in seconds for which the tokens will be locked
     */
    function lockTokens(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(locks[msg.sender].amount == 0, "Tokens already locked");

        // Calculate the unlock time
        uint256 unlockTime = block.timestamp + duration;

        // Transfer tokens to the contract for locking
        _transfer(msg.sender, address(this), amount);

        // Update locked tokens and record the lock
        lockedTokens += amount;
        locks[msg.sender] = Lock(amount, unlockTime);

        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Unlock tokens after the specified duration
     */
    function unlockTokens() external nonReentrant {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No locked tokens found");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        uint256 amountToUnlock = userLock.amount;
        userLock.amount = 0; // Reset the lock
        
        // Transfer the unlocked tokens back to the user
        _transfer(address(this), msg.sender, amountToUnlock);
        lockedTokens -= amountToUnlock;

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Override the _transfer function to prevent transfers of locked tokens
     */
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(locks[sender].amount == 0 || block.timestamp >= locks[sender].unlockTime, "Tokens are locked");
        super._transfer(sender, recipient, amount);
    }
}
```
