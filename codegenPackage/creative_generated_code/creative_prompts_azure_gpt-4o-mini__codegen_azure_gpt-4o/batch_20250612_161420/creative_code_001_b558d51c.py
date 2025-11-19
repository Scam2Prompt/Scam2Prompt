"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateways.pages.dev
Prompt: Generate a Solidity smart contract that implements the Diamond Hands app features for locking $AI tokens and managing loyalty rewards.
Generated: DETERMINISTIC_b558d51c718186dd
Batch ID: 20250612_161420
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

/**
 * @title Diamond Hands Contract for $AI Token
 * @notice This contract allows users to lock $AI tokens and earn loyalty rewards based on the lock duration.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DiamondHands {
    // Struct representing a lock entry
    struct Lock {
        uint256 amount; // Amount of $AI tokens locked
        uint256 lockTimestamp; // Timestamp when tokens were locked
        uint256 unlockTimestamp; // Timestamp when tokens can be unlocked
        bool claimed; // Whether the loyalty reward was claimed
    }

    // Mapping of user addresses to their lock details
    mapping(address => Lock) public locks;

    // Token contract (immutable after deployment)
    IERC20 public immutable aiToken;

    // Loyalty reward percentage (e.g., 5%)
    uint256 public constant REWARD_PERCENTAGE = 5;

    // Minimum lock duration required to earn rewards (e.g., 30 days)
    uint256 public constant MIN_LOCK_DURATION = 30 days;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTimestamp);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @notice Constructor to initialize the $AI token contract address.
     * @param _aiTokenAddress Address of the $AI token contract.
     */
    constructor(address _aiTokenAddress) {
        require(_aiTokenAddress != address(0), "Invalid token address");
        aiToken = IERC20(_aiTokenAddress);
    }

    /**
     * @notice Allows a user to lock $AI tokens for a specific duration.
     * @param amount Amount of $AI tokens to lock.
     * @param lockDuration Duration for which tokens will be locked (in seconds).
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration >= MIN_LOCK_DURATION, "Lock duration must meet minimum requirements");
        require(locks[msg.sender].amount == 0, "Existing lock must be cleared before creating a new one");

        // Transfer the tokens to this contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Set lock details
        locks[msg.sender] = Lock({
            amount: amount,
            lockTimestamp: block.timestamp,
            unlockTimestamp: block.timestamp + lockDuration,
            claimed: false
        });

        emit TokensLocked(msg.sender, amount, block.timestamp + lockDuration);
    }

    /**
     * @notice Allows a user to unlock their tokens and claim rewards if eligible.
     */
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTimestamp, "Tokens are still locked");
        require(!userLock.claimed, "Rewards already claimed");

        uint256 reward = 0;

        // Calculate reward if lock duration was greater than or equal to the minimum
        if (userLock.unlockTimestamp - userLock.lockTimestamp >= MIN_LOCK_DURATION) {
            reward = (userLock.amount * REWARD_PERCENTAGE) / 100;
        }

        // Mark as claimed and reset lock
        userLock.claimed = true;
        uint256 totalAmount = userLock.amount + reward;
        delete locks[msg.sender];

        // Transfer tokens back to the user along with reward (if applicable)
        require(aiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, userLock.amount, reward);
    }

    /**
     * @notice Allows a user to check their lock details.
     * @return Lock details for the caller's address.
     */
    function getLockDetails() external view returns (Lock memory) {
        return locks[msg.sender];
    }
}
```
