"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainbitcoinbsc.pages.dev
Prompt: Write a Solidity smart contract that simulates the BTCBSC staking rewards mechanism, where rewards are distributed every 10 minutes based on the staking pool percentage.
Generated: DETERMINISTIC_82e66e45f6a8d9b7
Batch ID: 20250612_152240
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
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract simulates a staking rewards mechanism similar to BTCBSC
contract StakingRewards is Ownable {
    // ERC20 token to be staked
    IERC20 public stakingToken;
    
    // Staker information
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimedTime;
        uint256 rewards;
    }
    
    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per minute (in tokens)
    uint256 public rewardRate;

    // Duration to wait for reward distribution
    uint256 public rewardInterval = 10 minutes;

    // Events for staking and claiming rewards
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    
    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        updateRewards(msg.sender);

        // Transfer tokens from staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker's staked amount and total staked
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        
        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset the rewards and transfer the rewards to the staker
        staker.rewards = 0;
        stakingToken.transfer(msg.sender, rewardsToClaim);
        
        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    // Internal function to update rewards for a staker
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        
        // Calculate the time elapsed since the last claim
        uint256 timeElapsed = block.timestamp - staker.lastClaimedTime;
        
        // Update rewards based on the elapsed time and staked amount
        if (timeElapsed >= rewardInterval) {
            uint256 numberOfIntervals = timeElapsed / rewardInterval;
            uint256 earnedRewards = (staker.amountStaked * rewardRate * numberOfIntervals) / 1e18;
            staker.rewards += earnedRewards;
            staker.lastClaimedTime = block.timestamp; // Update last claimed time
        }
    }

    // Function to get the total rewards of a staker
    function getTotalRewards(address stakerAddress) external view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 totalRewards = staker.rewards;

        // Calculate potential rewards if they haven't been claimed yet
        uint256 timeElapsed = block.timestamp - staker.lastClaimedTime;
        if (timeElapsed >= rewardInterval) {
            uint256 numberOfIntervals = timeElapsed / rewardInterval;
            totalRewards += (staker.amountStaked * rewardRate * numberOfIntervals) / 1e18;
        }

        return totalRewards;
    }

    // Function to withdraw all staked tokens (for owner before deploy)
    function withdrawStakedTokens(uint256 amount) external onlyOwner {
        require(amount <= totalStaked, "Cannot withdraw more than total staked");
        stakingToken.transfer(owner(), amount);
        totalStaked -= amount;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
