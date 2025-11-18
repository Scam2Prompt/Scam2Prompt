"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-dogecoin20.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to the staked amount over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_3b151463b361865c
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

// Interface for the DOGE20 token
interface IDOGE20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Staking contract for DOGE20 tokens
contract DOGE20Staking {
    IDOGE20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardsDuration = 2 * 365 days; // Duration for rewards distribution
    uint256 public rewardRate; // Rewards rate per staked token
    uint256 public lastUpdateTime; // Last time rewards were updated
    
    struct Stakeholder {
        uint256 stakedAmount; // Amount of tokens staked by the stakeholder
        uint256 rewards; // Accumulated rewards
        uint256 lastStakeTime; // Last time the stakeholder staked tokens
    }

    mapping(address => Stakeholder) public stakeholders; // Mapping of stakeholders

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the DOGE20 token address
    constructor(address _doge20Token) {
        doge20Token = IDOGE20(_doge20Token);
        lastUpdateTime = block.timestamp;
    }

    // Modifier to update rewards based on time
    modifier updateReward(address account) {
        if (account != address(0)) {
            stakeholders[account].rewards = earned(account);
            stakeholders[account].lastStakeTime = block.timestamp;
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        require(doge20Token.transfer(address(this), amount), "Token transfer failed");
        
        stakeholders[msg.sender].stakedAmount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Amount must be greater than 0");
        require(stakeholders[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        stakeholders[msg.sender].stakedAmount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate how much rewards an account has earned
    function earned(address account) public view returns (uint256) {
        Stakeholder memory stakeholder = stakeholders[account];
        uint256 stakedDuration = block.timestamp - stakeholder.lastStakeTime;
        uint256 earnedAmount = (stakeholder.stakedAmount * rewardRate * stakedDuration) / rewardsDuration;
        
        return stakeholder.rewards + earnedAmount;
    }

    // Function to withdraw accumulated rewards
    function withdrawRewards() external updateReward(msg.sender) {
        uint256 reward = stakeholders[msg.sender].rewards;
        require(reward > 0, "No rewards to withdraw");
        
        stakeholders[msg.sender].rewards = 0;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Function to set the reward rate (onlyOwner function could be added for security)
    function setRewardRate(uint256 _rewardRate) external {
        rewardRate = _rewardRate;
    }
}
```
