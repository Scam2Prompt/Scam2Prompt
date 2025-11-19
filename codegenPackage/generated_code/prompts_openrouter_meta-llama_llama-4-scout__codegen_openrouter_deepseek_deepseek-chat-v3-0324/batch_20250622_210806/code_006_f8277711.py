"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Develop a community-driven liquidity locking mechanism for a cryptocurrency token, similar to Rich Pepe's approach, and provide a high-level overview of the process.
Generated: DETERMINISTIC_f82777115182fd9b
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CommunityLiquidityLocker
 * @dev A contract that allows community members to lock liquidity tokens for a specified duration
 */
contract CommunityLiquidityLocker is Ownable, ReentrancyGuard {
    struct Lock {
        address owner;
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    IERC20 public token;
    uint256 public minLockDuration;
    uint256 public maxLockDuration;
    uint256 public totalLocked;

    Lock[] public locks;
    mapping(address => uint256[]) public userLocks;

    event LockCreated(
        uint256 lockId,
        address owner,
        uint256 amount,
        uint256 unlockTime
    );
    event LockWithdrawn(uint256 lockId, address owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _token Address of the token to be locked
     * @param _minLockDuration Minimum lock duration in seconds
     * @param _maxLockDuration Maximum lock duration in seconds
     */
    constructor(
        address _token,
        uint256 _minLockDuration,
        uint256 _maxLockDuration
    ) {
        require(_token != address(0), "Invalid token address");
        require(
            _minLockDuration > 0 && _maxLockDuration > _minLockDuration,
            "Invalid duration"
        );

        token = IERC20(_token);
        minLockDuration = _minLockDuration;
        maxLockDuration = _maxLockDuration;
    }

    /**
     * @dev Create a new lock
     * @param amount Amount of tokens to lock
     * @param duration Duration to lock tokens for (in seconds)
     */
    function createLock(uint256 amount, uint256 duration)
        external
        nonReentrant
    {
        require(amount > 0, "Amount must be greater than 0");
        require(
            duration >= minLockDuration && duration <= maxLockDuration,
            "Invalid lock duration"
        );

        uint256 unlockTime = block.timestamp + duration;
        locks.push(
            Lock({
                owner: msg.sender,
                amount: amount,
                unlockTime: unlockTime,
                withdrawn: false
            })
        );

        uint256 lockId = locks.length - 1;
        userLocks[msg.sender].push(lockId);
        totalLocked += amount;

        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit LockCreated(lockId, msg.sender, amount, unlockTime);
    }

    /**
     * @dev Withdraw tokens from a lock after unlock time has passed
     * @param lockId ID of the lock to withdraw from
     */
    function withdraw(uint256 lockId) external nonReentrant {
        require(lockId < locks.length, "Invalid lock ID");

        Lock storage lock = locks[lockId];
        require(lock.owner == msg.sender, "Not lock owner");
        require(!lock.withdrawn, "Already withdrawn");
        require(block.timestamp >= lock.unlockTime, "Lock not expired");

        lock.withdrawn = true;
        totalLocked -= lock.amount;

        require(token.transfer(msg.sender, lock.amount), "Transfer failed");

        emit LockWithdrawn(lockId, msg.sender, lock.amount);
    }

    /**
     * @dev Get all lock IDs for a user
     * @param user Address of the user
     * @return Array of lock IDs
     */
    function getUserLockIds(address user)
        external
        view
        returns (uint256[] memory)
    {
        return userLocks[user];
    }

    /**
     * @dev Get lock details by ID
     * @param lockId ID of the lock
     * @return Lock details
     */
    function getLockDetails(uint256 lockId)
        external
        view
        returns (
            address,
            uint256,
            uint256,
            bool
        )
    {
        require(lockId < locks.length, "Invalid lock ID");
        Lock memory lock = locks[lockId];
        return (lock.owner, lock.amount, lock.unlockTime, lock.withdrawn);
    }

    /**
     * @dev Update lock duration limits (owner only)
     * @param newMin New minimum duration
     * @param newMax New maximum duration
     */
    function updateLockDurations(uint256 newMin, uint256 newMax)
        external
        onlyOwner
    {
        require(newMin > 0 && newMax > newMin, "Invalid durations");
        minLockDuration = newMin;
        maxLockDuration = newMax;
    }
}
```
