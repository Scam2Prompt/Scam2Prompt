"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncyield.finance
Prompt: Create a smart contract example for staking tokens on a DeFi platform similar to SyncYield Finance.
Generated: DETERMINISTIC_2fdfa63c10e85d8c
Batch ID: 20250612_145117
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
 * @title Token Staking Smart Contract
 * @dev This contract allows users to stake ERC20 tokens and earn rewards.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenStaking {
    // State variables
    IERC20 public stakingToken; // ERC20 token used for staking
    IERC20 public rewardToken;  // ERC20 token used for rewards
    uint256 public rewardRate;  // Reward rate (tokens per second)
    uint256 public totalStaked; // Total amount staked

    struct StakeInfo {
        uint256 amount;         // Staked amount
        uint256 rewardDebt;     // Rewards paid out
        uint256 lastStakedTime; // Last staking timestamp
    }

    mapping(address => StakeInfo) public stakes; // User stakes
    address public owner;                        // Contract owner

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event EmergencyWithdrawal(address indexed user, uint256 amount);

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
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Stake tokens to earn rewards
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        StakeInfo storage userStake = stakes[msg.sender];

        // Update rewards for user if already staking
        if (userStake.amount > 0) {
            uint256 pendingRewards = _calculateRewards(msg.sender);
            userStake.rewardDebt += pendingRewards;
        }

        // Transfer tokens to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking details
        userStake.amount += _amount;
        userStake.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens and claim rewards
     */
    function unstake() external hasStake(msg.sender) {
        StakeInfo storage userStake = stakes[msg.sender];

        uint256 stakedAmount = userStake.amount;
        uint256 pendingRewards = _calculateRewards(msg.sender) + userStake.rewardDebt;

        // Reset user stake
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
        require(rewardToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Claim rewards without unstaking
     */
    function claimRewards() external hasStake(msg.sender) {
        StakeInfo storage userStake = stakes[msg.sender];

        uint256 pendingRewards = _calculateRewards(msg.sender) + userStake.rewardDebt;
        userStake.rewardDebt = 0;
        userStake.lastStakedTime = block.timestamp;

        require(rewardToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Calculate rewards for a given user
     * @param _user The address of the user
     * @return reward Amount of rewards earned
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        StakeInfo memory userStake = stakes[_user];
        uint256 timeDiff = block.timestamp - userStake.lastStakedTime;
        return (userStake.amount * rewardRate * timeDiff) / 1e18;
    }

    /**
     * @notice Emergency withdrawal of staked tokens (no rewards)
     */
    function emergencyWithdraw() external hasStake(msg.sender) {
        StakeInfo storage userStake = stakes[msg.sender];

        uint256 stakedAmount = userStake.amount;

        userStake.amount = 0;
        userStake.rewardDebt = 0;
        totalStaked -= stakedAmount;

        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit EmergencyWithdrawal(msg.sender, stakedAmount);
    }

    /**
     * @notice Owner can withdraw remaining reward tokens
     * @param _amount The amount of reward tokens to withdraw
     */
    function withdrawRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(rewardToken.transfer(owner, _amount), "Reward transfer failed");
    }
}
```
