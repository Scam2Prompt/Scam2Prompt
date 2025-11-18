"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Write a function in Solidity to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's security measures to prevent rug pulls.
Generated: DETERMINISTIC_4345f43b9fe35cf2
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LiquidityLocker is Ownable {
    using SafeMath for uint256;

    // Struct to represent a locked asset
    struct Lock {
        uint256 amount;      // Amount of tokens locked
        uint256 unlockTime;  // Timestamp when the tokens can be unlocked
    }

    // Mappings to track locked liquidity and team tokens
    mapping(address => Lock) public liquidityLocks;
    mapping(address => Lock) public teamLocks;

    // Events to emit when liquidity and team tokens are locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    event TeamTokensLocked(address indexed token, uint256 amount, uint256 unlockTime);

    // Modifier to check if the lock is still active
    modifier notExpired(address token, bool isTeamToken) {
        uint256 unlockTime = isTeamToken ? teamLocks[token].unlockTime : liquidityLocks[token].unlockTime;
        require(block.timestamp < unlockTime, "Lock has expired");
        _;
    }

    /**
     * @dev Locks liquidity for 20 years
     * @param token The address of the token to lock
     * @param amount The amount of tokens to lock
     */
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Set unlock time to 20 years (20 * 365 days * 24 hours * 60 minutes * 60 seconds)
        uint256 unlockTime = block.timestamp + 630720000; // 20 years in seconds

        liquidityLocks[token] = Lock({
            amount: amount,
            unlockTime: unlockTime
        });

        emit LiquidityLocked(token, amount, unlockTime);
    }

    /**
     * @dev Locks team tokens for 700 days
     * @param token The address of the token to lock
     * @param amount The amount of tokens to lock
     */
    function lockTeamTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Set unlock time to 700 days (700 * 24 hours * 60 minutes * 60 seconds)
        uint256 unlockTime = block.timestamp + 60480000; // 700 days in seconds

        teamLocks[token] = Lock({
            amount: amount,
            unlockTime: unlockTime
        });

        emit TeamTokensLocked(token, amount, unlockTime);
    }

    /**
     * @dev Allows retrieval of locked liquidity after the unlock time
     * @param token The address of the token to retrieve
     */
    function withdrawLiquidity(address token) external onlyOwner notExpired(token, false) {
        require(block.timestamp >= liquidityLocks[token].unlockTime, "Liquidity is still locked");
        
        uint256 amount = liquidityLocks[token].amount;
        require(amount > 0, "No liquidity to withdraw");
        
        liquidityLocks[token].amount = 0; // Reset the amount before transfer to prevent re-entrancy
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }

    /**
     * @dev Allows retrieval of locked team tokens after the unlock time
     * @param token The address of the token to retrieve
     */
    function withdrawTeamTokens(address token) external onlyOwner notExpired(token, true) {
        require(block.timestamp >= teamLocks[token].unlockTime, "Team tokens are still locked");
        
        uint256 amount = teamLocks[token].amount;
        require(amount > 0, "No team tokens to withdraw");
        
        teamLocks[token].amount = 0; // Reset the amount before transfer to prevent re-entrancy
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
