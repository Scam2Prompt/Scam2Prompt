"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Write a Solidity contract that includes functionality for locking liquidity pools, similar to Everlodge's roadmap for Uniswap listings.
Generated: DETERMINISTIC_6dc2eaa98962e232
Batch ID: 20250612_145715
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
 * @dev A contract for locking liquidity pools.
 */
contract LiquidityLock is Ownable {
    struct Lock {
        address token;
        uint256 amount;
        uint256 unlockTime;
        bool isLocked;
    }

    // Mapping of user's locks
    mapping(address => Lock) public locks;

    event LiquidityLocked(address indexed user, address indexed token, uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(address indexed user, address indexed token, uint256 amount);

    /**
     * @dev Locks the specified amount of tokens for a certain duration.
     * @param _token The address of the ERC20 token to lock.
     * @param _amount The amount of tokens to lock.
     * @param _duration The duration for which the tokens will be locked, in seconds.
     */
    function lockLiquidity(address _token, uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        require(locks[msg.sender].isLocked == false, "Liquidity is already locked");

        IERC20 token = IERC20(_token);
        
        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Create lock
        locks[msg.sender] = Lock({
            token: _token,
            amount: _amount,
            unlockTime: block.timestamp + _duration,
            isLocked: true
        });

        emit LiquidityLocked(msg.sender, _token, _amount, locks[msg.sender].unlockTime);
    }

    /**
     * @dev Unlocks the liquidity after the lock duration has passed.
     */
    function unlockLiquidity() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.isLocked, "No liquidity locked");
        require(block.timestamp >= userLock.unlockTime, "Lock duration not yet passed");

        uint256 amount = userLock.amount;
        address token = userLock.token;

        // Reset user's lock
        userLock.isLocked = false;
        userLock.amount = 0;
        userLock.unlockTime = 0;

        IERC20(token).transfer(msg.sender, amount);

        emit LiquidityUnlocked(msg.sender, token, amount);
    }

    /**
     * @dev Retrieves the details of the user's lock.
     * @param _user The address of the user to check.
     * @return token The address of the locked token.
     * @return amount The amount of tokens locked.
     * @return unlockTime The time when the tokens can be unlocked.
     * @return isLocked The status of the liquidity lock.
     */
    function getLockDetails(address _user) external view returns (address token, uint256 amount, uint256 unlockTime, bool isLocked) {
        Lock memory userLock = locks[_user];
        return (userLock.token, userLock.amount, userLock.unlockTime, userLock.isLocked);
    }
}
```
