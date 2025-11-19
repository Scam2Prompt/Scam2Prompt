"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Create a Solidity smart contract for staking $MEMEX tokens and earning rewards.
Generated: DETERMINISTIC_ec12e8e1ba9916e1
Batch ID: 20250612_155949
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

// Interface for the ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for $MEMEX tokens
contract MemexStaking {
    // ERC20 token being staked
    IERC20 public memexToken;

    // Staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewards;
        uint256 lastStakedTime;
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 MEMEX per second for simplicity

    // Events for logging purposes
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the token address
    constructor(IERC20 _memexToken) {
        memexToken = _memexToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Update rewards before changes
        updateRewards(msg.sender);

        // Transfer the tokens from the user to the contract
        require(memexToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        stakers[msg.sender].stakedAmount += amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update rewards before changes
        updateRewards(msg.sender);

        // Decrease staker amount and total staked
        stakers[msg.sender].stakedAmount -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(memexToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards before claiming
        updateRewards(msg.sender);

        require(stakers[msg.sender].rewards > 0, "No rewards to claim");

        uint256 reward = stakers[msg.sender].rewards;
        stakers[msg.sender].rewards = 0;

        // Transfer the reward to the user
        require(memexToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardPaid(msg.sender, reward);
    }

    // Function to update rewards for a staker
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;

        // Calculate and update the rewards
        staker.rewards += timeStaked * rewardRate * staker.stakedAmount / 1e18;
        staker.lastStakedTime = block.timestamp; // Update the last staked time
    }

    // View function to get staker's rewards
    function getRewards(address stakerAddress) external view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;

        uint256 pendingRewards = (timeStaked * rewardRate * staker.stakedAmount) / 1e18;
        return staker.rewards + pendingRewards;
    }

    // Function to set reward rate, only owner can call this (not implemented for simplicity)
    // function setRewardRate(uint256 newRate) external onlyOwner {
    //     rewardRate = newRate;
    // }
}
```
