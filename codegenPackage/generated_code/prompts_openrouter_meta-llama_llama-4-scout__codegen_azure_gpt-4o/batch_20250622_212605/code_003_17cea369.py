"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Generate a smart contract code snippet in Solidity for a custom staking pool on Story Staking, incorporating dynamic interest rates and automated reward distribution.
Generated: DETERMINISTIC_17cea369ad8f97c4
Batch ID: 20250622_212605
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

/**
 * @title StoryStakingPool
 * @dev A custom staking pool with dynamic interest rates and automated reward distribution.
 */
contract StoryStakingPool {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount staked in the pool
    uint256 public rewardRate; // Dynamic reward rate (percentage per year)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60; // Seconds in a year

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor
    constructor(uint256 _initialRewardRate) {
        owner = msg.sender;
        rewardRate = _initialRewardRate;
    }

    /**
     * @dev Allows users to stake tokens in the pool.
     * @param _amount The amount to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match stake amount");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Calculate and update pending rewards before adding new stake
            rewards[msg.sender] += calculateReward(msg.sender);
        }
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        // Calculate and update pending rewards
        rewards[msg.sender] += calculateReward(msg.sender);

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked amount back to user
        payable(msg.sender).transfer(stakedAmount);

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset user's rewards
        rewards[msg.sender] = 0;

        // Transfer reward to user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their stake and time staked.
     * @param _user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 annualReward = (userStake.amount * rewardRate) / 100;
        return (annualReward * stakingDuration) / SECONDS_IN_YEAR;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate The new reward rate (percentage per year).
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
