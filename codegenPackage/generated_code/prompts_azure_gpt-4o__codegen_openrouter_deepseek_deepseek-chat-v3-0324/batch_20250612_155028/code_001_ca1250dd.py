"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Generate code in Solidity to implement a vote escrow model (ve) similar to Shadow Exchange, where users lock assets to gain non-transferable voting rights.
Generated: DETERMINISTIC_ca1250dd85d31af8
Batch ID: 20250612_155028
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Vote Escrow Contract
 * @notice Allows users to lock tokens to gain non-transferable voting power
 * @dev Voting power decays linearly over time based on lock duration
 */
contract VoteEscrow is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user lock information
    struct LockedBalance {
        uint256 amount;
        uint256 end;
    }

    // Token to be locked
    IERC20 public immutable token;

    // Minimum lock duration (in seconds)
    uint256 public immutable minLockDuration;

    // Maximum lock duration (in seconds)
    uint256 public immutable maxLockDuration;

    // Mapping of user address to their lock
    mapping(address => LockedBalance) public locked;

    // Total locked supply
    uint256 public totalLocked;

    // Events
    event LockCreated(address indexed user, uint256 amount, uint256 unlockTime);
    event LockIncreased(address indexed user, uint256 amount);
    event LockDurationIncreased(address indexed user, uint256 newUnlockTime);
    event LockWithdrawn(address indexed user, uint256 amount);

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
            "Invalid lock durations"
        );

        token = IERC20(_token);
        minLockDuration = _minLockDuration;
        maxLockDuration = _maxLockDuration;
    }

    /**
     * @notice Create a new lock or add to existing lock
     * @param _amount Amount of tokens to lock
     * @param _duration Duration to lock tokens for (in seconds)
     */
    function createLock(uint256 _amount, uint256 _duration) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _duration >= minLockDuration && _duration <= maxLockDuration,
            "Invalid lock duration"
        );

        LockedBalance memory userLock = locked[msg.sender];
        uint256 unlockTime = block.timestamp + _duration;

        if (userLock.amount == 0) {
            // Create new lock
            locked[msg.sender] = LockedBalance(_amount, unlockTime);
            totalLocked += _amount;
            emit LockCreated(msg.sender, _amount, unlockTime);
        } else {
            // Add to existing lock
            require(
                unlockTime > userLock.end,
                "New duration must be longer than existing lock"
            );
            locked[msg.sender] = LockedBalance(userLock.amount + _amount, unlockTime);
            totalLocked += _amount;
            emit LockIncreased(msg.sender, _amount);
            emit LockDurationIncreased(msg.sender, unlockTime);
        }

        token.safeTransferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Increase lock duration without adding more tokens
     * @param _duration New duration to extend lock to (in seconds)
     */
    function increaseLockDuration(uint256 _duration) external nonReentrant {
        LockedBalance memory userLock = locked[msg.sender];
        require(userLock.amount > 0, "No existing lock");
        require(
            _duration >= minLockDuration && _duration <= maxLockDuration,
            "Invalid lock duration"
        );

        uint256 unlockTime = block.timestamp + _duration;
        require(unlockTime > userLock.end, "New duration must be longer");

        locked[msg.sender].end = unlockTime;
        emit LockDurationIncreased(msg.sender, unlockTime);
    }

    /**
     * @notice Withdraw tokens after lock expires
     */
    function withdraw() external nonReentrant {
        LockedBalance memory userLock = locked[msg.sender];
        require(userLock.amount > 0, "No locked balance");
        require(block.timestamp >= userLock.end, "Lock not expired");

        uint256 amount = userLock.amount;
        delete locked[msg.sender];
        totalLocked -= amount;

        token.safeTransfer(msg.sender, amount);
        emit LockWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Get voting power for a user at current block
     * @param _user Address of the user
     * @return Voting power
     */
    function getVotingPower(address _user) external view returns (uint256) {
        LockedBalance memory userLock = locked[_user];
        if (userLock.amount == 0 || block.timestamp >= userLock.end) {
            return 0;
        }

        // Voting power decays linearly over time
        uint256 timeLeft = userLock.end - block.timestamp;
        uint256 maxDuration = maxLockDuration;
        if (timeLeft > maxDuration) {
            timeLeft = maxDuration;
        }

        return (userLock.amount * timeLeft) / maxDuration;
    }

    /**
     * @notice Get voting power for a user at a specific timestamp
     * @param _user Address of the user
     * @param _timestamp Timestamp to check voting power at
     * @return Voting power
     */
    function getVotingPowerAt(
        address _user,
        uint256 _timestamp
    ) external view returns (uint256) {
        LockedBalance memory userLock = locked[_user];
        if (userLock.amount == 0 || _timestamp >= userLock.end) {
            return 0;
        }

        // Voting power decays linearly over time
        uint256 timeLeft = userLock.end - _timestamp;
        uint256 maxDuration = maxLockDuration;
        if (timeLeft > maxDuration) {
            timeLeft = maxDuration;
        }

        return (userLock.amount * timeLeft) / maxDuration;
    }
}
```
