"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Create a Solidity function that calculates staking rewards based on the number of $STARS tokens held, incentivizing long-term holding.
Generated: DETERMINISTIC_8430987dd840bf46
Batch ID: 20250612_154307
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

contract StakingRewards {
    // State variable to store the total supply of STARS tokens
    uint256 public totalSupply;

    // Mapping to track the staked amount of STARS tokens for each user
    mapping(address => uint256) private stakedAmounts;

    // Mapping to track the last reward time for each user
    mapping(address => uint256) private lastRewardTime;

    // Event to log staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Reward rate (in tokens) per second based on staked tokens
    uint256 public rewardRate = 1e18; // Example: 1 STARS token per second per token staked

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakedAmounts[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Function to stake $STARS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(totalSupply >= amount, "Not enough tokens in total supply");

        // Update the total supply and the user's staked amount
        totalSupply -= amount;
        stakedAmounts[msg.sender] += amount;

        // Update the last reward time
        lastRewardTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the pending rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedAmounts[user];
        uint256 rewardDuration = block.timestamp - lastRewardTime[user];
        return (stakedAmount * rewardRate * rewardDuration) / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external hasStaked {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update last reward time after claiming
        lastRewardTime[msg.sender] = block.timestamp;

        // Optionally, mint or transfer rewards to the user
        // (This should be implemented according to the tokenomics of the $STARS token)

        emit RewardPaid(msg.sender, reward);
    }

    // Function to unstake $STARS tokens
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate pending rewards before unstaking
        claimRewards();

        // Update the staked amount and total supply
        stakedAmounts[msg.sender] -= amount;
        totalSupply += amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Function to set the reward rate (only owner can set this in a real contract)
    function setRewardRate(uint256 newRate) external {
        // This is a placeholder for ownership check logic
        rewardRate = newRate;
    }
}
```
