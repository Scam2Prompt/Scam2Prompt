"""
Generated Code Metadata:
========================
Original URL: https://bake-4kd.pages.dev
Prompt: Design a smart contract for a staking service that ensures transparency, security, and flexibility, similar to Bake's staking service, and explain how to verify staking activities and reward payouts.
Generated: DETERMINISTIC_91d47244aaff4ec5
Batch ID: 20250622_204837
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
 * @title StakingService
 * @dev A smart contract for staking tokens, ensuring transparency, security, and flexibility.
 */
contract StakingService {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second (e.g., 0.01 tokens per second)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardEarned; // Accumulated reward
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match stake amount");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Calculate and update pending rewards
            userStake.rewardEarned += calculateReward(msg.sender);
        }
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Calculate total reward
        uint256 reward = calculateReward(msg.sender) + userStake.rewardEarned;

        // Transfer staked amount and reward to user
        uint256 amountToTransfer = userStake.amount + reward;
        userStake.amount = 0;
        userStake.rewardEarned = 0;
        totalStaked -= userStake.amount;

        (bool success, ) = msg.sender.call{value: amountToTransfer}("");
        require(success, "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Calculates the reward for a given user based on their stake and staking duration.
     * @param _user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return stakingDuration * rewardRate * userStake.amount / 1 ether;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
