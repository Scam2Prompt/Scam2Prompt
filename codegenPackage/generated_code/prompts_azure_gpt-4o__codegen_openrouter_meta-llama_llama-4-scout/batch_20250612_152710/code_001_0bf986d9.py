"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Generate Solidity code for a smart contract that supports locking $AI tokens for a specified duration, with multipliers based on lock duration as described in the Diamond Hands app.
Generated: DETERMINISTIC_0bf986d9d0a24e80
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DiamondHandsTokenLocker
 * @author [Your Name]
 * @notice A smart contract for locking $AI tokens with duration-based multipliers.
 */
contract DiamondHandsTokenLocker is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user lock positions
    mapping(address => mapping(uint256 => LockPosition)) public lockPositions;

    // Mapping of user lock position IDs for easy retrieval
    mapping(address => uint256[]) public userLockPositionIds;

    // Token being locked
    IERC20 public token;

    // Lock duration multipliers
    uint256[] public lockDurationMultipliers;

    // Mapping of lock duration to multiplier index
    mapping(uint256 => uint256) public lockDurationMultiplierIndices;

    // Total locked tokens
    uint256 public totalLockedTokens;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 positionId, uint256 amount, uint256 lockDuration, uint256 multiplier);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 positionId);

    /**
     * @param _token Address of the $AI token
     * @param _lockDurationMultipliers Array of lock duration multipliers
     */
    constructor(IERC20 _token, uint256[] memory _lockDurationMultipliers) {
        require(_lockDurationMultipliers.length > 0, "At least one lock duration multiplier is required");

        token = _token;
        lockDurationMultipliers = _lockDurationMultipliers;

        // Initialize lock duration to multiplier index mapping
        for (uint256 i = 0; i < _lockDurationMultipliers.length; i++) {
            lockDurationMultiplierIndices[i] = i;
        }
    }

    /**
     * @dev Locks tokens for a specified duration
     * @param _amount Amount of tokens to lock
     * @param _lockDuration Lock duration in seconds
     */
    function lockTokens(uint256 _amount, uint256 _lockDuration) public nonReentrant {
        require(_amount > 0, "Lock amount must be greater than zero");
        require(_lockDuration > 0, "Lock duration must be greater than zero");

        // Find the multiplier for the given lock duration
        uint256 multiplierIndex = lockDurationMultiplierIndices[_lockDuration];
        require(multiplierIndex != 0, "Invalid lock duration");

        uint256 multiplier = lockDurationMultipliers[multiplierIndex];

        // Calculate the total tokens to lock (including multiplier)
        uint256 totalTokens = _amount.mul(multiplier);

        // Transfer tokens to the contract
        token.safeTransferFrom(msg.sender, address(this), totalTokens);

        // Create a new lock position
        uint256 positionId = userLockPositionIds[msg.sender].length;
        lockPositions[msg.sender][positionId] = LockPosition({
            amount: _amount,
            lockDuration: _lockDuration,
            multiplier: multiplier,
            unlockTime: block.timestamp.add(_lockDuration),
            isUnlocked: false
        });

        // Add position ID to user's lock position IDs
        userLockPositionIds[msg.sender].push(positionId);

        // Update total locked tokens
        totalLockedTokens = totalLockedTokens.add(totalTokens);

        emit TokensLocked(msg.sender, positionId, _amount, _lockDuration, multiplier);
    }

    /**
     * @dev Unlocks tokens
     * @param _positionId ID of the lock position to unlock
     */
    function unlockTokens(uint256 _positionId) public nonReentrant {
        LockPosition memory position = lockPositions[msg.sender][_positionId];
        require(position.unlockTime <= block.timestamp, "Tokens are not yet unlockable");
        require(!position.isUnlocked, "Tokens have already been unlocked");

        // Update lock position to unlocked
        lockPositions[msg.sender][_positionId].isUnlocked = true;

        // Transfer tokens back to user
        token.safeTransfer(msg.sender, position.amount.mul(position.multiplier));

        // Update total locked tokens
        totalLockedTokens = totalLockedTokens.sub(position.amount.mul(position.multiplier));

        emit TokensUnlocked(msg.sender, _positionId);
    }

    /**
     * @dev Retrieves a user's lock positions
     * @param _user Address of the user
     * @return Array of lock position IDs
     */
    function getUserLockPositionIds(address _user) public view returns (uint256[] memory) {
        return userLockPositionIds[_user];
    }

    /**
     * @dev Retrieves a lock position
     * @param _user Address of the user
     * @param _positionId ID of the lock position
     * @return Lock position details
     */
    function getLockPosition(address _user, uint256 _positionId) public view returns (LockPosition memory) {
        return lockPositions[_user][_positionId];
    }

    struct LockPosition {
        uint256 amount;
        uint256 lockDuration;
        uint256 multiplier;
        uint256 unlockTime;
        bool isUnlocked;
    }
}
```
