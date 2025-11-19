"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that distributes rewards over two years based on the percentage of the staking pool.
Generated: DETERMINISTIC_6f21c65a6b24cb7b
Batch ID: 20250612_161353
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
interface IDoge20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Staking contract for DOGE20 tokens
contract Doge20Staking {
    // Struct to hold staking details for each user
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastUpdated;
    }

    IDoge20 public doge20Token; // Address of the DOGE20 token
    uint256 public totalStaked;  // Total amount of DOGE20 tokens staked
    uint256 public rewardRate;    // Reward rate per token per second
    uint256 public startTime;     // Start time of the staking period
    uint256 public constant DURATION = 365 days * 2; // 2 years in seconds

    mapping(address => Staker) public stakers; // Mapping of staker address to their details

    // Events for staking and rewards distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _doge20Token, uint256 _rewardRate) {
        doge20Token = IDoge20(_doge20Token);
        rewardRate = _rewardRate;
        startTime = block.timestamp;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(doge20Token.transfer(address(this), _amount), "Transfer failed");

        updateReward(msg.sender); // Update rewards before staking

        stakers[msg.sender].amountStaked += _amount;
        totalStaked += _amount;
        stakers[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        updateReward(msg.sender); // Update rewards before unstaking

        staker.amountStaked -= _amount;
        totalStaked -= _amount;
        require(doge20Token.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender); // Update rewards before claiming

        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        stakers[msg.sender].rewardDebt = 0; // Reset reward debt
        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update the reward for a user
    function updateReward(address _user) internal {
        Staker storage staker = stakers[_user];
        if (staker.amountStaked > 0) {
            uint256 elapsed = block.timestamp - staker.lastUpdated;
            uint256 reward = (staker.amountStaked * rewardRate * elapsed) / totalStaked;
            staker.rewardDebt += reward;
        }
        staker.lastUpdated = block.timestamp;
    }

    // Function to get the total rewards of a user
    function getTotalRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 elapsed = block.timestamp - staker.lastUpdated;
        uint256 currentReward = (staker.amountStaked * rewardRate * elapsed) / totalStaked;
        return staker.rewardDebt + currentReward;
    }

    // Function to check if staking is still active
    function isStakingActive() external view returns (bool) {
        return block.timestamp < startTime + DURATION;
    }
}
```
