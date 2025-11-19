"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Generate a smart contract in Solidity for staking DOGE20 tokens that distributes rewards over a two-year period, based on the staking pool percentage.
Generated: DETERMINISTIC_d17ed1ef058393ff
Batch ID: 20250612_161500
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

contract StakingContract {
    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 reward;
        uint256 stakingStartTime;
    }

    IDOGE20 public doge20Token; // Interface for DOGE20 token
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardPool; // Total rewards available for distribution
    uint256 public constant STAKING_DURATION = 730 days; // 2 years

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    constructor(address _doge20Token) {
        doge20Token = IDOGE20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake a positive amount");
        require(doge20Token.transfer(address(this), amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.stakingStartTime = block.timestamp;

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");
        
        uint256 reward = calculateReward(msg.sender);
        require(doge20Token.transfer(msg.sender, userStake.amount), "Token transfer failed");

        userStake.amount = 0; // Reset stake amount
        userStake.reward += reward; // Update the reward
        totalStaked -= userStake.amount;

        emit Unstaked(msg.sender, userStake.amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on staking duration
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (block.timestamp < userStake.stakingStartTime + STAKING_DURATION) {
            return (userStake.amount * (block.timestamp - userStake.stakingStartTime)) / STAKING_DURATION;
        }
        return (userStake.amount * 100) / 100; // Example: for simplicity, 1:1 reward at the end of staking
    }

    // Function to withdraw rewards only after staking period
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.stakingStartTime + STAKING_DURATION, "Staking period not ended");
        
        uint256 reward = userStake.reward;
        require(reward > 0, "No rewards to claim");
        
        require(doge20Token.transfer(msg.sender, reward), "Token transfer failed");
        userStake.reward = 0; // Reset reward after claiming
        
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to withdraw remaining tokens by the owner (for emergencies)
    function withdrawTokens(uint256 amount) external {
        require(msg.sender == address(this), "Only contract owner can withdraw");
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
