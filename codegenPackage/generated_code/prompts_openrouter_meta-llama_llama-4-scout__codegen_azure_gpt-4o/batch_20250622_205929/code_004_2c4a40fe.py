"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Write a smart contract in Solidity that enables staking, unstaking, and reward distribution for a token, with features like emergency withdrawal and reward tracking.
Generated: DETERMINISTIC_2c4a40fe13fec1da
Batch ID: 20250622_205929
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
 * @title StakingContract
 * @dev A smart contract for staking tokens, unstaking, and distributing rewards.
 * Includes emergency withdrawal functionality and reward tracking.
 */
contract StakingContract {
    // Token interface
    IERC20 public stakingToken;

    // Struct to track staker information
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already paid out
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Last timestamp when rewards were calculated
    uint256 public lastRewardTimestamp;

    // Accumulated rewards per token
    uint256 public accRewardPerToken;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Updates the reward variables.
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTimestamp = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
        uint256 reward = timeElapsed * rewardRate;
        accRewardPerToken += (reward * 1e18) / totalStaked;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        updateRewards();

        Staker storage staker = stakers[msg.sender];
        if (staker.stakedAmount > 0) {
            uint256 pendingReward = (staker.stakedAmount * accRewardPerToken) / 1e18 - staker.rewardDebt;
            if (pendingReward > 0) {
                stakingToken.transfer(msg.sender, pendingReward);
                emit RewardClaimed(msg.sender, pendingReward);
            }
        }

        stakingToken.transferFrom(msg.sender, address(this), amount);
        staker.stakedAmount += amount;
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / 1e18;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");

        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        updateRewards();

        uint256 pendingReward = (staker.stakedAmount * accRewardPerToken) / 1e18 - staker.rewardDebt;
        if (pendingReward > 0) {
            stakingToken.transfer(msg.sender, pendingReward);
            emit RewardClaimed(msg.sender, pendingReward);
        }

        staker.stakedAmount -= amount;
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / 1e18;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw all staked tokens in case of emergency.
     */
    function emergencyWithdraw() external {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.stakedAmount;
        require(amount > 0, "No tokens to withdraw");

        staker.stakedAmount = 0;
        staker.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.transfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate The new reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        updateRewards();
        rewardRate = _rewardRate;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
