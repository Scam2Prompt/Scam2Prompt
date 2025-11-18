"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Create a function in Solidity for a smart contract that locks liquidity for a specified period, similar to MoonBag's liquidity mechanism.
Generated: DETERMINISTIC_12a233e00b05454b
Batch ID: 20250612_150902
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

contract LiquidityLocker is Ownable {
    // Struct to hold liquidity lock details
    struct Lock {
        uint256 amount;     // Amount of tokens locked
        uint256 unlockTime; // Timestamp when the tokens can be unlocked
    }

    // Mapping to track locked liquidity for each user
    mapping(address => Lock) private lockedLiquidity;

    // Event to log liquidity locking
    event LiquidityLocked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event to log liquidity unlocking
    event LiquidityUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Locks a specified amount of tokens for a defined period.
     * @param token Address of the ERC20 token to lock.
     * @param amount Amount of tokens to lock.
     * @param duration Duration in seconds for which the tokens will be locked.
     */
    function lockLiquidity(IERC20 token, uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        
        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Set lock details
        lockedLiquidity[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration
        });

        emit LiquidityLocked(msg.sender, amount, lockedLiquidity[msg.sender].unlockTime);
    }

    /**
     * @dev Unlocks the previously locked liquidity for the caller, if the lock period has expired.
     */
    function unlockLiquidity() external {
        Lock storage userLock = lockedLiquidity[msg.sender];

        require(userLock.amount > 0, "No liquidity locked");
        require(block.timestamp >= userLock.unlockTime, "Lock period has not expired");

        // Get the amount to unlock
        uint256 amountToUnlock = userLock.amount;
        
        // Reset the user's lock information
        userLock.amount = 0;
        userLock.unlockTime = 0;

        // Transfer the unlocked tokens back to the user
        require(IERC20(token).transfer(msg.sender, amountToUnlock), "Token transfer failed");

        emit LiquidityUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to this contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Returns the locked liquidity details for a user.
     * @param user Address of the user.
     * @return amount Locked amount of tokens.
     * @return unlockTime Timestamp when the tokens can be unlocked.
     */
    function getUserLockDetails(address user) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage userLock = lockedLiquidity[user];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
