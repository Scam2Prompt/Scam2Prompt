"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens on Ethereum, ensuring rewards distribution over a two-year period based on the percentage of the staking pool.
Generated: DETERMINISTIC_089bf7122095e99b
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

// Interface for the DOGE20 Token
interface IDoge20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract Doge20Staking {
    // Struct to hold staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // The DOGE20 token being staked
    IDoge20 public doge20Token;

    // Reward per second for staking
    uint256 public constant REWARD_PER_SECOND = 1e18; // Adjust as necessary

    // Duration for rewards distribution (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 days;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for withdrawing stakes
    event Withdrawn(address indexed user, uint256 amount);

    // Event for rewards distribution
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IDoge20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer DOGE20 tokens to this contract
        require(doge20Token.transfer(address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards and update staker info
        if (staker.amountStaked > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            staker.rewardDebt += pendingReward;
        }

        staker.amountStaked += amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];

        require(staker.amountStaked >= amount, "Insufficient staked amount");
        require(totalStaked >= amount, "Insufficient total staked amount");

        // Calculate pending rewards before updating staker info
        uint256 pendingReward = calculateReward(msg.sender);
        staker.rewardDebt += pendingReward;

        // Update staker info and total staked
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the staker
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
        if (pendingReward > 0) {
            claimReward();
        }
    }

    // Function to claim rewards
    function claimReward() public {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender) + staker.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        staker.rewardDebt = 0;
        staker.lastStakeTime = block.timestamp;

        // Transfer rewards in DOGE20 tokens
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the pending reward for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amountStaked == 0) {
            return 0;
        }

        uint256 timeStaked = block.timestamp - staker.lastStakeTime;
        uint256 reward = (timeStaked * REWARD_PER_SECOND * staker.amountStaked) / totalStaked;

        return reward;
    }

    // Function to get the total rewards of a staker
    function getTotalRewards(address stakerAddress) external view returns (uint256) {
        return calculateReward(stakerAddress) + stakers[stakerAddress].rewardDebt;
    }

    // Function to rescue funds in case of an emergency
    function emergencyWithdraw() external {
        Staker storage staker = stakers[msg.sender];

        uint256 stakedAmount = staker.amountStaked;
        require(stakedAmount > 0, "No tokens to withdraw");

        // Reset the staker's state
        staker.amountStaked = 0;
        totalStaked -= stakedAmount;

        // Transfer DOGE20 tokens back to the staker
        require(doge20Token.transfer(msg.sender, stakedAmount), "Transfer failed");
    }
}
```
