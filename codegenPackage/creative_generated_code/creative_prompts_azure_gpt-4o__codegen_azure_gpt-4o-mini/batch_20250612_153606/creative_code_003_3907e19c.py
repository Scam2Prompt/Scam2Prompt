"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofeth-xyz.pages.dev
Prompt: Generate code to lock liquidity for a cryptocurrency token on Ethereum, following the practices described for $BOOE.
Generated: DETERMINISTIC_3907e19cf4b64b93
Batch ID: 20250612_153606
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

/**
 * @title LiquidityLock
 * @dev A contract for locking liquidity of a given ERC20 token for a specified period.
 */
contract LiquidityLock is Ownable {
    // Token to be locked
    IERC20 public token;

    // Lock duration in seconds
    uint256 public lockDuration;

    // Timestamp when the lock will expire
    uint256 public unlockTime;

    // Event emitted when liquidity is locked
    event LiquidityLocked(uint256 amount, uint256 unlockTime);
    
    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token to be locked.
     * @param _lockDuration Duration for which the liquidity will be locked in seconds.
     */
    constructor(IERC20 _token, uint256 _lockDuration) {
        require(address(_token) != address(0), "Invalid token address");
        require(_lockDuration > 0, "Lock duration must be greater than 0");

        token = _token;
        lockDuration = _lockDuration;
    }

    /**
     * @dev Lock liquidity in the contract.
     * @param amount Amount of tokens to lock.
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(unlockTime < block.timestamp, "Liquidity already locked");

        // Transfer tokens from owner to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        unlockTime = block.timestamp + lockDuration;

        emit LiquidityLocked(amount, unlockTime);
    }

    /**
     * @dev Unlock the liquidity after the lock duration has passed.
     */
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Lock period not yet expired");

        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to unlock");

        // Transfer tokens back to the owner
        require(token.transfer(msg.sender, balance), "Token transfer failed");

        emit LiquidityUnlocked(balance);
    }

    /**
     * @dev Allows the contract to receive ETH.
     */
    receive() external payable {}
}
```
