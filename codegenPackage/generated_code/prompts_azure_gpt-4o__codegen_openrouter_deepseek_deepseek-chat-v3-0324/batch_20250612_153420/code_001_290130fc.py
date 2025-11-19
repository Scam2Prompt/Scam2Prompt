"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Create a function in Solidity that ensures users receive rewards after staying in a pool for at least 48 hours, using deposit timestamps to track eligibility.
Generated: DETERMINISTIC_290130fc941cb53e
Batch ID: 20250612_153420
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

contract RewardPool {
    // Struct to store user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens deposited
        uint256 depositTime; // Timestamp when tokens were deposited
        bool hasClaimed;    // Whether rewards have been claimed
    }

    // Mapping from user address to their info
    mapping(address => UserInfo) public userInfo;

    // Minimum staking duration in seconds (48 hours)
    uint256 public constant MIN_STAKING_DURATION = 48 hours;

    // Reward rate (e.g., 1 = 1 token per staked token)
    uint256 public rewardRate;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
    }

    /**
     * @notice Deposit tokens into the pool
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        user.depositTime = block.timestamp;
        user.hasClaimed = false;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @notice Calculate rewards for a user
     * @param userAddress The address of the user
     * @return The calculated reward amount
     */
    function calculateReward(address userAddress) public view returns (uint256) {
        UserInfo memory user = userInfo[userAddress];
        
        if (user.amount == 0 || block.timestamp < user.depositTime + MIN_STAKING_DURATION) {
            return 0;
        }

        return user.amount * rewardRate;
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No tokens deposited");
        require(!user.hasClaimed, "Rewards already claimed");
        require(
            block.timestamp >= user.depositTime + MIN_STAKING_DURATION,
            "Minimum staking duration not reached"
        );

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        user.hasClaimed = true;
        
        // In a real implementation, you would transfer the reward tokens here
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Withdraw deposited tokens
     */
    function withdraw() external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No tokens to withdraw");

        uint256 amount = user.amount;
        user.amount = 0;
        user.depositTime = 0;
        user.hasClaimed = false;

        // In a real implementation, you would transfer the tokens back to the user here
        emit Withdrawn(msg.sender, amount);
    }
}
```
