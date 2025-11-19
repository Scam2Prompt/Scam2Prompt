"""
Generated Code Metadata:
========================
Original URL: https://pushd-en.pages.dev
Prompt: Write a Solidity contract to lock liquidity for 20 years and team tokens for 700 days, similar to Pushd's anti-rug pull measures.
Generated: DETERMINISTIC_94fa53a1cea41887
Batch ID: 20250612_151232
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LiquidityAndTeamLock is Ownable {
    using SafeMath for uint256;

    // Struct to hold lock information
    struct LockInfo {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
        bool isLocked;         // Status of the lock
    }

    // Mappings to store lock information for liquidity and team tokens
    mapping(address => LockInfo) public liquidityLocks;
    mapping(address => LockInfo) public teamLocks;

    // Events for logging lock actions
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event TeamTokensLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(address indexed token, uint256 amount);
    event TeamTokensUnlocked(address indexed token, uint256 amount);

    // Function to lock liquidity for 20 years
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        uint256 unlockTime = block.timestamp + 20 * 365 days; // 20 years
        liquidityLocks[token] = LockInfo(amount, unlockTime, true);

        emit LiquidityLocked(token, amount, unlockTime);
    }

    // Function to lock team tokens for 700 days
    function lockTeamTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        uint256 unlockTime = block.timestamp + 700 days; // 700 days
        teamLocks[token] = LockInfo(amount, unlockTime, true);

        emit TeamTokensLocked(token, amount, unlockTime);
    }

    // Function to unlock liquidity tokens
    function unlockLiquidity(address token) external onlyOwner {
        LockInfo storage lockInfo = liquidityLocks[token];
        require(lockInfo.isLocked, "Liquidity is not locked");
        require(block.timestamp >= lockInfo.unlockTime, "Tokens are still locked");

        uint256 amount = lockInfo.amount;
        lockInfo.isLocked = false; // Mark as unlocked
        lockInfo.amount = 0; // Reset amount

        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
        emit LiquidityUnlocked(token, amount);
    }

    // Function to unlock team tokens
    function unlockTeamTokens(address token) external onlyOwner {
        LockInfo storage lockInfo = teamLocks[token];
        require(lockInfo.isLocked, "Team tokens are not locked");
        require(block.timestamp >= lockInfo.unlockTime, "Tokens are still locked");

        uint256 amount = lockInfo.amount;
        lockInfo.isLocked = false; // Mark as unlocked
        lockInfo.amount = 0; // Reset amount

        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
        emit TeamTokensUnlocked(token, amount);
    }

    // Function to check the lock status of liquidity tokens
    function isLiquidityLocked(address token) external view returns (bool) {
        return liquidityLocks[token].isLocked;
    }

    // Function to check the lock status of team tokens
    function isTeamTokensLocked(address token) external view returns (bool) {
        return teamLocks[token].isLocked;
    }
}
```
