"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimanyinu.pages.dev
Prompt: Generate Solidity code for a smart contract that supports locking $AI tokens for a specified duration, with multipliers based on lock duration as described in the Diamond Hands app.
Generated: DETERMINISTIC_0bf986d9d0a24e80
Batch ID: 20250612_152710
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
 * @title DiamondHands
 * @dev Smart contract for locking $AI tokens with duration-based multipliers.
 * Users can lock their tokens for a specified duration and earn rewards based on the duration multiplier.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DiamondHands {
    // Address of the $AI token contract
    IERC20 public immutable aiToken;

    // Struct to hold information about a user's lock
    struct Lock {
        uint256 amount;         // Amount of tokens locked
        uint256 unlockTime;     // Timestamp when tokens can be unlocked
        uint256 multiplier;     // Multiplier based on lock duration
        bool claimed;           // Whether the reward has been claimed
    }

    // Mapping of user address to their lock information
    mapping(address => Lock) public locks;

    // Multiplier values based on lock duration (in seconds)
    uint256 constant MULTIPLIER_1_MONTH = 110;  // 10% bonus for 1 month
    uint256 constant MULTIPLIER_3_MONTHS = 125; // 25% bonus for 3 months
    uint256 constant MULTIPLIER_6_MONTHS = 150; // 50% bonus for 6 months

    event Locked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event Claimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the $AI token contract address.
     * @param _aiToken Address of the $AI token contract.
     */
    constructor(IERC20 _aiToken) {
        require(address(_aiToken) != address(0), "Invalid token address");
        aiToken = _aiToken;
    }

    /**
     * @dev Allows a user to lock their $AI tokens for a specified duration.
     * @param amount The amount of tokens to lock.
     * @param duration The lock duration in seconds (e.g., 30 days, 90 days, 180 days).
     */
    function lock(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration == 30 days || duration == 90 days || duration == 180 days, "Invalid lock duration");
        require(locks[msg.sender].amount == 0, "Existing lock found");

        uint256 multiplier = getMultiplier(duration);
        require(multiplier > 0, "Invalid multiplier");

        uint256 unlockTime = block.timestamp + duration;

        // Update user's lock information
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: unlockTime,
            multiplier: multiplier,
            claimed: false
        });

        // Transfer tokens from the user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Locked(msg.sender, amount, unlockTime, multiplier);
    }

    /**
     * @dev Allows a user to claim their tokens and reward after the lock duration has passed.
     */
    function claim() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No active lock found");
        require(block.timestamp >= userLock.unlockTime, "Lock period not yet completed");
        require(!userLock.claimed, "Reward already claimed");

        userLock.claimed = true;

        // Calculate reward based on multiplier
        uint256 reward = (userLock.amount * userLock.multiplier) / 100;

        // Transfer tokens and reward back to the user
        require(aiToken.transfer(msg.sender, reward), "Token transfer failed");

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Fetch the multiplier based on lock duration.
     * @param duration Lock duration in seconds.
     * @return Multiplier value.
     */
    function getMultiplier(uint256 duration) public pure returns (uint256) {
        if (duration == 30 days) {
            return MULTIPLIER_1_MONTH;
        } else if (duration == 90 days) {
            return MULTIPLIER_3_MONTHS;
        } else if (duration == 180 days) {
            return MULTIPLIER_6_MONTHS;
        }
        return 0;
    }
}
```
