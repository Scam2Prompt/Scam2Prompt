"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum that distributes rewards proportionally to stakers over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_0b524440a48d9a87
Batch ID: 20250612_153400
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

interface IDOGE20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingDoge20 {
    IDOGE20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardRate; // Reward rate for staking
    uint256 public stakingEndTime; // Staking period end time
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewardDebt; // Reward debt for each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _doge20Token, uint256 _rewardRate, uint256 durationInDays) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        doge20Token = IDOGE20(_doge20Token);
        rewardRate = _rewardRate;
        stakingEndTime = block.timestamp + (durationInDays * 1 days);
    }

    modifier onlyDuringStakingPeriod() {
        require(block.timestamp < stakingEndTime, "Staking period has ended");
        _;
    }

    // Stake DOGE20 tokens
    function stake(uint256 amount) external onlyDuringStakingPeriod {
        require(amount > 0, "Stake amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's staked amount and total staked amount
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Update reward debt
        rewards[msg.sender] += calculateReward(msg.sender);

        emit Staked(msg.sender, amount);
    }

    // Calculate the rewards based on the staked amount
    function calculateReward(address user) internal view returns (uint256) {
        return (stakedAmount[user] * rewardRate * (block.timestamp - stakingEndTime + 1)) / (totalStaked);
    }

    // Unstake DOGE20 tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's staked amount and total staked amount
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Update reward debt before transferring rewards
        rewards[msg.sender] += calculateReward(msg.sender);
        
        // Transfer DOGE20 tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Claim accumulated rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender] + calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        // Reset user's rewards and reward debt
        rewards[msg.sender] = 0;

        // Transfer rewards in DOGE20 tokens
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Get the amount of DOGE20 tokens staked by a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Get the total rewards accumulated by a user
    function getAccumulatedRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateReward(user);
    }

    // Emergency function to withdraw DOGE20 tokens
    function emergencyWithdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
