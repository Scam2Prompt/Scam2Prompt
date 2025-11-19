"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullperks.pages.dev
Prompt: Explain how to implement a staking mechanism for BLP tokens within the BullPerks ecosystem, including sample code.
Generated: DETERMINISTIC_0dac82a02aaf1a81
Batch ID: 20250612_161035
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
 * @title BLP Staking Contract
 * @dev This contract allows users to stake BLP tokens within the BullPerks ecosystem
 * and earn rewards over time. It includes functionality for staking, withdrawing, 
 * and calculating rewards.
 */
contract BLPStaking {
    // ERC20 interface for the BLP token
    IERC20 public immutable blpToken;

    // Mapping to track user stakes and reward balances
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardBalances;

    // Mapping to track last staked timestamps for reward calculation
    mapping(address => uint256) public lastStakedTimestamps;

    // Annual reward rate (e.g., 10% represented as 0.1 * 10**18)
    uint256 public immutable annualRewardRate;

    // Events for logging staking, withdrawing, and reward claims
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _blpToken Address of the BLP token contract.
     * @param _annualRewardRate Annual reward rate in wei format (e.g., 0.1 * 10**18 for 10%).
     */
    constructor(IERC20 _blpToken, uint256 _annualRewardRate) {
        require(address(_blpToken) != address(0), "Invalid BLP token address");
        require(_annualRewardRate > 0, "Annual reward rate must be greater than zero");
        
        blpToken = _blpToken;
        annualRewardRate = _annualRewardRate;
    }

    /**
     * @dev Allows users to stake BLP tokens into the contract.
     * @param amount Amount of BLP tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Calculate pending rewards and update user balances
        _updateRewards(msg.sender);

        // Transfer BLP tokens from the user to the contract
        require(blpToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        lastStakedTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked BLP tokens.
     * @param amount Amount of BLP tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate pending rewards and update user balances
        _updateRewards(msg.sender);

        // Deduct the withdrawn amount from the user's staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer BLP tokens back to the user
        require(blpToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their reward tokens.
     */
    function claimRewards() external {
        // Calculate pending rewards and update user balances
        _updateRewards(msg.sender);

        uint256 rewardAmount = rewardBalances[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset reward balance for the user
        rewardBalances[msg.sender] = 0;

        // Transfer reward tokens to the user
        // NOTE: The contract must have sufficient reward tokens to distribute
        require(blpToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        uint256 stakedAmount = stakedBalances[user];
        uint256 lastTimestamp = lastStakedTimestamps[user];

        if (stakedAmount > 0 && lastTimestamp > 0) {
            // Calculate the time difference in seconds
            uint256 timeElapsed = block.timestamp - lastTimestamp;

            // Calculate rewards based on the annual reward rate
            uint256 rewards = (stakedAmount * annualRewardRate * timeElapsed) / (365 days * 10**18);

            // Update reward balance for the user
            rewardBalances[user] += rewards;
        }

        // Update the user's last staked timestamp
        lastStakedTimestamps[user] = block.timestamp;
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user Address of the user to query.
     * @return Pending rewards in wei format.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        uint256 lastTimestamp = lastStakedTimestamps[user];

        if (stakedAmount > 0 && lastTimestamp > 0) {
            uint256 timeElapsed = block.timestamp - lastTimestamp;
            uint256 rewards = (stakedAmount * annualRewardRate * timeElapsed) / (365 days * 10**18);
            return rewardBalances[user] + rewards;
        }

        return rewardBalances[user];
    }
}

/**
 * @dev Minimal ERC20 interface to interact with the BLP token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
