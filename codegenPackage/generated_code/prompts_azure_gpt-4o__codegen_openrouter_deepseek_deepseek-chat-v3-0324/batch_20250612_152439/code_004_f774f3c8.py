"""
Generated Code Metadata:
========================
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a smart contract in Solidity to implement a leaderboard system for tracking $AI holders' lock durations and reward multipliers in the Diamond Hands app.
Generated: DETERMINISTIC_f774f3c88f9d1062
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DiamondHandsLeaderboard is Ownable {
    // Struct to store user lock information
    struct LockInfo {
        uint256 amount;
        uint256 lockDuration;
        uint256 lockStartTime;
        uint256 rewardMultiplier;
        bool isLocked;
    }

    // Constants
    uint256 public constant MIN_LOCK_DURATION = 30 days;
    uint256 public constant MAX_LOCK_DURATION = 365 days;
    uint256 public constant BASE_MULTIPLIER = 1e18; // 1x

    // Token contract
    IERC20 public immutable aiToken;

    // Mapping from user address to their lock info
    mapping(address => LockInfo) public userLocks;

    // Leaderboard entries
    address[] public leaderboard;
    mapping(address => uint256) public leaderboardIndices;

    // Events
    event LockCreated(
        address indexed user,
        uint256 amount,
        uint256 lockDuration,
        uint256 rewardMultiplier
    );
    event LockExtended(
        address indexed user,
        uint256 newLockDuration,
        uint256 newRewardMultiplier
    );
    event LockWithdrawn(address indexed user, uint256 amount);
    event LeaderboardUpdated(address indexed user);

    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    /**
     * @dev Locks AI tokens for a specified duration
     * @param amount Amount of tokens to lock
     * @param lockDuration Duration to lock tokens (in seconds)
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            lockDuration >= MIN_LOCK_DURATION &&
                lockDuration <= MAX_LOCK_DURATION,
            "Invalid lock duration"
        );

        LockInfo storage userLock = userLocks[msg.sender];
        require(!userLock.isLocked, "Tokens already locked");

        // Calculate reward multiplier based on lock duration
        uint256 multiplier = calculateMultiplier(lockDuration);

        // Transfer tokens from user to contract
        bool success = aiToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user lock info
        userLock.amount = amount;
        userLock.lockDuration = lockDuration;
        userLock.lockStartTime = block.timestamp;
        userLock.rewardMultiplier = multiplier;
        userLock.isLocked = true;

        // Add to leaderboard if not already present
        if (leaderboardIndices[msg.sender] == 0) {
            leaderboard.push(msg.sender);
            leaderboardIndices[msg.sender] = leaderboard.length;
        }

        emit LockCreated(msg.sender, amount, lockDuration, multiplier);
        emit LeaderboardUpdated(msg.sender);
    }

    /**
     * @dev Extends the lock duration for already locked tokens
     * @param additionalDuration Additional duration to extend (in seconds)
     */
    function extendLock(uint256 additionalDuration) external {
        LockInfo storage userLock = userLocks[msg.sender];
        require(userLock.isLocked, "No tokens locked");
        require(
            additionalDuration > 0,
            "Additional duration must be greater than 0"
        );

        uint256 newLockDuration = userLock.lockDuration + additionalDuration;
        require(
            newLockDuration <= MAX_LOCK_DURATION,
            "Total lock duration exceeds maximum"
        );

        // Calculate new reward multiplier
        uint256 newMultiplier = calculateMultiplier(newLockDuration);

        // Update lock info
        userLock.lockDuration = newLockDuration;
        userLock.rewardMultiplier = newMultiplier;

        emit LockExtended(msg.sender, newLockDuration, newMultiplier);
        emit LeaderboardUpdated(msg.sender);
    }

    /**
     * @dev Withdraws locked tokens after lock duration has passed
     */
    function withdraw() external {
        LockInfo storage userLock = userLocks[msg.sender];
        require(userLock.isLocked, "No tokens locked");
        require(
            block.timestamp >= userLock.lockStartTime + userLock.lockDuration,
            "Lock duration not expired"
        );

        uint256 amount = userLock.amount;
        userLock.amount = 0;
        userLock.isLocked = false;

        // Transfer tokens back to user
        bool success = aiToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit LockWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculates reward multiplier based on lock duration
     * @param duration Lock duration in seconds
     * @return multiplier Calculated reward multiplier
     */
    function calculateMultiplier(uint256 duration) public pure returns (uint256) {
        // Linear scaling from 1x (30 days) to 5x (365 days)
        uint256 minDays = MIN_LOCK_DURATION / 1 days;
        uint256 maxDays = MAX_LOCK_DURATION / 1 days;
        uint256 lockDays = duration / 1 days;

        if (lockDays <= minDays) return BASE_MULTIPLIER;
        if (lockDays >= maxDays) return BASE_MULTIPLIER * 5;

        uint256 multiplier = BASE_MULTIPLIER +
            ((lockDays - minDays) * (BASE_MULTIPLIER * 4)) /
            (maxDays - minDays);

        return multiplier;
    }

    /**
     * @dev Returns the current leaderboard (top N holders by lock duration)
     * @param count Number of top holders to return
     * @return topHolders Array of top holder addresses
     */
    function getLeaderboard(uint256 count)
        external
        view
        returns (address[] memory topHolders)
    {
        require(count > 0, "Count must be greater than 0");
        uint256 leaderboardLength = leaderboard.length;
        count = count > leaderboardLength ? leaderboardLength : count;

        topHolders = new address[](count);
        for (uint256 i = 0; i < count; i++) {
            topHolders[i] = leaderboard[i];
        }
        return topHolders;
    }

    /**
     * @dev Returns lock information for multiple users
     * @param users Array of user addresses to query
     * @return lockInfos Array of LockInfo structs
     */
    function getBatchLockInfo(address[] calldata users)
        external
        view
        returns (LockInfo[] memory lockInfos)
    {
        lockInfos = new LockInfo[](users.length);
        for (uint256 i = 0; i < users.length; i++) {
            lockInfos[i] = userLocks[users[i]];
        }
        return lockInfos;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(aiToken),
            "Cannot recover the AI token"
        );
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
