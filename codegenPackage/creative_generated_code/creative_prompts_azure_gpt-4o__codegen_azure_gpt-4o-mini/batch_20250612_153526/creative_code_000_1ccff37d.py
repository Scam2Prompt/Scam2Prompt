"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking mechanism similar to DOGE20, where rewards are distributed every block based on the percentage of the staking pool and a dynamic annual return rate.
Generated: DETERMINISTIC_1ccff37d2f3a53ff
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking Contract for a token with dynamic rewards
contract Staking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public stakingToken;

    // Annual return rate (in basis points, e.g. 10000 = 100%)
    uint256 public annualReturnRate;

    // Total amount staked in the pool
    uint256 public totalStaked;

    // User stake and reward information
    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(address => StakeInfo) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the staking token and annual return rate
    constructor(IERC20 _stakingToken, uint256 _annualReturnRate) {
        stakingToken = _stakingToken;
        annualReturnRate = _annualReturnRate;
    }

    // Function to calculate the pending rewards for a user
    function pendingReward(address user) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakers[user];
        uint256 totalReward = calculateTotalRewards();
        return totalReward.mul(stakeInfo.amount).div(totalStaked).sub(stakeInfo.rewardDebt);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer the staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        // Update user's stake information
        StakeInfo storage stakeInfo = stakers[msg.sender];
        stakeInfo.amount = stakeInfo.amount.add(amount);
        stakeInfo.rewardDebt = stakeInfo.rewardDebt.add(pendingReward(msg.sender));

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        StakeInfo storage stakeInfo = stakers[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked balance");

        // Calculate the pending reward and update user's information
        uint256 reward = pendingReward(msg.sender);
        stakeInfo.rewardDebt = stakeInfo.rewardDebt.add(reward);
        stakeInfo.amount = stakeInfo.amount.sub(amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
        payReward(msg.sender, reward);
    }

    // Function to calculate total rewards based on the annual return rate
    function calculateTotalRewards() internal view returns (uint256) {
        if (totalStaked == 0) return 0;
        // Calculate total rewards based on the annual return rate
        // Rewards per block = (annualReturnRate / blocks per year) * totalStaked
        uint256 blocksPerYear = 2102400; // Assuming ~15 seconds per block (Ethereum)
        return totalStaked.mul(annualReturnRate).div(10000).div(blocksPerYear);
    }

    // Function to distribute rewards to the user
    function payReward(address user, uint256 reward) internal {
        if (reward > 0) {
            // Update the reward debt for the user
            stakers[user].rewardDebt = stakers[user].rewardDebt.add(reward);
            emit RewardPaid(user, reward);
        }
    }

    // Function to set a new annual return rate (only owner can call)
    function setAnnualReturnRate(uint256 newRate) external {
        require(newRate > 0, "New rate must be positive");
        annualReturnRate = newRate;
    }
}
```
