"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Design a staking system that allows users to withdraw their staked tokens and claimable rewards, taking into account the 3-year reward period and dynamic rewards rate.
Generated: DETERMINISTIC_2ba64425a6b74fb0
Batch ID: 20250622_210216
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

contract StakingSystem {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Duration for rewards (3 years in seconds)
    uint256 public constant REWARD_DURATION = 3 * 365 days;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        if (stakedDuration > REWARD_DURATION) {
            stakedDuration = REWARD_DURATION; // Cap the duration to the reward period
        }

        return (userStake.amount * rewardRate * stakedDuration) / 1e18; // Adjust for reward rate precision
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens to withdraw");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        userStake.rewards += rewards; // Update user's rewards

        // Reset user's stake
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Update total staked amount
        totalStaked -= amountToWithdraw;

        // Transfer staked tokens and rewards to the user
        // Assuming the contract has a function to transfer tokens
        _transferTokens(msg.sender, amountToWithdraw + userStake.rewards);

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amountToWithdraw);
        emit RewardsClaimed(msg.sender, userStake.rewards);
    }

    // Internal function to handle token transfers (placeholder)
    function _transferTokens(address to, uint256 amount) internal {
        // Implement token transfer logic here
        // This could involve calling an ERC20 token contract's transfer function
    }

    // Function to get user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get user's claimable rewards
    function getClaimableRewards(address user) external view returns (uint256) {
        return calculateRewards(user) + stakes[user].rewards;
    }
}
```
