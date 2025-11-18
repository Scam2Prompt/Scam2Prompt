"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-neurolance.web.app
Prompt: Develop a smart contract that integrates with the Neurolance Portal's staking dApp to enable staking of NEROX tokens and calculate rewards.
Generated: DETERMINISTIC_88a847e37d53b421
Batch ID: 20250612_150446
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
 * @title Neurolance Staking Contract
 * @dev This contract allows users to stake NEROX tokens, earn rewards, and interact with the Neurolance Portal's dApp.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract NeurolanceStaking {
    IERC20 public neroxToken;
    address public owner;
    uint256 public rewardRate; // Rewards per block (e.g., 10 tokens per block)
    uint256 public totalStaked;
    uint256 public constant REWARD_PRECISION = 1e18;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier updateRewards(address staker) {
        if (stakes[staker].amount > 0) {
            uint256 pendingReward = calculatePendingRewards(staker);
            stakes[staker].rewardDebt += pendingReward;
        }
        _;
    }

    constructor(address _neroxToken, uint256 _rewardRate) {
        require(_neroxToken != address(0), "Invalid token address");
        neroxToken = IERC20(_neroxToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Allows a user to stake NEROX tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Stake amount must be greater than zero");
        require(neroxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to unstake all their NEROX tokens and claim rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        uint256 userStakedAmount = stakes[msg.sender].amount;
        require(userStakedAmount > 0, "No tokens to unstake");

        uint256 reward = stakes[msg.sender].rewardDebt;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= userStakedAmount;

        // Transfer staked tokens back to the user
        require(neroxToken.transfer(msg.sender, userStakedAmount), "Token transfer failed");

        // Transfer rewards to the user
        if (reward > 0) {
            require(neroxToken.balanceOf(address(this)) >= reward, "Insufficient contract balance for rewards");
            require(neroxToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, userStakedAmount);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Allows stakers to claim only their pending rewards without unstaking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0;

        require(neroxToken.balanceOf(address(this)) >= reward, "Insufficient contract balance for rewards");
        require(neroxToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Allows the owner to update the reward rate.
     * @param newRate The new reward rate.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Calculates the pending rewards for a specific staker.
     * @param staker The address of the staker.
     * @return pendingRewards The pending rewards amount.
     */
    function calculatePendingRewards(address staker) public view returns (uint256 pendingRewards) {
        Stake storage userStake = stakes[staker];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.lastStakeTime;
            pendingRewards = (userStake.amount * rewardRate * stakingDuration) / REWARD_PRECISION;
        }
    }
}
```
